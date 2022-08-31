import random

aspect_ratio_list = ["235:100", "255:100", "21:9", "2:1", "185:100", "166:100", "175:100",
                     "16:9", "14:9", "133:100", "4:3", "1:1", "9:16", "5:4", "4:3", "3:2", "3:1"]


def get_aspect_ratio():
    return "--ar " + random.choice(aspect_ratio_list) + " "
