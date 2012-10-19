# -*- coding: utf-8 -*-
''''
Created on Aug 18, 2012
@author: YuqiChou
'''
APP_KEY = "2267878554"

APP_SECRET = "e374fc2aee769b3158bf3e86a59638f6"

AUTH_REDIRECT_URI_PORT=8000

APP_REDIRECT_URL="http://127.0.0.1:"+str(AUTH_REDIRECT_URI_PORT)+"/"

APP_AUTH_URL='https://api.weibo.com/oauth2/authorize?client_id='+APP_KEY+'&response_type=code&redirect_uri='+APP_REDIRECT_URL

LOCAL_SAVE_PATH="c:/weibo_spider/"

API_HOST="api.weibo.com"

API_USER_TIMELINE="/2/statuses/user_timeline.json"

API_GET_OAUTH2_TOKEN="/oauth2/access_token?client_id="+APP_KEY+"&client_secret="+APP_SECRET+"&grant_type=authorization_code&redirect_uri="+APP_REDIRECT_URL+"&code={code}"


