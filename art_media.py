import random

art_media_list = ["Cement", "Concrete", "Mortar", "Cob", "Glass", "Metal", "Stone", "Brick", "Wood", "Bone china",
                  "Clay", "Glaze", "Porcelain", "Pottery", "Terracotta", "Acrylic paint", "Chalk", "Charcoal", "Conté",
                  "Crayon", "Gouache", "Graphite", "Ink", "Oil paint", "Glass paint", "Pastel", "Pixel", "Sketch",
                  "Tempera", "Watercolor", "Glitter", "Canvas", "Card stock", "Concrete", "Fabric", "Glass",
                  "Human body", "Metal", "Paper", "Plaster", "Scratchboard", "Stone", "Vellum", "Wood", "Brush",
                  "Pen", "Ballpoint pen", "Fountain pen", "Gel pen", "Technical pen", "Marker", "Pencil",
                  "Mechanical pencil", "Colored pencil", "Stylus", "Charcoal", "Animation", "Cel animation",
                  "Computer animation", "Cutout animation", "Drawn-on-film animation", "Stop motion", "Live action",
                  "Puppet film", "Video art", "Single-channel video", "Video installation", "Glassblowing",
                  "Card stock", "Ruled Paper", "Vellum", "VHS", "Acrylic paint", "Blacklight paint", "Encaustic paint",
                  "Fresco", "Gesso", "Glaze", "Gouache", "Ink", "Latex paint", "Oil paint", "Primer", "Ink wash ",
                  "Tempera", "Vinyl paint ", "Vitreous enamel", "Watercolor", "Black and white", "Action painting",
                  "Aerosol paint", "Airbrush", "Batik", "Brush", "Cloth", "Palette knife", "Sponge", "Pencil",
                  "LED Screen"]


def get_art_media(number=1):
    am_string = ""
    while number > 0:
        am_string = am_string + "in " + random.choice(art_media_list) + ", "
        number -= 1
    return am_string

