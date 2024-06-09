import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")

    words = []

    append_random_words(words)
    print(f"words {words}")

    append_random_words(words, 5)
    print(f"words {words}")

    sentences = []

    append_random_sentences(sentences)
    print(f"sentences {sentences}")

    append_random_sentences(sentences, 5)
    print(f"sentences {sentences}")


def append_random_numbers(numbers_list, quantity = 1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


def append_random_words(words_list, quantity = 1):

    candidates = ["bird", "red", "blue", "whale", "car", "tire",
                  "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"]

    for _ in range(quantity):
         word = random.choice(candidates)
         words_list.append(word)

def append_random_sentences(sentences_list, quantity = 1):
    candidates = ['The brown fox ran.', 'The yellow cat meowed.', 'The blue bird flew away.'
                   'Cats and dogs fight.', 'Cheese is not a food.', 'the moon is not green.',
                   'Children can be polite.', 'Programming can be fun sometimes.', 
                   'BYUI education systems are challenging.', 'The sun will rise tomorrow.', 
                   'the weather is really nice outside.']
    for _ in range(quantity):
         sentence = random.choice(candidates)
         sentences_list.append(sentence)




if __name__ == "__main__":
        main()