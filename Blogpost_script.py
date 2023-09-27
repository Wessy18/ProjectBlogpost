#!/usr/bin/env python
# coding: utf-8

# # Project  blogpost team 12

# **Pierce, Nikhil, Oskay. Adam, Wesley**

# # 1. Setup

# Setup the required packages for this project

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import nbformat


# In[ ]:





# In[4]:


jupyter nbconvert --to script your_notebook.ipynb


# # 2. Data Setup

# ## 2.1 The Netflix data 

# In[2]:


# loading in the netflix data from the csv file and assigning it to 'netflix' 
netflix = pd.read_csv('netflix_titles.csv')


# In[3]:


#test to see if the data is loaded in correctly
netflix.head()


# In[52]:


print(netflix.info())


# In[43]:


print(netflix.isna().sum())


# In[ ]:





# **Transforming the data**

# If we look at the dataset we see a column called description. This column gives a brief summary of the movie/show. The data column called cast lists the different star cast members in the movie/show. These data columns aren't usefull for our project, therefore we will remove it from the dataset. 

# In[4]:


# We will drop the column description and cast and update the dataset
netflix = netflix.drop(columns=['description','cast'])


# In[5]:


# See if the desirerd result has been achieved
netflix.head()


# We want to seperate the Movie and TV Show type so we can look at them seperatly. To achieve this we will make 2 new datasets. One containing all the movies (called netflix_movies) and one containing all tvshows (called netflix_tvshow)

# In[6]:


#Creating 2 new datasets to seperate the 'type' colomn of the original dataset
netflix_movies = netflix[netflix['type'] == 'Movie']
netflix_tvshow = netflix[netflix['type'] == 'TV Show']


# In[7]:


netflix_movies.head()


# In[8]:


netflix_tvshow.head()


# In[ ]:





# ## 2.2 The Disney+ data

# In[9]:


# loading in the disney data from the csv file and assigning it to 'disney' 
disney = pd.read_csv('disney_plus_titles.csv')


# In[10]:


#test to see if the data is loaded in correctly
disney.head()


# In[51]:


print(disney.info())


# In[37]:


print(disney.isna().sum())


# In[ ]:





# **Transforming the data**

# Just like before we won't be needing the columns description and cast and will be dropping it from the data

# In[11]:


# We will drop the column description and cast and update the dataset
disney = disney.drop(columns=['description','cast'])


# In[12]:


# See if the desirerd result has been achieved
disney.head()


# Again we would like to seperate the type into two different datasets so we can look at the movies and Tv shows seperatly

# In[13]:


#Creating 2 new datasets to seperate the 'type' colomn of the original dataset
disney_movies = disney[disney['type'] == 'Movie']
disney_tvshow = disney[disney['type'] == 'TV Show']


# In[14]:


disney_movies.head()


# In[15]:


disney_tvshow.head()


# In[ ]:





# ## 2.3 The Amazon Prime data 

# In[16]:


# loading in the amazon data from the csv file and assigning it to 'amazon' 
amazon = pd.read_csv('amazon_prime_titles.csv')


# In[17]:


#test to see if the data is loaded in correctly
amazon.head()


# In[50]:


print(amazon.info())


# In[38]:


print(amazon.isna().sum())


# In[ ]:





# **Transforming the data**

# Just like before we won't be needing the columns description and cast and will be dropping it from the data

# In[18]:


# We will drop the column description and cast and update the dataset
amazon = amazon.drop(columns=['description','cast'])


# In[19]:


# See if the desirerd result has been achieved
amazon.head()


# In[ ]:





# In[20]:


#Creating 2 new datasets to seperate the 'type' colomn of the original dataset
amazon_movies = amazon[amazon['type'] == 'Movie']
amazon_tvshow = amazon[amazon['type'] == 'TV Show']


# In[21]:


amazon_movies.head()


# In[22]:


amazon_tvshow.head()


# In[ ]:





# ## 2.4 The Hulu data 

# In[23]:


# loading in the hulu data from the csv file and assigning it to 'hulu' 
hulu = pd.read_csv('hulu_titles.csv')


# In[24]:


#test to see if the data is loaded in correctly
hulu.head()


# In[49]:


print(hulu.info())


# In[40]:


print(hulu.isna().sum())


# In[ ]:





# In[25]:


# We will drop the column description and update the dataset
hulu = hulu.drop(columns=['description','cast'])


# In[26]:


# See if the desirerd result has been achieved
hulu.head()


# In[ ]:





# In[27]:


#Creating 2 new datasets to seperate the 'type' colomn of the original dataset
hulu_movies = hulu[hulu['type'] == 'Movie']
hulu_tvshow = hulu[hulu['type'] == 'TV Show']


# In[28]:


hulu_movies.head()


