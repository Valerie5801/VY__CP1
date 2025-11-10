#VY 2nd Dictionaries Notes
omori  = {
    "Aubrey": {
        "intro": "Hey! I'm Aubrey! Oh, did you want to come see my pet bunny? She's sooo cute!",
        "quote": "Do you like my raincoat, Sunny? Its pink, my favorite color!"
    },
    "Kel": {
        "intro": "Yo! I'm Kel, and I really like playing basketball! I'm also the brother of Hero! Have you met him yet??",
        "quote": "Ew...pink is a gross color."
    },
    "Hero": {
        "intro": "Hello, I'm Henry, but everyone calls me Hero. Are you new around here?"
    },
    "Basil": {
        "intro": "Hi...I'm Basil, and I like taking photos. Say, can I take a picture of you?"
    },
    "Mari": {
        "intro": "Hello! I'm Mari, the older sister of my dear brother Sunny. We're going to perform at the recital in a week, are you coming?"
    }
}

print(omori["Kel"]["intro"])

person = {
    #key: value,
    "name": "Sunny",
    "age": 16,
    "item": "violin",
    "friends": ["Aubrey", "Kel", "Hero", "Basil"],
    "sibling": "Mari"
}

print(person["name"])
print(person.keys())

for key in person.keys():
    if key == "friends":
        for friend in person[key]:
            print(f"{person["name"]} has a friend named {friend}")
    else:
        print(f"{key} is {person[key]}")
    
person["pet"] = "Mewo"
print(f"{person["name"]} has a pet named {person["pet"]}")
#print(person.items())
person["imagination"] = "Headspace"
#print(person.items())
person["item"] = "Jump Rope"
print(person.items())