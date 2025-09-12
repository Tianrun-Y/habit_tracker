# Habit Tracker CLI
Habit Tracker CLI is a simple command-line habit tracker written in Python.

## Background
See my personal homepage

## Installation
TODO

## Usage

The programme has a command-line interface (CLI), and the user interacts with the programme by typing in commands. When the user runs the script, the command-line interface will display a menu where the user can select options. This menu looks like this:

```zsh
 ---menu--- 

1. View habits
2. Add a habit
3. List current habits status
4. Mark a habit as done
5. Check the dates of completion of a habit
6. Save and quit

```
As one can see from the menu, the user can add the habit that they would like to track, and can later mark the days when the habit is complete. 

Option 3, for example, then allows the user to check the habits which are completed on that day, and those which are not yet completed. This is to encourage the user to track and slowly build a habit that the user like to perform everyday.

For example:
```zsh
 ---menu--- 

1. View habits
2. Add a habit
3. List current habits status
4. Mark a habit as done
5. Check the dates of completion of a habit
6. Save and quit


Please type in your selection 
3
Completed task:
1. coding
2. journaling

Not yet completed task:
1. going to the gym

Press any key to return to the menu...
```

After performing actions such as adding a habit and marking a habit, the user can save the changes by choosing option 6. The data will be saved locally, and will be loaded when the programme is next run.