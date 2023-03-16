import wikipediaapi
import matplotlib.pyplot as plt

# Define list of language codes
languages = ['en', 'fr', 'de', 'es', 'it', 'Ja', 'ko', 'vi', 'zh', 'hi']

# Initialize lists to store article counts and translation ratios for each language
article_counts = []
translation_ratios = []

# Loop through list of languages and retrieve article counts and translation ratios
for lang in languages:
    wiki = wikipediaapi.Wikipedia(lang)
    article_count = len(wiki.page('Wikipedia:Contents').links)
    article_counts.append(article_count)
    translation_ratio = float(input(f'Enter {lang} translation ratio (e.g. 0.2 for 20%): '))
    translation_ratios.append(translation_ratio)

# Plot scatterplot of translation ratios against article counts
plt.scatter(article_counts, translation_ratios)

# Add labels and title to scatterplot
plt.xlabel('Article Count')
plt.ylabel('Translation Ratio')
plt.title('Translation Ratio vs Wiki Article Count for Different Languages')

# Show plot
plt.show()
print(f'{lang} Wikipedia articles: {article_count}')
print(f'{lang} translation ratio: {translation_ratio}')
