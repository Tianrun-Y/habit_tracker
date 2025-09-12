# Learning Note
## 05/08/2025 The Beginning
### Purpose of this project
* To get first-hand experience building a simple coding project
* To learn about the basic structure and approach of a coding project
* To assess my ability and fitness to proceed further and build more complex projects

### What I have learned so far
* Step-by-step of building a project like this
* **directory tree view** or, in another name, **folder structure diagram**
* In a project like this, there should be a python script, which can be called by using command lines, and a data file such as `.json`, which can be created from the python script
* In the python script, there shall be a `main()` function, which is called when and only when the script is run directly, and seperate functions for different features (an example of modular thinking)

### Step-by-step
1. Define the purpose
2. Design the User Interface
3. Design the data structure
4. Break into functions (modular thinking)
5. Test as you go
6. Save and load data
7. Reflect and expand

### Goal for tomorrow and later
* Learn how to interact with `.json` file in python
* If possible, finish the project
* Most important thing, however, is not finishing it, but reflecting on it!
* Ideally, make a video explaining things in the project, or it can be done in writing

## 06/08/2025 The Project

### Interact with JSON File in Python
* One can use the built in `json` module in python to interact with a `.json` file in a python script. This module is technically a JSON encoder and decoder.

This is the documentation of the module
https://docs.python.org/3/library/json.html

### Opening a file in Python

``` python
with open("file.txt", "r") as f:
    data = f.read()
```

This `with...as` syntax is to manage resources in python safely and automatically, like files, network connections, or locks. This syntax is officially called a *context manager*.

This line below is a way of opening a file, directly, without mechanisms of error handling. This is also what I am more familiar with in the past, because, I assume, when using this in command lines, the requirement for error handling is not as strict, but when opening a file as part of a script, or programme, handling exception cases will be essential to the script of programme running smoothly.

```python
f = open("important_file.txt", "r")
```

### User Interface

* There should be a menu displayed as soon as the programme is run.
* There should be several options in the menu, and in this case, such as adding a habit or tracking a habit.
* To implement this, one can include a `input` function to take in user input in the `display_menu()` function, and one can put the `display_menu()` function in `main()` in side a `while True` loop, which ensures the user can come back to the menu indefinitely if they so wish.

