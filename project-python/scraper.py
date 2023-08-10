# from datetime import datetime
import os
import pandas as pd
import praw
from praw.models import MoreComments
from tqdm import tqdm


# connect to reddit developer
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# select the top posts of the last month
feminism = reddit.subreddit("Feminism").top(time_filter='month')
xxchromosomes = reddit.subreddit("TwoXChromosomes").top(time_filter='month')
me2 = reddit.subreddit("meToo").top(time_filter='month')
opsafeescape = reddit.subreddit("OperationSafeEscape").top(time_filter='month')
domestic_violence = reddit.subreddit("domesticviolence").top(time_filter='month')

subreddits = [feminism, xxchromosomes, me2, opsafeescape, domestic_violence]

# collect all posts of all subreddits
posts = []
print("Start to collect posts")
for subs in subreddits:
    for post in subs:
        posts.append(
            [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

# convert the list of posts in dataframe
posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])


print("Posts collection done!")
print("_______________________\n")


# collect all the comments of all the posts of all subreddits
comments = []
print("Start to collect all the comments")
for idx in tqdm(posts.id):
    submission = reddit.submission(id=idx)
    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append(
            [comment.link_id, comment.author, comment.body, comment.created_utc, comment.id, comment.is_submitter,
             comment.parent_id, comment.score])

# convert list of comments in dataframe
comments = pd.DataFrame(comments,
                        columns=['link_id', 'author', 'body', 'created', 'id', 'is_submitter', 'parent_id', 'score'])


print("Comments collection done!")
print("_______________________\n")


# # "created" columns in both dataframes contain the timestamp of when a given post was submitted
# # it is possible to convert it in string in such way it is easier to understand
# # specify the date format
# time_format = "%Y/%m/%d %H:%M:%S"
# posts['created'] = posts.created.apply(lambda x: datetime.strftime(datetime.fromtimestamp(x), time_format))
# comments['created'] = comments.created.apply(lambda x: datetime.strftime(datetime.fromtimestamp(x), time_format))


print("Saving the data")

# save the collected data
os.mkdir('./data')
posts.to_csv('./data/posts.csv', index=False)
comments.to_csv('./data/comments.csv', index=False)

print("Process done!")
