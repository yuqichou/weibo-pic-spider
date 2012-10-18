# -*- coding: utf-8 -*-
import BaseHTTPServer
import weibo_spider
import urllib

class HttpRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def handleRequestRedirect(self):
        
        self.parameterDict=dict()
        if '?' in self.path:#如果带有参数     
            self.queryString=self.path.split('?')[1]
            ps=self.queryString.split('&')
            for t in ps:
                if '=' in t:
                    if len(t.split('='))==2:
                        temp=t.split('=')
                        self.parameterDict[temp[0]]=temp[1]
        
        self.send_response(200, None);
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>weibo redirect page</title></head>")
        self.wfile.write("<body>")
        
        if 'code' in self.parameterDict:
            access_token=self.parameterDict['code']
            self.wfile.write("<p>your access_token is <b>"+access_token+"</b></p>")
            self.wfile.write("<p>now working!!!</p>")
            
        if 'action' in self.parameterDict:
            access_token=self.parameterDict['code']
            screen_name=urllib.unquote(self.parameterDict.get('screen_name'))
                        
            page=1
            end=False
            while(not end):
                end=not weibo_spider.fetch_weibo(access_token, page, screen_name=screen_name)
                page=page+1
            
            
            
        self.wfile.write("</body></html>")
    
    def do_GET(self):
        self.handleRequestRedirect()
        
    def do_POST(self):
        self.handleRequestRedirect()
    
    
    
def run_while_true(server_class=BaseHTTPServer.HTTPServer,
                     handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    while True:
        httpd.handle_request()
        
        

if __name__ == '__main__':
    run_while_true(handler_class=HttpRequestHandler);
    