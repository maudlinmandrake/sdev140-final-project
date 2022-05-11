"""
File: tarot-deck.py
Object for adding and managing cards in a tarot deck
"""


class TarotCard(object):
    """Creates a tarot card"""
    def __init__(self, card_img, card_name, card_keywords):
        self.card_img = card_img
        self.card_name = card_name
        self.card_keywords = card_keywords

    def get_img(self):
        """Return image file associated with card"""
        return self.card_img

    def get_name(self):
        """Get name of card"""
        return self.card_name

    def get_keywords(self):
        """Get keywords associated with card"""
        return self.card_keywords

    def set_img(self, card_img):
        """Set image of a tarot card"""
        self.card_img = card_img

    def set_name(self, card_name):
        """Set name of tarot card"""
        self.card_name = card_name

    def set_keywords(self, card_keywords):
        """Set keywords of tarot card"""
        self.card_keywords = card_keywords
        