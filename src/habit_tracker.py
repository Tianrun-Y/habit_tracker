import json
import os
from datetime import date
# Here, as per Python style guides, import of packeges stat at the very top of a script

DATA_FILE = "data/habits.json"
# Here, this is a well-established idiom
# And, it follows the stylish convention of using capitalised letters for a constant
# This makes it easy to change file paths, as it can be done only once here, not every place in the code where the path appears

def display_menu():
    print("\n ---menu--- \n")
    print("1. View habits")
    print("2. Add a habit")
    print("3. List current habit status")
    print("4. Mark a habit as done")
    print("5. Check the dates of completion of a habit")
    print("6. Save and quit")
    print("\n")
    choice = input("Please type in your selection \n")
    return choice

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {}
        # This creates an empty dictionary
    
def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f)

def view_habits(habits):
    print("The following are your current habits!")
    i = 1
    for habit in habits:
        print(str(i) + ". " + habit["name"])
        i = i + 1

def add_habit():
    habit_name = input("Please type in the name of your new habit \n")
    today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    new_habit = {"name": habit_name, "date_of_creation": today_str, "dates_of_completion": []}
    return new_habit

def mark_habit(habits, finished_habit):
    exist = False
    for habit in habits:
        if habit["name"] == finished_habit:
            today = date.today()
            today_str = today.strftime("%Y-%m-%d")
            if today_str not in habit["dates_of_completion"]:
                habit["dates_of_completion"].append(today_str)
                exist = True
                print("Congratulations for having done", finished_habit, "today!")
                break
            else:
                print("You've already completed this habit today!")
                exist = True
                break
        #need some error handling here
    if exist == False:
        print("Please type in an existing habit \n")
    return habits

def check_habits(habits):
    completed = []
    incompleted = []
    today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    for habit in habits:
        if today_str in habit["dates_of_completion"]:
            completed.append(habit["name"])
        else:
            incompleted.append(habit["name"])
    print("Completed task:")
    if completed == []:
        print("You haven't completed any habits yet. Start tracking them now!")
    i = 1
    for habit in completed:
        print(str(i) + ". " + habit)
        i = i + 1
    print("\nNot yet completed task:")
    if incompleted == []:
        print("You've completed all your habits!")
    i = 1
    for habit in incompleted:
        print(str(i) + ". " + habit)
        i = i + 1

def check_dates(inquired_habit, habits):
    exist = False
    for habit in habits:
        if habit["name"] == inquired_habit:
            exist = True
            i = 1
            for date in habit["dates_of_completion"]:
                print(str(i) + ". " + date)
                i = i + 1
            break
    if exist == False:
        print("Please type in an existing habit \n")
    

def main():
    habits = load_data()
    while True:
        choice = display_menu()
        if choice == "1":
            if habits == {}:
                print("You currently do not have any habits tracked!")
            else:
                view_habits(habits)
        elif choice == "2":
            habits.append(add_habit())
            print("habit added successfully!")
        elif choice == "3":
            check_habits(habits)          
        elif choice == "4":
            finished_habit = input("Please type in the habit you finished today! \n")
            habits = mark_habit(habits, finished_habit)
        elif choice == "5":
            inquired_habit = input("Please type in the habit want to see the dates of completion! \n")
            check_dates(inquired_habit, habits)
        elif choice == "6":
            print(" \n Habits saved successfully!")
            print(" \n Goodbye \n")
            save_habits(habits)
            break
        else:
            print("Please type in a valid input")
        input("\nPress any key to return to the menu...")

if __name__ == "__main__":
    main()