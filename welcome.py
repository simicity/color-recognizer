import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
import cv2
from color_recognizer_app import ImageLabel, ColorRecognizerApp

class ColorRecognizerWelcome( QWidget ):
    def __init__( self ):
        super().__init__()
        self.resize( 300, 300 )
        self.setAcceptDrops( True )
 
        main_layout = QVBoxLayout()
 
        self.photoViewer = ImageLabel()
        self.photoViewer.set_welcome_window()
        main_layout.addWidget( self.photoViewer )
 
        self.setLayout( main_layout )
 
    def dragEnterEvent( self, event ):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
 
    def dragMoveEvent( self, event ):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
 
    def dropEvent( self, event ):
        if event.mimeData().hasImage:
            event.setDropAction( Qt.CopyAction )
            file_path = event.mimeData().urls()[ 0 ].toLocalFile()
            self.set_image( file_path )
            event.accept()
        else:
            event.ignore()
 
    def set_image( self, file_path ):
        self.color_recognizer_app = ColorRecognizerApp( file_path )
        self.color_recognizer_app.show()

def main():
    app = QApplication( sys.argv )
    welcome_app = ColorRecognizerWelcome()
    welcome_app.show()
    sys.exit( app.exec_() )

if __name__ == '__main__':
    main()