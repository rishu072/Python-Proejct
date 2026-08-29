import random

print("===== Fake Headline Generator =====")

subjects = [
    "Scientists",
    "Engineers",
    "College Students",
    "Tech Companies",
    "Researchers",
    "AI Experts",
    "Government Officials"
]

actions = [
    "discover a new technology",
    "launch a revolutionary AI system",
    "invent a machine that changes everything",
    "announce a shocking breakthrough",
    "develop a robot capable of learning emotions",
    "create a new form of digital communication"
]

places = [
    "in India",
    "in Silicon Valley",
    "at a secret laboratory",
    "during a technology conference",
    "at a university research center",
    "in a futuristic smart city"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING: {subject} {action} {place}!"

    print("\nGenerated Headline:")
    print(headline)

    choice = input("\nGenerate another? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using Fake Headline Generator!")
        break