# -*- coding: utf-8 -*-
import BaseHTTPServer

class NervHttpRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
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
            self.wfile.write("<p>your code is <b>"+self.parameterDict['code']+"</b></p>")
            
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
    
    
    run_while_true(handler_class=NervHttpRequestHandler);
    