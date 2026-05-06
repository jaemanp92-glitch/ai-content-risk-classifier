import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="AI Content Moderation Tool",
    page_icon="🛡️",
    layout="wide"
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

st.sidebar.title("🛡️ Moderator Console")
page = st.sidebar.radio(
    "Navigation",
    ["Review Tool", "Dashboard", "Policy Guide", "About Project"]
)

if page == "Review Tool":
    st.title("AI Content Moderation Tool")
    st.write("A Trust & Safety moderation prototype for reviewing user-generated comments.")

    comment = st.text_area("Enter comment", height=160)

    if st.button("Analyze Comment"):
        if comment.strip() == "":
            st.warning("Please enter a comment first.")
        else:
            policy, matched_words = detect_policy(comment)
            severity = decide_severity(matched_words)
            action = decide_action(severity)

            st.divider()

            if policy:
                violation = "YES"
                reason = f"Detected policy violation based on matched terms: {matched_words}"

                col1, col2, col3 = st.columns(3)
                col1.error("Violation: YES")
                col2.warning(f"Policy: {policy}")

                if severity == "HIGH":
                    col3.error(f"Severity: {severity}")
                else:
                    col3.info(f"Severity: {severity}")

                st.subheader("Moderation Decision")
                st.write(f"Recommended Action: **{action}**")
                st.write(f"Detected Terms: `{matched_words}`")
                st.write(f"Reason: {reason}")

            else:
                violation = "NO"
                policy = "None"
                severity = "LOW"
                action = "Allow"
                reason = "No harmful or policy-violating language detected."

                col1, col2, col3 = st.columns(3)
                col1.success("Violation: NO")
                col2.success("Policy: None")
                col3.success("Severity: LOW")

                st.subheader("Moderation Decision")
                st.write(f"Recommended Action: **{action}**")
                st.write(f"Reason: {reason}")

            save_log(comment, violation, policy, severity, action, reason)

elif page == "Dashboard":
    st.title("Moderator Dashboard")
    st.write("Overview of moderation activity and content risk trends.")

    try:
        logs = pd.read_csv("moderation_logs.csv")

        total_reviews = len(logs)
        violation_count = len(logs[logs["violation"] == "YES"])
        safe_count = len(logs[logs["violation"] == "NO"])
        high_count = len(logs[logs["severity"] == "HIGH"])

        violation_rate = round((violation_count / total_reviews) * 100, 1) if total_reviews > 0 else 0

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Reviews", total_reviews)
        col2.metric("Violations", violation_count)
        col3.metric("Safe Comments", safe_count)
        col4.metric("Violation Rate", f"{violation_rate}%")

        st.divider()

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.subheader("Policy Breakdown")
            policy_counts = logs["policy"].value_counts()
            st.bar_chart(policy_counts)

        with chart_col2:
            st.subheader("Severity Breakdown")
            severity_counts = logs["severity"].value_counts()
            st.bar_chart(severity_counts)

        st.divider()

        st.subheader("High Risk Queue")
        high_risk = logs[logs["severity"] == "HIGH"]

        if len(high_risk) > 0:
            st.dataframe(high_risk.tail(10), use_container_width=True)
        else:
            st.info("No high-risk cases detected yet.")

        st.subheader("Recent Moderation Reviews")
        st.dataframe(logs.tail(20), use_container_width=True)

        csv = logs.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            label="Download Moderation Logs as CSV",
            data=csv,
            file_name="moderation_logs.csv",
            mime="text/csv"
        )

    except FileNotFoundError:
        st.info("No moderation logs yet. Submit comments from the Review Tool first.")

elif page == "Policy Guide":
    st.title("Policy Guide")
    st.write("Internal-style policy taxonomy used by this moderation prototype.")

    for policy, keywords in POLICIES.items():
        with st.expander(policy):
            st.write("Example detection keywords:")
            st.write(", ".join(keywords))

    st.divider()

    st.subheader("Severity Rules")
    st.write("""
    - LOW: No policy violation detected
    - MEDIUM: One harmful keyword detected
    - HIGH: Two or more harmful keywords detected
    """)

    st.subheader("Action Rules")
    st.write("""
    - LOW → Allow
    - MEDIUM → Human Review
    - HIGH → Remove Immediately
    """)

elif page == "About Project":
    st.title("About This Project")
    st.write("""
    This project is an AI-powered Trust & Safety moderation prototype.

    It demonstrates a practical content moderation workflow, including:
    - Policy-based classification
    - Severity assessment
    - Human review recommendation
    - Moderation logging
    - Dashboard monitoring

    This project is designed to showcase understanding of real-world platform safety operations.
    """)

    st.subheader("Tech Stack")
    st.write("""
    - Python
    - Streamlit
    - Pandas
    - GitHub
    - Streamlit Cloud
    """)
