import math
import re


def dms_to_decimal(lat_dms,lon_dms):
    #lat_dms = "38° 4′ 26"
    #lon_dms = "46° 17′ 46"
    lat_parts = lat_dms.split(" ")
    lon_parts = lon_dms.split(" ")
    lat_degree, lat_minute, lat_second = extract_Fomrat(lat_parts)
    lon_degree, lon_minute, lon_second = extract_Fomrat(lon_parts)

    lat_decimal = lat_degree + (lat_minute / 60) + (lat_second / 3600)
    lon_decimal = lon_degree + (lon_minute / 60) + (lon_second / 3600)
    print(to_Coordinate(lat_decimal, lon_decimal))


def extract_Fomrat(parts):
    degree = int(re.sub(r'[^0-9]', "", parts[0]))
    minute = int(re.sub(r'[^0-9]', "", parts[1]))
    second = int(re.sub(r'[^0-9]', "", parts[2]))
    return degree,minute,second


def to_Coordinate(lat_deg, lon_deg, R=6378137):
    lon_rad = math.radians(lon_deg)
    lat_rad = math.radians(lat_deg)

    x = R * lon_rad
    y = R * math.log(math.tan(math.pi / 4 + lat_rad / 2))
    return x, y
