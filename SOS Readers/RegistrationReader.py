'''
These scripts read the master registrations file from the La SOS for the 2021 xls format.
An SVG file is created for the purposes of illustration. 

Future: a D3 optimized file, script, generated here. 
'''

import pandas as pd

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
        print(id, parish.upper(), str(id).zfill(2))
        pF= pd.read_excel(io=file_name, sheet_name=sheet, skiprows=8, names=labels)
        pF.Name = pF.Name.str.replace('\xa0', ' ')
        
        totF = pF.loc[pF['Name'].str.endswith(f'PAR {str(id).zfill(2)}')]
        cdF = pF.loc[pF['Name'].str.endswith('CONG 02')]
        
        print (cdF)
        fullTable = fullTable.append(totF).append(cdF)
        
    fullTable = fullTable.drop(columns=['Throwaway'])
    print(fullTable.head(5))
    return fullTable

def 


if __name__ == "__main__":
    fullTable = ParseRegistrationStats()
    analyzedTable = AnalyzeResults()
    WriteSVG(analyzedTable)
