import streamlit as st
import requests

import numpy as np
import pandas as pd
import datetime

'''
# Your Taxi assistant is ready to help
'''
def get_map_data():

    return pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)

st.markdown('''Let us know what's your best taxi fit 🚕

Select in the below fields:
''')
d = st.date_input("Your preferred date", datetime.date(2019, 7, 6))

t = st.time_input('Your preferred time', datetime.time(8, 45, 00))

st.write('You need the taxi on:', d, t)

pickup_longtitude = st.number_input('Your longtitude?')
pickup_latitude = st.number_input('Your latitude?')

st.write('Your pick up should be at these coordinates: ', pickup_longtitude, pickup_latitude)

dropoff_longtitude = st.number_input('Destination ongtitude?')
dropoff_latitude = st.number_input('Destination atitude?')

st.write('You want to be dropped off here: ', dropoff_longtitude, dropoff_latitude)

passenger_count = st.slider('How many passengers are you?', 1, 5, 1)

st.write('You are: ', passenger_count)


datetime=f'{d} {t}'
params = {
    "pickup_datetime": datetime,
    "pickup_longitude": pickup_longtitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longtitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

if st.button('Calculate the price'):


    url = 'https://taxifare.lewagon.ai/predict?'
    #url = url +'pickup_datetime=' + '+' + str(d) + str(t) + '&pickup_longtitude=' + str(pickup_longtitude) + '&pickup_latitude=' + str(pickup_latitude) + '&dropoff_longtitude=' + str(dropoff_longtitude) + '&dropoff_latitude=' + str(dropoff_latitude) + '&passenger_count=' + str(passenger_count)

    if url == 'https://taxifare.lewagon.ai/predict':
        st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


    pred = requests.get(url, params=params).json()

    st.write('Your taxi fare is: ', pred['fare'])
