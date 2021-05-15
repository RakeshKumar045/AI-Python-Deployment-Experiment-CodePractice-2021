import pickle

from fastapi import FastAPI
from pydantic import BaseModel

from model_files.data_transformation import predict_mpg


class Vehicle(BaseModel):
    cylinders: int = 42
    displacement: float = 155.0
    horsepower: float = 93.0
    weight: float = 3500.0
    acceleration: float = 15.0
    model_year: int = 60


app = FastAPI()


@app.get("/")
def root():
    return {'message': "Hello World!"}


@app.get("/raka_testing")
def raka_test():
    return {'message': "rakesh kumar"}


@app.get("/test1")
def test1():
    return {'message': "welcome raka"}


@app.post("/predict")
def predict(vehicle: Vehicle):
    '''
    This is the main prediction function which returns
    mileage of a vehicle.
    '''
    vehicle_config = {
        'Cylinder': [vehicle.cylinders],
        'Displacement': [vehicle.displacement],
        'Horsepower': [vehicle.horsepower],
        'Weight': [vehicle.weight],
        'Acceleration': [vehicle.acceleration],
        'Model Year': [vehicle.model_year],
    }

    with open('./model_files/model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()

    prediction = predict_mpg(vehicle_config, model)

    result = {'mpg_prediction': list(prediction)}
    return result

# run this command in terminal : uvicorn main:app --reload
# do not run : python main.py

# please must check fastapi run, it will be very compulsory
# check : http://127.0.0.1:8000/docs
