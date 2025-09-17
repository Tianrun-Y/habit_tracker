# Habit Tracker CLI
Habit Tracker CLI is a simple command-line habit tracker written in Python.

## Background
See my personal homepage

## Installation

We recommend two ways to install this programme on your local computer.

1. Clone this repo (recommended for developers)

```bash
git clone https://github.com/your-username/habit-tracker.git
cd habit-tracker
```

2. Download the project folder as a zip file, from Github.



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

## Limitations

1. The programme in its current version does not support removing a tracked habit. If the user is comfortable with editing `.json` files, the user can remove a habit by deleting the corresponding `json` object from the data file.

2. Due to the nature of a command-line interface programme, the user experience is the best when the number of habits being tracked does not exceed a couple of dozens, but that should not be a problem as one should not have to track that many habits every day! However, the current way of displaying dates of completetion is not ideal for users to track over a long period of time, say, more than a few months. In the future, perhaps we can add a feature that allows users to export their data into a calender view, for better user experience. 