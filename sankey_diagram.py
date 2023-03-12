import pandas as pd
import plotly.graph_objects as go
import requests

# Define the API 
url = "https://en.wikipedia.org/w/api.php?action=query&list=contenttranslationstats&format=json"

# Send a request to the API and retrieve the response data
response = requests.get(url)
data = response.json()

# Extract the translation data from the response data and convert it to a list of dictionaries
translations = data['query']['contenttranslationstats']['pages']
translations_list = []
for t in translations:
    translations_list.append({
        'from': t['sourceLanguage'],
        'to': t['targetLanguage'],
        'count': t['count']
    })

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(translations_list)

# Define the languages of interest
languages = ['es', 'fr', 'de', 'it', 'pt', 'Ja', 'ko', 'vi', 'zh', 'ar', 'Ro', 'Hi', 'ta', 'nl', 'sv', 'no', 'da', 'rv', 'pl', 'uk', 'cs', 'sk']

# Filter the data to exclude English and only include the languages of interest
df_filtered = df[df['to'] != 'en']
df_filtered = df_filtered[df_filtered['from'].isin(languages) & df_filtered['to'].isin(languages)]

# Summarize the data by counting the number of translations between each pair of languages
df_summary = df_filtered.groupby(['from', 'to']).sum().reset_index()

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = languages
    ),
    link = dict(
      source = df_summary['from'].apply(lambda x: languages.index(x)),
      target = df_summary['to'].apply(lambda x: languages.index(x)),
      value = df_summary['count']
  ))])

# Customize the layout of the Sankey diagram
fig.update_layout(title_text="Translation flow between smaller subset of languages (excluding English)", font_size=10)
fig.show()
