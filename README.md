Software Engineer Hands-On Exercise

Implement the following program in the language and environment of your choice:

Write a program that accepts a text file with addresses, one on each line, and outputs the county associated with each address. 
Query the Google Maps API (specifically, the Google Places API) to determine the county name of the address (the field is named administrative_area_level_2 in the API result). Save the results - together with the input addresses - into a JSON file (see example below). You may use a 3rd party library to query the API.

The API key: AIzaSyBM-cHMaetej-OC9cck1Auo-x18zaw38RM

Step 1
Just make it work - better done than perfect. You should have a working app that reads the addresses from the input file and writes the expected results to the output file.

Follow-up
We’ll talk about how to improve the performance of the program:

What if the file contains tens of millions of addresses - how would you make it work as quickly as and efficiently as possible.

We’ll follow up with an architectural design discussion about how to make this code production-ready.




Example input

3601 Washtenaw Avenue Ann Arbor, MI 48104
1628 Shore Parkway Brooklyn, NY 11214
284 7th Ave Brooklyn, NY 11215
1512 Western Ave Albany, NY 12203



Example output
[
  {
    "address": "2000 Montauk Hwy, Montauk, NY 11954, United States",
    "county": "Suffolk County"
  },
  {
    "address": "1 Balboa Pier, Newport Beach, CA 92661, United States",
    "county": "Orange County"
  }
]
