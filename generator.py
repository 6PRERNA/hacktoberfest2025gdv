# 1- Import the random module to generate random choices
import random

# 2 - create subjects
subjects = [
    "Shahrukh khan",
    "Virat Kholi",
    "Nirmala Sitharamana",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "a new movie",
    "a cricket match",
    "a new policy",
    "a street food stall",
    "a new tech startup",
    "a festival",
    "a charity event"
]


#3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)
    
    headline = f"Breaking News:{subject} {action} {places_or_thing}"
    print("\n" + headline)
    
    user_input = input("\n Do you want another headline? (yes/no): ").strip().lower()
    # .strip() remove the extra spaces , lower to convert the input into lowercase
    if user_input == "no":
        break
    
#print goodbye message

print("\nThanks for using the fake news Headline Generator. Have a fun day \n")
