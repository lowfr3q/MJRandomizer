import random

camera_list = ["super-resolution", "microscopy", "microscopy", "macro lens", "pinhole lens", "first person view",
               "wide angle lens", "ultra-wide angle lens", "telephoto lens", "panorama 360", "panorama",
               "tilt-shift lens", "telescope view", "drone view", "aerial",  "from above", "satellite imagery",
               "blurry", "bokeh", "ICM", "long exposure", "motion blur", "soft focus", "8mm lens", "35mm lens",
               "50mm lens", "80mm lens", "200mm lens", "500mm lens"]


def get_camera():
    return random.choice(camera_list)
