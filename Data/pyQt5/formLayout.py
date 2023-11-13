import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
  def __init__(self):
    super().__init__()

    # Add Title 
    self.setWindowTitle("Hello World!!")

    # Set Vertical Layout
    #self.setLayout(qtw.QVBoxLayout())
    
    # Create Layout
    formLayout = qtw.QFormLayout()
    self.setLayout(formLayout)

    # Add Widgets
    label1 = qtw.QLabel("This is a Cool Label Row")
    label1.setFont(qtg.QFont("Helvetica", 24))

    fname = qtw.QLineEdit(self)
    lname = qtw.QLineEdit(self)

    # Add Rows to App
    formLayout.addRow(label1)
    formLayout.addRow("First Name: ", fname)
    formLayout.addRow("Last Name: ", lname)
    formLayout.addRow(qtw.QPushButton("Press Me !", clicked = lambda: press_it()))
    
    # Show app
    self.show()

    def press_it():
      label1.setText(f'You click the button {fname.text()} {lname.text()}!')

app = qtw.QApplication([])
mw = MainWindow()

# Run App
app.exec_()


# Notes
# PyQt5 Designer
# Install PyQt5Desinger
# Open app (terminal type designer)
# Create Design
# Conver to python object - pyuic5 -x hello.ui -o hello_world.py