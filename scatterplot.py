import requests
import matplotlib.pyplot as plt

# Define API endpoint and parameters
endpoint = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "list": "contenttranslationstats",
    "format": "json"
}

# Make API request and parse response as JSON
response = requests.get(endpoint, params=params)
data = response.json()

# Extract translations matrix from JSON object
translations = data["query"]["contenttranslationstats"]

# Create lists of languages and translation counts
languages = []
translations_from = []
translations_to = []
for lang_data in translations:
    if isinstance(lang_data, dict): 
     languages.append(lang_data['language'])
     translations_from.append(lang_data['translations']['from'])
     translations_to.append(lang_data['translations']['to'])

# Create scatterplot of translations from and to
plt.figure(figsize=(8, 6))
plt.scatter(translations_from, translations_to, color='blue', marker='o')
plt.xlabel("Translations from")
plt.ylabel("Translations to")
plt.title("Translations from and to for different languages")
plt.grid(True)
plt.show()

# Create scatterplot of translations ratio
translations_ratio = [tf/tt for tf, tt in zip(translations_from, translations_to)]
plt.figure(figsize=(12, 8))
plt.scatter(languages, translations_ratio, color='red', marker='s')
plt.xticks(rotation=90)
plt.xlabel("Language pair")
plt.ylabel("Translations from/to ratio")
plt.title("Ratio of translations from/to for different language pairs")
plt.grid(True)
plt.show()
