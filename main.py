#!/usr/bin/env python
import os
import PySimpleGUI as sg
from attributes import artist, aspect_ratio, prompts, art_media, lighting, descriptors, camera

form = sg.FlexForm('Midjourney Randomizer')
layout = [
    [sg.Text('Select the attributes you would like to randomize', size=(40, 1)),
     sg.Checkbox("Multi-prompt?", default=True, k="include-multi-prompt"), sg.Text("     Count")],
    [sg.Checkbox("prompt:", size=15, default=True, k="include-prompt"),
     sg.InputText(size=42, k="prompt-text"), sg.InputText(size=5, k="prompt-count")],
    [sg.Checkbox("artist:", size=15, default=True, k="include-artist"),
     sg.Combo(artist.artist_list, size=40, k="artist-text"),
     sg.InputText(size=5, k="artist-count")],
    [sg.Checkbox("art media: ", size=15, default=True, k="include-am"),
     sg.Combo(art_media.art_media_list, size=40, k="am-text"),
     sg.InputText(size=5, k="am-count")],
    [sg.Checkbox("descriptors: ", size=15, default=True, k="include-descriptor"),
     sg.Combo(descriptors.descriptors_list, size=40, k="descriptor-text"), sg.InputText(size=5, k="descriptor-count")],
    [sg.Checkbox("lighting: ", size=15, default=True, k="include-lighting"),
     sg.Combo(camera.camera_list, size=40, k="lighting-text"), sg.InputText(size=5, k="lighting-count")],
    [sg.Checkbox("aspect ratio: ", size=15, default=True, k="include-ar"),
     sg.Combo(aspect_ratio.aspect_ratio_list, size=40, k="ar-text")],
    [sg.Checkbox("camera: ", size=15, default=True, k="include-camera"),
     sg.Combo(camera.camera_list, size=40, k="camera-text")],
    [sg.Checkbox("test", default=False, k="include-test")],
    [sg.Checkbox("testp", default=False, k="include-testp")],
    [sg.Button("Randomize Prompt")],
    [sg.Multiline(size=(45, 5), key='output')]
]
window = sg.Window('Midjourney Randomizer', layout, size=(600, 600))
while True:
    event, values = window.read()
    include_multi_prompt = bool(values['include-multi-prompt'])
    # Prompt Section
    include_prompt = bool(values['include-prompt'])
    prompt_text = values['prompt-text']
    prompt_count = values['prompt-count']
    if include_prompt & (prompt_text != ""):
        prompt_text = "\"" + values['prompt-text'] + "\", "
    elif include_prompt:
        if prompt_count != "":
            prompt_text = prompts.get_prompt(int(prompt_count))
        else:
            prompt_text = prompts.get_prompt()
    # Artist Section
    include_artist = bool(values['include-artist'])
    artist_text = values['artist-text']
    artist_count = values['artist-count']
    if include_artist & (artist_text != ""):
        artist_text = "by " + values['artist-text'] + ", "
    elif include_artist:
        if artist_count != "":
            artist_text = artist.get_artist(int(artist_count))
        else:
            artist_text = artist.get_artist()
    # Art Media Section
    include_am = bool(values['include-am'])
    am_text = values['am-text']
    am_count = values['am-count']
    if include_am & (am_text != ""):
        am_text = "by " + values['am-text'] + ", "
    elif include_am:
        if am_count != "":
            am_text = art_media.get_art_media(int(am_count))
        else:
            am_text = art_media.get_art_media()
    # Camera Section
    include_camera = bool(values['include-camera'])
    camera_text = values['camera-text']
    if include_camera & (camera_text != ""):
        camera_text = "::" + values['camera-text'] + "::, "
    elif include_camera & include_multi_prompt:
        camera_text = "::" + camera.get_camera() + "::, "
    elif include_camera:
        camera_text = camera.get_camera() + ", "
    # Lighting Section
    include_lighting = bool(values['include-lighting'])
    lighting_text = values['lighting-text']
    if include_lighting & (lighting_text != ""):
        lighting_text = "::" + values['lighting-text'] + "::, "
    elif include_lighting & include_multi_prompt:
        lighting_text = "::" + lighting.get_lighting() + "::, "
    elif include_lighting:
        lighting_text = lighting.get_lighting() + ", "
    # Aspect Ratio Section
    include_ar = bool(values['include-ar'])
    ar_text = values['ar-text']
    if include_ar & (ar_text != ""):
        ar_text = "ar " + values['ar-text']
    elif include_ar:
        ar_text = aspect_ratio.get_aspect_ratio()
    # Descriptor Section
    include_descriptor = bool(values['include-descriptor'])
    descriptor_text = values['descriptor-text']
    descriptor_count = values['descriptor-count']
    if include_descriptor & (descriptor_text != ""):
        descriptor_text = values['descriptor-text'] + ", "
    elif include_descriptor:
        if descriptor_count != "":
            descriptor_text = descriptors.get_descriptors(int(descriptor_count))
        else:
            descriptor_text = descriptors.get_descriptors()
    # test Section
    include_test = bool(values['include-test'])
    # testp Section
    include_testp = bool(values['include-testp'])

    prompt = ""
    if include_prompt:
        prompt = prompt + prompt_text
    if include_artist:
        prompt = prompt + artist_text
    if include_am:
        prompt = prompt + am_text
    if include_descriptor:
        prompt = prompt + descriptor_text
    if include_camera:
        prompt = prompt + camera_text
    if include_lighting:
        prompt = prompt + lighting_text
    if include_ar:
        prompt = prompt + ar_text
    if include_test:
        prompt = prompt + "--test"
    if include_testp:
        prompt = prompt + "--testp"

    print(os.getenv("OPENAI_API_KEY1"))
    prompt = prompt.strip()
    window['output'].update(value=prompt)

    if event == sg.WIN_CLOSED or event == 'Bye!':
        break
