#----IMPORTS----
import string
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

#----FUNCTIONS----


def clean_initial_data(text):
    lower_case = text.lower()
    return lower_case.translate(str.maketrans('', '', string.punctuation))


def remove_stop_words(words_list):
    stop_words = ['has', "you've", 'yourselves', 'too', 'only', 'about', 'a', 'when',
                  "you'll", 'that', 'do', "you're", 're', "didn't", 'them', 'had', 'o', "weren't",
                  'he', 'wouldn', 'after', "that'll", 'through', 'over', 'me', 'doing', "haven't",
                  'whom', 'having', 'so', 'hadn', 'wasn', 'in', "mustn't", 'and', 'won', 'during',
                  'these', 'up', 'some', 'did', 'she', 'being', 'but', 'aren', 'such', 'if', 'couldn',
                  'here', 'all', "doesn't", "shouldn't", 'for', 'should', 'because', 'needn', 'is',
                  've', 'my', 'her', 'not', 'his', 'haven', 'or', 'as', 'hasn', 'ours', "isn't",
                  'until', 'on', "hadn't", 'mightn', "won't", "aren't", 'itself', 's', "don't",
                  'down', 'most', 'been', 'ourselves', 'were', 'above', 'below', 'don', 'll', 'under',
                  'weren', 'just', 'myself', 'out', "wouldn't", "hasn't", 'mustn', 'off', 'shouldn',
                  'you', 'now', 'then', 'our', 'didn', 'once', 'm', 'herself', 'to', 'own', 'of',
                  'we', 'from', "needn't", 'himself', 'into', 'this', 'was', 'an', 'what', "she's",
                  'each', 'nor', 'both', 'have', "you'd", 'few', 'again', 'there', 'their', 'by',
                  'further', 'more', 'why', "couldn't", 'be', 'while', 'any', 'other', 'its', 'ma',
                  "should've", 'those', 'isn', "mightn't", 'the', 'hers', 'they', 'does', 'before',
                  'theirs', 'which', 'doesn', 't', 'him', 'with', 'it', 'same', 'where', 'very', "shan't",
                  'yourself', 'can', 'are', 'shan', 'no', 'at', 'd', 'between', "it's", 'will', 'who',
                  'than', 'against', 'ain', 'y', "wasn't", 'yours', 'how', 'am', 'your', 'i', 'themselves']
    final_words = []
    for word in words_list:
        if word not in stop_words:
            final_words.append(word)
    return final_words


#----CODE----
text = open('read.txt', encoding='utf-8').read()

# initial data cleaning
cleaned_text = clean_initial_data(text)
tokenized_words = cleaned_text.split()
final_words = remove_stop_words(tokenized_words)

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(
            ',', '').replace("'", '').replace(' ', '')
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

emotion_counts = Counter(emotion_list)
print(emotion_counts)

fig, ax1 = plt.subplots()
ax1.bar(emotion_counts.keys(), emotion_counts.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
