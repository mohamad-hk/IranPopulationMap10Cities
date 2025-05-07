import math
import re
import numpy as np


def DMS_to_decimal(data_frame):
    list_x = []
    list_y = []

    for lat_DMS, lon_DMS in zip(data_frame["Latitude"], data_frame["Longitude"]):
        lat_parts = lat_DMS.replace("\xa0", " ").split(" ")
        lon_parts = lon_DMS.replace("\xa0", " ").split(" ")
        lat_degree, lat_minute, lat_second = extract_DMS_values(lat_parts)
        lon_degree, lon_minute, lon_second = extract_DMS_values(lon_parts)
        lat_decimal = lat_degree + (lat_minute / 60) + (lat_second / 3600)
        lon_decimal = lon_degree + (lon_minute / 60) + (lon_second / 3600)

        temp_x, temp_y = lat_decimal, lon_decimal

        list_x.append(temp_x)
        list_y.append(temp_y)

    data_frame["lat_decimal"] = np.array(list_x)
    data_frame["lon_decimal"] = np.array(list_y)

    return data_frame


def extract_DMS_values(DMS_parts):
    degree = int(re.sub(r'[^0-9]', "", DMS_parts[0]))
    minute = int(re.sub(r'[^0-9]', "", DMS_parts[1]))
    second = int(re.sub(r'[^0-9]', "", DMS_parts[2]))
    return degree, minute, second


def to_Coordinate(lat_deg, lon_deg, R=6378137):
    lon_rad = math.radians(lon_deg)
    lat_rad = math.radians(lat_deg)

    x = R * lon_rad
    y = R * math.log(math.tan(math.pi / 4 + lat_rad / 2))

    return x, y
