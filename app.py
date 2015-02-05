#!/usr/bin/env python

from flask import Flask, request, json, make_response
import requests
import geojson
from haversine import haversine
from shapely.geometry import asShape
from operator import itemgetter

#GEOJSON_URL = 'https://raw.githubusercontent.com/osmlab/localgroups/master/osmgroups.geojson'

GEOJSON_URL = 'https://raw.githubusercontent.com/mahemoff/geodata/master/cities.geojson'
DEFAULT_RADIUS = 100  # kilomters

app = Flask(__name__)
# app.debug = True


@app.route('/closest')
def closest():
    lon = float(request.args.get('lon', 0))
    lat = float(request.args.get('lat', 0))
    radius = float(request.args.get('radius', DEFAULT_RADIUS))
    result = close_features(lon, lat, radius)
    return make_response(
        json.dumps(result),
        200,
        {"Content-Type": "application/json"})


def close_features(lon, lat, radius):
    features = geojson.loads(get_features()).features
    result = []
    for feature in features:
        feature_location = asShape(feature.geometry).representative_point()
        user_location = (lat, lon)
        feature_location = (feature_location.y, feature_location.x)
        distance = haversine(user_location, feature_location)
        if distance <= radius:
            result.append({'distance': distance, 'details': feature.properties})
    return sorted(result, key=itemgetter('distance'))


def get_features():
    try:
        result = requests.get(GEOJSON_URL)
        return result.text
    except requests.exceptions.RequestException:
        raise

if __name__ == '__main__':
    app.run()
