# AI Content Moderation Tool

An AI-powered Trust & Safety moderation prototype for reviewing user-generated comments.

## Overview

This project simulates a real-world content moderation workflow.  
It classifies user comments based on policy categories, assigns severity levels, recommends moderation actions, and stores review logs for dashboard analysis.

## Features

- Policy-based content classification
- Harassment, hate speech, violence, sexual content, spam, and self-harm detection
- Severity classification: LOW, MEDIUM, HIGH
- Recommended moderation action
- Detected keyword explanation
- Moderation dashboard
- Review log storage using CSV
- Built with Streamlit

## Policy Categories

- Harassment / Insult
- Hate Speech
- Violence / Threat
- Sexual Content
- Spam / Scam
- Self Harm

## Moderation Flow

1. User enters a comment.
2. The system checks the comment against policy keywords.
3. If a policy violation is detected, the system assigns a severity level.
4. The system recommends an action:
   - LOW: Allow
   - MEDIUM: Human Review
   - HIGH: Remove Immediately
5. The review result is saved to the moderation log.
6. The dashboard displays moderation activity and policy trends.

## Tech Stack

- Python
- Streamlit
- Pandas
- GitHub
- Streamlit Cloud

## Demo

Streamlit App:  
https://ai-moderation-tool-jaeman.streamlit.app/

## Why I Built This

I built this project to demonstrate my understanding of Trust & Safety operations, policy enforcement, content risk classification, and human review workflows.

This project is inspired by real-world moderation workflows used in online platforms, where policy interpretation, severity assessment, and escalation decisions are critical.

## Relevant Background

I have experience in content moderation and policy enforcement through roles related to Trust & Safety and content regulation.  
This project connects my operational experience with practical AI tool development.

## Future Improvements

- Add machine learning-based classification
- Add OpenAI Moderation API integration
- Add multilingual detection
- Add moderator note function
- Add appeal review workflow
- Add downloadable CSV reports
- Improve dashboard visualization
