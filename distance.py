import os
import googlemaps

class DistanceCalculator:
    def __init__(self, origin, destination):
        self.client = googlemaps.Client(os.environ.get("GOOGLE_API_KEY"))
        self.origin = origin
        self.destination = destination

    def calculate(self):
        response = self.client.distance_matrix(self.origin, self.destination, departure_time="now", units="imperial")
        return response["rows"][0]["elements"][0]["duration"]["text"]

