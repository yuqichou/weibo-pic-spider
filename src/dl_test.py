#-*-coding:utf-8-*-'

import urllib
def urlcallback(blocknum, bs, size):
    print 'blocknum: {blocknum}  bs:{bs}  size:{size}'.format(blocknum=str(blocknum), bs=str(bs),size=str(size))
    
if __name__=="__main__":
    urllib.urlretrieve("http://127.0.0.1:8080/mecool/js/datepicker/skin/default/img.gif"
                      ,"c:/img.jpg"
                      ,urlcallback)

