#  Ideas for Local Districtr Maps

Districtr is a great resource that allows people to draw and take statistics on their own districts selected from precincts. The app has a native JSON format that allows people to save and load their projects. Before redrawing the lines, I want a way to load extant districts and take advantage of the webapps census and results recall facilities. 

What is needed is a list that ties each district with a list of precincts. There are several ways to achieve this.

1. **Secretary of State Results** ties together offices with precincts and results, but not all offices are contested. Thus, not all districts are paired with precincts if no race occurs in a certain election. 
2. By law, districts are written into each **Municipal Code** in parish specific formats. The law text must be parsed using regular expressions and aren't always listed by precinct. 
3. **GIS.** While this is the least programmatic solution, it is usually much easier to use GIS to generate a list that ties districts with precincts by hand- if juristictions provide GIS boundary files. 

## New Orleans
*Districtr format: "Orleans, 11 11"*

* City of New Orleans GIS portal is [here.](https://portal-nolagis.opendata.arcgis.com/)

#### Whole City

The simplest file, all 300+ precincts in New Orleans. Can be found checking Statewide or Presidential Precinct Totals.

> See Louisiana Parishes JSON Generator

#### Wards

Precincts are labelled in pairs of numbers, the first representing ward. 

#### City Council Districts

There are 5 City Council Districts outlined by 2011 Ordinance No. 24511 M.C.S. These boundaries split precincts!

#### School Districts

There are 7 School Districts outlined by Feb. 28, 2012 resolution. Individual precincts are not listed. 


## Jefferson Parish
*Districtr format: "Jefferson, 00 K025", "Jefferson, 00 123", "Jefferson, 00 G005", "Jefferson, 00 G003", "Jefferson, 00 246", "Jefferson, 00 W006"*

* Municipal Code is here.
* City GIS is here.

### Whole Parish



### Towns

Several Cities and Towns are incorporated within Jefferson Parish. Precincts in each are labelled with a prefix. 

### Parish Council Districts

There are 5 City Council Districts outlined by...

# Other GNO Parishes

* St. Bernard Parish
* Plaquemines Parish
* St. Tammany Parish
* Washington Parish
* Tangipahoa Parish
* St. Charles Parish
* St. James Parish
* St. John the Baptist Parish
