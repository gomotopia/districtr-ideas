# districtr-ideas

Districtr-Ideas is a repository of my ideas on how to use Python to programatically generate JSON files for use in [MGGG](https://github.com/mggg)'s [districtr](https://districtr.org/) app. MGGG's districtr app is an interactive mapping browser application that allows the public to select and draw political voting precincts and ties those boundaries with extensive, historical demographic and electoral data.

Given my experience working with local campaigns, I wanted to use their power tool with extant local political boundaries, to describe to my neighbors how their local boundaries are currently cut and the impact of future decisions. 

Unfortunately, for now, these ideas are set for the state-wide Louisiana juristictions. This is ideal for Congressional, State Legislative, Public Service Commission and Judicial districts. Since my aim, however, concerns local parish or city-wide districts, I'll have to find a way to set the statistics to cover these smaller juristictions. 

# Ideas for Local Districtr Maps

Districtr is a great resource that allows people to draw and take statistics on their own districts selected from precincts. The app has native CSV and JSON formats that allows for saving and loading maps. The purpose of these ideas is to generate maps I can load, of current political boundaries or otherwise. 

Essentially, each file contains a list of precincts and their assigned districts. For current districts, we can find or generate this data the following ways... 

1. **Secretary of State Results** ties together offices with precincts and results. However, not all offices are contested and not all current districts may be included. 
2. By law, districts are written into each **Municipal Code** in parish specific formats. Legal text can be parsed, but published sources aren't always current.  
3. **GIS.** It is easiest to use QGIS to generate our own district assignments with help from whichever boundary files are available. While currently a manual process, this can be programmed later using, say, geopandas.  

### Wards of New Orleans

Wards are an old political unit, used only in the name of current precincts. Since we can already parse this from districtr data, this first project generates and manipulates a JSON downloaded form Districtr. 

#### Jefferson Parish Council

JeffParishCouncil.py uses language in the Jefferson Parish municipal code to collect district assignments. A Districtr JSON file is generated from a blank template. Unfotunately, the language in the Parish code is out of date. 

In the future, we can try to generate this by comparing the language with the precincts that Districtr has on file. 

#### Orleans Parish School Board Districts

Found in SchoolBoard.py There are 7 School Districts outlined by Feb. 28, 2012 resolution, but precinct assingments are mapped, not listed. Fortunately, we can find the boundary file in the City of New Orleans GIS portal, [here](https://portal-nolagis.opendata.arcgis.com/). A simple CSV file of assignments was generated this way, with requisite name conversion into precinct titles used by Districtr.

#### City Council Districts

There are 5 City Council Districts outlined by 2011 Ordinance No. 24511 M.C.S. These boundaries split precincts! Isn't that wild?

## Future

Districtr can also read CSV format file, which are easier to use than its JSON format. 

## Other GNO Parishes

* St. Bernard Parish
* Plaquemines Parish
* St. Tammany Parish
* Washington Parish
* Tangipahoa Parish
* St. Charles Parish
* St. James Parish
* St. John the Baptist Parish

_Ryan Gomez.  
N.O., LA.  
February 2021_
