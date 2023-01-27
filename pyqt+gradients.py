import PyQt5
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2
import numpy
app=QtWidgets.QApplication([])
window= QtWidgets.QWidget()
window.setMinimumSize(300,150)
res=2
sliderredleft=QtWidgets.QSlider(Qt.Horizontal)
slidergreenleft=QtWidgets.QSlider(Qt.Horizontal)
sliderblueleft=QtWidgets.QSlider(Qt.Horizontal)

sliderredleft.setMinimum(0)

def gen():
    #function to genarate gradients
    global slidergreenleft
    global sliderblueleft
    global sliderredleft
    global slidergreenright
    global sliderblueright
    global sliderredright
    global aspectRatioInput
    global slidersize
    #global size
    global aspectratio
    #global aspect_list1
   
    global res
    aspectratio=aspectRatioInput.toPlainText()
    print(aspectratio)
    aspect_list1=aspectratio.split(":")
    aspectx=int(aspect_list1[0])
    aspecty=int(aspect_list1[1])
    print("aspectx=",aspectx)
    print("aspecty=",aspecty)
    

    size=slidersize.value()
    yx=aspecty/aspectx
    yxxsize=int(yx*size)

    #printing the varibles
    print("size=",size)
    redleft=sliderredleft.value()
    print("redleft=",redleft)
    greenleft=slidergreenleft.value()
    print("greenleft=",greenleft)
    blueleft=sliderblueleft.value()
    print("blueleft=",blueleft)
    
    redright=sliderredright.value()
    print("redright=",redright)
    greenright=slidergreenright.value()
    print("greenleft=",greenleft)
    blueright=sliderblueright.value()
    print("blueright=",blueright)

    
    
    #generating Gradient with Cv2 
    first=numpy.array([blueleft,greenleft,redleft])
    last=numpy.array([blueright,greenright,redright])
    row=numpy.linspace(first,last,num=5000)
    image=numpy.linspace(row,row,num=5000)
    image=numpy.uint8(image)
    image=cv2.resize(image,(size,yxxsize))
    cv2.imshow("Genarated Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def settext():
    global slidersize
    global slidersizevalue
    global sizelabel2
  
    slidersizevalue=slidersize.value()
    if slidersizevalue > 68:
        sizelabel2.setText(str(slidersizevalue))
#setting slider min + max values
slidergreenleft.setMaximum(255)
slidergreenleft.setMinimum(0)
sliderblueleft.setMaximum(255)
sliderblueleft.setMinimum(0)
sliderredleft.setMaximum(255)
slidersize=QtWidgets.QSlider(Qt.Horizontal)
slidersize.setMaximum(1300)
slidersize.setMinimum(50)

labelredleft=QtWidgets.QLabel("Red")
labelgreemleft=QtWidgets.QLabel("Green")
labelblueleft=QtWidgets.QLabel("Blue")
button=QtWidgets.QPushButton("Genarate")
button.clicked.connect(gen)
layout=QtWidgets.QGridLayout()

layout.setColumnStretch(0,6)
layout.setColumnStretch(1,6)
mainlayout=QtWidgets.QGridLayout()
layout3=QtWidgets.QGridLayout()
labelredright=QtWidgets.QLabel("Red")
#setting custom fonts
labelredright.setFont(QtGui.QFont("",12))
labelblueleft.setFont(QtGui.QFont("",12))
labelgreemright=QtWidgets.QLabel("Green")
labelgreemright.setFont(QtGui.QFont("Lato",12))
labelblueright=QtWidgets.QLabel("Blue")
labelblueright.setFont(QtGui.QFont("Lato",12))
sliderredright=QtWidgets.QSlider(Qt.Horizontal)
#setting custom fonts 
sliderredright.setFont(QtGui.QFont("Lato",12))

slidergreenright=QtWidgets.QSlider(Qt.Horizontal)
sliderblueright=QtWidgets.QSlider(Qt.Horizontal)
sizelabel1=QtWidgets.QLabel("^50")
leftlabel=QtWidgets.QLabel("Left")

sizelabel2=QtWidgets.QLabel("Size")
sizelabel2.setAlignment(QtCore.Qt.AlignCenter)
sizelabel3=QtWidgets.QLabel("^1300")
sizelabel3.setAlignment(QtCore.Qt.AlignRight)
rightlabel=QtWidgets.QLabel("Right")                                                                                                                                           
rightlabel.setFont(QtGui.QFont("Lato",14,QtGui.QFont.Bold))
leftlabel.setFont(QtGui.QFont("",14,QtGui.QFont.Bold))
#setting main layout 
window.setLayout(mainlayout) 
#setting custom fonts
labelredleft.setFont(QtGui.QFont("Lato",12))
labelgreemleft.setFont(QtGui.QFont("Lato",12))
labelblueleft.setFont(QtGui.QFont("Lato",12))
button.setFont(QtGui.QFont("Lato",12))


#setting custom fonts
sizelabel1.setFont(QtGui.QFont("Lato",12))
sizelabel2.setFont(QtGui.QFont("Lato",12))
sizelabel3.setFont(QtGui.QFont("Lato",12))

loop=QtCore.QTimer()
loop.timeout.connect(settext)
aspectRatioInput=QtWidgets.QTextEdit()
aspectRatioInput.setMaximumHeight(30)
aspectRatioInput.setText("1:1")
#adding widgets to layout 

mainlayout.addWidget(aspectRatioInput,4,0)

layout.addWidget(leftlabel,0,0)
layout.addWidget(sliderredleft,2,0)
layout.addWidget(labelredleft,1,0)
layout.addWidget(slidergreenleft,4,0)
layout.addWidget(labelgreemleft,3,0)
layout.addWidget(sliderblueleft,6,0)
layout.addWidget(labelblueleft,5,0)

layout.addWidget(rightlabel,0,1)
layout.addWidget(sliderredright,2,1)
layout.addWidget(labelredright,1,1)
layout.addWidget(slidergreenright,4,1)
layout.addWidget(labelgreemright,3,1)
layout.addWidget(sliderblueright,6,1)
layout.addWidget(labelblueright,5,1)
mainlayout.addLayout(layout,1,0)
mainlayout.addLayout(layout3,3,0)
mainlayout.addWidget(slidersize,2,0)
layout3.addWidget(sizelabel1,2,0)
layout3.addWidget(sizelabel2,2,8)
layout3.addWidget(sizelabel3,2,16)
mainlayout.addWidget(button,7,0)
window.setWindowIcon(PyQt5.QtGui.QIcon('logo.png'))
window.show()
window.setWindowTitle("Window")
loop.start(10)
app.exec() 


