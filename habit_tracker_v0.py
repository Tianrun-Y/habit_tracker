import json
import os
from datetime import date

# Here, as per Python style guides, import of packeges stat at the very top of a script
DATA_FILE = "sample.json"
# Here, this is a well-established idiom
# And, it follows the stylish convention of using capitalised letters for a constant

def display_menu():
    print("\n ---menu---")
    print("1. View habits")
    print("2. Add a habit")
    print("3. List current habits")
    print("4. Mark a habit as done")
    print("5. quit")
    print("\n")
    choice = input("Please type in your selection \n")
    return choice

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {"habits": []}
        # This creates an empty dictionary
    
def save_habits(habits):
    with open("sample.json", "w") as f:
        json.dump(habits, f)

def view_habits(habits):
    print(habits)

def add_habit():
    habit_name = input("Please type in the name of your new habit \n")
    today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    new_habit = {"name": habit_name, "date_of_creation": today_str, "dates_of_completion": []}
    return new_habit

def mark_habit(habits, finished_habit):
    for habit in habits:
        if habit["name"] == finished_habit:
            today = date.today()
            today_str = today.strftime("%Y-%m-%d")
            habit["dates_of_completion"].append(today_str)
            break
        #need some error handling here
    return habits

def main():
    habits = load_data()
    while True:
        choice = display_menu()
        if choice == "1":
            view_habits(habits)
        elif choice == "2":
            habits.append(add_habit())
        # elif choice == "3":
        elif choice == "4":
            finished_habit = input("Please type in the habit you finished today! \n")
            habits = mark_habit(habits, finished_habit)
        elif choice == "5":
            print("goodbye")
            save_habits(habits)
            break
        else:
            print("Please type in a valid input")

if __name__ == "__main__":
    main()