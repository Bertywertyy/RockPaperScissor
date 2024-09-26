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
images = {"rock": rock_image, "paper": paper_image, "scissors": scissors_image}

# Streamlit UI
st.title("Rock, Paper, Scissors Game")

# Display radio buttons with images as labels
user_input = st.radio(
    "Choose your option",
    options,
    format_func=lambda x: x.capitalize(),
    horizontal=True
)

# Display the selected image
st.image(images[user_input], caption=user_input.capitalize(), use_column_width=True)

# Randomly pick for the computer
if st.button("Play"):
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
