'''
    Boilerplate for Louisana Districtr JSON Files
'''

IDCOLUMN = {"idColumn": {"key": "Code","name": "Precinct unique identifier"}}
PLACE = {"place": {"id": "louisiana",
                   "landmarks": {"type": "geojson",
                                "data": {"type": "FeatureCollection",
                                         "features": []}},
                   "state": "Louisiana"}}
PLACEID = {"placeId": "louisiana",
           "units": {"id": "precincts",
                    "name": "Precincts",
                    "unitType": "Precincts",
                    "idColumn": {
                        "name": "Precinct unique identifier",
                        "key": "Code"},
                    "tilesets": [{"type": "circle",
                                  "source": {"type": "vector",
                                             "url": "mapbox://districtr.louisiana_precincts_points"},
                                  "sourceLayer": "louisiana_precincts_points"},
                                  { "type": "fill",
                                   "source": {"type": "vector",
                                              "url": "mapbox://districtr.louisiana_precincts"},
                                   "sourceLayer": "louisiana_precincts"}
                                  ]
                    }
            }