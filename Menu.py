"""
Handles the creation of the GUI using tkinter. 

It spawns the menu as a MainWindow instance to input the required parameters.

It also spawns a second menu as a SecondWindow instance to add custom solar system bodies.
"""

import tkinter as tk


class MainWindow:
    """

    The main menu for the application.

        Attributes:
            entries (list-like): Contains all tk.Entry instances.

            outputs (list-like): Contains all data taken from tk.Entry instances.

            customBodies (list-like): Contains the data for user-defined custom bodies.

            main (tk.Tk): The main menu window.

        Methods:
            time_period(): Creates the time period input frame.

            dates(): Creates the date input frames.

            algorithm(): Creates the algorithm input frame.

            enter_button(): Creates the 'Continue' button to move onto the simulation itself.

            new_body_button(): Creates the 'Add new body' button to allow the user to add custom Particle instances.

            enter(): Scrapes all data from the entries and destroys the window.

            new_body(): Spawns a SecondWindow instance, allowing the user to add custom Particle instances.

    """

  

    def __init__(self):
        """

        Initialises a new instance of MainWindow.

        """
        #Stores the entries for the main menu.
        self.entries = []

        #Stores the data in each entry.
        self.outputs = []

        #Stores the data for the custom bodies in the same format as data.py outputs.
        self.customBodies = []

        #Creates the main window.
        self.main = tk.Tk()
        self.main.title('Simulation')

        #Creates the other frames in the menu
        self.time_period()
        self.dates()
        self.algorithm()
        self.enter_button()
        self.new_body_button()

        #Spawns the menu.
        self.main.mainloop()


    def time_period(self):
        """

        Creates the time period entry in its own frame.

        """

        #The frame containing the time period input.
        frm_timePeriod = tk.Frame(master = self.main)

        #Creates and inserts the label for the entry.
        lbl_timePeriod = tk.Label(master = frm_timePeriod, text = 'Time period (seconds)', width = 20, anchor = 'w')
        lbl_timePeriod.grid(row = 0, column = 0, sticky = 'W')

        #Creates and inserts the entry.
        ent_timePeriod = tk.Entry(master = frm_timePeriod, width = 16)
        ent_timePeriod.insert(0, '100')
        self.entries.append(ent_timePeriod)
        ent_timePeriod.grid(row = 0, column = 1)

        #Inserts the time period frame into the master window.
        frm_timePeriod.grid(row = 0, column = 0, columnspan = 2)


    def dates(self):
        """

        Creates frames for the Start date and Finish date, and adds them to the main window.

        """

        #Contains the label names
        labels = ['Start date (dd/mm/yyyy)', 'End date (dd/mm/yyyy)']

        #Iterates the creation of the date inputs, as they are the same
        for count, i in enumerate(labels):

            #The frame containing the date
            frm_date = tk.Frame(master = self.main)

            #Creates and inserts the label for the date entry.
            lbl_date = tk.Label(master = frm_date, text = i, width = 20, anchor = 'w')
            lbl_date.grid(row = 0, column = 0)

            #Creates and inserts the day entry.
            ent_day = tk.Entry(master = frm_date, width = 5)
            ent_day.insert(0, string = '0' + str(4+count))
            self.entries.append(ent_day)
            ent_day.grid(row = 0, column = 1)

            #Creates and inserts the month entry.
            ent_month = tk.Entry(master = frm_date, width = 5)
            ent_month.insert(0, string = '12')
            self.entries.append(ent_month)
            ent_month.grid(row = 0, column = 2)

            #Creates and inserts the year entry.
            ent_year = tk.Entry(master = frm_date, width = 5)
            ent_year.insert(0, string = '2023')
            self.entries.append(ent_year)
            ent_year.grid(row = 0, column = 3)

            frm_date.grid(row = count + 1, column = 0, pady = 2, columnspan = 4)


    def algorithm(self):
        """

        Creates the algorithm section, allowing the user to select from the three available algorithms.

        """

        #Creates the frame for the algorithm section
        frm_algorithm = tk.Frame(master = self.main)

        #Creates the label for the algorithm input
        lbl_algorithm = tk.Label(master = frm_algorithm, text = 'Algorithm', 
                                width = 18, anchor = 'w')
        lbl_algorithm.grid(row = 0, column = 0)

        #Creates the input for the algorithm
        ent_algorithm = tk.Entry(master = frm_algorithm, width = 18)
        ent_algorithm.grid(row = 0, column = 1)
        
        #Adds the algorithm entry to the entry list
        self.entries.append(ent_algorithm)

        #Inserts the algorithm section frame
        frm_algorithm.grid(row = 3, column = 0, columnspan = 2)


    def enter_button(self):
        """

        Creates the 'continue' button in its own frame.

        """ 

        #Creates the frame for the button.
        frm_enter = tk.Frame(master = self.main)

        #Creates and inserts the button.
        btn_enter = tk.Button(master = frm_enter, text = 'Continue', command = self.enter, width = 15)
        btn_enter.grid(row = 0, column = 0)

        #Inserts the button frame into the window.
        frm_enter.grid(row = 4, column = 1, columnspan = 2, sticky = 'e')


    def new_body_button(self):
        """

        Button that spawns a new menu that allows the user to input another body.

        """

        #Creates the frame for the button
        frm_newBody = tk.Frame(master = self.main)

        #Creates the button and inserts it into the frame
        btn_newBody = tk.Button(master = frm_newBody, text = 'Add new object', command = lambda: self.new_body(), width = 15)
        btn_newBody.grid(row = 0, column = 0)

        #Inserts the button frame into the window
        frm_newBody.grid(row = 4, column = 0, columnspan = 2, sticky = 'w')


    def enter(self):
        """

        Runs when the Continue button is pressed. Scrapes the text from the entries and stores them to a list that can be
        accessed later.

        """

        #Scrapes all values from entries
        for entry in self.entries:
            
            self.outputs.append((entry.get()).lower())

        
        self.main.destroy()


    def new_body(self):
        """

        Spawns the secondary window that handles adding new bodies.

        """
        SecondWindow(self)



