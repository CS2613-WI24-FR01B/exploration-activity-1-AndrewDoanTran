[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FJiO-WNb)
# EA1
My name is Tran Gia Khanh Doan (#3736543)

1. The package/library I select:

   In this exploration activity, I utilized the PyQt5 package, which combines over 35 extensions in Python. PyQt5, developed by the British firm Riverbank Computing, is free software that supports users in building user interfaces. It enables Python to serve as an alternative application development language to C++ and supports various platforms such as iOS and Android.
    In this exploration, I have so discover about enumerate library in Python.
The PyQt5 package:
  + The purpose of PyQt5 is to support the user in building graphical user interfaces (GUIs) using the Python language.
  
How to use it:
  - Install the package:
    + If you're using a Macbook M1 machine:
      - Firstly, ensure you have Python 3 installed on macOS.
      - Next, open the terminal and run the following command:
        ![Screenshot 2024-02-13 at 5 03 09 PM](https://github.com/CS2613-WI24-FR01B/exploration-activity-1-AndrewDoanTran/assets/155690892/5a389db1-739d-4c2a-8c8b-6048facec473)
      - After that, upgrade pip by running:
        ![Screenshot 2024-02-13 at 5 04 18 PM](https://github.com/CS2613-WI24-FR01B/exploration-activity-1-AndrewDoanTran/assets/155690892/72ad820c-47cd-4b9e-9777-4624a63c34b3)
      - Finally, install PyQt5 using pip3 by running:
        ![Screenshot 2024-02-13 at 5 04 58 PM](https://github.com/CS2613-WI24-FR01B/exploration-activity-1-AndrewDoanTran/assets/155690892/0d3267e7-76a6-4146-9acd-383a0ff05326)

  - Using it in code:
    + Import the necessary package at the top of your code:
      ```python
      import sys
      from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
      ```
2. what is the PyQt:
   - The purpose of PyQt is used for building the graphical user interface. The main point is this package is free for developer to design the large-program.
   - For this package PyQt5, I used this package to build the graphical user interface about displaying, adding, removing the students and course. Besides that, this package help the user to visualize about a window show that text boxes, messages. Not similarly with boring black window of terminal or terminal on PC operating system. This user interface help the users easy to know what is going and displaying in the program.
   - Important part:
   + QLabel: QLabel is used to display either text or images. Additionally, it supports updating the displayed text dynamically.
   + QApplication: When creating a QApplication instance with QApplication(sys.argv), sys.argv represents a list of command-line arguments passed to the script. If the Python interpreter is invoked with the '-c' command line option, the value of argv[0] is set to the string '-c'. In cases where no script name is provided, argv[0] is an empty string.
   + QMainWindow: QMainWindow serves as the primary window for an application, providing a foundation for constructing its user interface. While QMainWindow offers various features such as QToolBars,          QDockWidgets, a QMenuBar, and a QStatusBar for efficient window management, your program may not utilize all of these functionalities. However, QMainWindow's central section remains capable of accommodating different types of widgets.
   + QLineEdit: QLineEdit allows users to input text, providing features such as undo and redo, cut and paste, and drag and drop functionalities. Additionally, developers can programmatically set or insert text into the QLineEdit.
   + QPushButton: QPushButton creates clickable buttons within the user interface. When clicked, these buttons trigger associated functions in Python to perform specific tasks or actions.
   + QWidget: Widgets are essential components of Qt-based graphical user interface (GUI) programs. Each GUI element, from text editors to buttons and labels, is considered a widget. These widgets can be positioned within a user interface window or displayed as standalone windows. QWidget serves as the base class for all widgets, offering extensive functionalities and customization options for building interactive and visually appealing interfaces.
    - On the other hand, I also discover the enumerate:The Python library method enumerate() transforms an iterable object by adding a counter to it, producing an enumerating object. By converting the object into a list and iterating over it using a loop, each element along with its corresponding counter value can be retrieved. 
4.Functionality:
    **Add student-code:**
      def add_student(self):
        max_students = int(self.lineedit_max_st.text())
        if len(self.students) >= max_students:
            self.label_message2.setText("Maximum number of students reached.")
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
      **Sample Output of Add student:**
      ![Screenshot 2024-02-13 at 11 16 45 PM](https://github.com/CS2613-WI24-FR01B/exploration-activity-1-AndrewDoanTran/assets/155690892/20345b92-ec16-4c13-a692-5ac254f66a48)

     ** Remove student source code:**
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
     **Sample output**
      ![Screenshot 2024-02-13 at 11 20 08 PM](https://github.com/CS2613-WI24-FR01B/exploration-activity-1-AndrewDoanTran/assets/155690892/116a7a1e-d5ab-483e-8042-65dee2fac539)
     **Sample of display_descending order**
     ![Screenshot 2024-02-13 at 11 21 32 PM](https://github.com/CS2613-WI24-FR01B/exploration-activity-1-AndrewDoanTran/assets/155690892/e36a2682-9ae2-4bd3-b2a5-d758140d19ac)

       With only three samples out put, they all have content QLabel, QApplication, ..... and enumerate library.
5. When was it created?
   The PyQt package was created in 1998 by Riverbank Computing. In August 2009, Nokia advocated for PyQt's Python binding to be available under the LGPL license.
6. The reason I choose this package:
   The reason I chose to use this package is because I was curious about how user interfaces in Python look. I previously used JavaFX-GUI but found it challenging to download the package onto my machine. However, PyQt5 proved to be very easy to install. Additionally, as I study Computer Science, I find it frustrating that I can write code but not see how the window, program, or interface looks. Using PyQt5 allows me to visualize game development and application interfaces, and I am curious to explore the differences between Java and Python interfaces.

7. How did learning the pacakage influence my learning of the language:
   Studying this language supports me in discovering more extension packages for GUI in Python, such as Tkinter, wxPython, PyQt, and more. In my free time, I plan to explore additional extensions to develop my own projects. Upon completing this exploration activity, my goal is to expand beyond Python and explore other languages to bring my ideas to life and enhance my resume.
8.  Overall experience with this package:
  Overall, my experience with this package has been positive. Upon receiving feedback from this exploration activity, I will determine whether to recommend this package to others based on how effectively I utilized its functions. I plan to continue using this package as I believe there are still more functions to explore and utilize.

    Text:
    "Widgets are the basic building blocks for graphical user interface (GUI) applications built with Qt. Each GUI component (e.g. buttons, labels, text editors) is a widget that is placed somewhere within a user interface window, or is displayed as an independent window." [11]
    "A main window provides a framework for building an application's user interface. Qt has QMainWindow and its related classes for main window management. QMainWindow has its own layout to which you can add QToolBars, QDockWidgets, a QMenuBar, and a QStatusBar. The layout has a center area that can be occupied by any kind of widget. You can see an image of the layout below."[10]
   "QApplication's main areas of responsibility are:... example through some kind of control panel."[9]
     "Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects ... applications." [8]
     "QApplication specializes QGuiApplication with some functionality needed for QWidget -based applications. It handles widget... finalization."[6]
   "QLabel is used for displaying text or an image. No user ... widget."[5]
      "The list of command line arguments passed to a Python script. argv[0] is the script name ... command line, see the fileinput module."[4]
      " line edit allows the ... and drop (see setDragEnabled())."[3]
       "The push button, or command button, is perhaps ... Yes, No and Help."[2]
     "The widget is the atom of the user interface: it receives mouse, keyboard and other events from the window system, and paints a representation of itself on the screen. Every widget is rectangular, and they are sorted in a Z-order. A widget is clipped by its parent and by the widgets in front of it.

    "A widget that is not embedded in a parent widget is called a window. Usually, ... common window types."[1]
    "The enumerate() is a Python library function used to add a counter to an iterable object and return it ...ps and indexes."[12]
    Reference:

    [1] https://doc.qt.io/qt-6/qwidget.html#details
    [2] https://doc.qt.io/qt-6/qpushbutton.html#details
    [3] https://doc.qt.io/qt-6/qlineedit.html#details
    [4] https://stackoverflow.com/questions/45992143/why-does-qtwidgets-qapplication-require-sys-argv
    [5] https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLabel.html#more
    [6] https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QApplication.html#more
    [7] https://datascientest.com/en/pyqt-how-does-the-wrapper-that-links-python-to-gui-qt-work#:~:text=PyQt%20is%20widely%20used%20for,with%20a%20graphical%20user%20interface.
    [8] https://pypi.org/project/PyQt5/#:~:text=PyQt5%20is%20a%20comprehensive%20set,platforms%20including%20iOS%20and%20Android.
    [9] https://doc.qt.io/qt-6/qapplication.html#:~:text=QApplication%27s%20main%20areas%20of%20responsibility,some%20kind%20of%20control%20panel.
    [10] https://doc.qt.io/qt-6/qmainwindow.html#details
    [11] https://doc.qt.io/qtforpython-6/overviews/widgets-tutorial.html#
    [12] https://www.scaler.com/topics/enumerate-in-python/
