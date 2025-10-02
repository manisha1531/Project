import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px

st.title ("Employee Database")
employee= {
    "emp_id":[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "name":["Ram","Sham","Diya","Komal","Preet","Naman","Rohan","Aryan","Gaurav","Sagar"],
    "job":["clerk","manager","saleman","manager","clerk","testing","president","testing","clerk","president"],
    "salary":[22000,25000,35000,85000,65000,75000,450000,90000,10000,60000],
    "comm":[100,None,200,300,None,100,200,None,None,200],
    "deptno":[10,20,30,40,20,50,20,10,30,20]
     }
df=pd.DataFrame(employee)
choose=st.multiselect("choose your job",df["job"].unique())
st.write("employee")
st.dataframe(df)
gender=st.sidebar.radio("choose your gender",["male","female"])
if choose:
    filter_df=df[df["job"].isin (choose)]
    st.dataframe(filter_df)

st.title("employee")
fig=px.bar(filter_df,x="name",y="salary",text="salary")
st.plotly_chart(fig)

 
fig2=px.pie(filter_df,"name","salary","comm")
st.plotly_chart(fig2)

fig3=px.line(filter_df,x="name",y="salary",text="salary")
st.plotly_chart(fig3)

fig4=px.area(filter_df,x="emp_id",y="salary",text="salary")
st.plotly_chart(fig4)

fig = px.scatter(
    df,
    x="deptno", 
    y="salary",
    color="job", 
    size="salary", 
    hover_name="name",
    title="Employee Salary by Department"
)

st.plotly_chart(fig)