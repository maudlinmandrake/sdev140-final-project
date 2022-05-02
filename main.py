from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font


class DigitalOracle(EasyFrame):
    # Press a button and get your fortune told with a tarot deck
    def __init__(self):
        # initialize window and set up components
        EasyFrame.__init__(self, title = "The Digital Oracle", width=600, height=800)
        self.setResizable(False)
        imageLabel = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        textLabel = self.addLabel(text="Your fortune is one click away!", row=1, column=0, sticky="NSEW")
        # TODO: Insert button!
        # display splash image
        self.image = PhotoImage(file="tarot-card.gif")
        imageLabel["image"] = self.image
        # text label to display
        font = Font(family="Times New Roman", size=20, slant="italic")
        textLabel["font"] = font
        textLabel["foreground"] = "purple"
        #

def main():
    # Pops up window for app
    DigitalOracle().mainloop()

if __name__ == "__main__":
    main()