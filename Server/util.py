import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft):
    try:
        loc_index = __data_columns.index(location)
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    # x[1] = bath
    # x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0]) 

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading Information")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/banglore_home_prices_model_random.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading Information Completed !!!")

if __name__ == '__main__':
    load_saved_artifacts()    