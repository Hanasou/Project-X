import json


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

    pass


if __name__ == '__main__':
    lat_home = 37.407398
    lon_hone = -121.859604
    lat_csu = 37.336718
    lon_cus = -121.881630
    print('Distance between home and CSU Engineering department is: ' + str(distance(lat_home, lon_hone, lat_csu, lon_cus)) + ' meters.');