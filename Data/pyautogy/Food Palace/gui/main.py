import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import win32con

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
    #myEntry = qtw.QLineEdit()
    #myEntry.setObjectName("name_field")
    #myEntry.setText("")
    #self.layout().addWidget(myEntry)
    
    # Create Combobox
    myCombo = qtw.QComboBox(self, editable = True, insertPolicy= qtw.QComboBox.InsertAtTop)
    # Add Items
    myCombo.addItem("Pepperoni", "Something")
    myCombo.addItem("Cheese" , 2)
    myCombo.addItem("Mushroom")
    myCombo.addItem("Pepper")
    
    win32con.WM_KEYDOWN()
    
    self.layout().addWidget(myCombo)
    
    # Create Button
    myButton = qtw.QPushButton("Press Me!", clicked = lambda:pressIt())
    self.layout().addWidget(myButton) 
     
    # Show Application       
    self.show()
    
    def pressIt():
      # Add name to label
      myLabel.setText(f'You Picked {myCombo.currentData()}')

    
app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()    