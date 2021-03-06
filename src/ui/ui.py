import sys
from PySide6.QtCore import Qt
import random
from PySide6 import QtCore, QtWidgets as qtw, QtGui


import src.ui.ui_comands as uic

class MyApp(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROBOT ARM APP")
        self.layout = qtw.QGridLayout()
        self.layout.setContentsMargins(25, 25, 25, 25)
        self.layout.setVerticalSpacing(35)

        title = qtw.QLabel("CONTROL BRAZO ROBÓTICO", )                
        self.layout.addWidget(title, 0, 0, 1, 2)

        # Pinzas
        self.create_slider_gripper()

        # Muñeca
        self.create_slider_wrist()

        # Brazos        
        self.create_slider_arm_top()
        self.create_slider_arm_bottom()
        
        # Hombros
        self.create_slider_shoulders()

        # Base 
        self.create_slider_base()        

        self.setLayout(self.layout)

    """ @QtCore.Slot()
    def magic(self):
        self.text1.setText(random.choice(self.hello))   """                                   

    def create_slider_gripper(self):        
        self.slider1 = qtw.QSlider(Qt.Horizontal)                
        self.text1 = qtw.QLabel("Pinzas", )
        self.slider1.valueChanged.connect(self.changed_gripper) 
        self.slider1.setRange(180, 300)        
        self.slider1.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider1.setTickInterval(50)
        self.slider1.setPageStep(10)
        self.layout.addWidget(self.slider1, 1, 0)
        self.layout.addWidget(self.text1, 1, 1)        


    def create_slider_wrist(self):
        self.slider2 = qtw.QSlider(Qt.Horizontal)        
        self.text2 = qtw.QLabel("Muñeca", )
        self.slider2.valueChanged.connect(self.changed_wrist) # command=uic.wrist
        self.slider2.setRange(180, 600)        
        self.slider2.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider2.setTickInterval(50)
        self.slider2.setPageStep(10)
        self.layout.addWidget(self.slider2)
        self.layout.addWidget(self.text2)


    def create_slider_arm_top(self):
        self.slider3 = qtw.QSlider(Qt.Horizontal)        
        self.text3 = qtw.QLabel("Brazo Arriba", )
        self.slider3.valueChanged.connect(self.changed_arm_top) # command=uic.arm_top
        self.slider3.setRange(180, 600)        
        self.slider3.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider3.setTickInterval(50)
        self.slider3.setPageStep(10)
        self.layout.addWidget(self.slider3)
        self.layout.addWidget(self.text3)


    def create_slider_arm_bottom(self):
        self.slider4 = qtw.QSlider(Qt.Horizontal)        
        self.text4 = qtw.QLabel("Brazo Abajo", )
        self.slider4.valueChanged.connect(self.changed_arm_bottom) # command=uic.arm_bottom
        self.slider4.setRange(180, 600)        
        self.slider4.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider4.setTickInterval(50)
        self.slider4.setPageStep(10)
        self.layout.addWidget(self.slider4)
        self.layout.addWidget(self.text4)


    def create_slider_shoulders(self):
        self.slider5 = qtw.QSlider(Qt.Horizontal)        
        self.text5 = qtw.QLabel("Hombros", )
        self.slider5.valueChanged.connect(self.changed_shoulders) # command=uic.shoulders
        self.slider5.setRange(180, 600)        
        self.slider5.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider5.setTickInterval(50)
        self.slider5.setPageStep(10)
        self.layout.addWidget(self.slider5)
        self.layout.addWidget(self.text5)


    def create_slider_base(self):
        self.slider6 = qtw.QSlider(Qt.Horizontal)        
        self.text6 = qtw.QLabel("Base")
        self.slider6.valueChanged.connect(self.changed_base) # command=uic.base
        self.slider6.setRange(180, 600)        
        self.slider6.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider6.setTickInterval(50)
        self.slider6.setPageStep(10)
        self.layout.addWidget(self.slider6)
        self.layout.addWidget(self.text6)


####  On change value
    def changed_gripper(self, i) -> None:
        self.text1.setText(f"Pinza {i}")
        uic.gripper(i)
        

    def changed_wrist(self, i) -> None:
        self.text2.setText(f"Muñeca {i}")
        uic.wrist(i)

    
    def changed_arm_top(self, i) -> None:
        self.text3.setText(f'Brazo Arriba {i}')
        uic.arm_top(i)


    def changed_arm_bottom(self, i) -> None:
        self.text4.setText(f'Brazo Abajo {i}')
        uic.arm_bottom(position=i)

    
    def changed_shoulders(self, i) -> None:
        self.text5.setText(f'Hombros {i}')
        uic.shoulders(position = i)


    def changed_base(self, i) -> None:
        self.text6.setText(f'Base {i}')
        uic.base(position = i)


class App:

    def __init__(self) -> None:            
        app = qtw.QApplication(sys.argv)
        widget = MyApp()
        #widget.resize(300, 600)
        widget.show()
        sys.exit(app.exec())