#-*-coding:utf-8-*-'

import urllib
import settings
import os



def urlcallback(blocknum, bs, size):
    print 'blocknum: {blocknum}  bs:{bs}  size:{size}'.format(blocknum=str(blocknum), bs=str(bs),size=str(size))
    
    
def download(file_url):
    print('download: '+file_url)
    file_name=file_url.split("/")[-1]
    if(not os.path.exists(settings.LOCAL_SAVE_PATH)):
        os.makedirs(settings.LOCAL_SAVE_PATH)
    if(not os.path.isfile(settings.LOCAL_SAVE_PATH+file_name)):
        urllib.urlretrieve(file_url,settings.LOCAL_SAVE_PATH+file_name)
    
    
if __name__=="__main__":
    download('http://ww3.sinaimg.cn/large/7257fa72jw1dxznttnxmyj.jpg')
