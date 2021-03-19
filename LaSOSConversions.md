# Louisiana Secretary of State File Formats

The Louisiana Secretary of State publishes election results and registration statistics down to the precinct level for the entire state.

### Registration Statistics

Registration statistics, published on a roughly monthly rolling basis is found [here](https://www.sos.la.gov/ElectionsAndVoting/Pages/RegistrationStatisticsParish.aspx). It is currently published in xls format with the following fields: 

* Registered voters
* Democrats
* Republicans
* Other Parties
	* Each broken into Total, White, Black and Other races
	
The current xls format has 64 pages, one for each parish, with a header that covers 1-9. Line 10 carries totals across the entire parish with a format akin to `ACADIA PAR 01.` Statistics are then broken into each Congressional district, `PAR 01 CONG 03`, State Senate district `PAR 01 SEN 25`, State Representative, `PAR 01 REP 041`, Parish Council, School Board, other offices and finally each precinct, `PAR 01 W 01 P01`... 