"Another common use for "while True" loops are creating command-line tools and interactive programs. In these cases, the loop continuously accepts and processes user input until the program is terminated." from [this link](https://www.boardinfinity.com/blog/use-while-true-in-python/#:~:text=%22While%20True%22%20is%20a%20looping,code%20to%20be%20repeated%20indefinitely.)

### Top-Level Code Environment
The following is an idiom in python
```python
if __name__ == '__main__':
    main()
```
Here, `__name__` is a special built-in variable that tells you:
* What **context** the current file or module is being run in
* Whether it is being run directly (as a script) or imported by another file

In the top-level code environment, the `__name__` variable is `__main__`. And this is why the if-statement is written in such a way.

[This is the official documentation explaining the usage](https://docs.python.org/3/library/__main__.html)

Note: it is good practice to put 

```python
if __name__ == '__main__':
    main()
```
at the very end of the script. One reason is stylish, and another is the `main()` function must have been fully defined before it can be called.

### Question to consider

Does one load data once in `main()` or in each individual modules

## 08/08/2025 The Project 2.0

### Problem

When loading the data in `main()`, what is the best way to do it such that other functions can use it also.

Solution: pass the habits on as a parameter, i.e., functions such as `view_habits()` becomes `view_habits(habits)` 

### Learning! (JSON Format)

A JSON object is an unordered set of **name-value pairs** (aka attribute-value pairs, key-value pairs, field-value pairs), like a python `dict` object. A JSON file consists of multiple such objects.

Hence, once a JSON file is parsed in python, the data becomes a list of dictionaries, where each dictionary represent one JSON object.

In the case of a habit tracker, it is appropriate to use a JSON format, because  each habit can be represented by a JSON object, and the attributes are things such as 'name', 'creation date', etc. For 'name', it should take a single value of `string`, such as 'going to the gym', same as 'creation date'. for 'dates of completion' however, it should take a list which is expandable (not a problem in python) where each entry is a date.

### Question

If the JSON file is loaded in python in a way such that the top-level structure is a list, would it not take linear time to look up each item, which is not very time-efficient?

### View_habit() function

* Easiest way to access loaded data is to take it in as a parameter of the function
* I should think of a way to make it more presentable than simply `print(habits)`

### Add_habit() function

* Most basic feature: ask user to type in a name
* Slightly more advanced, perhaps asking the user to confirm the name? With [y/n] question
* The date of creation should be added automatically from the os of the computer

```python
from datetime import date

today = date.today()
print(today)  # e.g., 2025-08-08
```
From chatgpt answer, what format to use when storing dates:
[link](date_format.md)

### Mark_habit() function
It should take two parameters: one is user input which is the habit being marked, and another one the entire list of habits to use and then return.

It should be simply a case of appending today's date to the list of dates of completion.

### Question
How to use the python Debug Console?

### FIRST WORKING FULL PROGRAMME
The file habit_tracker_v0.py is the first version of the programme that works, with the most basic features, and not much exception handling capability. It interacts with the sample.py file.

It can do:
* see habits
* add habit
* mark a habit as done for today
* save the result in a json file

So much more features could be added, and the most immediate ones I can think of:
* error handling
* better ways of presenting the list of habits
* the status of habits as done or not yet done

Some further features:
* calender views??

### Task for now
Create a README.md file that accompanies the most basic programme, after adding more error handling. Make it into a package. Perhaps, include version control in this project too.

### Learning: Error Handling in Python
* The most common way: `try`-`except` block
```python
try:
    result = 10/0
except ZeroDivisionError:
    print("You can't divide by zero!")
```
## 11/08/2025 The Improvements

Added a check habit status feature

Fixed the problem with adding the same date more than once to "dates_of_completion"

### How to write a good README.md file

[This link](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/) is very helpful.

A good README.md file should be in a hybrid format, consisting of contents for users of both technical or non-technical background.

### How to improve the User interface

At the moment, the UI looks something like this:
```python
---menu---
1. View habits
2. Add a habit
3. List current habit status
4. Mark a habit as done
5. quit


Please type in your selection 
1 
[{'name': 'Drink water', 'date_of_creation': '2025-08-08', 'dates_of_completion': ['2025-08-08', '2025-08-11']}, {'name': 'Play chess', 'date_of_creation': '2025-08-08', 'dates_of_completion': ['2025-08-11']}, {'name': 'Gym', 'date_of_creation': '2025-08-11', 'dates_of_completion': ['2025-08-11']}, {'name': 'Leetcode', 'date_of_creation': '2025-08-11', 'dates_of_completion': ['2025-08-11']}]

Press any key to return to the menu...
```
This is definitely not how I wanted to present the data to the user, at all. 

## 18/08/2025 Learning continued

Today's objective is to learn more about using `git` for a personal project like this, and the best practices around it. 

What I've learned so far:
* Using Source Control feature in VSCode, as an alternative to using command line for git
* How to use `.gitignore`
* The best practice in organising a git folder, naming things, writing commit messages, etc. 

### Using Git in VSCode

[This](https://code.visualstudio.com/docs/sourcecontrol/overview) is the official documentation in VSCode

#### Colour scheme

| Color / Decoration  | Meaning                       | Git Equivalent                |
| ------------------- | ----------------------------- | ----------------------------- |
| **Green**           | New file, not yet committed   | `git add` / staged            |
| **Blue**            | Modified file, not yet staged | `git diff` / unstaged changes |
| **Red**             | Deleted file, not yet staged  | `git rm` / unstaged deletion  |
| **Orange / Yellow** | Renamed or moved file         | `git mv` / tracked rename     |
| **Gray**            | Ignored file (`.gitignore`)   | Git is not tracking           |
| **Plain / White**   | Unmodified, tracked file      | Clean (no changes)            |

#### Symbols
* M → Modified
* A → Added / staged
* D → Deleted
* U → Unmerged / conflict

### About `.gitignore`

[This](https://git-scm.com/docs/gitignore) is the official documentation. 

In a project like this, there are personal notes, or experimental files. They should be excluded from the tracking of git. ChatGPT recommended putting experimental codes in a `scratch/` folder.

### Best Practices

* `doc/` folder for documentations, like this
* `src/` folder for source codes
* Use imperivatives, for example, 'add feature A', rather than 'adding feature A', or 'added feature A'

The following could also be a good way to organise files, in the case where there are not multiple documents for notes.
```css
my-project/
  ├── src/
  ├── .gitignore
  ├── README.md
  └── NOTES.md
```
## 28/08/2025 The continuation

The progress on this project took a pause, since I spent the entire week last week learning to build a website, and finally I have a website! 

Now, the goal is still to make a first publishable version of the most basic features, add into error handling and enhanced user experiences. 

### Where to put the json file?
It appears putting it in a seperate folder works the best! And currently the programme can handle the cases: 1) no `habits.json` file -- create one; 2) `habits.json` file consisting of no objects -- when used view habits print a message rather than nothing; 3) `habits.json` file exists and has content -- all good!

### The question, or chanllenge?
How does one keep enough notes for oneself, such that when one comes back to the project after a gap, one can pick it up where it was finished last time? Today for example, I found errors in the code which I did not fix last time, but I had no idea, and diagnosing perhaps took longer than it should because of this. Learning needed!

### Problem
A problem arised when trying to deal with the empty data file. I wanted it to stay there on github as an empty file, but I also want git to stop tracking my local file. Still trying to find a solution, unfixed still. 

### TOMORROW
Tomorrow! I should try to fix the above problems, and start to write a README.md file. Hopefully, this project will be publishable by the end of tomorrow.

## 03/09/2025 The actually tomorrow

I did not remember that I had to work on the 29th of August. Now, after 6 days, I am back at the project.

## 05/09/2025 The return

### New feature added!
I added another feature which I considered essential. This new feature allows the user to type in the name of an exising habit, and the terminal will list all the dates where this habit is completed on that date.

### Future feature idea
Currently, this programme works the best if there is only a small amount of habits, and they are tracked over a short period of time. However, I was thinking that a good feature for the future is to export a calender, perhaps in the form of a pdf document, so that the user can easily see all the dates where one habit is marked as complete. 

### Next step
Write a README.md file! It does not need to be perfect, fun, or detailed. But, it must be done according to the best practices.

## 12/09/2025 README

The main objective today is to write a README document.

For the future blog:
The project exists because I, a novice in the field of software engineering, decided that I needed some more hand-on experiences building a project from start to finish. I chose to build a command-line programme because of my experiences in Python and a research software called GAP. This would be more appropriate than, say, a web app using JavaScript. The topic itself, not exactly exciting, was an option offered by ChatGPT, but I was very clear that the sole purpose of building this project was for me to learn. In the future, having completed more similar projects like this, I can hopefully step into the more original creations.

### "Programme" vs "Software"

I am calling this project a programme because of its scale. It can be run with a single python script, and is indeed written in this way.