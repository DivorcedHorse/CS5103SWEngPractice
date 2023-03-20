# CS 5103 Software Engineering Course Project - README
## Project by Daniel Tellez

1. ### **Purpose:**
    The goal of this project is to go through all software engineering practices by creating a small personal project.  As I develop my given project, I will be implementing various software engineering practices such as creating textual-based specifications to better understand requirements engineering, testing, designing, using a version control system, applying different tool applications, and much more.

2. ### **Project Topic:**
    The project topic I have chosen for my personal project will be **String and Words**.<br></br>
    The goal for **String and Words** is to create a simple application that will
    `perform various word statistics of a given document (as a string)`.  This includes, but may not be limited to, counting the `frequency of each unique word` and supporting `combinations of space, tab, and newline characters as seperators`.

    #### **NEW REQUIREMENT CHANGE**
    As of Monday, March 13th, new requirements were introduced to the **String and Words** system.  Two new features were introduced to the system that will be implemented.  The two features includes:

    1. Counting the number of lines (LineCount)
    2. Counting the number of characters (CharCount)

    The following new features will be thoroughly specified to make requirements clear and help define the implementation of the features.  New test cases will also be created to ensure the validity and correctness of said features.

3. ### **Project Implementation:**
    I will implement **String and Words** using Python 3.  This includes creating the source code and test files in Python.<br><br>
    I will also utilize GitHub as my Version Control System (VCS) to keep track of all my changes using separate branches.

    - Branch *requirement1* will contain the initial implementation of the **String and Words** system.  This will be the starting point of the system.
    - Branch *requirement2* will contain the new features that will be provided later to the system.  The new features will be documented, tested, and implemented in the code.

4. ### **Project Process and Documentation:**
    - GitHub will be used for keeping track of my code and changes related to it.
        - Unit tests/files will also be tracked here.
    - A separate document for specifications (requirements engineering) will be created.  This document will contain the textual-based specifications as well as test cases.  

5. ### **Project Execution:**
    - To execute the **String and Words** application, navigate to the *src* folder.  Here two files will exists:
        1. **main.py** - The source code for the **String and Words** implementation.
        2. **exec.sh** - The executable file that will invoke **main.py**.  This script will only accept one argument, the file wanting to be executed on.

        To execute, please run the following command down below: <br>
        ```
        ./exec.sh <filename>
        ```
        Where *\<filename>* is the path of the file wanting to be looked at. 

6. ### **Test Cases**:
    - Test cases can also be found in the *src* directory to validate the requirements of the 
        **String and Words** application.

    - Test cases can be ran by navigating to the *src* folder, and running one of the following commands seen down below: <br>

        - To run a single test file:
            ```
            python3 test_<testFileName>.py
            ```
        - To run all test files:
            ```
            python3 -m unittest
            ```
    

