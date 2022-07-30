#prompt for user to input a journal entry
journal = input("Journal your feelings and vent about a time you were stressed")
print("Journal entry: " + journal)

#creating txt file for the user input
y=open('C:\Users\gurmo\OneDrive\Desktop\Sait 2022\nathacks 2022\Doc1.txt', 'w')
y.write(journal)

# Load Our Packages
import pandas as pd
import spacy
from collections import Counter
 
from tables import split_type
#nlp = spacy.load('en')
 
# Load spacy pipeline
# nlp = spacy.load("en_core_web_sm")
 
# Load spacy pipeline
nlp = spacy.load("en_core_web_sm")
 
# redditcontent = nlp(open('MigraineText.txt', 'r', encoding='utf-8'))
# redditcontentstring = nlp(redditcontent.read())
redditcontentstring = nlp(open('Doc1.txt', 'r', encoding='utf-8').read())
# docx
#print(redditcontentstring)
 
nouns = [ token.text for token in redditcontentstring if token.is_stop != True and token.is_punct !=True and token.pos_ == 'NOUN']
# nouns
 
word_freq = Counter(nouns)
common_nouns = word_freq.most_common(100)
print(common_nouns)
 
# Export to CSV
df = pd.DataFrame(common_nouns)
# df.columns = [Input,'Sentence', 'Aspect', 'Descriptive Term', 'Polarity', 'Subjectivity']
df.columns = ["WordPosts","WordPostCounts"]
df.to_csv('kneepainCount.csv', index=False)