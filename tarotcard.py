"""
File: tarotcard.py
Create a tarot deck and pull cards from it at random
"""

import random


def tarot_deck():
    """Create a tarot deck"""
    deck = [
        {
            "img": "deck/00-TheFool.gif",
            "title": "The Fool",
            "keywords": "Innocence, New Beginnings, Foolishness",
            "alt": "A man appears to be dancing precariously on a cliffside",
        },

        {
            "img": "deck/01-TheMagician.gif",
            "title": "The Magician",
            "keywords": "Willpower, Creation, Mastery",
            "alt": "A man in red robes stands before a table full of ceremonial objects",
        },

        {
            "img": "deck/02-TheHighPriestess.gif",
            "title": "The High Priestess",
            "keywords": "Inner Voice, Intuition, Wisdom",
            "alt": "A woman in blue robes sits before two columns. There is a scroll in her lap and a crescent moon at her feet",
        },

        {
            "img": "deck/03-TheEmpress.gif",
            "title": "The Empress",
            "keywords": "Nurturing, Luxury, Creativity",
            "alt": "A woman in flowery robes lays on a chaise lounge in a lush forest, with a river running behind her",
        },

        {
            "img": "deck/04-TheEmperor.gif",
            "title": "The Emperor",
            "keywords": "Structure, Ambition, Authority, Rationality",
            "alt": "A stern, crowned man sits atop a stone throne",
        },

        {
            "img": "deck/05-TheHierophant.gif",
            "title": "The Hierophant",
            "keywords": "Tradition, Legacy, Society",
            "alt": "A priest sits between two columns. There are two monks at his feet, and he holds a scroll",
        },

        {
            "img": "deck/06-TheLovers.gif",
            "title": "The Lovers",
            "keywords": "Choices, Union, Love",
            "alt": "A man and woman stand before an angel",
        },

        {
            "img": "deck/07-TheChariot.gif",
            "title": "The Chariot",
            "keywords": "Self Control, Discipline, Success",
            "alt": "A warrior sits in a chariot pulled by two sphinxes; one is black, the other white",
        },

        {
            "img": "deck/08-Strength.gif",
            "title": "Strength",
            "keywords": "Courage, Inner Strength, Conviction",
            "alt": "A woman gently cradles a lion's head",
        },

        {
            "img": "deck/09-TheHermit.gif",
            "title": "The Hermit",
            "keywords": "Contemplation, Solitude, Insight",
            "alt": "An elderly man stands on a mountain top. He is robed in grey and holds up a lit lantern",
        },

        {
            "img": "deck/10-WheelOfFortune.gif",
            "title": "Wheel of Fortune",
            "keywords": "Karma, Destiny, Cycles",
            "alt": "A wheel floating in the sky, with various beasts surrounding it",
        },

        {
            "img": "deck/11-Justice.gif",
            "title": "Justice",
            "keywords": "Truth, Fairness, Cause and Effect",
            "alt": "A robed woman sits between two columns. In one hand she holds a sword pointing up, and in the other she holds a set of scales",
        },

        {
            "img": "deck/12-TheHangedMan.gif",
            "title": "The Hanged Man",
            "keywords": "Sacrifice, Suspension, Release",
            "alt": "A man hangs upside down from a tree branch. He seems serene, despite his situation"
        },

        {
            "img": "deck/13-Death.gif",
            "title": "Death",
            "keywords": "End of Cycle, New Beginnings, Metamorphosis",
            "alt": "A skeletal knight passes by villagers on his white horse. The sun is rising in the background"
        },

        {
            "img": "deck/14-Temperance.gif",
            "title": "Temperance",
            "keywords": "Middle Path, Patience, Finding Meaning",
            "alt": "An angel is pour liquid between two chalices. One foot is dipped into a pond, the other remains on dry land"
        },

        {
            "img": "deck/15-TheDevil.gif",
            "title": "The Devil",
            "keywords": "Materialism, Playfulness, Addiction",
            "alt": "A winged demon sits on a pedestal. A woman and a man are both chained to it."
        },

        {
            "img": "deck/16-TheTower.gif",
            "title": "The Tower",
            "keywords": "Upheaval, Disaster, Foundational Shift",
            "alt": "A tower is caught ablaze by lightning. Two people are falling from it"
        },

        {
            "img": "deck/17-TheStar.gif",
            "title": "The Star",
            "keywords": "Hope, Rejuvenation, Rebuilding",
            "alt": "A woman bends over a lake, with two jugs in her hands. One pours water into the lake, the other onto land. A large star has risen in the night sky behind her"
        },

        {
            "img": "deck/18-TheMoon.gif",
            "title": "The Moon",
            "keywords": "Unconscious, Illusions, Lack of Clarity",
            "alt": "The moon rises between two towers; a dog and a wolf can be seen howling at it"
        },

        {
            "img": "deck/19-TheSun.gif",
            "title": "The Sun",
            "keywords": "Joy, Success, Celebration, Pleasure",
            "alt": "The sun rises above a sunflower garden, and we can see a child riding out of the garden on a white horse"
        },

        {
            "img": "deck/20-Judgement.gif",
            "title": "Judgement",
            "keywords": "Reflection, Reckoning, Awakening",
            "alt": "An angel blows a trumpet in the sky; we see a man, a woman, and a child rising out of their graves"
        },

        {
            "img": "deck/21-TheWorld.gif",
            "title": "The World",
            "keywords": "Fulfillment, Harmony, Completion",
            "alt": "A woman floats in the sky surrounded by a laurel wreath"
        },

        {
            "img": "deck/Wands01.gif",
            "title": "Ace of Wands",
            "keywords": "Creation, Willpower, Inspiration",
            "alt": "A mysterious hand appears floating in the sky, and it holds a large budding branch in its hand"
        },

        {
            "img": "deck/Wands02.gif",
            "title": "Two of Wands",
            "keywords": "Planning, Making Decisions, Leaving Home",
            "alt": "A man gazes out over a city. He holds a small globe in his hand",
        },

        {
            "img": "deck/Wands03.gif",
            "title": "Three of Wands",
            "keywords": "Looking Ahead, Expansion, Rapid Growth",
            "alt": "A man gazes out at several ships in the sea"
        },

        {
            "img": "deck/Wands04.gif",
            "title": "Four of Wands",
            "keywords": "Community, Home, Celebration",
            "alt": "Four branches support a wreath of flowers; in the foreground we see a couple celebrating"
        },

        {
            "img": "deck/Wands05.gif",
            "title": "Five of Wands",
            "keywords": "Competition, Conflict, Reality",
            "alt": "Five men in a skirmish, all holding branches in their hands"
        },

        {
            "img": "deck/Wands06.gif",
            "title": "Six of Wands",
            "keywords": "Victory, Success, Public Reward",
            "alt": "A man with a laurel crown rides through a crowd on a white horse"
        },

        {
            "img": "deck/Wands07.gif",
            "title": "Seven of Wands",
            "keywords": "Perseverance, Mounting a Defense, Maintaining Control",
            "alt": "A man stands on a hillside and appears to be defending himself against unseen assailants"
        },

        {
            "img": "deck/Wands08.gif",
            "title": "Eight of Wands",
            "keywords": "Rapid Action, Movement, Quick Decisions",
            "alt": "Eight branches are seen entering the frame from the left; there is a green hillside in the background"
        },

        {
            "img": "deck/Wands09.gif",
            "title": "Nine of Wands",
            "keywords": "Resilience, Grit, Taking Last Stand",
            "alt": "A wounded man stands before a fence made of branches; he holds another in his hand. He looks tired"
        },

        {
            "img": "deck/Wands10.gif",
            "title": "Ten of Wands",
            "keywords": "Accomplishment, Responsibility, Burden",
            "alt": "A man is carrying a large bundle of ten large branches, and appears to be slowly making his way to a house in the distance"
        },

        {
            "img": "deck/Wands11.gif",
            "title": "Page of Wands",
            "keywords": "Exploration, Excitement, Freedom",
            "alt": "A young boy in a yellow robe gazes up at a flowering branch in his hand"
        },

        {
            "img": "deck/Wands12.gif",
            "title": "Knight of Wands",
            "keywords": "Action, Adventure, Fearlessness",
            "alt": "A knight in yellow armaments rides atop a brown horse that is leaping into the air"
        },

        {
            "img": "deck/Wands13.gif",
            "title": "Queen of Wands",
            "keywords": "Courage, Determination, Passion, Joy",
            "alt": "A crowned woman in yellow robes sits atop a throne in the desert. There is a black cat sitting at her foot"
        },

        {
            "img": "deck/Wands14.gif",
            "title": "King of Wands",
            "keywords": "Big Picture, Leader, Overcoming Challenges",
            "alt": "A red-haired king sits on a throne. He wears yellow robes, and his throne is decorated with lizards"
        },
        {
            "img": "deck/Cups01.gif",
            "title": "Ace of Cups",
            "keywords": "New Feelings, Spirituality, Intuition",
            "alt": "A floating hand offers an a chalice overflowing with water"
        },

        {
            "img": "deck/Cups02.gif",
            "title": "Two of Cups",
            "keywords": "Unity, Partnership, Connection",
            "alt": "A man and woman face each other, each holding a chalice in their hands"
        },

        {
            "img": "deck/Cups03.gif",
            "title": "Three of Cups",
            "keywords": "Friendship, Community, Happiness",
            "alt": "Three women appear to be dancing together. They each hold aloft a chalice."
        },

        {
            "img": "deck/Cups04.gif",
            "title": "Four of Cups",
            "keywords": "Apathy, Contemplation, Disconnection",
            "alt": "A man sits underneath a tree. There are three cups before him, and a mysterious floating hand offers him a fourth one"
        },

        {
            "img": "deck/Cups05.gif",
            "title": "Five of Cups",
            "keywords": "Loss, Grief, Disappointment",
            "alt": "A person in black robes appears to be bent over three spilled cups. Two more stand upright behind them"
        },

        {
            "img": "deck/Cups06.gif",
            "title": "Six of Cups",
            "keywords": "Familiarity, Memories, Restoration, Nostalgia",
            "alt": "Two small children, a boy and a girl, appear in a garden"
        },

        {
            "img": "deck/Cups07.gif",
            "title": "Seven of Cups",
            "keywords": "Searching for Purpose, Choices, Daydreaming",
            "alt": "A person gazes up at seven cups floating in the sky, and each cup appears to be offering them a different treasure"
        },

        {
            "img": "deck/Cups08.gif",
            "title": "Eight of Cups",
            "keywords": "Walking Away, Disillusionment, Leaving Something Behind",
            "alt": "A traveler in a red coat is walking into the distance. There are eight cups stacked up behind them"
        },

        {
            "img": "deck/Cups09.gif",
            "title": "Nine of Cups",
            "keywords": "Satisfaction, Luxury, Emotional Stability",
            "alt": "A merchant sits in front of nine cups, and he looks very pleased with himself"
        },

        {
            "img": "deck/Cups10.gif",
            "title": "Ten of Cups",
            "keywords": "Inner Happiness, Fulfillment, Dreams Coming True",
            "alt": "A family stands arm in arm and gazes up at a rainbow in the sky; there are ten cups floating in front of the rainbow"
        },

        {
            "img": "deck/Cups11.gif",
            "title": "Page of Cups",
            "keywords": "Happy Surprise, Dreamer, Sensitivity",
            "alt": "A young man gazes at a little fish jumping out of the chalice in his hands"
        },

        {
            "img": "deck/Cups12.gif",
            "title": "Knight of Cups",
            "keywords": "Idealist, Romantic, Following One's Heart",
            "alt": "A knight in silver armor sits atop a grey horse; he gazes solemnly at the chalice in his hands"
        },

        {
            "img": "deck/Cups13.gif",
            "title": "Queen of Cups",
            "keywords": "Compassion, Calm, Comfort",
            "alt": "A queen sits on her throne at the side of a lake. She holds a very ornate chalice, and she gazes into it"
        },

        {
            "img": "deck/Cups14.gif",
            "title": "King of Cups",
            "keywords": "Emotional Control, Balance, Between Heart and Head",
            "alt": "A king sits on a throne floating above an ocean. He is wearing blue robes."
        },

        {
            "img": "deck/Swords01.gif",
            "title": "Ace of Swords",
            "keywords": "Breakthrough, Clarity, Sharp Mind",
            "alt": "A floating hands holds aloft a large sword. A crown encircles the blade"
        },

        {
            "img": "deck/Swords02.gif",
            "title": "Two of Swords",
            "keywords": "Difficult Choices, Indecision, Stalemate",
            "alt": "A woman sits blindfolded, and balances two large swords in her hands"
        },

        {
            "img": "deck/Swords03.gif",
            "title": "Three of Swords",
            "keywords": "Heartbreak, Suffering, Grief",
            "alt": "A heart pierced by three swords; there is a rainstorm depicted behind it"
        },

        {
            "img": "deck/Swords04.gif",
            "title": "Four of Swords",
            "keywords": "Rest, Restoration, Contemplation",
            "alt": "A knight rests atop a table; there are three swords hanging on the wall behind him, and another sword is carved into the table"
        },

        {
            "img": "deck/Swords05.gif",
            "title": "Five of Swords",
            "keywords": "Unbridled Ambition, Win At All Costs, Sneakiness",
            "alt": "A smug man holds three swords and watches several other men walk away from him. He appears to have beaten these men in a fight"
        },

        {
            "img": "deck/Swords06.gif",
            "title": "Six of Swords",
            "keywords": "Transition, Leaving Behind, Moving On",
            "alt": "A man rows a boat with a woman and child sitting in it. There are six swords in the boat with them"
        },

        {
            "img": "deck/Swords07.gif",
            "title": "Seven of Swords",
            "keywords": "Deception, Trickery, Tactics and Strategy",
            "alt": "A man carries an armload of swords and seems to be sneaking out of a camp"
        },

        {
            "img": "deck/Swords08.gif",
            "title": "Eight of Swords",
            "keywords": "Imprisonment, Entrapment, Self-Victimization",
            "alt": "A bound and blindfolded woman is surrounded by a wall of swords"
        },

        {
            "img": "deck/Swords09.gif",
            "title": "Nine of Swords",
            "keywords": "Anxiety, Hopelessness, Trauma",
            "alt": "A person sitting up in their bed. They cover their face with their hands. There are nine swords hanging on a black wall behind them"
        },

        {
            "img": "deck/Swords10.gif",
            "title": "Ten of Swords",
            "keywords": "Failure, Collapse, Defeat, Backstabbing",
            "alt": "A person appears to be lying dead on the ground; there are ten swords sticking out of their back, but there is no blood"
        },

        {
            "img": "deck/Swords11.gif",
            "title": "Page of Swords",
            "keywords": "Curiosity, Restlessness, Mental Energy",
            "alt": "A young man holds aloft a sword and gazes into the distance"
        },

        {
            "img": "deck/Swords12.gif",
            "title": "Knight of Swords",
            "keywords": "Action, Impulsiveness, Defending Beliefs",
            "alt": "A knight holds aloft a sword and appears to be riding into battle"
        },

        {
            "img": "deck/Swords13.gif",
            "title": "Queen of Swords",
            "keywords": "Complexity, Perceptive, Clear Mindedness",
            "alt": "A queen sits at her throne. One hand holds a sword, the other appears to be beckoning."
        },

        {
            "img": "deck/Swords14.gif",
            "title": "King of Swords",
            "keywords": "Head Over Heart, Truth, Discipline",
            "alt": "A king sitting at his throne. He wears blue robes and holds a sword in his left hand"
        },

        {
            "img": "deck/Pentacles01.gif",
            "title": "Ace of Pentacles",
            "keywords": "Opportunity, Prosperity, New Venture",
            "alt": "A floating hands holds a large gold coin in its hand. There is a walled garden in the background"
        },

        {
            "img": "deck/Pentacles02.gif",
            "title": "Two of Pentacles",
            "keywords": "Balancing Decisions, Priorities, Adaptation",
            "alt": "A man in an orange and red suit juggles two coins."
        },

        {
            "img": "deck/Pentacles03.gif",
            "title": "Three of Pentacles",
            "keywords": "Teamwork, Collaboration, Building Together",
            "alt": "A worker of some sort stares at a column with three coins carved into it. His patrons stand next to him."
        },

        {
            "img": "deck/Pentacles04.gif",
            "title": "Four of Pentacles",
            "keywords": "Conservation, Security, Frugality",
            "alt": "A man sits with two coins under his feet, another in his arms, and a fourth balancing on top of his head"
        },

        {
            "img": "deck/Pentacles05.gif",
            "title": "Five of Pentacles",
            "keywords": "Need, Poverty, Insecurity",
            "alt": "An elderly woman and a man on crutches walk past a church window on a snowy night"
        },

        {
            "img": "deck/Pentacles06.gif",
            "title": "Six of Pentacles",
            "keywords": "Charity, Generosity, Sharing",
            "alt": "A merchant in red robes holds a scale in his hands. There are two beggars at his feet, and he gives a coin to one of them"
        },

        {
            "img": "deck/Pentacles07.gif",
            "title": "Seven of Pentacles",
            "keywords": "Hard Work, Perseverance, Diligence",
            "alt": "A farmer gazes at a full, green shrub. There are coins hanging off of it."
        },

        {
            "img": "deck/Pentacles08.gif",
            "title": "Eight of Pentacles",
            "keywords": "Diligence, Passion, High Standards",
            "alt": "A craftsman is sitting on his work bench chiseling away at a large gold coin"
        },

        {
            "img": "deck/Pentacles09.gif",
            "title": "Nine of Pentacles",
            "keywords": "Fruits of Labor, Reckless Spending, Rewards",
            "alt": "A richly robed woman stands in a lush garden. There is a a bird perched on her hand"
        },

        {
            "img": "deck/Pentacles10.gif",
            "title": "Ten of Pentacles",
            "keywords": "Legacy, Inheritance, Culmination",
            "alt": "An elderly man greets two dogs outside of a stone arch. There is a family in the background, and the man appears to be walking towards them."
        },

        {
            "img": "deck/Pentacles11.gif",
            "title": "Page of Pentacles",
            "keywords": "Ambition, Desire, Diligence, Craving New Venture",
            "alt": "A young man in a green tunic holds aloft a coin and gazes at it. He stands in a verdant field full of blooms"
        },

        {
            "img": "deck/Pentacles12.gif",
            "title": "Knight of Pentacles",
            "keywords": "Efficiency, Hard Work, Responsibility",
            "alt": "A solemn knight on a black horse. He holds a gold coin in his hand"
        },

        {
            "img": "deck/Pentacles13.gif",
            "title": "Queen of Pentacles",
            "keywords": "Practicality, Creature Comforts, Security",
            "alt": "A queen in red robes sits on an ornate throne located in a garden. She is surrounded by roses, and there is a rabbit passing by"
        },

        {
            "img": "deck/Pentacles14.gif",
            "title": "King of Pentacles",
            "keywords": "Abundance, Prosperity, Provider",
            "alt": "A king sits on top of a black throne. He is surrounded by grape vines full of fruit, and there is a city in the distance."
        }
    ]

    return deck


def draw_card(deck):
    """Draw a random card from our tarot deck"""
    num = random.randint(0, 77)  # choose a random number between 0-77
    card = deck[num]  # assign number to a card in list
    return card





