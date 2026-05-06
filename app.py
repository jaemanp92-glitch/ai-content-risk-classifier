import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="AI Content Moderation Tool",
    page_icon="🛡️",
    layout="centered"
)

POLICIES = {
    "Harassment / Insult": ["멍청이", "바보", "한심", "쓰레기", "idiot", "stupid", "moron"],
    "Hate Speech": ["흑인은", "여자는 다", "남자는 다", "racist"],
    "Violence / Threat": ["죽여", "죽인다", "죽어", "kill you", "threat"],
    "Sexual Content": ["섹스", "야한", "sexual"],
    "Spam / Scam": ["무료 투자", "클릭하세요", "돈 벌기", "scam", "click here"],
    "Self Harm": ["자해", "죽고싶다", "self harm"]
}

def detect_policy(text):
    detected_policy = None
    matched_words = []

    for policy, keywords in POLICIES.items():
        for word in keywords:
            if word.lower() in text.lower():
                detected_policy = policy
                matched_words.append(word)

    return detected_policy, matched_words

def decide_severity(matched_words):
    if len(matched_words) >= 2:
        return "HIGH"
    elif len(matched_words) == 1:
        return "MEDIUM"
    else:
        return "LOW"

def decide_action(severity):
    if severity == "HIGH":
        return "Remove Immediately"
    elif severity == "MEDIUM":
        return "Human Review"
    else:
        return "Allow"

def save_log(comment, violation, policy, severity, action, reason):
    log_data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "comment": comment,
        "violation": violation,
        "policy": policy,
        "severity": severity,
        "action": action,
        "reason": reason
    }

    df = pd.DataFrame([log_data])

    try:
        existing_df = pd.read_csv("moderation_logs.csv")
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        updated_df.to_csv("moderation_logs.csv", index=False)
    except FileNotFoundError:
        df.to_csv("moderation_logs.csv", index=False)

st.title("AI Content Moderation Tool")
st.write("A simple AI-powered Trust & Safety moderation tool for reviewing user-generated comments.")

comment = st.text_area("Enter comment", height=120)

if st.button("Check"):
    if comment.strip() == "":
        st.warning("Please enter a comment first.")
    else:
        policy, matched_words = detect_policy(comment)
        severity = decide_severity(matched_words)
        action = decide_action(severity)

        if policy:
            violation = "YES"
            reason = f"Detected policy violation based on matched terms: {matched_words}"

            st.error("🚨 Violation: YES")
            st.warning(f"Policy: {policy}")

            if severity == "HIGH":
                st.error(f"Severity: {severity}")
            else:
                st.info(f"Severity: {severity}")

            st.write(f"Action: {action}")
            st.write(f"Detected Terms: {matched_words}")
            st.write(f"Reason: {reason}")

        else:
            violation = "NO"
            policy = "None"
            severity = "LOW"
            action = "Allow"
            reason = "No harmful or policy-violating language detected."

            st.success("✅ Violation: NO")
            st.write(f"Policy: {policy}")
            st.write(f"Severity: {severity}")
            st.write(f"Action: {action}")
            st.write(f"Reason: {reason}")

        save_log(comment, violation, policy, severity, action, reason)

st.divider()

st.subheader("Moderator Dashboard")

try:
    logs = pd.read_csv("moderation_logs.csv")

    total_reviews = len(logs)
    violation_count = len(logs[logs["violation"] == "YES"])
    safe_count = len(logs[logs["violation"] == "NO"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews", total_reviews)
    col2.metric("Violations", violation_count)
    col3.metric("Safe Comments", safe_count)

    st.write("Policy Breakdown")
    policy_counts = logs["policy"].value_counts()
    st.bar_chart(policy_counts)

    st.write("Recent Reviews")
    st.dataframe(logs.tail(10))

except FileNotFoundError:
    st.info("No moderation logs yet. Submit a comment to generate dashboard data.")
