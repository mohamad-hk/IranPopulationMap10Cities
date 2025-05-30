import pandas as pd
from ConvertToCoordinate import DMS_to_decimal


def pre_processing_data():
    data = pd.read_csv("iran.csv", encoding='utf-8')
    populations = data["Population"].values
    cities = data["City"].values

    df = DMS_to_decimal(data)

    return cities, populations,df
