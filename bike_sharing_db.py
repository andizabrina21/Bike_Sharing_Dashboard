#bikesharing_analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency
from matplotlib.ticker import FuncFormatter
sns.set(style='dark')

#MENYIAPKAN DATAFRAME
def create_daily_sharing_df(df):
    daily_sharing_df = df.resample(rule='D', on='dteday').agg({
        "cnt": "sum",
        "casual": "sum",
        "registered": "sum"
    })
    daily_sharing_df = daily_sharing_df.reset_index()
    
    return daily_sharing_df

def create_peak_hour_df(df):
    peak_hour_df = df.groupby("hr")["cnt"].sum().idxmax()
    return peak_hour_df

def create_total_sharing_bike_df(df):
    total_sharing_bike_df = df.groupby("hr").cnt.sum().sort_values(ascending=False).reset_index()

    return total_sharing_bike_df

def create_byday_df(df):
    byday_df = df.groupby(by="weekday").cnt.sum().reset_index()
    byday_df.rename(columns={
        "cnt": "count",
    }, inplace=True)
    byday_df['weekday'] = pd.Categorical(byday_df['weekday'].map({0: 'Minggu',1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'}), ordered=True)

    return byday_df

def create_byhour_df(df):
    byhour_df = df.groupby(by="hr").cnt.sum().reset_index()
    byhour_df.rename(columns={
        "cnt": "count"
    }, inplace=True)

    return byhour_df

def create_byyear_df(df):
    byyear_df = df.groupby(by="yr").cnt.sum().reset_index()
    byyear_df.rename(columns={
        "cnt": "count"
    }, inplace=True)

    byyear_df['yr'] = pd.Categorical(byyear_df['yr'].map({0: '2011', 1: '2012'}), ordered=True)

    return byyear_df

def create_bymnth_df(df):
    bymnth_df = df.groupby(by="mnth").cnt.sum().reset_index()
    bymnth_df.rename(columns={
        "cnt": "count",
    }, inplace=True)
    
    bymnth_df['mnth'] = pd.Categorical(bymnth_df['mnth'].map({
        1: 'January', 2: 'February', 
        3: 'March', 4: 'April', 
        5: 'May', 6: 'June', 
        7: 'July', 8: 'August',
        9: 'September', 10: 'October',
        11: 'November', 12:'December'}), ordered=True)
    return bymnth_df

def create_by_season_df(df):
    byseason_df = df.groupby(by="season").cnt.sum().reset_index()
    byseason_df.rename(columns={
        "cnt": "count"
    }, inplace=True)

    byseason_df['season'] = pd.Categorical(byseason_df['season'].map({1: 'Musim Semi',2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}), ordered=True)

    return byseason_df

def create_by_weather_df(df):
    byweather_df = df.groupby(by="weathersit").cnt.sum().reset_index()
    byweather_df.rename(columns={
        "cnt": "count"
    }, inplace=True)

    byweather_df['weathersit'] = pd.Categorical(byweather_df['weathersit'].map({1: 'Cerah',2: 'Kabut', 3: 'Salju Ringan', 4: 'Hujan Lebat'}), ordered=True)

    return byweather_df

def create_workingday_df(df):
    byworkingday_df = df.groupby(by="workingday")[["casual", "registered"]].sum().reset_index()
    byworkingday_df['workingday'] = pd.Categorical(byworkingday_df['workingday'].map({
        0: 'Weekend/Holiday', 
        1: 'Working Day'}), ordered=True)
    byworkingday_df.rename(columns={
        "casual": "Casual",
        "registered": "Registered"
    }, inplace=True)
    byworkingday_df = byworkingday_df.melt(id_vars='workingday',
                                       var_name='user_type',
                                       value_name='count')
    return byworkingday_df

def create_userhour_df(df):
    byuserhour_df = df.groupby("hr")[["casual", "registered"]].sum().reset_index()
    return byuserhour_df

def create_bytemp_df(df):
    bytemp_df = df.groupby(by="dteday").agg({"temp":"mean"})
    return bytemp_df

def create_byhum_df(df):
    byhum_df = df.groupby(by='dteday').agg({"hum":"mean"})
    return byhum_df

def create_bywindspeed_df(df):
    bywindspeed_df = df.groupby(by="dteday").agg({"windspeed":"mean"})
    return bywindspeed_df

day_df = pd.read_csv("data/data_day.csv")
hour_df = pd.read_csv("data/data_hours.csv")

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

min_date = hour_df["dteday"].min()
max_date = hour_df["dteday"].max()

with st.sidebar:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/andizabrina21/bike_sharing_db/main/images/bikepic.jpg", caption="Pic From Google")

    start_date, end_date = st.date_input(
        "Rentang Waktu",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    st.markdown("""
    <h2 style='text-align:center;'>🚲 Capital Bikeshare</h2>
    
    <p style='font-size:16px; text-align:justify;'>
    Capital Bikeshare is a public bicycle-sharing system serving the Washington, D.C.
    It launched in 2010 and has grown into one of the largest bike-share programs in the United States.
    </p>
    
    <p style='font-size:16px; text-align:justify;'>
    The system allows users to rent bikes from automated stations and return them to any other station in the network.
    This flexibility makes it a convenient option for short trips, commuting, and last-mile connectivity.
    </p>
    """, unsafe_allow_html=True)

main_df = hour_df[(hour_df["dteday"] >= str(start_date)) & 
                (hour_df["dteday"] <= str(end_date))]

daily_sharing_df = create_daily_sharing_df(main_df)
peak_hour_df = create_peak_hour_df(main_df)
bytemp_df = create_bytemp_df(main_df)
byhum_df = create_byhum_df(main_df)
bywindspeed_df = create_bywindspeed_df(main_df)
total_sharing_bike_df = create_total_sharing_bike_df(main_df)
byday_df = create_byday_df(main_df)
byhour_df = create_byhour_df(main_df)
byyear_df = create_byyear_df(main_df)
bymnth_df = create_bymnth_df(main_df)
byseason_df = create_by_season_df(main_df)
byweather_df = create_by_weather_df(main_df)
byworkingday_df = create_workingday_df(main_df)
byuserhour_df = create_userhour_df(main_df)

#MELENGKAPI DASHBOARD DGN VISUALISASI DATA
st.header('Bike Sharing Dashboard :bike:')

st.subheader('Key Metrics Overview of Bike Sharing Usage')

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sharing = daily_sharing_df.cnt.sum()
    st.metric("Total Rides", value=total_sharing)

with col2:
    total_casual = daily_sharing_df.casual.sum()
    st.metric("Total Casual", value=total_casual)

with col3:
    total_registered = daily_sharing_df.registered.sum()
    st.metric("Total Registered", value=total_registered)

with col4:
    st.metric("Peak Hour", value=f"{peak_hour_df:02d}:00")

with st.expander("see explanation"):
    st.write(
        "**Total Rides** represents the overall number of bike-sharing users."
    )
    st.write(
        "**Total Casual** refers to the total number of non-registered users."
    )
    st.write(
        "**Total Registered** refers to the total number of registered users"
    )
    st.write(
        "**Peak Hour** shows the hour of the day with the highest number of bike rentals."
    )

st.subheader("User Trends Over Time")
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(8, 4))
    colors = "rocket"
    sns.barplot(
        y="count",
        x="yr",
        data=byyear_df,
        order=byyear_df.sort_values(by="count", ascending=False).yr,
        palette=colors
    )
    for container in ax.containers:
        labels = [f'{v/1000:.2f}K' for v in container.datavalues]
        ax.bar_label(container, labels=labels, padding=2)
    ax.set_title("Annual User Trends")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Users")
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}K'))
    ax.tick_params(labelsize=12)
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots(figsize=(8, 4))
    colors = "rocket"
    sns.barplot(
        y="count",
        x="mnth",
        data=bymnth_df,
        order=bymnth_df.sort_values(by="count", ascending=False).mnth,
        palette=colors
    )
    for container in ax.containers:
        labels = [f'{v/1000:.2f}K' for v in container.datavalues]
        ax.bar_label(container, labels=labels, padding=5)
    ax.set_title("Monthly User Trends")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Users")
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}K'))
    ax.tick_params(labelsize=12)
    st.pyplot(fig)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(
        byday_df["weekday"],
        byday_df["count"],
        marker='o',
        markersize=10,
        linewidth=5,
        color="C22100",
    )
    ax.set_title("Daily User Trends")#, loc="center", fontsize=25)
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Users")
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}K'))
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)
    for x, y in zip(byday_df["weekday"], byday_df["count"]):
        ax.text(
            x, y,
            f'{y/1000:.1f}K',
            ha='center',
            va='bottom',
            fontsize=18
        )
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    plt.plot(
        byhour_df['hr'],
        byhour_df["count"],
        marker='o',
        markersize=10,
        linewidth=5,
        color="C22100",
    )
    ax.set_title("Hourly User Trends")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Number of Users")
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}K'))
    ax.set_xticks(range(24))
    ax.set_xticklabels([f"{i:02d}:00" for i in range(24)], rotation=45)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)
    for x, y in zip(byhour_df["hr"], byhour_df["count"]):
        ax.text(
            x, y,
            f'{y/1000:.1f}K',
            ha='center',
            va='bottom',
            fontsize=15
        )
    plt.tight_layout()
    st.pyplot(fig)

