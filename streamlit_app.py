import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.header('Ini percobaan Streamlit di Google Colab')

days_df = pd.read_csv("Bike-sharing-dataset/day.csv")

filtered_data = days_df[(days_df["yr"] == 1) & (days_df["workingday"] == 0)]

filtered_data_2 = days_df[(days_df["workingday"] == 1) | (days_df["workingday"] == 0)]

grouped_data = filtered_data.groupby(["dteday", "workingday"]).agg({
    "instant":"nunique",
    "cnt":["max", "min"]
}).reset_index()

grouped_data_2 = filtered_data_2.groupby(['workingday', 'weathersit'])['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(20, 5))
ax.plot(
    grouped_data["dteday"], grouped_data["cnt"]["max"],
    label="Maximum Count",
    marker='o',
    linewidth=2,
    color="#72BCD4"
)

ax.plot(
    grouped_data["dteday"], grouped_data["cnt"]["min"],
    label="Minimum Count",
    marker='o',
    linewidth=2,
    color="#72BCD4"
)
ax.set(title='Number of Orders Weekend (2012)')
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

figs, ax = plt.subplots(figsize=(10,6))
sns.barplot(data=grouped_data_2, x='weathersit', y='cnt', hue='workingday', palette=['skyblue', 'orange'])
ax.set(title='Working Day')

st.pyplot(figs)


    
