def print_dict_elements(dct):
    for key, value in dct.items():
        print(f'Rocket: {key}, Description: {value}')
        

rocket_info = {
    'falcon 1': 'First privately developed liquid-fueled rocket',
    'atlas V': 'Launch vehicle for Mars Rovers',
    'Saturn V': 'Rocket that took humans to hte moon',
    'Space Shuttle': 'First reusable spacecraft'
}


print_dict_elements(rocket_info)