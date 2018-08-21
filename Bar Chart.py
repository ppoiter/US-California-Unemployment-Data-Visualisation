
# coding: utf-8

# In[106]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np


# In[107]:


df = pd.read_csv('Unemployment_Rates_1967_To_2018.csv')


# In[108]:


df.head()


# In[109]:


df.dtypes


# In[110]:


df['Year'] = pd.to_datetime(df['Year'])
df['Year'] = pd.DatetimeIndex(df['Year']).year


# In[111]:


set_1 = df.iloc[33:,0:2]
set_1.head()


# In[112]:


set_2 = df.drop('California', axis = 1)
set_2 = set_2.iloc[33:,0:2]
set_2.head()


# In[113]:


trace1 = go.Bar(
    x=set_1['Year'],
    y=set_1['California'],
    name='California',
    marker=dict(
        color='rgb(169,169,169)'
    )
)
trace2 = go.Bar(
    x=set_2['Year'],
    y=set_2['U.S.'],
    name='USA',
    marker=dict(
        color='rgb(220,20,60)'
)
    )


# In[114]:


data = [trace1, trace2]
layout = go.Layout(
    title='California and USA Unemployment',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
            #tickangle=-45
            #tick0 = 0,
            #dtick = 5
        )
    ),
    yaxis=dict(
        title='% unemployment',
        titlefont=dict(
            size=18,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0.85,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='style-bar')

