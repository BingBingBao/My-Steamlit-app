import streamlit as st
import pandas as pd
from copy import deepcopy
import matplotlib.pyplot as plt
import plotly.express as px


st.text('I change smth')

# mpg_df = pd.read_csv("./data/raw/mpg.csv")
# mpg_df

@st.cache_data # decorator  ????
def load_data(path):
    df = pd.read_csv(path)
    return df

mpg_df_raw = load_data(path="./data/raw/mpg.csv")

# 
mpg_df =deepcopy(mpg_df_raw) # for security

# see my df
# st.dataframe(data=mpg_df)
# create a side bar

if st.sidebar.checkbox("Show dataframe:"):
    st.dataframe(data=mpg_df)

# See a title
st.title('My 1st version')
st.header('MPG data exploration')

# create cols
col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

# 添加的新代码
left_column, middle_column, right_column = st.columns(3)

show_means = middle_column.radio(
    'Show Class Means', ['Yes', 'No']
)

# 选择年份的部分
years = ["All"] + sorted(pd.unique(mpg_df['year']))
year = left_column.selectbox("Choose a year", years)

# 根据选择的年份过滤数据
if year == "All":
    reduced_df = mpg_df
else:
    reduced_df = mpg_df[mpg_df["year"] == year]

#计算各类的平均值
means = reduced_df.groupby('class').mean(numeric_only=True)

# 定义绘图类型
plot_types = ["Matplotlib", "Plotly"]
plot_type = right_column.radio("Choose a plot type", plot_types)

m_fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(reduced_df['displ'], reduced_df['hwy'], alpha=0.7)
ax.set_title("Engine Size vs. Highway Fuel Mileage")
ax.set_xlabel('Displacement (Liters)')
ax.set_ylabel('MPG')

if show_means == "Yes":
    ax.scatter(means['displ'], means['hwy'], alpha=0.7,
               color="red", label="Class Means")

#st.pyplot(m_fig)
# In Plotly

p_fig = px.scatter(reduced_df, x='displ', y='hwy', opacity=0.5,
                   range_x=[1, 8], range_y=[10, 50],
                   width=750, height=600,
                   labels={"displ": "Displacement (Liters)",
                           "hwy": "MPG"},
                   title="Engine Size vs. Highway Fuel Mileage")

p_fig.update_layout(title_font_size=22)