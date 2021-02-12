#!/usr/bin/env python

import os
import json
import requests
import PIL.Image

areas_validation_html = '''
<html>
<head>
<style>

a:link {
  color: white;
}

.area {
    display:block;
    opacity:0;
    position:absolute;
    background-color: blue;
    text-align: center;
}
.area:hover {
    opacity:0.5;
}

</style>
</head>

<body>

<div class="image">
    <!-- 
        <a class="area" style="left:0px; top: 0px; height:100px; width:320px;" href="#">area 1</a>
        <a class="area" style="left:320px; top: 0px; height:50px; width:320px;" href="#">area 2</a>
        <img src="default.png" width="1000">
    -->
    VALIDATION_HTML_GOES_HERE
</div>

</body>
</html>
'''


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


def validate_object(obj_file):
    
    working_dir = os.path.split(obj_file)[0]
    print(' ' * 8 + working_dir)

    with open(obj_file) as f:
        data = json.load(f)

    default_image_file = data['default_image']

    # validate that default_image exists
    if not os.path.exists( os.path.join(working_dir, default_image_file) ):
        error('Default image not found')

    default_image = PIL.Image.open( os.path.join(working_dir, default_image_file) )

    # validate that object readme file exists
    object_readme_file = data['readme']
    if not os.path.exists( os.path.join(working_dir, object_readme_file) ):
        error('Object readme file not found')

    validation_html = ''

    # validate each status
    for status_name in data['statuses']:
        status = data['statuses'][status_name]

        # validate that status readme file exists
        status_readme_file = status['readme']
        if not os.path.exists( os.path.join(working_dir, status_readme_file) ):
            error('Status readme file not found :' + status_name )

        image = status['image']
        if not os.path.exists( os.path.join(working_dir, image) ):
            error('image not found: ' + image)

        status_image = PIL.Image.open( os.path.join(working_dir, image) )
        if status_image.size != default_image.size:
            error('Different image sizes wihin the same object')

        img_width, img_height = status_image.size

        width = float(status['width'])
        if width < 0 or width > 100:
            error('invalid width: ' + width)

        height = float(status['height'])
        if height < 0 or height > 100:
            error('invalid height: ' + height)

        left = float(status['left'])
        if left < 0 or left > 100:
            error('invalid left: ' + left)

        top = float(status['top'])
        if top < 0 or top > 100:
            error('invalid top: ' + top)

        validation_html += '<a class="area" style="left:{LEFT_PX}px; top:{TOP_PX}px; height:{HEIGHT_PX}px; width:{WIDTH_PX}px;" href="#{AREA_NAME}">{AREA_NAME}</a>\n'.format(
            LEFT_PX = int(left / 100.0 * img_width),
            TOP_PX = int(top / 100.0 * img_height),
            HEIGHT_PX = int(height / 100.0 * img_height),
            WIDTH_PX = int(width / 100.0 * img_width),
            AREA_NAME = status_name
        )

    validation_html += '<img src="{IMAGE_FILE}" width="{IMAGE_WIDTH}">\n'.format(
        IMAGE_FILE = default_image_file,
        IMAGE_WIDTH = img_width
        )

    with open( os.path.join(working_dir, 'validation.html'), "w") as validation_out:
        validation_out.write(
            areas_validation_html.replace( 'VALIDATION_HTML_GOES_HERE', validation_html )
            )


def main():

    icons = get_material_icon_names()

    print('validating modules...')

    with open('./workflows.json') as f:
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

