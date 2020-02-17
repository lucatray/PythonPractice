import tkinter
import tkinter.messagebox


class kilo_converterGUI:
    def __init__(self):
        # create the main window widget.
        self.main_window = tkinter.Tk()


        # create a button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = tkinter.Button(self.main_window,
                                        text = 'Click me!',
                                        command = self.do_something)

        # create a Quit Button. When this button is clicked
        # the root widget's destroy method is called.
        # (The main_window variable references the root widget,
        # so the callback function is self.main_window.destroy)
        self.quit_button = tkinter.Button(self.main_window,
                                          text = 'Quit.',
                                          command = self.main_window.destroy)

        # pack the buttons.
        self.my_button.pack()
        self.quit_button.pack()

        # Enter tkinter into main loop
        tkinter.mainloop()


    # The do_something method is a callback function
    # for the Button widget.

    def do_something(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Response',
                                    'Thanks for clicking the button.')

# Create an instance of the class

kilo_convert = kilo_converterGUI()

