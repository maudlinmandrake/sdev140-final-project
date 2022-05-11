"""
File: tarotcard.py
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


theFool = TarotCard("deck/00-TheFool.gif", "The Fool", "Innocence, New Beginnings, Foolishness")
theMagician = TarotCard("deck/01-TheMagician.gif", "The Magician", "Willpower, Creation, Mastery")
thePriestess = TarotCard("deck/02-TheHighPriestess.gif", "The High Priestess", "Inner Voice, Intuition, Wisdom")
theEmpress = TarotCard("deck/03-TheEmpress.gif", "The Empress", "Nurturing, Luxury, Creativity")
theEmperor = TarotCard("deck/04-TheEmperor.gif", "The Emperor", "Structure, Ambition, Authority, Rationality")
theHierophant = TarotCard("deck/05-TheHierophant.gif", "The Hierophant", "Tradition, Legacy, Society")
theLovers = TarotCard("deck/06-TheLovers.gif", "The Lovers", "Choices, Union, Love")
theChariot = TarotCard("deck/07-TheChariot.gif", "The Chariot", "Self Control, Discipline, Success")
strength = TarotCard("deck/08-Strength.gif", "Strength", "Courage, Inner Strength, Conviction")
theHermit = TarotCard("deck/09-TheHermit.gif", "The Hermit", "Contemplation, Solitude, Insight")
theWheel = TarotCard("deck/10-WheelOfFortune.gif", "Wheel of Fortune", "Karma, Destiny, Cycles")
justice = TarotCard("deck/11-Justice.gif", "Justice", "Truth, Fairness, Cause and Effect")
theHangedMan = TarotCard("deck/12-TheHangedMan.gif", "The Hanged Man", "Sacrifice, Suspension, Release")
death = TarotCard("deck/13-Death.gif", "Death", "End of Cycle, New Beginnings, Metamorphosis")
temperance = TarotCard("deck/14-Temperance.gif", "Temperance", "Middle Path, Patience, Finding Meaning")
theDevil = TarotCard("deck/15-TheDevil.gif", "The Devil", "Materialism, Playfulness, Addiction")
theTower = TarotCard("deck/16-TheTower.gif", "The Tower", "Upheaval, Disaster, Foundational Shift")
theStar = TarotCard("deck/17-TheStar.gif", "The Star", "Hope, Rejuvenation, Rebuilding")
theMoon = TarotCard("deck/18-TheMoon.gif", "The Moon", "Unconscious, Illusions, Lack of Clarity")
theSun = TarotCard("deck/19-TheSun.gif", "The Sun", "Joy, Success, Celebration, Pleasure")
judgement = TarotCard("deck/20-Judgement.gif", "Judgement", "Reflection, Reckoning, Awakening")
theWorld = TarotCard("deck/21-TheWorld.gif", "The World", "Fulfillment, Harmony, Completion")
aceOfWands = TarotCard("deck/Wands01.gif", "Ace of Wands", "Creation, Willpower, Inspiration")
twoOfWands = TarotCard("deck/Wands02.gif", "Two of Wands", "Planning, Making Decisions, Leaving Home")
threeOfWands = TarotCard("deck/Wands03.gif", "Three of Wands", "Looking Ahead, Expansion, Rapid Growth")
fourOfWands = TarotCard("deck/Wands04.gif", "Four of Wands", "Community, Home, Celebration")
fiveOfWands = TarotCard("deck/Wands05.gif", "Five of Wands", "Competition, Conflict, Reality")
sixOfWands = TarotCard("deck/Wands06.gif", "Six of Wands", "Victory, Success, Public Reward")
sevenOfWands = TarotCard("deck/Wands07.gif", "Seven of Wands", "Perseverance, Mounting a Defense, Maintaining Control")
eightOfWands = TarotCard("deck/Wands08.gif", "Eight of Wands", "Rapid Action, Movement, Quick Decisions")
nineOfWands = TarotCard("deck/Wands09.gif", "Nine of Wands", "Resilience, Grit, Taking Last Stand")
tenOfWands = TarotCard("deck/Wands10.gif", "Ten of Wands", "Accomplishment, Responsibility, Burden")
pageOfWands = TarotCard("deck/Wands11.gif", "Page of Wands", "Exploration, Excitement, Freedom")
knightOfWands = TarotCard("deck/Wands12.gif", "Knight of Wands", "Action, Adventure, Fearlessness")
queenOfWands = TarotCard("deck/Wands13.gif", "Queen of Wands", "Courage, Determination, Passion, Joy")
kingOfWands = TarotCard("deck/Wands14.gif", "King of Wands", "Big Picture, Leader, Overcoming Challenges")
aceOfCups = TarotCard("deck/Cups01.gif", "Ace of Cups", "New Feelings, Spirituality, Intuition")
twoOfCups = TarotCard("deck/Cups02.gif", "Two of Cups", "Unity, Partnership, Connection")
threeOfCups = TarotCard("deck/Cups03.gif", "Three of Cups", "Friendship, Community, Happiness")
fourOfCups = TarotCard("deck/Cups04.gif", "Four of Cups", "Apathy, Contemplation, Disconnection")
fiveOfCups = TarotCard("deck/Cups05.gif", "Five of Cups", "Loss, Grief, Disappointment")
sixOfCups = TarotCard("deck/Cups06.gif", "Six of Cups", "Familiarity, Memories, Restoration, Nostalgia")
sevenOfCups = TarotCard("deck/Cups07.gif", "Seven of Cups", "Searching for Purpose, Choices, Daydreaming")
eightOfCups = TarotCard("deck/Cups08.gif", "Eight of Cups", "Walking Away, Disillusionment, Leaving Something Behind")
nineOfCups = TarotCard("deck/Cups09.gif", "Nine of Cups", "Satisfaction, Luxury, Emotional Stability")
tenOfCups = TarotCard("deck/Cups10.gif", "Ten of Cups", "Inner Happiness, Fulfillment, Dreams Coming True")
pageOfCups = TarotCard("deck/Cups11.gif", "Page of Cups", "Happy Surprise, Dreamer, Sensitivity")
knightOfCups = TarotCard("deck/Cups12.gif", "Knight of Cups", "Idealist, Romantic, Following One's Heart")
queenOfCups = TarotCard("deck/Cups13.gif", "Queen of Cups", "Compassion, Calm, Comfort")
kingOfCups = TarotCard("deck/Cups14.gif", "King of Cups", "Emotional Control, Balance, Between Heart and Head")
aceOfSwords = TarotCard("deck/Swords01.gif", "Ace of Swords", "Breakthrough, Clarity, Sharp Mind")
twoOfSwords = TarotCard("deck/Swords02.gif", "Two of Swords", "Difficult Choices, Indecision, Stalemate")
threeOfSwords = TarotCard("deck/Swords03.gif", "Three of Swords", "Heartbreak, Suffering, Grief")
fourOfSwords = TarotCard("deck/Swords04.gif", "Four of Swords", "Rest, Restoration, Contemplation")
fiveOfSwords = TarotCard("deck/Swords05.gif", "Five of Swords", "Unbridled Ambition, Win At All Costs, Sneakiness")
sixOfSwords = TarotCard("deck/Swords06.gif", "Six of Swords", "Transition, Leaving Behind, Moving On")
sevenOfSwords = TarotCard("deck/Swords07.gif", "Seven of Swords", "Deception, Trickery, Tactics and Strategy")
eightOfSwords = TarotCard("deck/Swords08.gif", "Eight of Swords", "Imprisonment, Entrapment, Self-Victimization")
nineOfSwords = TarotCard("deck/Swords09.gif", "Nine of Swords", "Anxiety, Hopelessness, Trauma")
tenOfSwords = TarotCard("deck/Swords10.gif", "Ten of Swords", "Failure, Collapse, Defeat, Backstabbing")
pageOfSwords = TarotCard("deck/Swords11.gif", "Page of Swords", "Curiosity, Restlessness, Mental Energy")
knightOfSwords = TarotCard("deck/Swords12.gif", "Knight of Swords", "Action, Impulsiveness, Defending Beliefs")
queenOfSwords = TarotCard("deck/Swords13.gif", "Queen of Swords", "Complexity, Perceptive, Clear Mindedness")
kingOfSwords = TarotCard("deck/Swords14.gif", "King of Swords", "Head Over Heart, Truth, Discipline")
aceOfCoins = TarotCard("deck/Coins01.gif", "Ace of Coins", "Opportunity, Prosperity, New Venture")
twoOfCoins = TarotCard("deck/Coins02.gif", "Two of Coins", "Balancing Decisions, Priorities, Adaptation")
threeOfCoins = TarotCard("deck/Coins03.gif", "Three of Coins", "Teamwork, Collaboration, Building Together")
fourOfCoins = TarotCard("deck/Coins04.gif", "Four of Coins", "Conservation, Security, Frugality")
fiveOfCoins = TarotCard("deck/Coins05.gif", "Five of Coins", "Need, Poverty, Insecurity")
sixOfCoins = TarotCard("deck/Coins06.gif", "Six of Coins", "Charity, Generosity, Sharing")
sevenOfCoins = TarotCard("deck/Coins07.gif", "Seven of Coins", "Hard Work, Perseverance, Diligence")
eightOfCoins = TarotCard("deck/Coins08.gif", "Eight of Coins", "Diligence, Passion, High Standards")
nineOfCoins = TarotCard("deck/Coins09.gif", "Nine of Coins", "Fruits of Labor, Reckless Spending, Rewards")
tenOfCoins = TarotCard("deck/Coins10.gif", "Ten of Coins", "Legacy, Inheritance, Culmination")
pageOfCoins = TarotCard("deck/Coins11.gif", "Page of Coins", "Ambition, Desire, Diligence, Craving New Venture")
knightOfCoins = TarotCard("deck/Coins12.gif", "Knight of Coins", "Efficiency, Hard Work, Responsibility")
queenOfCoins = TarotCard("deck/Coins13.gif", "Queen of Coins", "Practicality, Creature Comforts, Security")
kingOfCoins = TarotCard("deck/Coins14.gif", "King of Coins", "Abundance, Prosperity, Provider")
