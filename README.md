# US State Capitals Geocoding Project

# Project Objective
The goal of this project is to create a structured dataset of all U.S. state capitals and enrich it with geographic coordinates (latitude and longitude) using Python and OpenStreetMap geocoding.

# Tools & Technologies Used
- Python
- JSON
- GeoPy library
- OpenStreetMap (Nominatim API)

# Dataset
The manually added dataset includes all 50 U.S. states with:
- State name
- Capital city
- Full address
- Latitude
- Longitude

# Steps Performed

# Part 1 – Create JSON Dataset
1. Created a structured list of U.S. state capitals.
2. Automatically generated full addresses.
3. Saved the data into a JSON file.

# Part 2 – Add Coordinates
1. Loaded the JSON file using Python.
2. Used GeoPy with Nominatim API to fetch latitude and longitude.
3. Added coordinates to each state capital.
4. Saved the enriched dataset into a new JSON file.

# Output Example

```json
{
  "state": "Texas",
  "capital": "Austin",
  "address": "Austin, Texas, USA",
  "latitude": 30.2672,
  "longitude": -97.7431
}