st.subheader("Environmental Impact")
col1, col2, col3 = st.columns(3)
with col1:
    rounded_mean_temp = round(bytemp_df['temp'].mean() * 41, 2)
    st.metric(label="Temperature", value=f"{rounded_mean_temp}°C")
with col2:
    rounded_mean_wind = round(bywindspeed_df['windspeed'].mean() * 67, 2)
    st.metric(label="Windspeed", value=f"{rounded_mean_wind}km/h")
with col3:
    rounded_mean_hum = round(byhum_df['hum'].mean() * 100, 2)
    st.metric(label="Humidity", value=f"{rounded_mean_hum}%")
with st.expander("see explanation"):
    st.caption('These metrics represent the average temperature, windspeed, and humidity during the bike-sharing usage period.')

col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(10, 5))
    colors="rocket"
    sns.barplot(
        y="count",
        x="season",
        data = byseason_df,
        order = byseason_df.sort_values(by="count", ascending=False).season,
        palette=colors,
        ax=ax
    )
    for container in ax.containers:
        labels = [f'{v/1000:.2f}K' for v in container.datavalues]
        ax.bar_label(container, labels=labels, padding=5)
    ax.set_title("Impact of Season on User Activity")
    ax.set_xlabel("Season")
    ax.set_ylabel("Number of Users")
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}K'))
    ax.tick_params(labelsize=12)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(10, 5))
    colors="rocket"
    sns.barplot(
        y="count",
        x="weathersit",
        data = byweather_df, 
        order = byweather_df.sort_values(by="count", ascending=False).weathersit,
        palette=colors,
        ax=ax
    )
    for container in ax.containers:
        labels = [f'{v/1000:.2f}K' for v in container.datavalues]
        ax.bar_label(container, labels=labels, padding=5)
    ax.set_title("Impact of Weather on User Activity")
    ax.set_xlabel("Weather")
    ax.set_ylabel("Number of Users")
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}K'))
    ax.tick_params(labelsize=12)
    st.pyplot(fig)

