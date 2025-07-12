# ---------------------------------------------
# 📋 Streamlit App: Sum from 1 to n Calculator
# ---------------------------------------------

import streamlit as st

# ------------------------
# 🎨 Page configuration
# ------------------------
st.set_page_config(
    page_title="Sum Calculator from 1 to n",
    page_icon="➕",
    layout="centered"
)

# ------------------------
# 📝 Title and description
# ------------------------
st.title("🔢 Sum of Numbers from 1 to n")
st.markdown("""
Welcome! This simple app allows you to calculate the **sum of all numbers from 1 to n**.

Just enter a positive integer and click the button to get the result.
""")

# ------------------------
# 🔧 User input section
# ------------------------
n = st.number_input(
    "Enter a positive integer n",
    min_value=1,
    value=10,
    step=1,
    help="This is the upper limit for the summation (1 + 2 + ... + n)"
)

# ------------------------
# 🚀 Compute sum on button click
# ------------------------
if st.button("Calculate Sum"):
    # Initialize the sum variable
    total_sum = 0
    
    # Loop from 1 to n and add each number
    for i in range(1, n + 1):
        total_sum += i

    # Display the result
    st.success(f"The sum of all numbers from 1 to {n} is: {total_sum}")

# ------------------------
# 📝 Footer
# ------------------------
st.markdown("""
---
Made with ❤️ using [Streamlit](https://streamlit.io)
""")