#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Load the datasets for Netflix, Disney+, Amazon Prime, and Hulu
netflix = pd.read_csv('netflix_titles.csv')
disney = pd.read_csv('disney_plus_titles.csv')
amazon = pd.read_csv('amazon_prime_titles.csv')
hulu = pd.read_csv('hulu_titles.csv')

# Define platform names and corresponding dataframes
platforms = ["Netflix", "Disney", "Hulu", "Amazon"]
dataframes = [netflix, disney, hulu, amazon]

#Creating 2 new datasets to separate the 'type' column of the original dataset
hulu_movies = hulu[hulu['type'] == 'Movie']
hulu_tvshow = hulu[hulu['type'] == 'TV Show']
amazon_movies = amazon[amazon['type'] == 'Movie']
amazon_tvshow = amazon[amazon['type'] == 'TV Show']
disney_movies = disney[disney['type'] == 'Movie']
disney_tvshow = disney[disney['type'] == 'TV Show']
netflix_movies = netflix[netflix['type'] == 'Movie']
netflix_tvshow = netflix[netflix['type'] == 'TV Show']

st.title("How to Choose the Perfect Streaming Service?")
import streamlit as st

# Set the title of your Streamlit app
st.title("How to Choose the Perfect Streaming Service?")

# Define the text content
text_content = """
In today's world, there are lots of movies and TV shows available on many different streaming services. It can be hard to figure out where to watch your favorite shows and movies. Netflix, Amazon Prime, Hulu, and Disney+ are some of the most well-known options, but how do you decide which one is right for you? In this blog, we'll help you choose the streaming service that matches what you like to watch.

**How important is the right choice of streaming service?**

Before we go further into talking about streaming services, it's really important to know why picking the right one is a big deal.

Let's be upfront: we all want value for our money. Subscribing to streaming services comes at a cost. It's a waste to spend your hard-earned money on a streaming service that won't provide the enjoyable movies or series you seek.

Before making a decision, it's important to understand your own preferences:
- Do you prefer watching movies or binge-watching series?
- What types of shows or movies do you like?
- Do you have preferences for specific countries or languages?
- How much time do you typically spend watching TV?

**Comparison Matrix**

To create a clear picture of the differences between streaming services, let's examine the following data:

**Countries:**

The maps tell us that the United States makes the most movies and TV shows, and most of them come from there. Almost all the movies and TV shows on these streaming services are from the United States. The United Kingdom is also in the top five for all four streaming services, and Canada is in the top five for all of them except Netflix. This is because these countries mainly speak English.

Furthermore, India, Japan, and South Korea are in the top five for Netflix. India is also in the top five for Amazon, but not for Hulu. Japan is the opposite; it's in the top five for Hulu but not for Amazon. So, if you like shows or movies from a specific country, you might want to look into this more.

**Type vs. Release Year: Type (Movies, TV Shows):**

When we examine the graphs closely, it becomes evident that all four streaming services predominantly offer more movies than TV shows. Netflix and Amazon provide the most extensive selection of both movies and TV shows. Disney+ offers the fewest options, mainly due to being a relatively new platform compared to the other three. Comparing the number of options per streaming service with the price, Amazon offers the most cost-effective choice.

**Country vs. Release Year:**

If you really like movies or TV shows from a specific country, you can figure that out from the graphs. There are lots of new American movies and TV shows on all four streaming services. On Amazon, you can also find many new Indian movies and TV shows. Amazon is focusing more on India because it's becoming a big market for them, so they're investing to make more Indian content available. If you're into classic movies or shows, Disney+ has a lot of those.

**Duration vs. Release Year + Duration and Country vs. Release Year:**

All of the streaming services offer more movies than TV series. Let’s compare the streaming services based on the duration and release year.

When we look at the movies available on Netflix, we can conclude that there are a vast number of movies spanning from the year 1942 to 2021. On average, most movies are from the year 2021 and onwards. The longest film runs up to 312 minutes.
Netflix offers a diverse range of TV series, with series ranging from 1 to 17 seasons. When a TV series has multiple seasons, it often indicates that they are successful. If you enjoy diversity, then Netflix is a recommendation.

Disney Plus is known for Disney movies and series. Compared to Netflix, the playback duration is shorter on Disney Plus. Are you someone with limited time and/or do you love Disney?
The number of TV series on Disney Plus is much more limited than Netflix. However, it does have a series with 32 seasons. If you are a fan of Disney series, then Disney Plus is a suitable streaming service for you.

Amazon, like Netflix, has an extensive selection of movies. Here, you can find longer films, some lasting up to 601 minutes. For longer movies, you can turn to Amazon.
Amazon Prime offers more series than Disney Plus but fewer than Netflix. Most series are from the year 1990 and onwards. For a variety of movies and series, Amazon Prime is a good choice alongside Netflix.

For most new movies, Hulu is your best option. Compared to other streaming services, Hulu offers more newer films than old ones.
Hulu has a good selection of TV series, although it has fewer than Amazon Prime.

**Type 'Movie' vs. Duration:**

Movie lover? Then Amazon Prime would be your best overall choice! They offer the biggest collection of movies with nearly 8000 different titles. Most of these titles are around 60 or 90 minutes long, ideal for a movie night! Got some more time to kill? A combination with Netflix will get you the most titles that last 2 hours or longer. Or perhaps you just want a quick movie to watch during dinner, in that case Disney+ would be your best option. Together with Amazon Prime they offer the most options of short movies between 15 and 45 minutes. Either way Amazon Prime has got you covered with the most options for your movie night!

If watching series is more your style than Netflix will be your go too service! They offer a wide variety of over 2500 different series to enjoy. If you want to hop from one series to another than Netflix and Amazon will fulfill your every need with a combination of  3200 series to pick from. However if you love binging a series look no further than Hulu they offer the largest range of long running series such as the beloved show Survivor.

**Recommendations:**

**Content Origin and Preferences:**

All four streaming services primarily feature American content, perfect for fans of American movies and TV shows.
Amazon Prime is your best bet if you're looking for a growing selection of Indian movies and TV shows.
Disney+ specializes in timeless Disney classics.

**Content Variety:**

Amazon Prime shines for movie enthusiasts, offering nearly 8000 titles, including shorter options for quick viewing.
For a wide range of both movies and TV series, Netflix and Amazon Prime are top choices.
Disney+ caters to Disney aficionados with its classic movie and series lineup.

**Duration and Release Year:**

Netflix boasts a vast movie library spanning from 1942 to 2021, including newer releases.
Netflix also excels in TV series, offering diverse options ranging from 1 to 17 seasons.
Disney+ is ideal for viewers with limited time, featuring shorter movie durations, and some TV series, including one with 32 seasons.
Amazon Prime offers longer cinematic experiences, with some films lasting up to 601 minutes.
Amazon Prime's series collection spans from 1990 onwards.
Hulu is your go-to service for the latest movie releases and offers a decent selection of TV series.

**Series Preferences:**

If you're all about TV series, Netflix offers a wide selection of over 2500 different series.
Amazon Prime, with 3200 series options, suits those who enjoy jumping between series.
For those who love binge-watching long-running series, Hulu has a selection of beloved shows.

**In summary**, your choice among these streaming services boils down to your - content preferences and viewing habits:

**Netflix** is ideal for series enthusiasts and those who enjoy diverse content.

**Amazon Prime** is perfect for movie lovers, with a massive collection and a variety of series.

**Disney+** caters to Disney fans and viewers with limited time for shorter content.

**Hulu** is great for staying up to date with new movie releases and offers some TV series.

Each service has its unique strengths, so consider what matters most to you when making your selection. Happy streaming!
"""

