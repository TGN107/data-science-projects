import random
import nltk
from nltk.corpus import words

nltk.download('words')

word_list = words.words()

# Filter to avoid very long words (optional)
filtered_words = [word for word in word_list if len(word) >= 4 and len(word) <= 10]

# Choose a random word
word = random.choice(filtered_words).lower()
jumbled_word = "".join(random.sample(word, len(word)))

# Game intro
print("*" * 30)
print("******* Jumble Bumble ********")
print("*" * 30)

# Game logic
chances = 3
while chances != 0:
    print("The word is:", jumbled_word)
    guess = input("Enter your guessed word: ").lower()
    if guess == word:
        print("Correct Guess!")
        print("You won")
        break
    else:
        chances -= 1
        print("Wrong guess!")
        print("Remaining chances are:", chances)
        print()
else:
    print("All chances are exhausted!")
    print("You lose!")
    print("The correct word is:", word)

print("Thank you for playing Jumble Bumble!")
