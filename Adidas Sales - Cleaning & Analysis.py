#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from matplotlib import pyplot


# In[9]:


df = pd.read_excel(r"C:\Users\Nikkil\Desktop\Tableau Doc Store\Adidas US Sales.xlsx", sheet_name="Analysis")
df


# In[8]:


pd.set_option("display.max.rows", 9650)


# In[10]:


df.info()


# In[12]:


df = df.drop_duplicates()
df


# In[13]:


df.info()


# In[22]:


df[["City", "Units Sold"]] = df[["City", "Units Sold"]].replace("_","", regex=True)
df


# In[24]:


df


# In[27]:


df = df.drop("Operating Margin", axis=1)
df


# In[29]:


Region_wisw_Sales = df.groupby("Region").sum("Total Sales")
Region_wisw_Sales


# In[46]:


Region_wisw_Sales["Total Sales"].plot(kind="pie", title="Region Wise Total Sales", autopct="%.2f%%")


# In[48]:


Product_wise_Sales = df.groupby("Product").sum("Sales")
Product_wise_Sales


# In[80]:


Product_wise_Sales["Total Sales"].plot(kind="bar", color="skyblue", edgecolor="blue", lw=2, title="Product Wise Sales", ylabel="Sales", yticks=())


# In[83]:


Sales_Channels = df.groupby("Sales Method").sum("Total Sales")
Sales_Channels


# In[94]:


Sales_Channels["Total Sales"].plot(kind="barh", color="skyblue", edgecolor="blue", lw=2, width=0.4, title="Sales By Channels", ylabel="Sales Channels")


# In[98]:


Region_wisw_SalesandProfit = df.groupby("Region").sum("Total Sales")
Region_wisw_SalesandProfit


# In[102]:


Region_wisw_SalesandProfit[["Total Sales", "Operating Profit"]].plot(title="Regin Wise Sales & Profit", yticks=())


# In[ ]:




