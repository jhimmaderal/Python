import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
  def __init__(self):
    super().__init__()
    # Add Title
    self.setWindowTitle("Food Palace")
    
    # Set Vertical Layout
    self.setLayout(qtw.QVBoxLayout())
    
    # Create Label
    myLabel = qtw.QLabel("Select on the List: ")
    # Change Font Size Label
    myLabel.setFont(qtg.QFont('Helvetica', 10))
    self.layout().addWidget(myLabel)
    
    # Create Textbox
    myEntry = qtw.QLineEdit()
    myEntry.setObjectName("name_field")
    myEntry.setText("")
    self.layout().addWidget(myEntry)
    
    # Create Button
    myButton = qtw.QPushButton("Press Me!", clicked = lambda:pressIt())
    self.layout().addWidget(myButton) 
     
    # Show Application       
    self.show()
    
    def pressIt():
      # Add name to label
      myLabel.setText(f'Hello {myEntry.text()}')
      # Clear Text
      myEntry.setText("")
    
app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()    