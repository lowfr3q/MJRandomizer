import PySimpleGUI as sg

import art_media
import artist
import aspect_ratio
import camera
import descriptors
import lighting
import prompts

form = sg.FlexForm('Midjourney Randomizer')
layout = [
    [sg.Text('Select the attributes you would like to randomize', size=(35, 1))],
    [sg.Checkbox("prompt: ", default=True, k="include-prompt"),
     sg.Combo(prompts.prompt_list, k="prompt-text"),
     sg.InputText(size=5, k="prompt-count")],
    [sg.Checkbox("artist: ", default=True, k="include-artist"),
     sg.Combo(artist.artist_list, k="artist-text"),
     sg.InputText(size=5, k="artist-count")],
    [sg.Checkbox("art media: ", default=True, k="include-am"),
     sg.Combo(art_media.art_media_list, k="am-text"),
     sg.InputText(size=5, k="am-count")],
    [sg.Checkbox("aspect ratio: ", default=True, k="include-ar"),
     sg.Combo(aspect_ratio.aspect_ratio_list, k="ar-text")],
    [sg.Checkbox("camera: ", default=True, k="include-camera"),
     sg.Combo(camera.camera_list, k="camera-text")],
    [sg.Checkbox("lighting: ", default=True, k="include-lighting"),
     sg.Combo(camera.camera_list, k="lighting-text"), sg.InputText(size=5, k="lighting-count")],
    [sg.Checkbox("descriptors: ", default=True, k="include-descriptor"),
     sg.Combo(descriptors.descriptors_list, k="descriptor-text"), sg.InputText(size=5, k="descriptor-count")],
    [sg.Checkbox("test: ", default=False, k="include-test")],
    [sg.Checkbox("testp: ", default=False, k="include-testp")],
    [sg.Button("Randomize Prompt")],
    [sg.Multiline(size=(45, 5), key='output')]
]
window = sg.Window('Midjourney Randomizer', layout, size=(600, 600))
event, values = window.read()
while True:
    event, values = window.read()
    # Prompt Section
    include_prompt = values['include-prompt']
    prompt_text = values['prompt-text']
    prompt_count = values['prompt-count']
    if bool(include_prompt) & (prompt_text != ""):
        prompt_text = "\"" + values['prompt-text'] + "\", "
    elif bool(include_prompt):
        if prompt_count != "":
            prompt_text = prompts.get_prompt(int(artist_count))
        else:
            prompt_text = prompts.get_prompt()
    # Artist Section
    include_artist = values['include-artist']
    artist_text = values['artist-text']
    artist_count = values['artist-count']
    if bool(include_artist) & (artist_text != ""):
        artist_text = "by " + values['artist-text'] + ", "
    elif bool(include_artist):
        if artist_count != "":
            artist_text = artist.get_artist(int(artist_count))
        else:
            artist_text = artist.get_artist()
    # Art Media Section
    include_am = values['include-am']
    am_text = values['am-text']
    am_count = values['am-count']
    if bool(include_am) & (am_text != ""):
        am_text = "by " + values['am-text'] + ", "
    elif bool(include_am):
        if am_count != "":
            am_text = art_media.get_art_media(int(am_count))
        else:
            am_text = art_media.get_art_media()
    # Camera Section
    include_camera = values['include-camera']
    camera_text = values['camera-text']
    if bool(include_camera) & (camera_text != ""):
        camera_text = "::" + values['camera-text'] + "::, "
    elif bool(include_camera):
        camera_text = camera.get_camera()
    # Lighting Section
    include_lighting = values['include-lighting']
    lighting_text = values['lighting-text']
    if bool(include_lighting) & (lighting_text != ""):
        lighting_text = "::" + values['lighting-text'] + "::, "
    elif bool(include_lighting):
        lighting_text = lighting.get_lighting()
    # Aspect Ratio Section
    include_ar = values['include-ar']
    ar_text = values['ar-text']
    if bool(include_ar) & (ar_text != ""):
        ar_text = "ar " + values['ar-text']
    elif bool(include_ar):
        ar_text = aspect_ratio.get_aspect_ratio()
    # Descriptor Section
    include_descriptor = values['include-descriptor']
    descriptor_text = values['descriptor-text']
    descriptor_count = values['descriptor-count']
    if bool(include_descriptor) & (descriptor_text != ""):
        descriptor_text = values['descriptor-text'] + ", "
    elif bool(include_descriptor):
        if descriptor_count != "":
            descriptor_text = descriptors.get_descriptors(int(descriptor_count))
        else:
            descriptor_text = descriptors.get_descriptors()
    # test Section
    include_test = values['include-test']
    # testp Section
    include_testp = values['include-testp']


    prompt = ""
    if include_prompt:
        prompt = prompt + prompt_text
    if include_artist:
        prompt = prompt + artist_text
    if include_am:
        prompt = prompt + am_text
    if include_camera:
        prompt = prompt + camera_text
    if include_lighting:
        prompt = prompt + lighting_text
    if include_descriptor:
        prompt = prompt + descriptor_text
    if include_ar:
        prompt = prompt + ar_text
    if include_test:
        prompt = prompt + "--test"
    if include_testp:
        prompt = prompt + "--testp"

    # prompt = "/imagine prompt: " + prompt
    window['output'].update(value=prompt)

    if event == sg.WIN_CLOSED or event == 'Bye!':
        break
