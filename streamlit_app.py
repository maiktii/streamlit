import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.header('Ini percobaan Streamlit di Google Colab')

days_df = pd.read_csv("Bike-sharing-dataset/day.csv")

st.write(days_df)

filtered_data = days_df[(days_df["yr"] == 1) & (days_df["workingday"] == 0)]

filtered_data_2 = days_df[(days_df["workingday"] == 1) | (days_df["workingday"] == 0)]

grouped_data = filtered_data.groupby(["dteday", "workingday"]).agg({
    "instant":"nunique",
    "cnt":["max", "min"]
}).reset_index()

grouped_data_2 = filtered_data_2.groupby(['workingday', 'weathersit'])['cnt'].mean().reset_index()

grouped_data.head(5)
