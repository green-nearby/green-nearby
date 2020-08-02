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
def format_greenspace_response(payload):
    """
    formats the return of the source API to structured data
    :param payload: results
    :return:
    """
    result_list = []
    for doc in payload:
        response = {
            "name" : doc["name"],
            "lat" : doc["geometry"]["location"]["lat"],
            "long": doc["geometry"]["location"]["lng"],
            "vincinity" : doc["vicinity"],
            "types": doc["types"]
        }
        result_list.append(response)
    return result_list


def get_nearby_greenspace(latitude, longitude):
    #https://maps.googleapis.com/maps/api/place/findplacefromtext/output?parameters
    URL = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    parameters = {
        "location": f"{latitude},{longitude}",
        "rankby": "distance",
        "type": "park",
        "key": os.environ["GOOGLE_API_KEY"],
    }
    response = requests.get(URL, parameters)
    json_response = json.loads(response.text)
    results = format_greenspace_response(json_response["results"])
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
