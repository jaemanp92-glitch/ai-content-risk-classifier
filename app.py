import streamlit as st

def policy_decision(text):
    text_lower = text.lower()

    threat_keywords = ["kill you", "hurt you", "attack you", "beat you", "i will kill"]
    hate_keywords = ["go back to your country", "immigrant scum", "your race", "foreigners are"]
    insult_keywords = ["stupid", "idiot", "dumb", "trash", "disgusting"]

    if any(word in text_lower for word in threat_keywords):
        return "YES", "Threat", "Remove", "Direct threat or violent language detected."

    elif any(word in text_lower for word in hate_keywords):
        return "YES", "Hate Speech", "Remove", "Attack based on nationality, ethnicity, or identity detected."

    elif any(word in text_lower for word in insult_keywords):
        return "YES", "Harassment / Insult", "Review", "Abusive or insulting language detected."

    else:
        return "NO", "Safe", "Allow", "No clear policy violation detected."


st.title("AI Content Moderation Tool")
st.write("A simple Trust & Safety prototype for reviewing user-generated comments.")

user_input = st.text_area("Enter comment")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a comment.")
    else:
        violation, policy, action, reason = policy_decision(user_input)

        if violation == "YES":
    st.error(f"Violation: {violation}")
    st.warning(f"Policy: {policy}")
    st.write(f"Action: {action}")
    st.write(f"Reason: {reason}")

else:
    st.success("Content is safe.")
    st.write(f"Policy: {policy}")
    st.write(f"Action: {action}")
