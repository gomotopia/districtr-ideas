'''
Districtr Idea 3.0

The easiest way to list precincts and districts together is by generating
this link in QGIS, then saving to a csv. 

NOLA Precincts and Districts are stored in the NOLA Open GIS format.
(Not all parishes make it this easy.) In QGIS, we match the precinct to the
relevant OPSB district and export a csv of attributes. CSV format...

id,Precinct,Parish,OPSB_District
1,1-1,ORLEANS,5

While currently manual, this could be made programmatic using geopandas, etc.

This script could also be a plugin in QGIS generating json files with
one click.
'''

from DistrictrJsonReader import DistrictrJson
import csv
import re


def OrleansPrecinctConverter(oldPrec):
    '''
        Takes NOLA GIS Format: "11-1A" and converts into 
        Districtr format "Orleans, 11 01A"
    '''
    ward, precinct = re.findall('\d{1,2}?(?!\d)',oldPrec)
    try: suffix = re.search('[A-Z]', oldPrec).group(0)
    except: suffix = ""
    return f"Orleans, {ward.zfill(2)} {precinct.zfill(2)}{suffix}"
    
def Wards():
    WardsObject = DistrictrJson(
                        "Orleans Parish School Board Districts",
                        "District",
                        "Districts",
                        oldfile='Data/Orleans-LA.json')
    
    newAssignment = {}
    with open('Data/OPSB-Districts.csv') as f:
        reader = csv.reader(f)
        next(reader) # skipheaders
        for row in reader:
            print(row)
            newAssignment[OrleansPrecinctConverter(row[1])] = int(row[3])-1
    
    print(newAssignment)
        
    WardsObject.setAssignment(newAssignment)
    WardsObject.write('Generated/OPSB-Districts.jsonraw')
    
if __name__ == "__main__":
    Wards()
