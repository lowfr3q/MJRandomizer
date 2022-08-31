import random

descriptors_list = ["fat", "female", "full body pose", "handsome", "male", "messy", "old", "short", "skinny", "tall",
                    "ugly", "white background", "black background", "flat background", "textured background",
                    "hazy background", "attractive", "baby", "beautiful", "child", "cute", "sphere shape", "cone shape",
                    "parallelogram shape", "rhombus shape", "trapezoid shape", "kite shape", "pentagon shape",
                    "hexagon shape", "rubik cube shape", "organic shape", "plasma", "circle shape", "semi-circle shape",
                    "oval shape", "square shape", "triangle shape", "rectangle shape", "polygonal shape", "cube shape",
                    "ice", "fire", "liquid", "fog", "wind", "storm", "flood", "rain", "organic", "Valentine's Day",
                    "Cinco De Mayo", "Diwali", "Easter", "Eid al-Fitr", "Halloween", "Hanukkah", "Independence Day",
                    "New Year", "Ramadan", "St. Patrick's Day", "Thanksgiving", "Bodhi Day", "Chinese New Year",
                    "Christmas", "spring", "summer", "autumn", "winter", "worried", "panicked", "revulsion", "sad",
                    "satanic", "scared", "sleepy", "stressed", "tired", "vengeful", "whimsical", "insulted", "lonely",
                    "mad", "mellow", "miserable", "moody", "nauseated", "nervous", "offended", "ominous", "excitement",
                    "fashion", "frustrated", "gloomy", "grateful dead", "happy", "hopeless", "horrified", "horror",
                    "infuriated", "creepy", "demonic", "depressing", "dislike", "dreamy", "dystopian", "ecstasy",
                    "elegant", "elite", "evil", "retro", "bitter", "Victorian", "vintage", "Emotions Plus", "angelic",
                    "angry", "annoyed", "anxious", "aversion", "European Renaissance", "Enlightenment",
                    "Industrial Revolution", "Age of Imperialism", "Victorian Era", "World War I", "Great Depression",
                    "World War II", "antique", "medieval", "modern", "1990s style", "Stone Age", "Bronze Age",
                    "Iron Age", "Ancient Greece", "Ancient Rome", "Persian Empire", "Byzantine Empire",
                    "Renaissance Humanism", "Protestant Reformation", "rough", "matte", "1930s style", "1950s style",
                    "1960s style", "1970s style", "1980s style", "raylectron", "sketchup", "unreal engine",
                    "vector graphic", "zbrush", "ray tracing reflections", "lumen reflections",
                    "screen space reflections", "diffraction grating", "cryengine", "houdini-render", "icon",
                    "low poly", "microsoft paint", "nintendo", "octane", "openGL", "photoshop", "Cinema 4D", "seamless",
                    "spirograph", "symmetrical", "trending on ArtStation", "Flickr", "DeviantArt", "3D Render", "atari",
                    "blender render", "luxury", "mandala", "mandelbrot", "mandelbulb", "maximum detail", "micro details",
                    "molecular", "newton fractal", "ornate pattern", "sacred geometry", "glassmorphism",
                    "gliophorus-psittacinus", "graph", "grid", "high definition", "hyperbolic", "insanely detailed",
                    "intricate", "kaleidoscope", "knotted", "bling", "camouflage", "chaotic", "chart", "complex",
                    "deep dream", "detailed", "diagram", "dreamcore", "fractal", "surreal", "synthwave", "vaporwave",
                    "depth of field", "flat", "flat shading", "minimalist", "simple", "asymetrical", "futuristic",
                    "glo-fi", "nanopunk", "psychedelic", "psychedelica", "rainbowcore", "sci-fi", "shpongle",
                    "sparklecore", "steampunk", "brutalism", "chakra", "cubism", "cyberpunk", "cyborgism",
                    "dark fantasy", "dreamlike", "forestpunk", "fractalpunk", "futurism"]


def get_descriptors(number=1):
    descriptor_string = ""
    while number > 0:
        descriptor_string = descriptor_string + random.choice(descriptors_list) + ", "
        number -= 1
    return descriptor_string
