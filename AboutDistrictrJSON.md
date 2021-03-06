# About the Districtr JSON Format

The [Districtr](http://districtr.org/) redistricting utility allows maps to be saved and loaded using their own JSON Format, outlined as follows.

Compare with [Districtr PlanLoader object](https://github.com/districtr/districtr/blob/657539de7271cf14649cd6ed999d6aee1dd12e8e/src/components/PlanUploader.js). It notes that...

> This does no validation or content-type checking, so there are tons of potential errors that are not caught or responded to.

### Districtr JSON Object

**Bold elements** are required in generated JSON files in order to be loaded into Districtr.

* **"assignment"**
	* Set of Precincts and Raw Districts
	* `"Orleans, 11 11": [0]`
* "id"
	* Generated by Districtr
	* `5d78403a`
* "idcolumn"
	```
	"key": "Code",
	"name": "Precinct unique identifier"
	```
* 	**"problem"**
	* Required field but information isn't updated when loaded. 
	```
	"name": "State House",
	"numberOfParts": 105,
	"pluralNoun": "State House Districts"
	```
*	**"parts"**
	* Sets display features for each district.
	```
		"id": 0,
		"displayNumber": 1,
		"name": "District 1"
	```
* **"place"**
	* State boilerplate feature collection.
	`"id": "louisiana"`
* **"placeid"**
	* `"placeid": "louisiana"`
* **"units"**
	* Loads state precint tileset from vis a vis mapbox. Contains `columnSets`, which stores state level stats and is not required.