import random

def choose_word():
    words = ["cat", "dog", "bat", "sun", "moon", "pen", "book", "fish", "tree", "frog",
        "star", "milk", "ball", "car", "bus", "lamp", "rain", "shoe", "hat", "cake"]
    return random.choice(words)

def display_words(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 10

    print("Welcome to Hangman!")
    print(display_words(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good Guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")  

        current_display = display_words(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            break

    if attempts == 0:
        print(f"Game over! The word was '{word}'.")  

if __name__ == "__main__":
    hangman()
