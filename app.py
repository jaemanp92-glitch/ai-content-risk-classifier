import streamlit as st

def policy_decision(text):
    text_lower = text.lower()

    if "kill you" in text_lower:
        return "YES", "Threat", "Remove", "Violence threat detected"

    elif "stupid" in text_lower:
        return "YES", "Harassment", "Review", "Insult detected"

    else:
        return "NO", "Safe", "Allow", "No violation"


st.title("AI Content Moderation Tool")

user_input = st.text_area("Enter comment")

if st.button("Check"):
    if user_input:
        v, p, a, r = policy_decision(user_input)

        st.write(f"Violation: {v}")
        st.write(f"Policy: {p}")
        st.write(f"Action: {a}")
        st.write(f"Reason: {r}")
