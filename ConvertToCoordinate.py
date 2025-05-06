import math
import re


def dms_to_decimal():
    const_dms = "38° 4′ 26"
    parts = const_dms.split(" ")
    degree = int(re.sub(r'[^0-9]', "", parts[0]))
    minute = int(re.sub(r'[^0-9]', "", parts[1]))
    second = int(re.sub(r'[^0-9]', "", parts[2]))
    decimal = degree + (minute / 60) + (second / 3600)
    print(decimal)



dms_to_decimal()
