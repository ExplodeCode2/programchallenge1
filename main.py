'''
OCR A Level Computer Science - Programming Challenge 1
Requirements:
- Add student record ✅
- View student record ✅
- Delete student record ✅
- Exit program ✅
'''
# Imports of libraries - built in only of course :D
import json

# colours I had noted down from a previous project I did myself. 
# Will be used for outputting with print statements to make it clearer what is what in my terminal.
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

def load_student_record(): # function to load json data
    try:
        with open("students.json", "r") as file: # r = read only ; opens the file "students.json".
            students = json.load(file) #setting the variable students as the content loaded from json.
            return students # breaks the function but returns the data
    except FileNotFoundError: # error handling
        print(RED + "Error: students.json file not found." + RESET) 
        students = [] #empty dictionairy if file not found
    if not students: # error handling if no data
        print(RED + "Error: No students record found in students.json" + RESET) # Error message.

def save_student_record(students): # saves the new json data into the "students.json" file.
    with open("students.json", "w") as file: # w = write ; opens the file "students.json"
        json.dump(students, file, indent=4)
        
def age_input(): # Function to check if age meets the boundaries.
    age_success = False # initial value to enable the true or false statements to be compared.
    while age_success == False: # while statement using the age_success value as a condition.
        age = int(input(RESET + "\nPlease enter the student's age: " + BLUE)) # input to get the age.
        age_valid = False # initial value as checks haven't been conducted yet.
        if 15 <= age < 19: # boundaries to ensure the ages are accurate for the year group (year 12 / 13)
            age_valid = True # the boundaries were met successfully.
        if age_valid == True: # checks that the condition age_valid is true.
            print(RESET) # outputs no text but makes the output have no colour.
            print(PURPLE + f"Age: {age} | validater result: True" + RESET) # output to state the age input was correct.
            age_success = True # exits the loop.
            return age # exits the function and returns the value for age.
        else:
            print(RED + f"Error: \tAge: {age} | validater result: False" + RESET) # Error message.
         
def add_student_record(students): # Function to add a student record.
    name = str(input(RESET + "Please enter the student's name: " + BLUE)).lower() # Name input with the value being forced to be lowercase.
    age = age_input() # calls the age function.
    grade = str(input(RESET+ "\nPlease enter their grade: " + BLUE)).upper() # grade input being forced to be capitalized.
    grades=["A*","A","B","C","D","E","U"] # list of the grades
    if grade not in grades: # compares the grade input to the list to see if the input matches a value in that list.
        print(RED + "Error: Grade was not entered correctly." + RESET) # error
        return # exits function.
        
    students.append({"name": name, "age": age, "grade": grade}) # appends the data (formats)
    save_student_record(students) # calls the function to save the data into the json file.
    print(GREEN + f"The student's ({name}'s) grade has been successfully added!" + RESET) # output to show success to user.

def view_student_record(students): # function to view the student record
    export_request = str(input("Do you want to export the student record into a text file? (y/n) " + BLUE)).lower() #(EXTRA) input asking if the user wants a text file format or a terminal output.
    print(RESET) # outputs no text but makes the output have no colour.
    if export_request == "y": # if user wants the text file option.
        with open("grade_report.txt", "w") as t:  # opens the text file.
            # prints data into the text file.
            print(f"{'Name':<10} {'Age':<5} {'Grade':<5}", file=t) # outputs headers to the text file.
            print("=" * 25, file=t) # outputs a seperator (25 of the character =)to the text file.
            for s in students: # loops through every student in the dataset "students".
                print(f"{s['name']:<10} {s['age']:<5} {s['grade']:<5}", file=t) # outputs the content into the text file
                print("-"*25, file=t) # outputs seperators (25 of the character -) in a row into text file.
            print(GREEN + "Successfully exported the student records to the grade_report.txt file." + RESET) # outputs a success message to inform the user that the view function was a success.
    
    if export_request == "n": # if user does *not* want the text file option
        print(RESET + f"{'Name':<10} {'Age':<5} {'Grade':<5}") # outputs the headers of table
        print("=" * 25) # outputs a seperator (25 of the character =).
        for s in students: # loops through every student in the dataset "students".
            print(CYAN + f"{s['name']:<10} {s['age']:<5} {s['grade']:<5}" + RESET) # outputs the content into the text file
            print("-"*25) # outputs a seperator (25 of the character -).

def delete_student_record(students): #Function to delete a student's data from the student record.
    student_to_remove = str(input("Enter the student's name you wish to remove: "+ BLUE)).lower() # input for user to request the name of the student that they wish to remove from the dataset "students".
    print(RESET) # outputs no text but makes the output have no colour.
    if not student_to_remove: # checks to see if the input was left blank.
        print(RED + "Error: No name was entered. Returning to the menu..." + RESET) # Error message.
    if student_to_remove not in students: # If the name that was entered is not in the dataset.
        print(RED + f"The student {student_to_remove} is not in the record." + RESET) # Error message.
        return # exits the function.
    for s in students: # loops through every student in the dataset "students".
        if s["name"].lower() == student_to_remove: # checks to see if the name from the student it is running through in the loop matches the input.
            students.remove(s) # removes it from the dataset
            save_student_record(students) # saves the modified dataset to the json file.
            print(GREEN + f"Successfully deleted {student_to_remove} and all relating data from the record." + RESET) # outputs a success message.
            return # exits the function.
    print(RED + f"The student ({student_to_remove}) was not found." + RESET) # Error message

def main(): # main function - contains the menu and contains the loading json function etc.
    program_status = True
    while program_status == True: # used to loop through if the program hasn't been exited.
        students = load_student_record() # calls the function that loads the json file content and assigns that data to the variable "students".
        task = int(input("\nEnter the task number you want to carry out:\n- Add Student Record (1)\n- View Student Record (2)\n- Delete Student Record (3)\n- Exit Program (4) " + BLUE)) # an input which outputs the menu.
        print(RESET) # outputs no text but makes the output have no colour.
        if task == 1: # if input is 1
            add_student_record(students) # calls the add_student_record function with the paremeter "students"
        elif task == 2: # if input is 2
            view_student_record(students) # calls the view_student_record function with the paremeter "students"
        elif task == 3: # if input is 3
            delete_student_record(students) # calls the delete_student_record function with the paremeter "students"
        elif task == 4: # if input is 4
            exit_request = str(input("Do you wish to exit this program? "+BLUE)).upper() # input which asks the user if they want to quit.
            print(RESET) # outputs no text but makes the output have no colour.
            if exit_request == "YES": # checks if the input was YES.
                program_status = False # value makes the conditional loop end.
            else:
                program_status = True # condition is set to ensure the main function repeats.
        else:
            print(RED + "You did not enter a task correctly. Please try again." + RESET) # error message.
# running the main function.     
main()
