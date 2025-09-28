def get_input(prompt):
    """Prompt the user and return the entered word."""
    return input(f"{prompt}: ").strip()

print("Please enter the following:\n")
adjective = get_input("adjective")
animal = get_input("animal")
verb1 = get_input("verb")
exclamation = get_input("exclamation").capitalize()   # auto‑capitalize
verb2 = get_input("verb")
verb3 = get_input("verb")

story = (
    "The other day, I was really in trouble. It all started when I saw a very\n"
    f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all\n"
    f"I could think to do was to {verb2} over and over. Miraculously,\n"
    f"that caused it to stop, but not before it tried to {verb3}\n"
    "right in front of my family."
)

print("\nThe story is:\n")

print(story)