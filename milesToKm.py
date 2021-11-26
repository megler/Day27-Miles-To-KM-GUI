# milesToKm.py
#
# Python Bootcamp Day 27 - Miles to KM Converter GUI
# Usage:
#      Using tkinter to create a GUI, input miles and receive kilometer output
#
# Marceia Egler November 26, 2021


from tkinter import *
import sys


def create_gui():

    root = Tk()
    root.minsize(width=250, height=100)
    root.config(padx=50, pady=50)
    root.title("Miles to Kilometers Converter")
    root.resizable(1, 1)

    def calculate_conversion():
        convert = int(miles.get()) * 1.609
        two_dec_convert = "{:.2f}".format(convert)
        conversion_display.config(text=two_dec_convert)

    # Row 0
    miles_label = Label(text="Miles")
    miles = Entry()

    # Row 1
    equal_to_label = Label(text="Is equal to: ")
    conversion_display = Label(text="0")
    km = Label(text="km")

    # Row 2
    calculate = Button(text="Calculate", command=calculate_conversion)

    # Grid Layout
    equal_to_label.grid(column=0, row=1, pady=5)
    miles.grid(column=1, row=0, padx=10)
    calculate.grid(column=1, row=2)
    conversion_display.grid(column=1, row=1)
    miles_label.grid(column=2, row=0, pady=5)
    km.grid(column=2, row=1, pady=5)

    root.mainloop()


def main():
    create_gui()
    return 0


if __name__ == "__main__":
    sys.exit(main())
