# 🛡️ AI Content Moderation Tool

An AI-powered Trust & Safety moderation prototype designed to detect and classify harmful user-generated content.

Built using Python, Streamlit, and Pandas.

---

# 📌 Overview

This project simulates a real-world content moderation workflow used by social media platforms and online communities.

The system analyzes user comments, detects policy violations, assigns severity levels, recommends moderation actions, and stores moderation logs for dashboard analytics.

---

# 🚀 Features

## ✅ Policy-Based Moderation
Detects multiple harmful content categories including:

- Harassment / Insult
- Hate Speech
- Violence / Threat
- Sexual Content
- Spam / Scam
- Self Harm

---

## ✅ Severity Classification

Automatically classifies detected content into:

- LOW
- MEDIUM
- HIGH

based on matched policy terms.

---

## ✅ Moderator Decision System

Provides recommended moderation actions such as:

- Allow
- Human Review
- Remove Immediately

---

## ✅ Moderator Dashboard

Interactive dashboard includes:

- Total review count
- Violation statistics
- Policy breakdown charts
- Severity analysis
- High-risk moderation queue
- Recent moderation history

---

## ✅ Moderation Logging

Stores moderation activity in CSV format for tracking and analytics.

---

# 🧠 Example Workflow

```text
User Comment
      ↓
Policy Detection
      ↓
Severity Classification
      ↓
Moderation Decision
      ↓
Dashboard Logging
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core logic |
| Streamlit | Web application UI |
| Pandas | Data processing |
| CSV Logging | Moderation history storage |

---

# 📷 Project Screenshots

## Review Tool
Detect harmful comments and classify moderation severity.

## Dashboard
Visualize moderation statistics and risk trends.

---

# 📂 Project Structure

```text
ai-content-risk-classifier/
│
├── app.py
├── policy_system.py
├── moderation_logs.csv
├── requirements.txt
└── README.md
```

---

# ⚡ Future Improvements

Planned upgrades include:

- OpenAI Moderation API integration
- Machine learning classification
- Real-time moderation queue
- User authentication
- Bulk CSV moderation
- Toxicity score analysis
- Korean NLP enhancement

---

# 🎯 Project Goal

The goal of this project is to demonstrate:

- Trust & Safety workflow understanding
- AI moderation system design
- Policy enforcement logic
- Dashboard analytics implementation
- Real-world moderation process simulation

---

# 👨‍💻 Author

**Jaeman Park**

AI / Trust & Safety / Content Moderation Portfolio Project

GitHub:
https://github.com/jaemanp92-glitch
## 🔗 Featured Project

### AI Content Moderation Tool

Live Demo:  
https://ai-moderation-tool-jaeman.streamlit.app

GitHub Repository:  
https://github.com/jaemanp92-glitch/ai-content-risk-classifier
---

# 📄 License

This project is for educational and portfolio purposes.
