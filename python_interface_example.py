import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student System")
        self.resize(500, 200)
        
        # Create widgets
        self.label_class_name = QLabel("Enter the name of Course:")
        self.lineedit_class_name = QLineEdit()
        
        self.label_max_st = QLabel("Maximum number of students:")
        self.lineedit_max_st = QLineEdit()
        
        self.label_name = QLabel("Name:")
        self.lineedit_name = QLineEdit()
        
        self.label_id = QLabel("ID:")
        self.lineedit_id = QLineEdit()
        
        self.button_add = QPushButton("Add Student")
        
        self.button_remove = QPushButton("Remove Student")
        self.button_display_ascending = QPushButton("Display ascending list")
        self.button_display_descending = QPushButton ("Display descending list")

        self.button_clear = QPushButton("Clear")

        self.label_message = QLabel("")
        self.label_message1 = QLabel("")
        self.label_message2 = QLabel("")


        layout = QVBoxLayout()
        
        layout.addWidget(self.label_class_name)
        layout.addWidget(self.lineedit_class_name)

        layout.addWidget(self.label_max_st)
        layout.addWidget(self.lineedit_max_st)

        layout.addWidget(self.label_name)
        layout.addWidget(self.lineedit_name)
        
        layout.addWidget(self.label_id)
        layout.addWidget(self.lineedit_id)
        
        layout.addWidget(self.button_add)
        layout.addWidget(self.button_remove)
        layout.addWidget(self.button_display_ascending)
        layout.addWidget(self.button_display_descending)
        
        layout.addWidget(self.button_clear)

        layout.addWidget(self.label_message)
        layout.addWidget(self.label_message1)
        layout.addWidget(self.label_message2)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.button_add.clicked.connect(self.add_student)
        self.button_remove.clicked.connect(self.remove_student)
        self.button_display_ascending.clicked.connect(self.dis_asc)
        self.button_display_descending.clicked.connect(self.dis_desc)
        self.button_clear.clicked.connect(self.clear) 

        self.students = [] 

    def dis_asc (self):
        course_name = self.lineedit_class_name.text()
        self.label_message.setText(f"Course: " + course_name)
        empty = "Name\t\t\t\tID_Number:\n" 
        for index, (name, id) in enumerate(self.students):
            empty += f"{name}\t\t\t\t{id}\n"  
        self.label_message2.setText(empty)
        

    def dis_desc(self):
        course_name = self.lineedit_class_name.text()
        self.label_message.setText(f"Course: " + course_name)
        empty = "Name\t\t\t\tID_Number:\n"
        index = len(self.students)
        
        empty = "Name\t\t\t\tID_Number:\n"  
        for index in range(len(self.students) - 1, -1, -1):  # Iterate in reverse
            name, id = self.students[index]  # Get name and ID from the tuple
            empty += f"{name}\t\t\t\t{id}\n"  # Append to the string
        self.label_message2.setText(empty)


    def add_student(self):

        max_students = int(self.lineedit_max_st.text())
        if len(self.students) >= max_students:
            self.statusBar().showMessage("Maximum number of students reached.")
            return
        
        student_name = self.lineedit_name.text()
        student_id = self.lineedit_id.text()
    
        # Check if the ID is already in use
        # if any(student[1] == student_id for student in self.students):
        for student in self.students:
            if student[1] == student_id:    
                self.label_message2.setText(f"Student with ID {student_id} already exists.")
                return

        # Find the correct position to insert the new student
        index = 0
        for index, (name, id) in enumerate(self.students):
            if id > student_id:
                break
            index += 1

        # Insert the new student at the correct position
        self.students.insert(index, (student_name, student_id))

        # Update the table widget
        # self.dissplay_list()

        # Clear the text boxes
        self.lineedit_name.setText("")
        self.lineedit_id.setText("")

        # Show status message
        self.label_message2.setText(f"Added {student_name} with ID {student_id} successfully.")
    def remove_student(self):
        student_id = self.lineedit_id.text()  # Get the student ID from the line edit field
        for student in self.students:
            if student[1] == student_id:  # Check if the student ID matches the given ID
                self.students.remove(student)  # Remove the student from the list
                
                self.label_message2.setText(f"Removed {student[0]} with ID {student[1]} successfully.")
                # Clear the text boxes for name and ID
                self.lineedit_name.setText("")
                self.lineedit_id.setText("")
                return
        # If no student with the given ID is found
        self.label_message2.setText(f"No student found with ID {student_id}.")


    def clear(self):
        # Clear the student list, student IDs set, and update the table
        self.students.clear()

        # Clear all text boxes and messages
        self.lineedit_class_name.setText("")
        self.lineedit_max_st.setText("")
        self.lineedit_name.setText("")
        self.lineedit_id.setText("")
        self.label_message.setText("")
        self.label_message1.setText("")
        self.label_message2.setText("")

        # Show a status message indicating that everything has been cleared


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())