import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline


posts = pd.read_csv('./data/posts.csv')
# remove posts not in "Feminism" or "domesticviolence"
posts = posts.loc[posts.subreddit.isin(["Feminism", "domesticviolence"])]

# create column joining title and body
posts['text'] = posts.title + posts.body.fillna('')


# Get emotions
# load model for sentiment analysis
model = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")

# get labels
id2label = model.config.id2label


def get_emotions(texts: list[str]) -> list[str]:
    inputs = [tokenizer(x, max_length=512, truncation=True, return_tensors='pt') for x in texts]
    logits = [model(**inp).logits for inp in inputs]
    emotions = [id2label[x.argmax().tolist()] for x in logits]
    return emotions


emotions = get_emotions(posts.text)
posts['emotion'] = emotions

# # Get positive-negative
# # load model for sentiment analysis
classifier = pipeline("sentiment-analysis",
                      model="cardiffnlp/twitter-roberta-base-sentiment-latest",
                      max_length=512,
                      truncation=True,
                      return_all_scores=False)


# classify positive-negative texts
pos_neg = classifier(posts.text.tolist())

# convert into numeric
diz = {'negative': -1, 'neutral': 0, 'positive': 1}
pos_neg = [diz[x['label']] for x in pos_neg]

posts['pos_neg'] = pos_neg

# save processed data
posts.to_csv('./data/posts_preprocessed.csv', index=False)


##########################
# Repeat for comments
##########################

comments = pd.read_csv('./data/comments.csv')

# remove posts not in "Feminism" or "domesticviolence"
# get posts ids and filter comment by parent_id

ids = posts.id
comments['parent_id'] = comments.parent_id.apply(lambda x: x.split("_")[-1])
comments = comments.loc[comments.parent_id.isin(ids)]

# get emotions
emotions = get_emotions(comments.body)
comments['emotion'] = emotions

# classify positive-negative texts
pos_neg = classifier(comments.body.tolist())

# convert into numeric
diz = {'negative': -1, 'neutral': 0, 'positive': 1}
pos_neg = [diz[x['label']] for x in pos_neg]

comments['pos_neg'] = pos_neg

# save processed data
comments.to_csv('./data/comments_preprocessed.csv', index=False)