# Display the text content
st.write(text_content)

# Create a Streamlit app
st.title("Movie and TV Show Duration Comparison")

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
disney_trace = go.Scatter(x=disney_tvshow['duration'], y=disney_tvshow['disney_count'], name='Disney+', line=dict(color='blue'))
fig.add_trace(disney_trace)

# Add a line plot for Amazon Prime Video TV show counts with the color yellow.
amazon_trace = go.Scatter(x=amazon_tvshow['duration'], y=amazon_tvshow['amazon_count'], name='Amazon Prime', line=dict(color='orange'))
fig.add_trace(amazon_trace)

# Add a line plot for Hulu TV show counts with the color green.
hulu_trace = go.Scatter(x=hulu_tvshow['duration'], y=hulu_tvshow['hulu_count'], name='Hulu', line=dict(color='green'))
fig.add_trace(hulu_trace)

# Update the layout of the graph with a title, axis labels, and legend positioning.
fig.update_layout(title='Duration of TV Shows on Different Streaming Services',
                  xaxis_title='Duration (in seasons)',
                  yaxis_title='Number of Titles',
                  legend=dict(x=1, y=1, traceorder='normal'))

# Add a range slider to the x-axis for interactive zooming and limit it so it can't go below zero
fig.update_xaxes(rangeslider_visible=True, rangemode='tozero')

# Display the interactive graph in Streamlit
st.plotly_chart(fig)

# Create a subplot figure for the line plots.
fig = make_subplots(rows=1, cols=1)

# Add a line plot for Netflix TV show counts with the color red.
netflix_trace = go.Scatter(x=netflix_movies['duration'], y=netflix_movies['netflix_count'], name='Netflix', line=dict(color='red'))
fig.add_trace(netflix_trace)

