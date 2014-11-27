#!/usr/bin/env python

"""
A short program to convert svg files to png files
"""
from PyQt4 import QtGui,QtCore,QtSvg

import sys

class MyView(QtGui.QGraphicsView):
    """
        Uses a graphics view to render an svg image.
    """
    def __init__(self,f):
        QtGui.QGraphicsView.__init__(self)
        
        item = QtSvg.QGraphicsSvgItem(f)
        self.scene = QtGui.QGraphicsScene(self)
        item.setPos(QtCore.QPointF(0,0))
        self.scene.addItem(item)

        self.setScene(self.scene)
        
        self.saveImage(f)
                
    def saveImage(self,f):
        """
            create a QImage and render graphics scene to it.
        """
        isize = self.scene.sceneRect().size().toSize()
        self.qimage = QtGui.QImage(isize,QtGui.QImage.Format_ARGB32)
        painter = QtGui.QPainter(self.qimage)
        self.scene.render(painter)    
        self.qimage.save(f.replace('.svg','.png'))
        
def main(arg1):
    app = QtGui.QApplication(sys.argv)
    db = MyView(arg1)
