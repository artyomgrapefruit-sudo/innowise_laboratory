students = list()

def get_command():
  print("--- Student Grade Analyzer ---\n1. Add a new student\n2. Add grades for a student\n3. Generate a full report\n4. Find thr top student\n5, Exit programm")
  try:
    input_value = input('Enter your choice: ')
  except:
    print('Somethink went wrong')
  return input_value

def menu():
  command = get_command()
  if(command == '1'):
    add_student()
  if(command == '2'):
    add_grade()
  if(command == '3'):
    show_report()
  if(command == '4'):
    find_top()
  if(command == '5'):
    return 0
  return

def add_student():
  name = input('Enter student name: ')
  # add normal find
  new_dict = {
    "name": name,
    "grades": list()
  }
  if new_dict in students:
    print('No2')
    return
  students.append(new_dict)
  return

def add_grade():
  name = input('Enter student name: ')
  # add normal find
  while True:
    grade = input("Enter student grade (or 'done' to finish): ")
    if (grade == 'done'):
      break
    students[name]["grades"].append(grade)
  return

def show_report():
  print(students)
  return

def find_top():
  name = input('')
  return

while True:
  if menu() == 0:
    break
print('Exiting program.')