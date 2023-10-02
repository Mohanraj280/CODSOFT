import tkinter as tk
import random


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


# Function to play the game
def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)

    # Update the labels with the game result and choices
    result_label.config(text=f"Computer chose {computer_choice}.\n{result}")

    # Update scores
    if result == "You win!":
        user_score_var.set(user_score_var.get() + 1)
    elif result == "Computer wins!":
        computer_score_var.set(computer_score_var.get() + 1)


# Function to reset the scores
def reset_scores():
    user_score_var.set(0)
    computer_score_var.set(0)
    result_label.config(text="")


# Function to get computer choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and set up user choice variable
user_choice_var = tk.StringVar()
user_choice_var.set("rock")

# Create labels and buttons
user_choice_label = tk.Label(root, text="Choose:")
user_choice_rock = tk.Radiobutton(root, text="Rock", value="rock", variable=user_choice_var)
user_choice_paper = tk.Radiobutton(root, text="Paper", value="paper", variable=user_choice_var)
user_choice_scissors = tk.Radiobutton(root, text="Scissors", value="scissors", variable=user_choice_var)
play_button = tk.Button(root, text="Play", command=play_game)
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
user_score_label = tk.Label(root, text="Your Score:")
user_score_display = tk.Label(root, textvariable=user_score_var, font=("Helvetica", 14, "bold"))
computer_score_label = tk.Label(root, text="Computer Score:")
computer_score_display = tk.Label(root, textvariable=computer_score_var, font=("Helvetica", 14, "bold"))
reset_button = tk.Button(root, text="Reset Scores", command=reset_scores)

# Place widgets on the window using grid layout
user_choice_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))
user_choice_rock.grid(row=1, column=0)
user_choice_paper.grid(row=1, column=1)
user_choice_scissors.grid(row=1, column=2)
play_button.grid(row=2, column=0, columnspan=3, pady=(10, 0))
result_label.grid(row=3, column=0, columnspan=3)
user_score_label.grid(row=4, column=0)
user_score_display.grid(row=4, column=1)
computer_score_label.grid(row=4, column=2)
computer_score_display.grid(row=4, column=3)
reset_button.grid(row=5, column=0, columnspan=3, pady=(10, 0))

# Start the Tkinter main loop
root.mainloop()