st.subheader("User Segmentation: Casual vs Registered")
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(10, 5))
    casual_total = daily_sharing_df["casual"].sum()
    registered_total = daily_sharing_df["registered"].sum()
    labels = [
        f"Casual\n({casual_total/1000:.1f}K)",
        f"Registered\n({registered_total/1000:.1f}K)"
    ]
    sizes = [casual_total, registered_total]
    colors = sns.color_palette("rocket")

    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        explode=(0.05, 0)
    )
    ax.set_title('User Type Distribution')
    ax.axis('equal')
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(10, 5))
    colors="rocket"
    sns.barplot(
        y="count",
        x="workingday",
        hue="user_type",
        data = byworkingday_df,
        palette=colors
    )
    for container in ax.containers:
        labels = [f'{v/1000:.2f}K' for v in container.datavalues]
        ax.bar_label(container, labels=labels, padding=5)
    ax.set_title("User Type Behaviour by Day Type")
    ax.set_xlabel("Day Type")
    ax.set_ylabel("Number of Users")
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}K'))
    ax.legend(title='User Type')
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(
    data=byuserhour_df,
    x="hr",
    y="casual",
    color="8A1F08",
    label="Casual",
    linewidth=2
)

sns.lineplot(
    data=byuserhour_df,
    x="hr",
    y="registered",
    color="C22100",
    label="Registered",
    linewidth=2
)
ax.set_title("User Type Behaviour by Hour")
ax.set_xlabel("Hour")
ax.set_ylabel("Number of Users")
ax = plt.gca()
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}K'))
ax.legend(title='User Type')
ax.tick_params(labelsize=12)
st.pyplot(fig)
