#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script will unfriend everyone on a Twitter account.
# Use this script to unfollow all of the people who aren't
# following you.

# Written by Glen Baker - iepathos@gmail.com

import tweepy
import time

token_key = ''
token_secret = ''
con_secret = ''
con_key = ''
auth = tweepy.OAuthHandler(con_key, con_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth)

if __name__ == '__main__':
  print 'Thank you for using my unfriend script. - iepathos'
  start = time.time()
  i = 0
  me = api.me()
  followed = api.friends_ids(me)
  followers = api.followers_ids()
  nonfriends = followed
  for friend in followers:
    if friend in nonfriends:
      nonfriends.remove(friend)

  try:
    for friend in nonfriends:
      api.destroy_friendship(friend)
      print 'Unfollowed %s' % friend
      i += 1

      if i % 5 == 0:
        print 'Waiting 60 seconds between next unfollow every 5 unfollows \nbecause Twitter doesn\'t like spammers. Clients are only allowed \n350 requests every hour. So, about 5.83 unfollows a minute.'
        time.sleep(60)
  except ValueError:
    print 'Twitter is unhappy with us.'

  elapsed = time.time() -  start
  print 'Deleted %s non-friends in %s seconds' % (str(i), str(elapsed))