# Add a line plot for Disney+ TV show counts with the color blue.
disney_trace = go.Scatter(x=disney_movies['duration'], y=disney_movies['disney_count'], name='Disney+', line=dict(color='blue'))
fig.add_trace(disney_trace)

# Add a line plot for Amazon Prime Video TV show counts with the color yellow.
amazon_trace = go.Scatter(x=amazon_movies['duration'], y=amazon_movies['amazon_count'], name='Amazon Prime', line=dict(color='orange'))
fig.add_trace(amazon_trace)

# Add a line plot for Hulu TV show counts with the color green.
hulu_trace = go.Scatter(x=hulu_movies['duration'], y=hulu_movies['hulu_count'], name='Hulu', line=dict(color='green'))
fig.add_trace(hulu_trace)

# Update the layout of the graph with a title, axis labels, and legend positioning.
fig.update_layout(title='Duration of Movies on Different Streaming Services',
                  xaxis_title='Duration (in minutes)',
                  yaxis_title='Number of Titles',
                  legend=dict(x=1, y=1, traceorder='normal'))

# Add a range slider to the x-axis for interactive zooming and limit it so it can't go below zero
fig.update_xaxes(rangeslider_visible=True, rangemode='tozero')

# Display the interactive graph in Streamlit
st.plotly_chart(fig)

# Dropdown for platform selection
selected_platform = st.selectbox(
    "Select a platform:",
    platforms
)

# Find the index of the selected platform
selected_index = platforms.index(selected_platform)

# Get the selected platform's data
selected_data = dataframes[selected_index]

# Group the data by 'country' and count the occurrences
country_counts = selected_data['country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

# Apply a logarithmic scale to the 'Count' column
country_counts['Log_Count'] = np.log(country_counts['Count'])

# Create a choropleth map using Plotly Express
fig = px.choropleth(country_counts.head(50), 
                    locations='Country',
                    locationmode='country names',
                    color='Log_Count',
                    range_color=(country_counts['Log_Count'].min(), country_counts['Log_Count'].max()),
                    hover_name='Country',
                    title=f'Content Distribution by Country {selected_platform} (Logarithmic Scale)',
                    color_continuous_scale='Viridis', 
                   )

# Update color axis to show the original count values
fig.update_coloraxes(colorbar_title='Count', colorbar_tickvals=np.arange(0, 10, 1), colorbar_ticktext=np.round(np.exp(np.arange(0, 10, 1)), 0))

# Show the choropleth map
st.plotly_chart(fig)

# Create a Streamlit app
st.title("Distribution of Titles by Country")

# Create a multi-select widget for selecting streaming services
selected_services = st.multiselect(
    "Select Services:",
    ['Netflix', 'Disney+', 'Amazon Prime', 'Hulu'],
    default=['Netflix']  # Default selected services
)

# Create a multi-select widget for selecting countries
selected_countries = st.multiselect(
    "Select Countries:",
    ['United States', 'United Kingdom', 'India'],  # Available country options
    default=['United States', 'United Kingdom', 'India']  # Default selected countries
)

# Define custom colors for the segments
custom_colors = {'United States': 'blue', 'United Kingdom': 'green', 'India': 'red'}

# Define a function to update the Pie chart based on the selected services and countries
def update_pie_chart(selected_services, selected_countries):
    # Filter the data based on the selected services
    data = []
    titles = []

    if 'Netflix' in selected_services:
        data.append(netflix)
        titles.append('Netflix')
    if 'Disney+' in selected_services:
        data.append(disney)
        titles.append('Disney+')
    if 'Amazon Prime' in selected_services:
        data.append(amazon)
        titles.append('Amazon Prime')
    if 'Hulu' in selected_services:
        data.append(hulu)
        titles.append('Hulu')

    # Combine data from selected services
    combined_data = pd.concat(data, ignore_index=True)

    # Filter the combined data based on the selected countries
    filtered_data = combined_data[combined_data['country'].isin(selected_countries)]

    # Calculate the count of titles for each selected country
    country_counts = filtered_data['country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']

    # Create a Pie chart using Plotly Express with custom colors and counts as labels
    title = 'Distribution of Titles between Countries for {}'.format(', '.join(titles))
    fig = px.pie(country_counts, names='country', values='count', title=title,
                 color='country', color_discrete_map=custom_colors,
                 labels={'country': 'Country', 'count': 'Count'})

    # Add count values as labels to the chart segments
    fig.update_traces(textinfo='percent+label')

    # Display the Pie chart in Streamlit
    st.plotly_chart(fig)

# Call the update_pie_chart function to initially display the chart
update_pie_chart(selected_services, selected_countries)

