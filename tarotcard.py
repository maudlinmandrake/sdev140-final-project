"""
File: tarotcard.py
"""

import random


def tarot_deck():
    """Create a tarot deck saved to a list"""
    deck = [
        {
            "img" : "deck/00-TheFool.gif",
            "title" : "The Fool",
            "keywords" : "Innocence, New Beginnings, Foolishness"
         },

        {
            "img" : "deck/01-TheMagician.gif",
            "title" : "The Magician",
            "keywords" : "Willpower, Creation, Mastery"
        },

        {
            "img" : "deck/02-TheHighPriestess.gif",
            "title" : "The High Priestess",
            "keywords" : "Inner Voice, Intuition, Wisdom"
        },

        {
            "img" : "deck/03-TheEmpress.gif",
            "title" : "The Empress",
            "keywords" : "Nurturing, Luxury, Creativity"
        },

        {
            "img" : "deck/04-TheEmperor.gif",
            "title" : "The Emperor",
            "keywords": "Structure, Ambition, Authority, Rationality"
        },

        {
            "img" : "deck/05-TheHierophant.gif",
            "title" : "The Hierophant",
            "keywords" : "Tradition, Legacy, Society"
        },

        {
            "img" : "deck/06-TheLovers.gif",
            "title" : "The Lovers",
            "keywords" : "Choices, Union, Love"
        },

        {
            "img" : "deck/07-TheChariot.gif",
            "title" : "The Chariot",
            "keywords" : "Self Control, Discipline, Success"
        },

        {
            "img" : "deck/08-Strength.gif",
            "title" : "Strength",
            "keywords" : "Courage, Inner Strength, Conviction"
        },

        {
            "img" : "deck/09-TheHermit.gif",
            "title" : "The Hermit",
            "keywords" : "Contemplation, Solitude, Insight"
        },

        {
            "img" : "deck/10-WheelOfFortune.gif",
            "title" : "Wheel of Fortune",
            "keywords" : "Karma, Destiny, Cycles"
        },

        {
            "img" : "deck/11-Justice.gif",
            "title" : "Justice",
            "keywords" : "Truth, Fairness, Cause and Effect"},
        {
            "img" : "deck/12-TheHangedMan.gif",
            "title" : "The Hanged Man",
            "keywords" : "Sacrifice, Suspension, Release"
        },

        {
            "img" : "deck/13-Death.gif",
            "title" : "Death",
            "keywords" : "End of Cycle, New Beginnings, Metamorphosis"
        },

        {
            "img" : "deck/14-Temperance.gif",
            "title" : "Temperance",
            "keywords" : "Middle Path, Patience, Finding Meaning"
        },

        {
            "img" : "deck/15-TheDevil.gif",
            "title" : "The Devil",
            "keywords" : "Materialism, Playfulness, Addiction"
        },

        {
            "img" : "deck/16-TheTower.gif",
            "title" : "The Tower",
            "keywords" : "Upheaval, Disaster, Foundational Shift"
        },

        {
            "img" : "deck/17-TheStar.gif",
            "title" : "The Star",
            "keywords" : "Hope, Rejuvenation, Rebuilding"
        },

        {
            "img" : "deck/18-TheMoon.gif",
            "title" : "The Moon",
            "keywords" : "Unconscious, Illusions, Lack of Clarity"
        },

        {
            "img" : "deck/19-TheSun.gif",
            "title" : "The Sun",
            "keywords" : "Joy, Success, Celebration, Pleasure"
        },

        {
            "img" : "deck/20-Judgement.gif",
            "title" : "Judgement",
            "keywords" : "Reflection, Reckoning, Awakening"
        },

        {
            "img" : "deck/21-TheWorld.gif",
            "title" : "The World",
            "keywords" : "Fulfillment, Harmony, Completion"
        },

        {
            "img" : "deck/Wands01.gif",
            "title" : "Ace of Wands",
            "keywords" : "Creation, Willpower, Inspiration"
        },

        {
            "img" : "deck/Wands02.gif",
            "title" : "Two of Wands",
            "keywords" : "Planning, Making Decisions, Leaving Home"
        },

        {
            "img" : "deck/Wands03.gif",
            "title" : "Three of Wands",
            "keywords" : "Looking Ahead, Expansion, Rapid Growth"
        },

        {
            "img" : "deck/Wands04.gif",
            "title" : "Four of Wands",
            "keywords" : "Community, Home, Celebration"
        },

        {
            "img" : "deck/Wands05.gif",
            "title" : "Five of Wands",
            "keywords" : "Competition, Conflict, Reality"
        },

        {
            "img" : "deck/Wands06.gif",
            "title" : "Six of Wands",
            "keywords" : "Victory, Success, Public Reward"
        },

        {
            "img" : "deck/Wands07.gif",
            "title" : "Seven of Wands",
            "keywords" : "Perseverance, Mounting a Defense, Maintaining Control"
        },

        {
            "img" : "deck/Wands08.gif",
            "title" : "Eight of Wands",
            "keywords" : "Rapid Action, Movement, Quick Decisions"
        },

        {
            "img" : "deck/Wands09.gif",
            "title" : "Nine of Wands",
            "keywords" : "Resilience, Grit, Taking Last Stand"
        },

        {
            "img" : "deck/Wands10.gif",
            "title" : "Ten of Wands",
            "keywords" : "Accomplishment, Responsibility, Burden"
        },

        {
            "img" : "deck/Wands11.gif",
            "title" : "Page of Wands",
            "keywords" : "Exploration, Excitement, Freedom"
        },

        {
            "img" : "deck/Wands12.gif",
            "title" : "Knight of Wands",
            "keywords" : "Action, Adventure, Fearlessness"
        },

        {
            "img" : "deck/Wands13.gif",
            "title" : "Queen of Wands",
            "keywords" : "Courage, Determination, Passion, Joy"
        },

        {
            "img" : "deck/Wands14.gif",
            "title" : "King of Wands",
            "keywords" : "Big Picture, Leader, Overcoming Challenges"
        },
        {
            "img" : "deck/Cups01.gif",
            "title" : "Ace of Cups",
            "keywords" : "New Feelings, Spirituality, Intuition"
        },

        {
            "img" : "deck/Cups02.gif",
            "title" : "Two of Cups",
            "keywords" : "Unity, Partnership, Connection"
        },

        {
            "img" : "deck/Cups03.gif",
            "title" : "Three of Cups",
            "keywords" : "Friendship, Community, Happiness"
        },

        {
            "img" : "deck/Cups04.gif",
            "title" : "Four of Cups",
            "keywords" : "Apathy, Contemplation, Disconnection"
        },

        {
            "img" : "deck/Cups05.gif",
            "title" : "Five of Cups",
            "keywords" : "Loss, Grief, Disappointment"
        },

        {
            "img" : "deck/Cups06.gif",
            "title" : "Six of Cups",
            "keywords" : "Familiarity, Memories, Restoration, Nostalgia"
        },

        {
            "img" : "deck/Cups07.gif",
            "title" : "Seven of Cups",
            "keywords" : "Searching for Purpose, Choices, Daydreaming"
        },

        {
            "img" : "deck/Cups08.gif",
            "title" : "Eight of Cups",
            "keywords" : "Walking Away, Disillusionment, Leaving Something Behind"
        },

        {
            "img" : "deck/Cups09.gif",
            "title" : "Nine of Cups",
            "keywords" : "Satisfaction, Luxury, Emotional Stability"
        },

        {
            "img" : "deck/Cups10.gif",
            "title" : "Ten of Cups",
            "keywords" : "Inner Happiness, Fulfillment, Dreams Coming True"
        },

        {
            "img" : "deck/Cups11.gif",
            "title" : "Page of Cups",
            "keywords" : "Happy Surprise, Dreamer, Sensitivity"
        },

        {
            "img" : "deck/Cups12.gif",
            "title" : "Knight of Cups",
            "keywords" : "Idealist, Romantic, Following One's Heart"
        },

        {
            "img" : "deck/Cups13.gif",
            "title" : "Queen of Cups",
            "keywords" : "Compassion, Calm, Comfort"
        },

        {
            "img" : "deck/Cups14.gif",
            "title" : "King of Cups",
            "keywords" : "Emotional Control, Balance, Between Heart and Head"
        },

        {
            "img" : "deck/Swords01.gif",
            "title" : "Ace of Swords",
            "keywords" : "Breakthrough, Clarity, Sharp Mind"
        },

        {
            "img" : "deck/Swords02.gif",
            "title" : "Two of Swords",
            "keywords" : "Difficult Choices, Indecision, Stalemate"
        },

        {
            "img" : "deck/Swords03.gif",
            "title" : "Three of Swords",
            "keywords" : "Heartbreak, Suffering, Grief"
        },

        {
            "img" : "deck/Swords04.gif",
            "title" : "Four of Swords",
            "keywords" : "Rest, Restoration, Contemplation"
        },

        {
            "img" : "deck/Swords05.gif",
            "title" : "Five of Swords",
            "keywords" : "Unbridled Ambition, Win At All Costs, Sneakiness"
        },

        {
            "img" : "deck/Swords06.gif",
            "title" : "Six of Swords",
            "keywords" : "Transition, Leaving Behind, Moving On"
        },

        {
            "img" : "deck/Swords07.gif",
            "title" : "Seven of Swords",
            "keywords" : "Deception, Trickery, Tactics and Strategy"
        },

        {
            "img" : "deck/Swords08.gif",
            "title" : "Eight of Swords",
            "keywords" : "Imprisonment, Entrapment, Self-Victimization"
        },

        {
            "img" : "deck/Swords09.gif",
            "title" : "Nine of Swords",
            "keywords" : "Anxiety, Hopelessness, Trauma"
        },

        {
            "img" : "deck/Swords10.gif",
            "title" : "Ten of Swords",
            "keywords" : "Failure, Collapse, Defeat, Backstabbing"
        },

        {
            "img" : "deck/Swords11.gif",
            "title" : "Page of Swords",
            "keywords" : "Curiosity, Restlessness, Mental Energy"
        },

        {
            "img" : "deck/Swords12.gif",
            "title" : "Knight of Swords",
            "keywords" : "Action, Impulsiveness, Defending Beliefs"
        },

        {
            "img" : "deck/Swords13.gif",
            "title" : "Queen of Swords",
            "keywords" : "Complexity, Perceptive, Clear Mindedness"
        },

        {
            "img" : "deck/Swords14.gif",
            "title" : "King of Swords",
            "keywords" : "Head Over Heart, Truth, Discipline"
        },

        {
            "img" : "deck/Coins01.gif",
            "title" : "Ace of Coins",
            "keywords" : "Opportunity, Prosperity, New Venture"
        },

        {
            "img" : "deck/Coins02.gif",
            "title" : "Two of Coins",
            "keywords" : "Balancing Decisions, Priorities, Adaptation"
        },

        {
            "img" : "deck/Coins03.gif",
            "title" : "Three of Coins",
            "keywords" : "Teamwork, Collaboration, Building Together"
        },

        {
            "img" : "deck/Coins04.gif",
            "title" : "Four of Coins",
            "keywords" : "Conservation, Security, Frugality"
        },

        {
            "img" : "deck/Coins05.gif",
            "title" : "Five of Coins",
            "keywords" : "Need, Poverty, Insecurity"
        },

        {
            "img" : "deck/Coins06.gif",
            "title" : "Six of Coins",
            "keywords" : "Charity, Generosity, Sharing"
        },

        {
            "img" : "deck/Coins07.gif",
            "title" : "Seven of Coins",
            "keywords" : "Hard Work, Perseverance, Diligence"
        },

        {
            "img" : "deck/Coins08.gif",
            "title" : "Eight of Coins",
            "keywords" : "Diligence, Passion, High Standards"
        },

        {
            "img" : "deck/Coins09.gif",
            "title" : "Nine of Coins",
            "keywords" : "Fruits of Labor, Reckless Spending, Rewards"
        },

        {
            "img" : "deck/Coins10.gif",
            "title" : "Ten of Coins",
            "keywords" : "Legacy, Inheritance, Culmination"
        },

        {
            "img" : "deck/Coins11.gif",
            "title" : "Page of Coins",
            "keywords" : "Ambition, Desire, Diligence, Craving New Venture"
        },

        {
            "img" : "deck/Coins12.gif",
            "title" : "Knight of Coins",
            "keywords" : "Efficiency, Hard Work, Responsibility"
        },

        {
            "img" : "deck/Coins13.gif",
            "title" : "Queen of Coins",
            "keywords" : "Practicality, Creature Comforts, Security"
        },

        {
            "img" : "deck/Coins14.gif",
            "title" : "King of Coins",
            "keywords" : "Abundance, Prosperity, Provider"
        }
    ]

    return deck


def draw_card(deck):
    """Draw a random card from our tarot deck"""
    num = random.randint(0, 77)
    card = deck[num]
    return card

my_deck = tarot_deck()
my_card = draw_card(my_deck)

print(my_card)

