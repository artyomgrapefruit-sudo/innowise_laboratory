def generate_profile (age):
  if age < 13:
    return "Child"
  if age < 20:
    return "Teenager"
  return "Adult"


user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")

birth_year = int(birth_year_str) # convert to int
current_age = 2025 - birth_year # calculate current age

hobbies = []

while True:
  hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
  if hobby == 'stop':
    break
  hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = {
  "name": user_name,
  "age": current_age,
  "stage": life_stage,
  "hobbies": hobbies
}

print(f"\n---")
print(f"Profile Summary:")
print(f"Name: {user_profile["name"]}")
print(f"Age: {user_profile["age"]}")
print(f"Life Stage: {user_profile["stage"]}")

# print(f"\n---\nProfile Summary:\nName: {user_profile["name"]}\nAge: {user_profile["age"]}\nLife Stage: {user_profile["stage"]}")

if len(user_profile["hobbies"]) == 0:
  print("You didn`t mention any hobbies")
else:
  for curr in user_profile["hobbies"]:
    print(f"- {curr}")
print("---")