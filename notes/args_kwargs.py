#VY 2nd *args and **kwargs

"""def hello(name="Sunny", sibling="Mari"):
    return f"Hello {name}. Is your sibling {sibling}?"

print(hello("OMORI", "Mari"))
print(hello(sibling = "Hero", name = "Kel"))"""

def hello(*names, **city):
    for name in names:
        print(f"Hi {name}. How long have you been in {city["tcity"]}?")

hello("Sunny", "Aubrey", "Kel", "Hero", "Basil", "Mari", tcity = "Faraway Town")