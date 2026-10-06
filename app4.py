import streamlit as st
import random

st.set_page_config(
    page_title="Krishi Sowja's Rock Paper Scissors",
    page_icon="🎮"
)

st.title("🎮 Krishi Sowja's Rock Paper Scissors Game")

st.write("Choose Rock, Paper, or Scissors!")

choices = ["Rock", "Paper", "Scissors"]

user_choice = st.selectbox(
    "Choose your option:",
    choices
)

if st.button("🎯 Play Game"):

    computer_choice = random.choice(choices)

    st.write(f"### 👤 Your Choice: {user_choice}")
    st.write(f"### 🤖 Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        st.info("🤝 It's a Draw!")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.success("🎉 You Win!")

    else:
        st.error("😢 Computer Wins!")