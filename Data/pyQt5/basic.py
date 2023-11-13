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
    
    
    #Create Textbox
    myEntry = qtw.QLineEdit()
    myEntry.setObjectName("name_field")
    myEntry.setText("")
    self.layout().addWidget(myEntry)
    
    
    # Create Combobox
    myCombo = qtw.QComboBox(self, editable = True, insertPolicy= qtw.QComboBox.InsertAtBottom)
    # Add Items
    myCombo.addItem("Pepperoni", "Something")
    myCombo.addItem("Cheese" , 2)
    myCombo.addItem("Mushroom", qtw.QWidget)
    myCombo.addItem("Pepper")
    myCombo.addItems(["One", "Two", "Three"])
    myCombo.insertItem(2, "Third")
    self.layout().addWidget(myCombo)

    
    # Create Spin Box
    # Float DoubleSpingBox
    mySpin = qtw.QSpinBox(self, value = 10, 
                          maximum = 100, 
                          minimum = 0, 
                          singleStep = 5, 
                          prefix = "#", 
                          suffix = " Order")
    mySpin.setFont(qtg.QFont('Helvetica', 15))
    self.layout().addWidget(mySpin) 


    # Create Textbox
    myText2 = qtw.QTextEdit(self, lineWrapMode = qtw.QTextEdit.FixedColumnWidth, 
                            # plainText = "This is real Text !", # add text 
                            # html = "<h1> Big Header</h1>", # Add HTML
                            acceptRichText = True, # accepting costum text
                            lineWrapColumnOrWidth = 50, 
                            placeholderText= "Hello World",
                            readOnly = False)
    myText2.setFont(qtg.QFont('Helvetica', 10))
    self.layout().addWidget(myText2) 


    # Create Button
    myButton = qtw.QPushButton("Press Me!", clicked = lambda:pressIt())
    self.layout().addWidget(myButton) 
    
     
    # Show Application       
    self.show()
    
    def pressIt():
      # Add name to label
      #myLabel.setText(f'You Picked {myCombo.currentData()}')
      #myLabel.setText(f'You Picked {mySpin.value()}')
      
      myLabel.setText(f'You Picked {myText2.toPlainText()}')
      myText2.setPlainText("You Pressed the button !")

    
app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()    