# In[29]:


hulu_tvshow.head()


# In[ ]:





# # 3. Visualisations

# In[35]:


# Calculate the count of movies for each duration on Netflix and add it as a new column 'netflix_count'.
netflix_movies.loc[netflix_movies['type'] == 'Movie', 'netflix_count'] = netflix_movies.groupby('duration')['type'].transform('size')

# Convert the 'duration' column to numeric values (in minutes) if it's not already in string format.
netflix_movies['duration'] = netflix_movies['duration'].astype(str).str.extract('(\d+)').astype(float)

# Sort the Netflix movie DataFrame by duration.
netflix_movies = netflix_movies.sort_values(by='duration')

# Calculate the count of movies for each duration on Disney+ and add it as a new column 'disney_count'.
disney_movies.loc[disney_movies['type'] == 'Movie', 'disney_count'] = disney_movies.groupby('duration')['type'].transform('size')

# Convert the 'duration' column to numeric values (in minutes) if it's not already in string format.
disney_movies['duration'] = disney_movies['duration'].astype(str).str.extract('(\d+)').astype(float)

# Sort the Disney+ movie DataFrame by duration.
disney_movies = disney_movies.sort_values(by='duration')

# Calculate the count of movies for each duration on Amazon Prime Video and add it as a new column 'amazon_count'.
amazon_movies.loc[amazon_movies['type'] == 'Movie', 'amazon_count'] = amazon_movies.groupby('duration')['type'].transform('size')

# Convert the 'duration' column to numeric values (in minutes) if it's not already in string format.
amazon_movies['duration'] = amazon_movies['duration'].astype(str).str.extract('(\d+)').astype(float)

# Sort the Amazon Prime Video movie DataFrame by duration.
amazon_movies = amazon_movies.sort_values(by='duration')

# Calculate the count of movies for each duration on Hulu and add it as a new column 'hulu_count'.
hulu_movies.loc[hulu_movies['type'] == 'Movie', 'hulu_count'] = hulu_movies.groupby('duration')['type'].transform('size')

# Convert the 'duration' column to numeric values (in minutes) if it's not already in string format.
hulu_movies['duration'] = hulu_movies['duration'].astype(str).str.extract('(\d+)').astype(float)

# Sort the Hulu movie DataFrame by duration.
hulu_movies = hulu_movies.sort_values(by='duration')

# Create a subplot figure for the line plots.
fig = make_subplots(rows=1, cols=1)

# Add a line plot for Netflix movie counts with the color red.
netflix_trace = go.Scatter(x=netflix_movies['duration'], y=netflix_movies['netflix_count'], name='Netflix', line=dict(color='red'))
fig.add_trace(netflix_trace)

# Add a line plot for Disney+ movie counts with the color blue.
disney_trace = go.Scatter(x=disney_movies['duration'], y=disney_movies['disney_count'], name='Disney', line=dict(color='blue'))
fig.add_trace(disney_trace)

# Add a line plot for Amazon Prime Video movie counts with the color yellow.
amazon_trace = go.Scatter(x=amazon_movies['duration'], y=amazon_movies['amazon_count'], name='Amazon', line=dict(color='orange'))
fig.add_trace(amazon_trace)

# Add a line plot for Hulu movie counts with the color green.
hulu_trace = go.Scatter(x=hulu_movies['duration'], y=hulu_movies['hulu_count'], name='Hulu', line=dict(color='green'))
fig.add_trace(hulu_trace)

# Update the layout of the graph with a title, axis labels, and legend positioning.
fig.update_layout(title='Duration of movies on different streaming services',
                  xaxis_title='Duration (in minutes)',
                  yaxis_title='Number of movies',
                  legend=dict(x=1, y=1, traceorder='normal'))

# Add a range slider to the x-axis for interactive zooming and limit it so it can't go below zero
fig.update_xaxes(rangeslider_visible=True, rangemode='tozero')

# Display the interactive graph.
fig.show()


# In[ ]:





# In[34]:


# Calculate the count of TV shows for each duration on Netflix and add it as a new column 'netflix_count'.
netflix_tvshow.loc[netflix_tvshow['type'] == 'TV Show', 'netflix_count'] = netflix_tvshow.groupby('duration')['type'].transform('size')

# Convert the 'duration' column to numeric values (in seasons) if it's not already in string format.
netflix_tvshow['duration'] = netflix_tvshow['duration'].astype(str).str.extract('(\d+)').astype(float)

# Sort the Netflix TV show DataFrame by duration.
netflix_tvshow = netflix_tvshow.sort_values(by='duration')

# Calculate the count of TV shows for each duration on Disney+ and add it as a new column 'disney_count'.
disney_tvshow.loc[disney_tvshow['type'] == 'TV Show', 'disney_count'] = disney_tvshow.groupby('duration')['type'].transform('size')

