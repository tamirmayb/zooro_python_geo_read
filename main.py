import json
import requests

api_key = 'AIzaSyBM-cHMaetej-OC9cck1Auo-x18zaw38RM'

url_place = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
url_place_details = "https://maps.googleapis.com/maps/api/place/details/json?place_id="

payload = {}
headers = {}

file_name = 'result.json'
listObj = []


def process():
    with open('input.txt', 'r', encoding='UTF-8') as file:
        while line := file.readline().rstrip():
            replace = line.replace(" ", "%20").replace(",", "%20")
            r = url_place + 'query=' + replace + '&key=' + api_key
            response = requests.request("GET", r, headers=headers, data=payload)
            data = json.loads(response.text)

            place_id = data['results'][0]['place_id']
            formatted_address = data['results'][0]['formatted_address']

            r = url_place_details + place_id + '&key=' + api_key
            response = requests.request("GET", r, headers=headers, data=payload)

            data = json.loads(response.text)
            for address in data['result']['address_components']:
                for adr_type in address['types']:
                    if adr_type == 'administrative_area_level_2':
                        long_name = address['long_name']

                        listObj.append({
                            "address": formatted_address,
                            "county": long_name,
                        })
                        break

            with open(file_name, "w") as fp:
                json.dump(listObj, fp,
                          indent=4,
                          separators=(',', ': '))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process()
