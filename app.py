import random

# 1. Predefined words list
words = ["apple", "banana", "orange", "grapes", "mango"]

# 2. Choose a random word from the list
word = random.choice(words)

# 3. Track guessed letters + remaining tries
guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(f"You have {tries} incorrect guesses.\n")

# 4. Display underscores for each letter in the word
display = ["_" for _ in word]

# 5. Main game loop
while tries > 0 and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Enter a letter: ").lower()

    # 6. Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.\n")
        continue

    # 7. Check if letter already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    # 8. Add guess to list
    guessed_letters.append(guess)

    # 9. If guess is correct, reveal the letter(s)
    if guess in word:
        print("✅ Good guess!\n")
        for i, ch in enumerate(word):
            if ch == guess:
                display[i] = guess
    else:
        # 10. Wrong guess, decrease tries
        tries -= 1
        print(f"❌ Wrong guess! {tries} tries left.\n")

# 11. Game result
if "_" not in display:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
