from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
import tarotcard


class DigitalOracle(EasyFrame):
    """Press a button and get your fortune told with a tarot deck"""

    def __init__(self):
        """Initialize main window frame"""
        EasyFrame.__init__(self, title="The Digital Oracle", width=600, height=800)
        self.setResizable(False)

        # CREATE TOP PANEL
        topPanel = self.addPanel(row=0, column=0)  # initialize top panel
        # contents of top panel
        self.title = topPanel.addLabel(text="The Digital Oracle", row=0, column=0, columnspan=2, sticky="NSEW")
        self.imageLabel = topPanel.addLabel(text="", row=1, column=0, columnspan=2, sticky="NSEW")
        self.textLabel = topPanel.addLabel(text="Your future is one click away...", row=2, column=0, columnspan=2, sticky="NSEW")

        # load splash image & associate with image label
        self.splash = PhotoImage(file="tarot-splash.gif")
        self.imageLabel["image"] = self.splash

        # CREATE BOTTOM PANEL
        controlPanel = self.addPanel(row=1, column=0)  # initialize panel for app controls
        # Contents of bottom panel
        self.drawButton = controlPanel.addButton(text="Pull a card", row=0, column=0, command=self.pull_card)  # draw a card
        self.backButton = controlPanel.addButton(text="Go back", row=0, column=1, command=self.go_back, state="disabled")  # go back to splash page
        self.exitButton = controlPanel.addButton(text="Exit", row=0, column=2, command=self.exit)  # exit app

        # Style text
        font1 = Font(family="Times New Roman", size=20, slant="italic")
        font_title = Font(family="Times New Roman", size=30, slant="italic")
        self.textLabel["font"] = font1  # assign body font
        self.textLabel["foreground"] = "black"  # assign body text color

        self.title["font"] = font_title  # assign title font
        self.title["foreground"] = "black"  # assign title color

    def pull_card(self):
        """Pull a card from the deck, display card, and give user some related keywords"""
        my_deck = tarotcard.tarot_deck()  # create a tarot deck
        my_card = tarotcard.draw_card(my_deck)  # generate a random card

        # Display card
        self.splash = PhotoImage(file=my_card['img'])  # reassign splash image to image of pulled card
        self.imageLabel["image"] = self.splash

        # Display name of card and related keywords
        self.title["text"] = my_card['title']  # reassign app title to card title
        self.textLabel["text"] = my_card['keywords']  # reassign flavor text to card keywords

        # Return button to normal state
        self.backButton["state"] = "normal"  # restore button to normal, active state

    def go_back(self):
        """Restore screen to original state"""
        self.title["text"] = "The Digital Oracle" # restore app title
        self.splash = PhotoImage(file="tarot-splash.gif")  # restore splash image
        self.imageLabel["image"] = self.splash

        self.backButton["state"] = "disabled"  # disable button

        self.textLabel["text"] = "Your future is one click away..."  # restore original flavor text

    def exit(self):
        """Exit the application"""
        self.quit()


def main():
    """Run the app!"""
    DigitalOracle().mainloop()


if __name__ == "__main__":
    main()
