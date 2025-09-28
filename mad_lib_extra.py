def get_input(prompt: str) -> str:
    """Prompt the user and return the entered word."""
    return input(f"{prompt}: ").strip()

def a_or_an(word: str) -> str:
    """Return the appropriate indefinite article for *word*."""
    return "an" if word and word[0].lower() in "aeiou" else "a"

print("Please enter the following:\n")

# ---- required inputs ----------------------------------------------------
adjective = get_input("adjective")
animal = get_input("animal")
verb1 = get_input("verb")
exclamation = get_input("exclamation").capitalize()   # auto‑capitalize
verb2 = get_input("verb")
verb3 = get_input("verb")

# ---- creative extension (optional) --------------------------------------
extra_adj = get_input("extra adjective (optional)")
extra_noun = get_input("extra noun (optional)")
extra_verb = get_input("extra verb (optional)")

# ---- build the story ----------------------------------------------------
story = (
    "The other day, I was really in trouble. It all started when I saw a very\n"
    f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all\n"
    f"I could think to do was to {verb2} over and over. Miraculously,\n"
    f"that caused it to stop, but not before it tried to {verb3}\n"
    "right in front of my family."
)

# If the user supplied all three optional words, add a bonus sentence.
if extra_adj and extra_noun and extra_verb:
    article = a_or_an(extra_adj)
    story += (
        f"\n\nLater, I saw {article} {extra_adj} {extra_noun} that decided to {extra_verb}."
    )

# ---- output -------------------------------------------------------------
print("\nYour story is:\n")
print(story)