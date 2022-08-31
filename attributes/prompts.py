import random

prompt_list = ["Donald Trump on a bike", "Keanu Reeves writing a letter", "Sunflowers in the rain", "Huge soccer match"]


def get_prompt(number=1):
    prompt_string = ""
    while number > 0:
        prompt_string = prompt_string + "\"" + random.choice(prompt_list) + "\", "
        number -= 1
    return prompt_string
