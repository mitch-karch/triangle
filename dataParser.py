import sys,re, base64
import svg_to_png
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

#generate a website to use the d3.js code to make the trianglify app.
#Save the generated image in temp.svg
webGenServer = "webgen/webapp.html"
html = getHtml(webGenServer)
rawData = str(re.search(r"<div.*>(.*,)(.*)<\/div>",html).group(2))
newBackground = base64.decodestring(rawData)
f = open("temp.svg", "w")
f.write(newBackground)
f.close()

#convert to png from orangepalantir
svg_to_png.main("temp.svg")
