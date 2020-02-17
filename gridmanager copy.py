# Lucas Traynor
# CSCI-1060
# 5/2/2018
# This program creates a colored grid using the Tkinter module


import tkinter
import tkinter.messagebox


for r in range(3):
    for c in range(4):

        tkinter.Label(text='Email', fg='white', bg='royalblue3', width = 15,
                      height=6).grid(row=0, column=0, padx=5, pady=5)
        tkinter.Label(text='D2L Brightspace', fg='white', bg='violetred4', width=15,
                      height=6).grid(row=0, column=1, padx=5, pady=5)
        tkinter.Label(text='OneDrive', fg='white', bg='royalblue3', width=15,
                      height=6).grid(row=0, column=2, padx=5, pady=5)
        tkinter.Label(text='Employee Home', fg='white', bg='slategray3', width=15,
                      height=6).grid(row=0, column=3, padx=5, pady=5)
        tkinter.Label(text='eServices', fg='white', bg='slategray3', width=15,
                      height=6).grid(row=1, column=0, padx=5, pady=5)
        tkinter.Label(text='Ask Century', fg='white', bg='darkorange2', width=15,
                      height=6).grid(row=1, column=1, padx=5, pady=5)
        tkinter.Label(text='Lynda.Com\nTraining', fg='white', bg='red4', width=15,
                      height=6).grid(row=1, column=2, padx=5, pady=5)
        tkinter.Label(text='Calender', fg='white', bg='darkorange2', width=15,
                      height=6).grid(row=1, column=3, padx=5, pady=5)
        tkinter.Label(text='Library', fg='white', bg='darkorange2', width=15,
                      height=6).grid(row=2, column=0, padx=5, pady=5)
        tkinter.Label(text='Search for\nCourses', fg='white', bg='slategray3', width=15,
                      height=6).grid(row=2, column=1, padx=5, pady=5)
        tkinter.Label(text='Bookstore', fg='white', bg='olivedrab4', width=15,
                      height=6).grid(row=2, column=2, padx=5, pady=5)
        tkinter.Label(text='Manage\nMyLogins', fg='white', bg='gray', width=15,
                      height=6).grid(row=2, column=3, padx=5, pady=5)

tkinter.mainloop()
