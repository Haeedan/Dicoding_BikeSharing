
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df_bike_sharing = pd.read_csv("dataset.csv")
df_bike_sharing['dteday'] = pd.to_datetime(df_bike_sharing['dteday'], format='%Y %m %d')
df_temp_rent = df_bike_sharing[['season', 'temp', 'cnt']]
st.scatter_chart(df_temp_rent, x='temp', y='cnt')

x = ['Spring', 'Summer', 'Fall', 'Winter']
y = df_temp_rent.groupby("season")["cnt"].sum().values.tolist()
dfbar = pd.DataFrame(list(zip(x, y)),
               columns =['season', 'cnt'])

st.bar_chart(dfbar, x='season', y='cnt')
