import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):

        # Create the Main Window
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.

        self.prompt_label = tkinter.Label(self.top_frame,
                                         text='Enter a distance in Kilometers: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame Widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Convert',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #enter the tkinter into main loop
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.

    def convert(self):
        # Get the value entered by the user
        # into kilo_entry widget.
        kilo = float(self.kilo_entry.get())

        # convert kilometers to miles.
        miles = kilo * 0.6214

        # display the results in an info dialog box.
        tkinter.messagebox.showinfo('Results',
                                    str(kilo) +
                                    ' kilometers is equal to ' +
                                    str(miles) + ' miles.')

kilo_conv = KiloConverterGUI()

        
