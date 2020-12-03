import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QBrush, QColor
import cv2
import color_recognizer as cr

class ImageLabel( QLabel ):
    def __init__( self ):
        super().__init__()

    def set_welcome_window( self ):
        self.setAlignment( Qt.AlignCenter )
        self.setText( '\n\n Drop Image Here \n\n' )
        self.setStyleSheet( '''
            QLabel{
                border: 4px dashed #aaa
            }
        ''' )
 
    def setPixmap( self, image ):
        super().setPixmap( image )

    def setCV2Pixmap( self, file_path ):
        self.img_bgr = cv2.imread( file_path )
        img_rgb = cv2.cvtColor( self.img_bgr, cv2.COLOR_BGR2RGB )
        img = QImage( img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB888 )
        self.pixmap_img = QPixmap.fromImage( img )
        self.setScaledContents( True )
        self.setPixmap( self.pixmap_img )

    def getImageWidth( self ):
        return self.pixmap_img.width()

    def getImageHeight( self ):
        return self.pixmap_img.height()

    def drawRecognizedColor( self, event ):
        b, g, r = self.img_bgr[ event.pos().y(), event.pos().x() ]
        b = int( b )
        g = int( g )
        r = int( r )

        painter = QPainter( self.pixmap_img )

        painter.setPen( QPen( QColor( r, g, b ), 1, Qt.SolidLine ) )
        painter.setBrush( QBrush( QColor( r, g, b ), Qt.SolidPattern ) )
        rect = QRect( 20, 20, 300, 40 )
        painter.drawRect( rect )

        painter.setPen( QPen( ( QColor( 0, 0, 0 ) if ( r + g + b >= 500 ) else QColor( 255, 255, 255 ) ), 1, Qt.SolidLine ) )
        text = cr.recognize_color( r, g, b ) + ' R=' + str( r ) +  ' G=' + str( g ) +  ' B=' + str( b )
        painter.drawText( rect, Qt.AlignCenter, text )

        self.setPixmap( self.pixmap_img )
        self.show()

class ColorRecognizerApp( QWidget ):
    def __init__( self, file_path ):
        super().__init__()
        main_layout = QVBoxLayout()
 
        self.photoViewer = ImageLabel()
        self.photoViewer.setCV2Pixmap( file_path )
        self.photoViewer.mousePressEvent = self.photoViewer.drawRecognizedColor
        main_layout.addWidget( self.photoViewer )

        self.setMouseTracking( True )
        self.setWindowTitle( file_path )
        self.setLayout( main_layout )
