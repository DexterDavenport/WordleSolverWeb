import random

def get_words():
    with open('biggest_list.txt') as f:
        words = f.readlines()
    return [word.strip() for word in words]

def get_guess(prompt):
    guess = input(prompt)
    while len(guess) != 5 or not guess.isalpha():
        guess = input('Invalid guess, please enter a five-letter word: ')
    return guess.lower()

def compare_words(word1, word2):
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches

def main():
    words = get_words()
    target_word = random.choice(words)
    print('The target word is a five-letter word. You have six guesses to find it.\n')
    
    remaining_words = words.copy()
    
    for i in range(6):
        guess = get_guess('Enter guess #{}: '.format(i+1))
        matches = compare_words(target_word, guess)
        print('Matching letters: {}'.format(matches))
        
        remaining_words = [word for word in remaining_words if compare_words(word, guess) == matches]
        
        if guess == target_word:
            print('You won! The target word was "{}".'.format(target_word))
            return
        
    print('You lost! The target word was "{}".\nPossible words were:'.format(target_word))
    print('\n'.join(remaining_words))
    
if __name__ == '__main__':
    main()
