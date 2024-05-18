
# to provide random slecgtions from a list
import random

# Main program to call the functions and print c
def main():

    # Call the first function
    word = get_determiner('single')
    adjective = get_adjective()
    noun = get_noun("single")
    adverb = get_adverb()
    verb = get_verb("past", "single")
    preposition = get_preposition()
    phrase = get_prepositional_phrase("quantity")
    phrase1 = get_prepositional_phrase("quantity")
    sentence = make_sentence("single", "past")

    word = get_determiner('single')
    adjective = get_adjective()
    noun = get_noun("single")
    adverb = get_adverb()
    verb = get_verb("present", "single")
    preposition = get_preposition()
    phrase = get_prepositional_phrase("quantity")
    phrase1 = get_prepositional_phrase("quantity")
    sentence = make_sentence("single", "present")

    word = get_determiner('single')
    adjective = get_adjective()
    noun = get_noun("single")
    adverb = get_adverb()
    verb = get_verb("future", "single")
    preposition = get_preposition()
    phrase = get_prepositional_phrase("quantity")
    phrase1 = get_prepositional_phrase("quantity")
    sentence = make_sentence("single", "present")

    word = get_determiner('plural')
    adjective = get_adjective()
    noun = get_noun("plural")
    adverb = get_adverb()
    verb = get_verb("past", "plural")
    preposition = get_preposition()
    phrase = get_prepositional_phrase("quantity")
    phrase1 = get_prepositional_phrase("quantity")
    sentence = make_sentence("single", "present")

    word = get_determiner('plural')
    adjective = get_adjective()
    noun = get_noun("plural")
    adverb = get_adverb()
    verb = get_verb("present", "plural")
    preposition = get_preposition()
    phrase = get_prepositional_phrase("quantity")
    phrase1 = get_prepositional_phrase("quantity")
    sentence = make_sentence("single", "present")

    word = get_determiner('plural')
    adjective = get_adjective()
    noun = get_noun("plural")
    adverb = get_adverb()
    verb = get_verb("future", "plural")
    preposition = get_preposition()
    phrase = get_prepositional_phrase("quantity")
    phrase1 = get_prepositional_phrase("quantity")
    sentence = make_sentence("single", "present")
    

    # Put it all together and print the sentence
    #make_sentence(quantity, tense)
    #make_sentence("single", "past")
    #make_sentence("single", "present")
    #make_sentence("single", "future")
    #make_sentence("plural", "past")
    #make_sentence("plural", "present")
    #make_sentence("plural", "future")


# Provides a random determing word.
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)

    return word

# Geta a noun from the list.
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if (quantity == 1):
        words =[ "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(words)
    return noun

# Get a verb from the list
def get_verb(tense, quantity):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.?
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if (tense == 'past'):
        words =[ "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif (tense == 'present' and quantity == 1):
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif (tense == 'present' and quantity != 1):
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif (tense == 'future'):
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    verb = random.choice(words)
    return verb


# Get a preposition from the list
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prep = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    preposition = random.choice(prep)
    return preposition

# Get prepostional phrase
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    word = get_determiner(quantity)
    noun = get_noun(quantity)

    phrase = f"{preposition} {word} {noun}"

    return phrase
    

# Defining for a second Prepositional phrase
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    word = get_determiner(quantity)
    noun = get_noun(quantity)

    phrase1 = f"{preposition} {word} {noun}"

    return phrase1
    
# Randomly chooses a adjective
def get_adjective():
    adject = ["blue", "red", "fast", "slow", 
    "strong", "weak", "round", "poosh"]

    adjective = random.choice(adject)

    return adjective

# Randomly chooses a adverb
def get_adverb():
    adv = ["quickly", "slowly", "poorly", "smelly", 
    "richly", "weakly", "greatly"]

    adverb = random.choice(adv)

    return adverb

# Makes a sentence from input
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    word = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    adverb = get_adverb()
    verb = get_verb(tense, quantity)
    phrase = get_prepositional_phrase(quantity)
    phrase1 = get_prepositional_phrase(quantity)
    
    # Capitalize the first letter.
    cap_word = word.capitalize()

    print(f"{cap_word} {adjective} {noun} {adverb} {verb} {phrase} {phrase1}.")


main()