# Convert the 'duration' column to numeric values (in seasons) if it's not already in string format.
disney_tvshow['duration'] = disney_tvshow['duration'].astype(str).str.extract('(\d+)').astype(float)

# Sort the Disney+ TV show DataFrame by duration.
disney_tvshow = disney_tvshow.sort_values(by='duration')

# Calculate the count of TV shows for each duration on Amazon Prime Video and add it as a new column 'amazon_count'.
amazon_tvshow.loc[amazon_tvshow['type'] == 'TV Show', 'amazon_count'] = amazon_tvshow.groupby('duration')['type'].transform('size')

# Convert the 'duration' column to numeric values (in seasons) if it's not already in string format.
amazon_tvshow['duration'] = amazon_tvshow['duration'].astype(str).str.extract('(\d+)').astype(float)

# Sort the Amazon Prime Video TV show DataFrame by duration.
amazon_tvshow = amazon_tvshow.sort_values(by='duration')

# Calculate the count of TV shows for each duration on Hulu and add it as a new column 'hulu_count'.
hulu_tvshow.loc[hulu_tvshow['type'] == 'TV Show', 'hulu_count'] = hulu_tvshow.groupby('duration')['type'].transform('size')

# Convert the 'duration' column to numeric values (in seasons) if it's not already in string format.
hulu_tvshow['duration'] = hulu_tvshow['duration'].astype(str).str.extract('(\d+)').astype(float)

# Sort the Hulu TV show DataFrame by duration.
hulu_tvshow = hulu_tvshow.sort_values(by='duration')

# Create a subplot figure for the line plots.
fig = make_subplots(rows=1, cols=1)

# Add a line plot for Netflix TV show counts with the color red.
netflix_trace = go.Scatter(x=netflix_tvshow['duration'], y=netflix_tvshow['netflix_count'], name='Netflix', line=dict(color='red'))
fig.add_trace(netflix_trace)

# Add a line plot for Disney+ TV show counts with the color blue.
disney_trace = go.Scatter(x=disney_tvshow['duration'], y=disney_tvshow['disney_count'], name='Disney', line=dict(color='blue'))
fig.add_trace(disney_trace)

# Add a line plot for Amazon Prime Video TV show counts with the color yellow.
amazon_trace = go.Scatter(x=amazon_tvshow['duration'], y=amazon_tvshow['amazon_count'], name='Amazon', line=dict(color='orange'))
fig.add_trace(amazon_trace)

# Add a line plot for Hulu TV show counts with the color green.
hulu_trace = go.Scatter(x=hulu_tvshow['duration'], y=hulu_tvshow['hulu_count'], name='Hulu', line=dict(color='green'))
fig.add_trace(hulu_trace)

# Update the layout of the graph with a title, axis labels, and legend positioning.
fig.update_layout(title='Duration of TV Shows on different streaming services',
                  xaxis_title='Duration (in seasons)',
                  yaxis_title='Number of series',
                  legend=dict(x=1, y=1, traceorder='normal'))

# Add a range slider to the x-axis for interactive zooming and limit it so it can't go below zero
fig.update_xaxes(rangeslider_visible=True, rangemode='tozero')

# Display the interactive graph.
fig.show()


# In[ ]:





# In[32]:


# Calculate the top 5 directors with the most content on Netflix.
director_count_netflix = netflix['director'].value_counts().head(5)

# Calculate the top 5 directors with the most content on Disney+.
director_count_disney = disney['director'].value_counts().head(5)

# Calculate the top 5 directors with the most content on Amazon Prime Video.
director_count_amazon = amazon['director'].value_counts().head(5)

# Assign colors to represent each streaming service.
color_netflix = 'red'
color_disney = 'blue'
color_amazon = 'orange'

# Create trace objects for the bar chart for each streaming service with assigned colors.
trace_netflix = go.Bar(x=director_count_netflix.index, y=director_count_netflix.values, name='Netflix',
                       marker=dict(color=color_netflix))
trace_disney = go.Bar(x=director_count_disney.index, y=director_count_disney.values, name='Disney+',
                      marker=dict(color=color_disney))
trace_amazon = go.Bar(x=director_count_amazon.index, y=director_count_amazon.values, name='Amazon Prime Video',
                      marker=dict(color=color_amazon))

# Create the figure with the trace objects.
fig = go.Figure(data=[trace_netflix, trace_disney, trace_amazon])

# Update the layout of the graph with a title, axis labels, and grouping bars together.
fig.update_layout(
    title='Top 5 directors on different streaming services',
    xaxis=dict(title='Director'),
    yaxis=dict(title='Number of Movies / TV Shows Directed'),
    barmode='group'
)

# Show the graph.
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




