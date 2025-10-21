import random

fake_newsname = [
    'Vivek World',
    'Vivek',
    'Elon Musk',
    'Mark Zuckerberg',
    'Bill Gates',
    'Jeff Bezos'
]

actions = [
    'defines the world order',
    'is the real king',
    'will define the future',
    'thinks about AI'
]

places_or_thinks = [
    'born in Lucknow, India',
    'born in Pakistan',
    'born in Afghanistan'
]

while True:
    subject = random.choice(fake_newsname)
    action = random.choice(actions)
    place_or_think = random.choice(places_or_thinks)

    headline = f"BREAKING NEWS: {subject} {action}, {place_or_think}!"
    print(f"\n{headline}\n")

    user_input = input("Do you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print('\nThank you for using the Fake News Headline Generator. Have a fun day! 😊')
