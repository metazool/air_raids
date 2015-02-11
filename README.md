# air_raids
JSON data describing air raid sites and related archive documentation

## contents 

1)

aberdeen_air_raids.json 

Converted from the KML in Google Maps Engine with ogr2ogr

$ ogr2ogr -f GeoJSON air_raids.json Downloads/Aberdeen\ City\ Air\ Raid\ Map\,\ 1940\ -\ 1943.kml

2)

aberdeen_airraid_logbooks.json

JSON scraped from the Aberdeen City Council archives, with permission 
and with copyright acknowledgement, describing logbook entries
written by children at Aberdeen schools after air raids.

3)

scripts/*

- a script to add a copyright statement to vanilla geojson
- the script to scrape the logbook web pages


