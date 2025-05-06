from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read Data from CSV
df=pd.read_csv("./DataSets/Sales Dataset.csv",index_col=0)

#Data Cleaning
#-------------------------------------------------------------------------------------
df.rename(columns=str.lower, inplace=True)
df.rename(columns={"paymentmode":"payment_mode","customername":"customer_name"},inplace=True)
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('-', '_')
df["order_date"]=pd.to_datetime(df["order_date"],yearfirst=True)
df["order_year"]=pd.DatetimeIndex(df["order_date"]).year
df["year_month"]=pd.to_datetime(df["year_month"])
df["actual_amount"]=df["amount"]-df["profit"]
df.drop(columns="amount",inplace=True)
df.drop(columns="year_month",inplace=True)
# Print Data from csv after cleansing
print(df.head(15))

def box_plots():
    #Data Visualization
    #-------------------------------------------------------------------------------------
    #Sales by Year
    fig,axes=plt.subplots(figsize=(12,10))
    s1=df.groupby("order_year")["quantity"].sum()
    s2=df["order_year"].unique()
    axes.bar(s2,s1,color="blue",width=0.5)
    axes.set_xlabel("Year",fontsize=15)
    axes.set_ylabel("Sales Calculated in Years",fontsize=15)
    axes.set_title("Sales by Year",fontsize=20)

    return fig.savefig("./Images/sales_by_year.png")

def piechart():
    #Pie Chart
    labels = df["payment_mode"].unique()
    data=df["payment_mode"].value_counts()
    myexplode = [0.2, 0, 0, 0,0]
    fig,axes=plt.subplots(figsize=(12,10))
    axes.pie(data,labels=labels,autopct='%1.1f%%',explode=myexplode)
    plt.title("Payment Mode",fontsize=20)
    return fig.savefig("./Images/payment_mode.png")