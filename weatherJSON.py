a={
    'request': {
        'type': 'City', 
        'query': 'Kolkata, India', 
        'language': 'en', 
        'unit': 'm'
    }, 
    'location': {
        'name': 'Kolkata', 
        'country': 'India', 
        'region': 'West Bengal', 
        'lat': '22.570', 
        'lon': '88.370', 
        'timezone_id': 'Asia/Kolkata', 
        'localtime': '2022-09-08 08:50', 
        'localtime_epoch': 1662627000, 
        'utc_offset': '5.50'
    }, 
    'current': {
        'observation_time': '03:20 AM', 
        'temperature': 31, 
        'weather_code': 143, 
        'weather_icons': ['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0006_mist.png'], 'weather_descriptions': ['Haze'], 
        'wind_speed': 9, 
        'wind_degree': 130, 
        'wind_dir': 'SE', 
        'pressure': 1008, 
        'precip': 0, 
        'humidity': 71, 
        'cloudcover': 50, 
        'feelslike': 38, 
        'uv_index': 7, 
        'visibility': 4, 
        'is_day': 'yes'
    }
} 

imp={
    'location':['name','country','region','localtime'],
    'current':['observation_time','weather_code','weather_descriptions',
               'wind_speed','humidity','feelslike','uv_index','is_day']
}
