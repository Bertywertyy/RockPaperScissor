import streamlit as st
import random

# Initialize session state for tracking wins
if 'user_wins' not in st.session_state:
    st.session_state.user_wins = 0
if 'computer_wins' not in st.session_state:
    st.session_state.computer_wins = 0

# Load your images (replace with your actual image paths)
rock_image = "rock_image.png"  # Replace with actual image path
paper_image = "paper_image.png"  # Replace with actual image path
scissors_image = "scissors_image.png"  # Replace with actual image path

# Game options
options = ["rock", "paper", "scissors"]

# Streamlit UI
st.title("Rock, Paper, Scissors Game")

# Display images for user selection
col1, col2, col3 = st.columns(3)

user_input = None  # Initialize user input

# Make the image act like a button
with col1:
    if st.image(rock_image, caption="Rock", use_column_width=True):
        user_input = "rock"

with col2:
    if st.image(paper_image, caption="Paper", use_column_width=True):
        user_input = "paper"

with col3:
    if st.image(scissors_image, caption="Scissors", use_column_width=True):
        user_input = "scissors"

# Randomly pick for the computer
if user_input:
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    st.write(f"Computer picked: {computer_pick.capitalize()}.")

    if user_input == computer_pick:
        st.write("It's a draw!")
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        st.write("You won!")
        st.session_state.user_wins += 1
    else:
        st.write("You lost!")
        st.session_state.computer_wins += 1

# Display the score
st.subheader("Score:")
st.write(f"You won: {st.session_state.user_wins} times")
st.write(f"The computer won: {st.session_state.computer_wins} times")

# Button to reset the game
if st.button("Reset Game"):
    st.session_state.user_wins = 0
    st.session_state.computer_wins = 0
    st.write("Game reset!")
