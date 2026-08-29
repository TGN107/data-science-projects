from collections import Counter

def word_counter():
    print("\n--- Word Counter ---")
    text = input("Enter your text: ").strip()

    words = text.split()
    word_count = len(words)
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))
    common_words = Counter(words).most_common(3)

    print(f"\nTotal words: {word_count}")
    print(f"Total characters (with spaces): {char_count}")
    print(f"Total characters (no spaces): {char_count_no_spaces}")
    print("Most common words:")
    for word, freq in common_words:
        print(f"  - {word}: {freq} time(s)")

if __name__ == "__main__":
    word_counter()
