'''
Jefferson Parish Council Districts

Districtr Idea 2.0

This was my attempt to generate a Districtr JSON file from scratch, rather than
extract off of an old file. I generated the assignments using the code found in 
Section 2.02 of Jefferson Parish Code of Ordinances.

1) Council District One shall consist of the following precincts: Precincts 192, 193, 198, 199, 203, 215, 217, 225, 226, 227, 228, 229, 230, 231, 234, 235, 236, 237, 238, 246, 247, 248, 194B, 197A, 212B, 216A, 216B, 232A, 232B, 1-G, 2-G, 3-G, 4-G, 5-G, 6-G, 7-G, 8-G, 9-G, 10-G, 11-G, 12-G, 13-G, 1-GI and 1-L.
2) Council District Two shall consist of the following precincts: Precincts 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 105, 106, 107, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 136, 138, 152, 155, 170, 171, 172, 174, 175, 176, 177, 178, 182, 183, 184, 210, 211, 185A, 213B, 214A, 1-H, 2-H, 3-H, 4-H, 5-H, 6-H, 7-H, 8-H, 9-H, 1-W, 2-W, 3-W, 4-W, 5-W, 6-W and 7-W.
3) Council District Three shall consist of the following precincts: Precincts 104, 108, 115, 116, 150, 151, 153, 154, 156, 173, 179A, 180, 181, 187, 188, 189, 190, 191, 195, 196, 200, 201, 202, 204, 205, 157A, 157B, 179B, 185B, 194A, 197B, 197C, 212A, 213A, 213C, 214B, 13-K(B), 21-K, 22-K, 23-K, 24-K, 26-K, 31-K and 33-K.
4) Council District Four shall consist of the following precincts: Precincts 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 21, 51, 52, 53, 54, 55, 56, 57, 58, 59, 1-K, 2-K, 3-K, 4-K, 5-K, 6-K, 7-K, 8-K, 9-K, 10-K, 11-K, 12-K, 13-K(A), 14-K, 15-K, 16-K, 17-K, 18-K, 19-K, 20-K, 25-K, 27-K, 28-K, 29-K, 30-K, 34-K and 35-K.
5) Council District Five shall consist of the following precincts: Precincts 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102 and 103."

Issue! The City Code is old! New Precincts have been split off since the coding of
this law. Namely...
    - 193 is replaced by 193A and 193B
    - 238 is replaced by 238A and 238B
    - 212A and B are merged back into 212
    - There is no longer precinct 107
    - 125 is replaced by 125B
    - Kenner K006 is replaced by K006A
    - Kenner K007 is replaced by K007B
    - 197C is brand new 
    - 216C is brand new 
    
    If old districts are assigned to the input JSON file, they remain and can't be  displayed,
    added or deleted by the web app. 
    
    One day, we would probably need to download Districtr's copy and compare the written code
    with available precincts. 
'''

import re
from DistrictrJsonReader import *

def JeffConvert(lawPrec):
    '''
        Converts Parish Code Precint string, returns Districtr Format string
        parish code:"000" or "000A" or "000-X" or "000-X(A)"       
        districtr code: "Jefferson, 00 X000A"
        X is City code, may be none
        A is A,B,C suffix, may be none. 
    '''
    
    number = city = suffix = ""
    
    try: number = re.search('\d{1,3}?(?!\d)', lawPrec).group(0) #000
    except: pass
    try: city = re.search('(?<=-)[A-Z]+', lawPrec).group(0) #000-X
    except: pass
    try: suffix = re.search('(?<=\d)[A-Z]',lawPrec).group(0) #000A
    except:
        try: suffix = re.search('(?<=\()[A-Z]+(?=\))', lawPrec).group(0) #000-X(A)
        except: pass
    
    clearnone = lambda i : i or '' # Print NoneTypes as '' rather than 'None'
    return f"Jefferson, 00 {clearnone(city)}{number.zfill(3)}{clearnone(suffix)}"

def JeffCouncil():
    '''
        Main script for creating a new Districtr JSON file by extracting district-precinct
        list from municipal code. Municipal code kept in Jefferson-Council-Law.txt. 
        
        Problem! Districtr reflects changes that have taken place after the municipal
        code was published. 
        
        Jefferson-LA-Council.jsonraw is the generated copy.
        Jefferson-LA-Council.json is the hand corrected copy.
    '''
    with open('Data/Jefferson-Council-Law.txt') as f:
        lawstrings = f.readlines()
        lawstrings = [x.strip() for x in lawstrings]
        
    newAssign = {}  
    
    for (i,lawstring) in enumerate(lawstrings):
        preclist = re.split(', | and |\.',lawstring.split('Precincts ')[1])
            # find precinct entries using splits
        for prec in [p for p in preclist if p]: # list comp. removes blank entries.
            newAssign[JeffConvert(prec)] = i

    JeffJson = DistrictrJson("Jefferson Parish Council District", "District", "Districts")
    JeffJson.setAssignment(newAssign)
    JeffJson.write('Generated/Jefferson-LA-Council.jsonraw')

if __name__ == "__main__":
    JeffCouncil()
    
