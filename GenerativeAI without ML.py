import random

templates = [
    "The quick {adj} fox jumps over the {noun}.",
    "A {adj} {noun} loves to {verb} all day."
]

words = {
    "adj": ["lazy", "bright", "happy"],
    "noun": ["dog", "moon", "hill"],
    "verb": ["run", "jump", "sleep"]
}

def generate_sentence():
    template = random.choice(templates)
    return template.format(
        adj=random.choice(words["adj"]),
        noun=random.choice(words["noun"]),
        verb=random.choice(words["verb"])
    )

print(generate_sentence())