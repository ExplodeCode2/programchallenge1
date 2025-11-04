# imports
import json
import os


# colours I had noted down from a previous project I did myself. 
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
# the data will be kept in a list of dictionairies. 

def load_student_record():
    try:
        with open("students.json", "r") as file: # r = read only
            students = json.load(file)
            return students
    except FileNotFoundError:
        print(RED + "Error: students.json file not found." + RESET)
        students = []
    if not students:
        print(RED + "Error: No students record found in students.json" + RESET)
def save_student_record(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
        
def age_input():
    age_success = False
    while age_success == False:
        age = int(input(RESET + "\nPlease enter the student's age: " + BLUE))
        age_valid = False
        if 15 <= age < 19:
            age_valid = True 
        if age_valid == True:
            print(RESET)
            print(PURPLE + f"Age: {age} | validater result: True" + RESET)
            age_success = True
            return age
        else:
            print(RED + f"Error: \tAge: {age} | validater result: False" + RESET)
         
def add_student_record(students):
    name = str(input(RESET + "Please enter the student's name: " + BLUE)).lower()
    age = age_input()
    grade = str(input(RESET+ "\nPlease enter their grade: " + BLUE)).upper()
    grades=["A*","A","B","C","D","E","U"]
    if grade not in grades:
        print(RED + "Error: Grade was not entered correctly." + RESET)
        return
        
    students.append({"name": name, "age": age, "grade": grade})
    save_student_record(students)
    print(GREEN + f"The student's ({name}'s) grade has been successfully added!" + RESET)

def view_student_record(students):
    export_request = str(input("Do you want to export the student record into a text file? (y/n) " + BLUE)).lower()
    print(RESET)
    if export_request == "y":
        with open("grade_report.txt", "w") as t: 
            print(f"{'Name':<10} {'Age':<5} {'Grade':<5}", file=t)
            print("=" * 25, file=t)
            for s in students:
                print(f"{s['name']:<10} {s['age']:<5} {s['grade']:<5}", file=t)
                print("-"*25, file=t)
            print(GREEN + "Successfully exported the student records to the grade_report.txt file." + RESET)
    
    if export_request == "n":    
        print(RESET + f"{'Name':<10} {'Age':<5} {'Grade':<5}")
        print("=" * 25)
        for s in students:
            print(CYAN + f"{s['name']:<10} {s['age']:<5} {s['grade']:<5}" + RESET)
            print("-"*25)

def delete_student_record(students):
    remove_request = str(input("Enter the student you wish to remove: "+ BLUE)).lower()
    print(RESET)
    if not remove_request:
        print(RED + "Error: No name was entered. Returning to the menu..." + RESET)
    for s in students:
        if s["name"].lower() == remove_request:
            students.remove(s)
            save_student_record(students)
            print(GREEN + f"Successfully deleted {remove_request} and all relating data from the record." + RESET) 
            return
    print(RED + f"The student ({remove_request}) was not found." + RESET)

def main():
    program_status = True
    while program_status == True:
        students = load_student_record()
        task = int(input("\nEnter the task number you want to carry out:\n- Add Student Record (1)\n- View Student Record (2)\n- Delete Student Record (3)\n- Exit Program (4) " + BLUE))
        print(RESET)
        if task == 1:
            add_student_record(students)
        elif task == 2:
            view_student_record(students)
        elif task == 3:
            delete_student_record(students)
        elif task == 4:
            exit_request = str(input("Do you wish to exit this program? "+BLUE)).upper()
            print(RESET)
            if exit_request == "YES":
                program_status = False
            else:
                main()
        else:
            print(RED + "You did not enter a task correctly. Please try again." + RESET)
# running the main function which contains the menu.     
main()
