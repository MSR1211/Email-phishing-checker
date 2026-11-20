def check_phishing(sender, subject, body):
    score = 0
    flags = []
#
    suspicious_words = [
        "urgent",
        "verify your account",
        "password",
        "bank details",
        "click here",
        "account suspended",
        "confirm your details",
    ]

    suspicious_senders = [
        "scammer@gmail.com",
        "scammer2@gmail.com",
    ]

    trusted_senders = [
        "user@gmail.com",
        "user2@gmail.com",
    ]

    email_text = (subject + " " + body).lower()
    sender = sender.lower().strip()

    # look for suspicious wording
    for word in suspicious_words:
        if word in email_text:
            score += 1
            flags.append(f"Suspicious wording: {word}")

    # Check if the sender is malicious 
    if sender in suspicious_senders:
        score += 3
        flags.append("Sender is on the suspicious list")

    elif sender in trusted_senders:
        flags.append("Sender is on the trusted list")

    else:
        score += 1
        flags.append("Sender is unknown")

    # find out score and return
    if score >= 4:
        verdict = "phishing"
    elif score >= 2:
        verdict = "suspicious"
    else:
        verdict = "safe"

    return {
        "score": score,
        "verdict": verdict,
        "flags": flags
    }