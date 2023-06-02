####------------------------------- Light Automation System --------------------------

def turn_off(device):
    if not isinstance(device, list):
        return device.turn_off()
    else:
        return [i.turn_off() for i in device]

def turn_on(device):
    if not isinstance(device, list):
        return device.turn_on()
    else:
        return [i.turn_on() for i in device]

def brightness(device, input):
    import math
    if '10' in input:
        change_brightness(device, 25)
    elif '20' in input:
        change_brightness(device, 50)
    elif '30' in input:
        change_brightness(device, 75)
    elif '40' in input:
        change_brightness(device, 100)
    elif '50' in input:
        change_brightness(device, 125)
    elif '60' in input:
        change_brightness(device, 150)
    elif '70' in input:
        change_brightness(device, 175)
    elif '80' in input:
        change_brightness(device, 200)
    elif '90' in input:
        change_brightness(device, 225)
    elif '100' in input or 'full' in input:
        change_brightness(device, 255)
    elif 'dim' in input:
        no = get_brightness(device)
        level = math.floor(int(no[0])/10)    
        change_brightness(device, level)
    else:
        return "sorry, i don't know that setting"

def change_brightness(device, input):
    if not isinstance(device, list):
        return device.set_brightness((input))
    else:
        return [i.set_brightness((input)) for i in device]

def get_brightness(device):
    if not isinstance(device, list):
        return device.brightness()
    else:
        return [i.brightness() for i in device]

def change_color(device, r, g, b):
    h, s, v = rgb_to_hsv(r, g, b)
    change_color_from_hsv(device, h, s, v)

def rgb_to_hsv(r, g, b):
    # Reference: https://www.w3resource.com/python-exercises/math/python-math-exercise-77.php
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    h = 0
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v

def change_color_from_hsv(device, h, s, v):
    if not isinstance(device, list):
        return device.set_color((h, s, v))
    else:
        return [i.set_color((h, s, v)) for i in device]

def color(device,input):
    if 'red' in input:
        change_color(device, 255, 0, 0)
    elif 'white' in input:
        change_color(device, 255, 255, 255)
    elif 'blue' in input:
        change_color(device, 0, 0, 255)
    elif 'green' in input:
        change_color(device, 0, 255, 0)
    elif 'black' in input:
        change_color(device, 0, 0, 0)
    elif 'warm' in input:
        change_color(device, 255,222,173)
    elif 'maroon' in input:
        change_color(device, 128,0,0)
    elif 'brown' in input:
        change_color(device, 165,42,42)
    elif 'gold' in input:
        change_color(device, 255,215,0)
    elif 'yellow' in input:
        change_color(device, 255,255,0)
    elif 'cyan' in input:
        change_color(device, 0,255,255)
    elif 'indigo' in input:
        change_color(device, 75,0,130)
    elif 'sky' in input:
        change_color(device, 135,206,235)
    elif 'purple' in input:
        change_color(device, 128,0,128)
    elif 'pink' in input:
        change_color(device, 255,192,203)
    elif 'violet' in input:
        change_color(device, 238,130,238)
    elif 'alice' in input:
        change_color(device, 240,248,255)
    elif 'peach' in input:
        change_color(device, 255,218,185)
    elif 'magenta' in input:
        change_color(device, 255,0,255)
    elif 'teal' in input:
        change_color(device, 0,128,128)
    else:
        return "sorry, i don't know that color"
    
####-------------------------------------- END ---------------------------------------