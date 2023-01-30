# country-app

The country app is a program with a user interface (Tkinter module). This program downloads data via API and allows the display of information about every country, plays quizzes based on this data, and display a plot. 

Program operation:\
In the first part of the program, we choose a country from the list and click the button "show information" to display information about this country.  We must choose at least two countries to take the quiz - it is the second part of the program. This quiz is about the populations of the countries selected previously. We have to click the button "start quiz" and choose a country that has more population. When our answer is wrong the question box will turn red, whereas when our answer is right to question box will turn green and we will get a point to the total score. The last functionality of the program is displaying the plot with the populations of the countries selected in the first part of the program.

## Requirement 
- Python 3.11.1
- Python - tkinter
- Python - pandas 1.5.3
- Python - matplotlib 3.6.3
## Program files description:

- main.py - calling a functions 
- widgets.py - function with all GUI widgets
- gui_helper_functions.py - functions responsible for the operation of the program 
- settings.py -  window settings 
- data.py- this file contains data used in the program
- up_arrow.png - image used for the button

## Screenshots

![App Screenshot](https://github.com/kinga1234/country-app/blob/master/ScreenShots/Image1.png?raw=true)

![App Screenshot](https://github.com/kinga1234/country-app/blob/master/ScreenShots/Image2.png?raw=true)

![App Screenshot](https://github.com/kinga1234/country-app/blob/master/ScreenShots/Image3.png?raw=true)

![App Screenshot](https://github.com/kinga1234/country-app/blob/master/ScreenShots/Image4.png?raw=true)
