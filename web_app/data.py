import json
from math import sin, cos, sqrt, radians, asin

def distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two locations according to their lat/lon.

    Args:
        lat1: The latitude of first location.
        lon1: The longitude of first location.
        lat2: The latitude of second location.
        lon2: The longitude of second location.

    Returns:
        The distance (meters) between the two location.
    """

    # Approximation of Earth's radius in meters
    earth_radius = 6378100

    # Convert latitudes and longitudes to radians
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)

    # Distances of latitudes and longitudes
    dlat = lat1 - lat2
    dlon = lon1 - lon2

    # Haversine Formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    
    return earth_radius * c


if __name__ == '__main__':
    lat_home = 37.407398
    lon_home = -121.859604
    lat_csu = 37.336718
    lon_csu = -121.881630
    print('Distance between home and CSU Engineering department is: ' + str(distance(lat_home, lon_home, lat_csu, lon_csu)) + ' meters.')