Charles Proudfoot
38602598
Lancaster University

PHYS281 Solar System Project Submission 2023


This folder contains the Python files for my PHYS281 project submission. This note is worth reading before using the simulation just in case some direction is required.

To run the simulation, run Main.py. This will create the first menu, where you can choose your time interval, start and end dates, and your choice of approximation algorithm (1 = Euler, 2 = Euler-Cromer, 3 = Euler-Richardson). You can also add a custom object to the system if you feel like it, using the 'Add new object' button. Bear in mind that doing so may affect the accuracy of the results.

When you're happy with the setup, go ahead and press Continue. This will begin the simulation. Depending on your parameters, it may take a little while, so your patience is appreciated. Once it's done, all the summary data will be available in ephemeride_data/!summary_file.txt, and a 3D graph will be displayed to show the movements of the planets.

Feel free to browse the testing folder, it's got plenty of data to look over and it's also where you'll find the code that I used to make graphs for my report. Those graphing files aren't really submitted for grading, they're just there for organisation purposes, but you're welcome to take a look anyway.

📁ephemeride_data: Where the position data for every body is stored for graphing later.

📁testing: Contains data from specific test cases I performed to evaluate the software.

📄data.py: Contains functions that collect and format JPL and time ephemeride_data.

📄Files.py: Contains functions that deal with opening, writing and creating external data files.

📄Graphics.py: Contains functions that create a graphical output from the data.

📄Main.py: The main file that calls others, sets up and runs the simulation.

📄Menu.py: Contains two menu classes for human data entry.

📄Particle.py: Contains the Particle class that models the solar system bodies.

📄Tests.py: Contains functions intended to check that data is correct and that certain variables are concerned.
