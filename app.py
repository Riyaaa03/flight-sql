import streamlit as st
from helper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Flight Analytics')

user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)
    city = db.fetch_city_name()
    with col1:
        source = st.selectbox('Source',sorted(city))

    with col2:
        destination = st.selectbox('Destination',sorted(city))

    if st.button('Search'):
        result = db.fetch_all_flight(source,destination)
        st.dataframe(result)


elif user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels = airline,
            values = frequency,
            hoverinfo="label + percent",
            textinfo="value"
        )
    )
    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x = city,
        y = frequency1
    )
    st.header("Bar chart")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    city, frequency2 = db.daily_frequency()
    fig = px.line(
        x=city,
        y=frequency2
    )
    st.header("line chart")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.title('This is a comprehensive flight dashboard that displays real-time information on flights at various airports across India. The dashboard will also incorporate interactive maps using Plotly to visually represent the flight data.')