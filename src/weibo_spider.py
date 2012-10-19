# -*- coding: utf-8 -*-
'''
Created on Oct 18, 2012
@author: YuqiChou
'''
import httplib
import urllib
import settings
import json
import dl_service


def has_next(jsonObj):
    if long==type(jsonObj['next_cursor']):
        if(jsonObj['next_cursor']>0):
            return True
        else:
            return False
    else:
        return False
    

def extract_pic(jsonObj):
    pic_list=list()
    statuses=jsonObj.get('statuses')
    for status in statuses:
        pic=status.get('original_pic')
        if(pic!=None):
            pic_list.append(pic)
        else:
            retweeted_status=status.get('retweeted_status')
            if(retweeted_status!=None):
                retweeted_original_pic=retweeted_status.get('original_pic')
                if(retweeted_original_pic!=None):
                    pic_list.append(retweeted_original_pic)
    
    return pic_list
    

def fetch_weibo(access_token,page=1,screen_name=None):
    
    paramDict={'access_token':access_token, 
                    'feature':'2',
                       'page':page}
    
    if(screen_name!=None):
        paramDict['screen_name']=screen_name
    
    params = urllib.urlencode(paramDict)
    
    conn = httplib.HTTPSConnection(settings.API_HOST)
    conn.request("GET", settings.API_USER_TIMELINE + "?" + params)
    response = conn.getresponse()
    data = response.read()
    jsonObj=json.loads(data)
    conn.close()
    
    print(jsonObj)
    
    pic_list=extract_pic(jsonObj)
    
    for pic in pic_list:
        dl_service.download(pic)
    
    return has_next(jsonObj)


