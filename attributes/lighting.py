import random

lighting_list= ["bright lighting", "campfire lighting", "candlelight", "cinematic lighting", "colorful lighting",
                "contre-jour lighting", "dark lighting", "dramatic lighting", "early morning lighting",
                "film noir lighting", "golden hour sunlight", "hard lighting", "moody lighting", "night lighting",
                "realistic lighting", "soft lighting", "studio lighting", "sunset lighting", "volumetric lighting",
                "backlight", "bioluminescence", "black light bulb", "candle light", "christmas lights",
                "crepuscular rays", "daylight", "edison bulb", "fire light", "floodlight", "fluorescent bulb",
                "glow in the dark light", "glow stick", "glowing light", "halfrear lighting", "infrared light",
                "lantern light", "laser light", "LED lights", "lens flare", "light rays", "natural lighting",
                "neon bulb", "nixie tube bulb", "plasma globe", "silhouette lighting", "spotlight", "sunlight",
                "vacuum tube bulb", "x-ray"]


def get_lighting(number=1):
    lighting_string = ""
    while number > 0:
        lighting_string = lighting_string + random.choice(lighting_list)
        number -= 1
    return lighting_string