class SecondWindow:
    """

    A second menu that takes in new bodies with custom mass, position, velocity, radius, name and colour.

        Attributes:
            entries (list-like): Contains all tk.Entry instances.

            attributeList (list-like): Contains names of all required attributes to create a Particle instance.

            defaultList (list-like): Contains default values for all Particle attributes.

            mainWindow (tk.Tk): The main window from which the SecondWindow instance spawned.

            secondary (tk.Tk): The secondary window spawned on initialisation.

        Methods:
            attribute_entries(): Creates frames for all Particle attribute entries.

            single_entry(count, attribute): Creates a label and entry for a scalar or text Particle attribute.

            vector_entry(count, attribute): Creates a label and three entries for a 3-vector Particle attribute.

            enter_button(): Creates the 'Continue' button to move back into the main window.

            enter(): Scrapes all data from the entries and destroys the window.

    """

    def __init__(self, MainWindow):
        """

        Initialises a new instances of SecondWindow.

        """
        #Stores all the entries for the secondary window.
        self.entries = []

        #Names all the attributes I want to take and gives default values so I can iterate the entry generation.
        self.attributeList = [
                'Name',
                'Mass (kg)',
                'Radius (m)',
                'Position vector (m)',
                'Velocity vector (m/s)',
                'Colour (hex)',
            ]

        self.defaultList = [
            'Satellite',
            '1000',
            '10',
            ['0','0','0'],
            ['0','0','0'],
            '#ffffff',
        ]

        self.MainWindow = MainWindow
        
        #Initialises the secondary window.
        self.secondary = tk.Tk()
        self.secondary.title('Add new body')

        #Adds all the entries.
        self.attribute_entries()
        self.enter_button()

        #Spawns the window.
        self.secondary.mainloop()


    def attribute_entries(self):
        """

        Creates a label and an input for each attribute in attributeList.

        """
        #Iterates across every attribute and gets the corresponding dict key.
        for count, attribute in enumerate(self.attributeList):
            
            #Decides the format of each entry depending if there is one or three inputs using the associated default.

            #If it is a scalar/text entry:
            if isinstance(self.defaultList[count], str):
                self.single_entry(count, attribute)

            #If it is a vector entry:
            else:
                self.vector_entry(count, attribute)


    def single_entry(self, count, attribute):
        """
        
        Creates a label and an input for a single entry, i.e. a name.
        
        """
        #Gives each attribute an individual frame.
        frm_input = tk.Frame(master = self.secondary)

        #Creates and inserts the label for the attribute.
        lbl_attribute = tk.Label(master = frm_input, text = attribute, width = 20, anchor = 'w')
        lbl_attribute.grid(row = 0, column = 0, sticky = 'w')

        #Creates and inserts the entry for the attribute.
        ent_attribute = tk.Entry(master = frm_input, width = 23)
        ent_attribute.grid(row = 0, column = 1)

        #Inserts a default value.
        ent_attribute.insert(0, string = self.defaultList[count])

        #Adds the entry to the list.
        self.entries.append(ent_attribute)

        #Inserts the frame into the window.
        frm_input.grid(row = count, column = 0, pady = 2)


    def vector_entry(self, count, attribute):
        """

        Creates a label and an input for a vector entry, i.e. a position.
        
        """
        #Gives each attribute an individual frame.
        frm_attribute = tk.Frame(master = self.secondary)

        #Creates and inserts the label for the attribute.
        lbl_attribute = tk.Label(master = frm_attribute, text = attribute, width = 20, anchor = 'w')
        lbl_attribute.grid(row = 0, column = 0, sticky = 'w')

        #Creates a separate frame for the three entries.
        frm_entries = tk.Frame(master = frm_attribute, width = 21)

        #Creates an n-dimensional input.
        for i, value in enumerate(self.defaultList[count]):
            #Creates and inserts the entry
            ent_attribute = tk.Entry(master = frm_entries, width = 7)
            ent_attribute.grid(row = 0, column = i)

            #Adds the entry to the list
            self.entries.append(ent_attribute)

            #Inserts a default value.
            ent_attribute.insert(0, string = self.defaultList[count][i])
        
        #Inserts the entry frame
        frm_entries.grid(row = 0, column = 1)

        #Inserts the attribute frame
        frm_attribute.grid(row = count, column = 0, pady = 2)


    def enter_button(self):
        """

        Creates the 'enter' button in its own frame.

        """ 

        #Creates the frame for the button.
        frm_enter = tk.Frame(master = self.secondary)

        #Creates and inserts the button.
        btn_enter = tk.Button(master = frm_enter, text = 'Continue', command = self.enter, width = 20)
        btn_enter.grid(row = 0, column = 0)

        #Inserts the button frame into the window.
        frm_enter.grid(row = len(self.attributeList), column = 0, columnspan = 2, sticky = 'e')


    def enter(self):
        """

        This function will run when the Enter button is pressed. 
        
        It scrapes the text from the entries and stores them to a list that can be accessed later.

        """
        #Uses the defined order of entries to add the new body data.
        self.MainWindow.customBodies.append(
            {
                'Name': self.entries[0].get(),
                'Mass': float(self.entries[1].get()),
                'Radius': float(self.entries[2].get()),
                'Position': [float(self.entries[3].get()), float(self.entries[4].get()), float(self.entries[5].get())],
                'Velocity': [float(self.entries[6].get()), float(self.entries[7].get()), float(self.entries[8].get())],
                'Colour': self.entries[9].get()
            },
        )        

        self.secondary.destroy()
