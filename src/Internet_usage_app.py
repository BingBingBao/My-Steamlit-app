import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

def load_data(path):
    df = pd.read_csv(path)
    return df

df_raw = load_data(path="./data/raw/share-of-individuals-using-the-internet.csv")
df_1 = deepcopy(df_raw)

# Add title, header and text
st.title("Internet Usage Across Countries (1997 - 2017)")
st.header("Discover the Global Internet Landscape with Our Interactive Map App!")
st.text("""
Explore how internet usage has transformed the world over the years with this
user-friendly web application. This app visualizes the percentage of individuals 
using the internet in countries worldwide between 1997 and 2007. 
                                     """)
st.markdown('''Dive into the data by selecting different years to see the rapid 
growth of internet penetration across the globe.
        ''')

# data from 1997 to 2017
df = df_1[(df_1.Year >= 1997) & (df_1.Year <= 2017)]

# side bar
if st.sidebar.checkbox("Show Data"):

    st.sidebar.subheader("Internet Usage (1997-2017):")
    st.sidebar.dataframe(data=df)

if st.sidebar.checkbox("More info"):
    st.sidebar.markdown("[Learn more about global internet usage](https://ourworldindata.org/internet#introduction)")




################
## Plotly
##############

geojson_path = './data/raw/countries.geojson'
with open(geojson_path) as f:
    geojson = json.load(f)



# years = sorted(pd.unique(df['Year']))

# year = st.selectbox("Select a Year", years)


# df_selected = df[df['Year'] == year]
    
# fig = px.choropleth_mapbox(
#     df_selected, 
#     geojson=geojson,
#     locations="Code", 
#     color="Individuals using the Internet (% of population)",  
#     featureidkey="properties.ISO_A3", 
#     mapbox_style="carto-positron",  
#     center={"lat": 60, "lon": 20},  
#     zoom=0.8,  
#     color_continuous_scale="Oranges", 
#     range_color=(0, 100),  
#     hover_name="Entity",            
#     hover_data={"Individuals using the Internet (% of population)": True}
# )


# fig.update_geos(
#         visible=False, 
#         showcountries=True,  
#         showcoastlines=True,  
#         lonaxis_range=[-180, 180],  
#         lataxis_range=[-90, 90] )


# fig.update_layout(
#         margin={"r": 0, "t": 0, "l": 0, "b": 0}, 
#         title_font_size=22,  
#         title_x=0.5, 
#         height=800, 
#         width=1200,  
#         coloraxis_colorbar=dict(
#             title = "Internet Usage%",  
#             tickvals=[0, 20, 40, 60, 80, 100],  
#             ticktext=["0%", "20%", "40%", "60%", "80%", "100%"]
#         )
#     )


# # show the plot
# st.plotly_chart(fig, use_container_width=True)

# # write the explanantion of fig
# st.write(f"Displaying the data for year {year}")


###########################
### slider
####################


years = sorted(pd.unique(df['Year']))

year = st.select_slider("Select a Year", options=years)

df_selected = df[df['Year'] == year]

#############
# plotly mapbox
###############

fig = px.choropleth_mapbox(
    df_selected, 
    geojson=geojson,
    locations="Code", 
    color="Individuals using the Internet (% of population)",  
    featureidkey="properties.ISO_A3", 
    mapbox_style="carto-positron",  
    center={"lat": 60, "lon": 20},  
    zoom=0.8,  
    color_continuous_scale="Oranges", 
    range_color=(0, 100),  
    hover_name="Entity",            
    hover_data={"Individuals using the Internet (% of population)": True}
)


fig.update_geos(
        visible=False, 
        showcountries=True,  
        showcoastlines=True,  
        lonaxis_range=[-180, 180],  
        lataxis_range=[-90, 90] )


fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0}, 
        title_font_size=22,  
        title_x=0.5, 
        height=800, 
        width=1200,  
        coloraxis_colorbar=dict(
            title = "Internet Usage%",  
            tickvals=[0, 20, 40, 60, 80, 100],  
            ticktext=["0%", "20%", "40%", "60%", "80%", "100%"]
        )
    )


# plot展示再app上
st.plotly_chart(fig, use_container_width=True)


st.write(f"Displaying the data for year {year}")