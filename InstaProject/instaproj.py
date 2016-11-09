# from instagram.client import InstagramAPI

# access_token = "291415499.1677ed0.ac0b0bd89ad24abf803af986a0ec04e5"
# client_id = "17dc76c2dacd4aaf9e7321ec0a261beb"
# client_secret = "420e82cf73964f5b8d9b91b78954a8b5"

# # api = InstagramAPI(access_token=access_token, client_secret=client_secret)
# # recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
# # for media in recent_media:
# #    print media.caption.text

# api = InstagramAPI(client_id=client_id, client_secret=client_secret)
# popular_media = api.media_popular(count=20)
# for media in popular_media:
#     print media.images['standard_resolution'].url

# from instagram.client import InstagramAPI

# access_token = "291415499.1677ed0.ac0b0bd89ad24abf803af986a0ec04e5"
# client_secret = "420e82cf73964f5b8d9b91b78954a8b5"
# api = InstagramAPI(access_token=access_token, client_secret=client_secret)
# recent_media, next_ = api.user_recent_media(user_id=api.user_search('rubaliciousabrams')[0].id, count=10)
# for media in recent_media:
#    print media.caption.text

import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np 
from pprint import pprint

with open('rubaliciousabrams.json') as data_file:
	data = json.load(data_file)

likes = []
dates = []

for pic in data['data']:
	likes.append(pic['likes']['count'])
	# print pic['likes']['count'], pic['caption']['text']
	temp = datetime.fromtimestamp(int(pic['caption']['created_time'])).strftime("%Y-%b-%d %H:%M")
	print temp
	dates.append(temp)
	# print dates[-1]
pprint(data['data'][0])
pprint(data['data'][-1])

dates = np.array([datetime.strptime(time, "%Y-%b-%d %H:%M") for time in dates])
likes = np.array(likes)

# print likes
# print dates

# some statistics 
# average number of likes
print 'average number of likes is %.2f'%np.mean(likes)
# how long you've been on insta
print 'your most recent post occurred on %s'%(dates[0].strftime("%Y-%b-%d %H:%M"))
plt.xlabel('Date of post')
plt.ylabel('Number of likes')
plt.plot(dates, likes)
plt.show()

# scatter plot likes vs time of day
time_of_day = np.array([int(date.time().strftime("%H %M").replace(' ', '')) for date in dates])
print time_of_day
plt.xlabel('Time of day of post')
plt.ylabel('Number of likes')
plt.scatter(time_of_day, likes)
plt.show()
