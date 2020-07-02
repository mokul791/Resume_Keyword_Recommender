import feedparser
from bs4 import BeautifulSoup

my_feed = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')

print('Feed Title: ', my_feed['feed']['title'])

post = my_feed.entries[2]

print('Post Title: ', post.title)

# contents = post.content[1].value
# print(contents)

# html_doc = open('sample-html.html', 'r').read()
soup = BeautifulSoup(my_feed.entries[0].content[0].value, 'html.parser')