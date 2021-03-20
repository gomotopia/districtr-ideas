'''
These scripts read the master registrations file from the La SOS for the 2021 xls format.
An SVG file is created for the purposes of illustration. 

Future: a D3 optimized file, script, generated here. 
'''

import pandas as pd
from pygments.unistring import Cf

labels = ['Name','Throwaway',
          'Tot_Tot','Tot_W','Tot_B','Tot_O',
          'Tot_Dem','Dem_W','Dem_B','Dem_O',
          'Tot_Rep','Rep_W','Rep_B','Rep_O',
          'Tot_Oth','Oth_W','Oth_B','Oth_O']

parishes = [ (3, 'Ascension'),
             (4, 'Assumption'),
             (17, 'East Baton Rouge'),
             (24, 'Iberville'),
             (26, 'Jefferson'),
             (36, 'Orleans'),
             (45, 'St. Charles'),
             (47, 'St. James'),
             (48, 'St. John the Baptist'),
             (61, 'West Baton Rouge')]

fullTable = pd.DataFrame(columns = labels)

file_name = "../Data/2021_0301_par_comb.xls"

def ParseRegistrationStats():
    '''
        Takes data from Secretary of State registrations statistics, provided in 
        xls form, and returns Pandas dataframe of total and 2nd Congressional District 
        stats. The xls stores each parish data as a page and row names provide 
        information parsed by total, office and precinct.
        
        Input: Global variables of labels, relevant parishes, filename. 
        Output: Returns table of total and CD2 stats across all categories. 
        Future: More flexible function for all Congressional districts, races, etc.
                Separate settings file for global variables.
    '''
    fullTable = pd.DataFrame(columns = labels)
    
    for (id, parish) in parishes:
        sheet = id-1
        pF= pd.read_excel(io=file_name, sheet_name=sheet, skiprows=8, names=labels,
                          thousands=',')
        pF.Name = pF.Name.str.replace('\xa0', ' ')
        totF = pF.loc[pF['Name'].str.endswith(f'PAR {str(id).zfill(2)}')]
        cdF = pF.loc[pF['Name'].str.endswith('CONG 02')]
        fullTable = fullTable.append(totF).append(cdF)
        
    fullTable = fullTable.drop(columns=['Throwaway'])
    return fullTable

def AnalyzeResults(fullTable):
    '''
        A congressional district overlays on top of multiple parishes. 
        Thus, each parish can be considered within and without a certain 
        district.
        
        Let A = {A | A is in minority group}
        Let D = {D | D is covered within relevant district}
        Let P = {P | P is everyone in the Parish}
        
        D and P are subsets of P.
        
        What percentage of group A inside a parish is covered in the congressional
        district? (A and P) / P
        
        What percentage of the congressional district comprises of group A?
        (A and P) / A

        Sample Data:
        Ascension...
        
        83,553 Total
        13,722 Total CD
        19,441 Total Black
         9,146 Total Black in CD
        27,985 Total Dems
         8,866 Total Dems in CD
           .66 CD is B 9.1k/14k
           .46 B in CD 9.1k/19k
           .63 CD is Dem 8.9k/14k
           .31 Dem in CD 8.9k/28k
           
           Also?
        
        14,997 Total Black Dems
         7,322 Total Black Dems in CD
   
        14,997/19,441 77% of Blacks are Dems 
        14,997/27,985 56% of Dems are Black
        
        435/19,441 2.2% of Blacks are Repubs
    '''

    labels = ["Tot_Tot", "Tot_CD",
              "Tot_B", "Tot_B_CD",
              "Tot_Dem", "Tot_Dem_CD",
              "CD_is_B", "B_in_CD",
              "CD_is_Dem", "Dem_in_CD"]

    analyzedTable = pd.DataFrame(columns=labels)

    for (id, parish) in parishes:
        idStr = str(id).zfill(2)
        pF = fullTable.loc[fullTable['Name'].str.endswith(f'PAR {idStr}')].iloc[0]
        cdF = fullTable.loc[fullTable['Name'].str.startswith(f'PAR {idStr}')].iloc[0]
        pLine = pd.DataFrame([{"Parish": idStr,
                               "Tot_Tot":pF['Tot_Tot'],
                               "Tot_CD":cdF['Tot_Tot'],
                               "Tot_B":pF['Tot_B'],
                               "Tot_B_CD":cdF['Tot_B'],
                               "Tot_Dem":pF['Tot_Dem'],
                               "Tot_Dem_CD":cdF['Tot_Dem'],
                               "CD_is_B": cdF['Tot_B']/cdF['Tot_Tot'],
                               "B_in_CD": cdF['Tot_B']/pF['Tot_B'],
                               "CD_is_Dem": cdF['Tot_Dem']/cdF['Tot_Tot'],
                               "Dem_in_CD": cdF['Tot_Dem']/pF['Tot_Dem']}])      
        analyzedTable = analyzedTable.append(pLine)     
    
    sumLine = analyzedTable.sum()
    sumLine['CD_is_B'] = sumLine['Tot_B_CD']/sumLine['Tot_CD']
    sumLine['B_in_CD'] = sumLine['Tot_B_CD']/sumLine['Tot_B']
    sumLine['CD_is_Dem'] = sumLine['Tot_Dem_CD']/sumLine['Tot_CD']
    sumLine['Dem_in_CD'] = sumLine['Tot_Dem_CD']/sumLine['Tot_Dem']
    sumLine['Parish'] = 'Sum'
    
    analyzedTable = analyzedTable.append(sumLine, ignore_index=True)
    return analyzedTable
    
if __name__ == "__main__":
    fullTable = ParseRegistrationStats()
    analyzedTable = AnalyzeResults(fullTable)
    print(analyzedTable)
    # WriteSVG(analyzedTable)
