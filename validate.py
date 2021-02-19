#!/usr/bin/env python

import os
import json
import requests
import markdown
import PIL.Image


def error(message):
    print('-' * 50)
    print('ERROR')
    print(message)
    print('-' * 50)
    raise(message)
    

def get_material_icon_names():
    
    ret = []

    target_url = 'https://raw.githubusercontent.com/google/material-design-icons/master/update/current_versions.json'
    response = requests.get(target_url)
    data = response.text
    icons_raw = json.loads(data)
    for i in icons_raw:
        icon_name = i.split('::')[1]
        ret.append(icon_name)

    return ret


def validate_transition(transition, known_statuses, output_dir, working_dir, default_image):

    _from = transition["from"]
    _to = transition["to"]
    _id = transition["id"]
    _name = transition["name"]
    _readme = _id + '.md'
    _image = _id + '.png'

    if _from not in ['New', 'Deleted']:
        if _from not in known_statuses:
            error('unnknown from status used in transtion: ' + _from )

    if _to not in ['New', 'Deleted']:
        if _to not in known_statuses:
            error('unnknown to status used in transtion: ' + _to )

    # validate that transition readme file exists
    if not os.path.exists( os.path.join(working_dir, _readme) ):
        error('Readme file not found for the transition: ' + _from + ' - ' + _to )

    # render markdown html
    from_markdown = os.path.join(working_dir, _readme)
    to_html = os.path.join(output_dir, os.path.splitext(_readme)[0] + '.html')
    markdown.markdownFromFile(
        input=from_markdown,
        output=to_html,
        encoding='utf8',
    )

    # make sure all images within the object have the same size    
    transition_image = PIL.Image.open( os.path.join(working_dir, _image) )
    img_width, img_height = transition_image.size    
    if transition_image.size != default_image.size:
        error('Different image sizes wihin the same object')


def validate_status(status, output_dir, working_dir, default_image):
    
    # validate that status readme file exists
    status_readme_file = status['id'] + '.md'
    if not os.path.exists( os.path.join(working_dir, status_readme_file) ):
        error('Status readme file not found: ' + status_readme_file )

    # render markdown html
    from_markdown = os.path.join(working_dir, status_readme_file)
    to_html = os.path.join(output_dir, os.path.splitext(status_readme_file)[0] + '.html')
    markdown.markdownFromFile(
        input=from_markdown,
        output=to_html,
        encoding='utf8',
    )

    # validate that image exists
    image = status['id'] + '.png'
    if not os.path.exists( os.path.join(working_dir, image) ):
        error('image not found: ' + image)

    # make sure all images within the object have the same size    
    status_image = PIL.Image.open( os.path.join(working_dir, image) )
    img_width, img_height = status_image.size
    if status_image.size != default_image.size:
        error('Different image sizes wihin the same object')


def validate_object(obj_file):
    
    working_dir = os.path.split(obj_file)[0]
    print(' ' * 8 + working_dir)

    with open(obj_file) as f:
        object = json.load(f)

    # validate and render object readme
    object_readme_file = 'object.md'
    if not os.path.exists( os.path.join(working_dir, object_readme_file) ):
        error('Object readme file not found')

    with open(os.path.join(working_dir, object_readme_file), 'r') as m:
        description_html = markdown.markdown(m.read())

    # reading default image
    default_image_file = object['image']
    default_image = PIL.Image.open( os.path.join(working_dir, default_image_file) )

    output_dir = os.path.join(working_dir, 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    known_statuses = []

    # validate each status
    for status in object['statuses']:
        known_statuses.append(status['name'])
        validate_status(status, output_dir, working_dir, default_image)

    # validate each transition
    for transition in object['transitions']:
        validate_transition(transition, known_statuses, output_dir, working_dir, default_image)

def main():

    icons = get_material_icon_names()

    print('validating modules...')

    with open('./modules.json') as f:
        data = json.load(f)

    counter = 1
    modules = data["modules"]
    for module_name in modules:

        m = modules[module_name]

        print('{counter}. {name}'.format(
            counter=counter,
            name=module_name
            ))

        print('    icons   ...', end='')
        icon = m['icon']
        if not icon in icons:
            error('Unknown icon: ' + icon)
        print(' ok')

        print('    objects ...', end='')
        if 'objects' in m:
            print(' ')
            for o in m['objects']:
                validate_object(o)
        else:
            print(' -')

        counter += 1

main()

