import json
import os
from pprint import pprint as print

import click
import requests


def get_lat_long(address):
    """
    Makes a call to the google maps API service and returns a list of lat, long with an ID
    :param address_csv: input address csv
    :return:
    """
    URL = f"https://maps.googleapis.com/maps/api/geocode/json"
    parameters = {
        "address": address,
        "key": {os.environ['GOOGLE_API_KEY']},
    }
    response = requests.get(URL, parameters)
    json_response = json.loads(response.text)
    try:
        latitude = json_response['results'][0]['geometry']['location']['lat']
    except:
        latitude = 0
    try:
        longitude = json_response['results'][0]['geometry']['location']['lng']
    except:
        longitude = 0
    try:
        formatted_address = json_response['results'][0]['formatted_address']
    except:
        formatted_address = ""
    return latitude, longitude, formatted_address


# TODO: data class maybe?
def format_greenspace_response(park_payload, poi_payload):
    """
    formats the return of the source API to structured data
    :param payload: results
    :return:
    """
    result_list = []
    for doc in park_payload:
        park_response = {
            "name" : doc["name"],
            "lat" : doc["geometry"]["location"]["lat"],
            "long": doc["geometry"]["location"]["lng"],
        }
        park_name = doc["name"]
        # checking for duplicate entries
        existing_parks = [result["name"] for result in result_list]
        if park_name not in existing_parks:
            # only add a park if it's name does not exist in the list already
            result_list.append(park_response)
    for doc in poi_payload:
        poi_response = {
            "name": doc["name"],
            "lat": doc["geometry"]["location"]["lat"],
            "long": doc["geometry"]["location"]["lng"],
        }
        poi_name = doc["name"]
        print(poi_name)
        # checking for nearby Playground in POI
        if "Playground" in poi_name or "Park" in poi_name:
            # checking for duplicate entries
            existing_parks = [result["name"] for result in result_list]
            if poi_name not in existing_parks:
                # only add a park if it's name does not exist in the list already
                result_list.append(poi_response)
    return result_list


def get_nearby_greenspace(latitude, longitude):
    #https://maps.googleapis.com/maps/api/place/findplacefromtext/output?parameters
    URL = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    park_parameters = {
        "location": f"{latitude},{longitude}",
        "rankby": "distance",
        "type": "park",
        "key": os.environ["GOOGLE_API_KEY"],
    }
    park_response = requests.get(URL, park_parameters)
    park_json_response = json.loads(park_response.text)
    poi_parameters = {
        "location": f"{latitude},{longitude}",
        "rankby": "distance",
        "type": "point_of_interest",
        "key": os.environ["GOOGLE_API_KEY"],
    }
    poi_response = requests.get(URL, poi_parameters)
    poi_json_response = json.loads(poi_response.text)
    results = format_greenspace_response(park_json_response["results"], poi_json_response["results"])
    return results


@click.command()
@click.argument("address")
def find_greenspace(address):
    latitude, longitude, full_address = get_lat_long(address)
    greenspaces = get_nearby_greenspace(latitude, longitude)
    click.echo(f"Parks near {full_address}:")
    for i in greenspaces:
        click.echo(f"* {i['name']}: {i['vincinity']}")


if __name__ == "__main__":
    find_greenspace()
