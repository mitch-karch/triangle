import sys,re, base64
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

#Scraper code from josechristian.com
class Render(QWebPage):  
    def __init__(self, url):  
        self.app = QApplication(sys.argv)  
        QWebPage.__init__(self)  
        self.loadFinished.connect(self._loadFinished)  
        self.mainFrame().load(QUrl(url))  
        self.app.exec_()  
   
    def _loadFinished(self, result):  
        self.frame = self.mainFrame()  
        self.app.quit()
 
def getHtml(str_url):
    r_html = Render(str_url)  
    html = r_html.frame.toHtml()
 
    return html

webGenServer = "webgen/webapp.html"
html = getHtml(webGenServer)
print(html)

rawData = str(re.search(r"<div.*>(.*)<\/div>",html).group(1))
rawData = rawData.strip('data:image/png;base64,')
newBackground = base64.decodestring(rawData)
f = open("temp.png", "w")
f.write(newBackground)
f.close()

