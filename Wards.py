'''
Districtr Idea 1.0

Wards in New Orleans are ancient political boundaries with little real
world use. However, they still serve as important psychological divisions
in New Orleans as they mimic the development of the city: neighborhoods 
perpendicular to the river that spread up and down over time. 

This first Districtr Idea demonstrates the ability to use the python 
DistrictrJSON Object to encapsulate a Districtr compatible boundary map. 

Wards in New Orleans can be determined by each precinct's name, which makes
this an ideal first demonstration. 

As with all current ideas, Districtr is unfortunately set only for state-wide 
comparisons, and not local parochial or municipal juristictions. 
'''

from DistrictrJsonReader import DistrictrJson
import re

if __name__ == "__main__":
    WardsObject = DistrictrJson(
                        "Wards of New Orleans",
                        "Ward",
                        "Wards",
                        oldfile='Orleans-LA.json',
                        ordinalnames=True)
    oldassignment = WardsObject.getAssignment()
    wardstrings = list(oldassignment.keys())
    
    # Districtr Format: "Orleans, 11 11" First pair of numbers singifies Ward.
    newAssignment = {x:int(re.search("(?<=Orleans, )\d\d", x).group())-1 for x in list(wardstrings)}  
    
    WardsObject.setAssignment(newAssignment)
    WardsObject.write('Wards-Test1.jsonraw')