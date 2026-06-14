# Spam Email Detector

import re

SPAM_KEYWORDS = {
    "free", "winner", "congratulations", "click here", "limited time",
    "act now", "save big", "urgent", "guaranteed", "risk free",
    "cash bonus", "make money", "earn money", "work from home",
    "no cost to you", "special offer", "exclusive deal", "buy now",
    "order now", "claim now", "prize", "you have been selected",
    "lowest price", "double your income", "instant access",
    "credit card", "password", "verify your account", "wire transfer",
    "unsubscribe"
}

# Gets an email message from the user and returns it as a string.
def get_email_message():
    print("Enter the email message you want to check for spam.")
    print("Press Enter on a blank line when you are finished.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    return "\n".join(lines)

    # Scans the message for spam keywords and phrases and returns the total spam score and a \
    # dictionary of matched words/phrases.
def calculate_spam_score(message, keywords):
    spam_score = 0
    matched_words = {}

    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword) + r"\b"
        matches = re.findall(pattern, message, re.IGNORECASE)

        if matches:
            count = len(matches)
            spam_score += count
            matched_words[keyword] = count

    return spam_score, matched_words

# Returns the spam likelihood rating based on spam score.
def rate_spam_likelihood(score):
    if score == 0:
        return "Not likely to be spam"
    elif score <= 1:
        return "Low chance of being spam"
    elif score <= 2:
        return "Medium chance of being spam"
    else:
        return "High chance of being spam"

# Displays the spam score, spam likelihood, and matching spam words.
def display_results(score, likelihood, matched_words):
    print("\n--- Spam check Results ---")
    print(f"Spam score: {score}")
    print(f"Spam likelihood: {likelihood}")

    if matched_words:
        print("\nWords/Phrases that casued points:")
        for word, count in matched_words.items():
            print(f"- {word}: {count}")

    else:
        print("\nNo spam words or phrases were found.")

def main():
    email_message = get_email_message()
    spam_score, matched_words = calculate_spam_score(email_message, SPAM_KEYWORDS)
    likelihood = rate_spam_likelihood(spam_score)
    display_results(spam_score, likelihood, matched_words)

if __name__ == "__main__":
    main()




