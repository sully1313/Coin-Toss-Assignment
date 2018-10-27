import random

replay = "y"
times_played = 0
heads_tossed = 0
tails_tossed = 0
correct_answers = 0
incorrect_answers = 0

while replay == "y":
    def coin_toss():
        # will return either 1 or 0 randomly
        return random.randint(0, 1)

    print("\n\tGuess whether the Coin is a Heads or a Tails")
    users_guess = str(input("\n\tEnter 'H' for Heads OR 'T' for Tails: ")).upper()
    coin_toss_result = coin_toss()
    times_played += 1


# print users guess
    if users_guess == "H":
        print("\tYou Guessed Heads")
    elif users_guess == "T":
        print("\tYou Guessed Tails")
    else:
        print("\tYou Guessed '%s'. This was not an option"% users_guess)

# Heads
    if coin_toss_result == 0:
        heads_tossed += 1
        print("\tToss #%d - Heads Tossed"% times_played)
        if users_guess == "H":
            correct_answers += 1
            print("\tYou Guessed Heads Correctly!")
        elif users_guess == "T":
            incorrect_answers += 1
            print("\tSorry. Incorrect Guess! You guessed: 'T'")
# Tails
    elif coin_toss_result == 1:
        tails_tossed += 1
        print("\tToss #%d - Tails Tossed"% times_played)
        if users_guess == "T":
            correct_answers += 1
            print("\tYou Guessed Tails Correctly!")
        elif users_guess == "H":
            incorrect_answers += 1
            print("\tSorry. Incorrect Guess! You guessed: 'H'")

    replay = str(input("\tWould you like to play again?(Y/N): "))
    replay.lower()

def correct_answer(correct, total_tosses):
    correct_percent = (correct/total_tosses)*100
    return correct_percent

def incorrect_answer(incorrect, total_tosses):
    incorrect_percent = (incorrect/total_tosses)*100
    return incorrect_percent

print("\n\t%d Heads Tossed"% heads_tossed)
print("\t%d Tails Tossed"% tails_tossed)
print("\t%d Total Tosses"% times_played)
print("\tYou guessed %d Time(s) Correctly:\t%.1f%%"% (correct_answers, correct_answer(correct_answers, times_played)))
print("\tYou guessed %d Time(s) Incorrectly:\t%.1f%%"% (incorrect_answers, incorrect_answer(incorrect_answers, times_played)))

print("\n\tThanks for playing Coin Toss")

exit()
