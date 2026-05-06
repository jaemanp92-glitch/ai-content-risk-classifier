def policy_decision(text):
    text_lower = text.lower()

    threat_keywords = ["kill you", "hurt you", "attack you", "beat you"]
    insult_keywords = ["stupid", "idiot", "disgusting", "trash"]
    hate_keywords = ["go back to your country", "your race", "immigrant scum"]

    if any(word in text_lower for word in threat_keywords):
        return {
            "violation": "YES",
            "policy": "Threat",
            "action": "Remove",
            "reason": "The comment contains a direct threat of violence."
        }

    elif any(word in text_lower for word in hate_keywords):
        return {
            "violation": "YES",
            "policy": "Hate Speech",
            "action": "Remove",
            "reason": "The comment targets identity or nationality."
        }

    elif any(word in text_lower for word in insult_keywords):
        return {
            "violation": "YES",
            "policy": "Harassment / Insult",
            "action": "Review",
            "reason": "The comment contains abusive language."
        }

    else:
        return {
            "violation": "NO",
            "policy": "Safe",
            "action": "Allow",
            "reason": "No violation detected."
        }


# 테스트
if __name__ == "__main__":
    test_cases = [
        "I will kill you",
        "You are stupid",
        "Go back to your country",
        "I love you"
    ]

    for text in test_cases:
        print(f"Input: {text}")
        print(policy_decision(text))
        print("-" * 50)
