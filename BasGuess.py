secret_word = "giraffe"
guess = ""
guess_cnt = 0
guess_limit = 5
out_of_guesses = False

#"!=" means not equal to
while guess != secret_word and not(out_of_guesses):
    if guess_cnt < guess_limit:
        guess = input("Enter Guess: ")
        guess_cnt += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses - you LOSE!")

else:
    print("You got it!")