def car_profile(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return(car_info)

car_spec = car_profile(
    'audi', 'fast one',
    colour = 'blue',
    speed = 'fast',
    wheels = 4,
    )

print(car_spec)