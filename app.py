import streamlit as st
import random
import time


ROWS, COLS = 3, 3
MAX_LINES = 3
MIN_BET, MAX_BET = 1, 100

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

symbol_images = {
    "A": "images/A.png",
    "B": "images/B.png",
    "C": "images/C.png",
    "D": "images/D.png"
}

# ---------------- GAME LOGIC ----------------
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="Slot Machine", page_icon="🎰")
st.title("🎰 Slot Machine Web App")

# Session state to check balance
if "balance" not in st.session_state:
    st.session_state.balance = 0

# to Deposit the amount for betting
deposit = st.number_input("Deposit Amount", min_value=0, step=10)
if st.button("Add Deposit"):
    st.session_state.balance += deposit

st.subheader(f"💰 Balance: ${st.session_state.balance}")

# take Betting inputs from the user
lines = st.selectbox("Number of lines", [1, 2, 3])
bet = st.number_input("Bet per line", min_value=MIN_BET, max_value=MAX_BET)

# Spin button 
if st.button("🎰 SPIN"):
    total_bet = lines * bet

    if total_bet > st.session_state.balance:
        st.error("Insufficient balance!")
    else:
        with st.spinner("Spinning..."):
            time.sleep(1)

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

        # Displaying the  slots
        for row in range(ROWS):
            cols = st.columns(3)
            for col_index in range(3):
                symbol = slots[col_index][row]
                cols[col_index].image(symbol_images[symbol], width=100)

        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        st.session_state.balance += winnings - total_bet

        if winnings > 0:
            st.success(f"🎉 You won ${winnings} on lines {winning_lines}")
        else:
            st.warning("No win, try again!")

        st.subheader(f"💰 Updated Balance: ${st.session_state.balance}")


