import random

def shuffle_word(word):
    word_list = list(word)  
    random.shuffle(word_list)  
    return ''.join(word_list) 
#
words = ["apple", "banana", "cherry", "grape", "orange"]


chosen_word = random.choice(words)


scrambled_word = shuffle_word(chosen_word)


attempts = 5

print("Welcome to the Word Scramble Game!")
print(f"Try to guess the original word from the scrambled word: pleap")


while attempts > 0:
    guess = input(f"You have {attempts} attempts left. Your guess: ")
    
    if guess == "apple":
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        attempts -= 1
        print("Incorrect guess.")

if attempts == 0:
    print(f"Sorry, you've run out of attempts. The correct word was: apple")
