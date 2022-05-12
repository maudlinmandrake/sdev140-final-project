from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
import tarotcard


class DigitalOracle(EasyFrame):
    """Press a button and get your fortune told with a tarot deck"""

    def __init__(self):
        """Initialize window and set up components"""
        EasyFrame.__init__(self, title="The Digital Oracle", width=600, height=800)
        self.setResizable(False)

        self.imageLabel = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        self.textLabel = self.addLabel(text="Your fortune is one click away!", row=1, column=0, sticky="NSEW")

        self.card_title = self.addLabel(text="", row=1, column=0)
        self.card_key = self.addLabel(text="", row=1, column=0)
        # Command button for drawing card
        self.addButton(text="Pull a card", row=2, column=0, command=self.pull_card)

        # Load splash image & associate with image label
        self.splash = PhotoImage(file="tarot-splash.gif")
        self.imageLabel["image"] = self.splash

        # Style text
        font = Font(family="Times New Roman", size=20, slant="italic")
        self.textLabel["font"] = font
        self.textLabel["foreground"] = "black"

    def pull_card(self):
        """Pull a card from the deck, display card, and give user some related keywords"""
        my_deck = tarotcard.tarot_deck()  # create a tarot deck
        my_card = tarotcard.draw_card(my_deck) # generate a random card

        self.splash = PhotoImage(file=my_card['img'])
        self.imageLabel["image"] = self.splash

        self.card_title = self.addLabel(text=my_card['title'] + "\n" + my_card['keywords'], row=1, column=0, sticky="NSEW")
        # self.card_key= self.addLabel(text=my_card['keywords'], row=2, column=0, sticky="NSEW")

        font = Font(family="Times New Roman", size=20, slant="italic")
        self.card_title["font"] = font
        self.card_title["foreground"] = "black"


def main():
    # Pops up window for app
    DigitalOracle().mainloop()


if __name__ == "__main__":
    main()

# TODO: New reading button
# TODO: Exit app button
# TODO: BONUS - refactor buttons to choose between one card and three card readings
