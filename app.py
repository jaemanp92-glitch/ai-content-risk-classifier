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

# -------------------------
# POLICY DETECTION
# -------------------------
def detect_policy(text):
    detected_policy = None
    matched_words = []

    for policy, keywords in POLICIES.items():
        for word in keywords:
            if word.lower() in text.lower():
                detected_policy = policy
                matched_words.append(word)

    return detected_policy, matched_words

# -------------------------
# SEVERITY
# -------------------------
def decide_severity(matched_words):
    if len(matched_words) >= 2:
        return "HIGH"
    elif len(matched_words) == 1:
        return "MEDIUM"
    else:
        return "LOW"

# -------------------------
# ACTION
# -------------------------
def decide_action(severity):
    if severity == "HIGH":
        return "Remove Immediately"
    elif severity == "MEDIUM":
        return "Human Review"
    else:
        return "Allow"

# -------------------------
# SAVE LOG
# -------------------------
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

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("🛡️ Moderator Console")

page = st.sidebar.radio(
    "Navigation",
    [
        "Review Tool",
        "Bulk CSV Review",
        "Dashboard",
        "Policy Guide",
        "About Project"
    ]
)

# ====================================================
# REVIEW TOOL
# ====================================================
if page == "Review Tool":

    st.title("AI Content Moderation Tool")

    st.write(
        "A Trust & Safety moderation prototype for reviewing user-generated comments."
    )

    comment = st.text_area("Enter comment", height=150)

    if st.button("Analyze Comment"):

        if comment.strip() == "":
            st.warning("Please enter a comment first.")

        else:

            policy, matched_words = detect_policy(comment)

            severity = decide_severity(matched_words)

            action = decide_action(severity)

            if policy:

                violation = "YES"

                reason = (
                    f"Detected policy violation based on matched terms: {matched_words}"
                )

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

                st.success("No policy violations detected.")

                st.write(f"Policy: {policy}")
                st.write(f"Severity: {severity}")
                st.write(f"Action: {action}")

            save_log(
                comment,
                violation,
                policy,
                severity,
                action,
                reason
            )

# ====================================================
# BULK CSV REVIEW
# ====================================================
elif page == "Bulk CSV Review":

    st.title("Bulk CSV Moderation")

    st.write(
        "Upload a CSV file containing comments for bulk moderation analysis."
    )

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    st.info("CSV format example: column name should be 'comment'")

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        if "comment" not in df.columns:

            st.error("CSV must contain a 'comment' column.")

        else:

            results = []

            for comment in df["comment"]:

                policy, matched_words = detect_policy(str(comment))

                severity = decide_severity(matched_words)

                action = decide_action(severity)

                if policy:
                    violation = "YES"
                    reason = f"Matched terms: {matched_words}"
                else:
                    violation = "NO"
                    policy = "None"
                    reason = "No violation detected."

                results.append({
                    "comment": comment,
                    "violation": violation,
                    "policy": policy,
                    "severity": severity,
                    "action": action,
                    "reason": reason
                })

            result_df = pd.DataFrame(results)

            st.subheader("Moderation Results")

            st.dataframe(result_df)

            csv = result_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download Results CSV",
                data=csv,
                file_name="moderation_results.csv",
                mime="text/csv"
            )

# ====================================================
# DASHBOARD
# ====================================================
elif page == "Dashboard":

    st.title("Moderator Dashboard")

    st.write(
        "Overview of moderation activity and content risk trends."
    )

    try:

        logs = pd.read_csv("moderation_logs.csv")

        total_reviews = len(logs)

        violation_count = len(
            logs[logs["violation"] == "YES"]
        )

        safe_count = len(
            logs[logs["violation"] == "NO"]
        )

        violation_rate = round(
            (violation_count / total_reviews) * 100,
            2
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Reviews", total_reviews)

        col2.metric("Violations", violation_count)

        col3.metric("Safe Comments", safe_count)

        col4.metric("Violation Rate", f"{violation_rate}%")

        st.divider()

        colA, colB = st.columns(2)

        with colA:

            st.subheader("Policy Breakdown")

            policy_counts = logs["policy"].value_counts()

            st.bar_chart(policy_counts)

        with colB:

            st.subheader("Severity Breakdown")

            severity_counts = logs["severity"].value_counts()

            st.bar_chart(severity_counts)

        st.divider()

        st.subheader("High Risk Queue")

        high_risk = logs[logs["severity"] == "HIGH"]

        st.dataframe(high_risk)

        st.subheader("Recent Moderation Reviews")

        st.dataframe(logs.tail(10))

        csv = logs.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Moderation Logs as CSV",
            data=csv,
            file_name="moderation_logs.csv",
            mime="text/csv"
        )

    except FileNotFoundError:

        st.info(
            "No moderation logs available yet."
        )

# ====================================================
# POLICY GUIDE
# ====================================================
elif page == "Policy Guide":

    st.title("Moderation Policy Guide")

    for policy, keywords in POLICIES.items():

        st.subheader(policy)

        st.write("Example keywords:")

        st.code(", ".join(keywords))

# ====================================================
# ABOUT
# ====================================================
elif page == "About Project":

    st.title("About This Project")

    st.write("""
    This project simulates a Trust & Safety moderation workflow
    commonly used by online platforms and social media companies.

    Features include:

    - Policy-based moderation
    - Severity classification
    - Moderator dashboard
    - Moderation logging
    - Bulk CSV moderation
    - Risk queue management

    Built using Python, Streamlit, and Pandas.
    """)

    st.success("Portfolio Project by Jaeman Park")
