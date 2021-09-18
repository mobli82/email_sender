from server_exceptions import ServerExceptions
from settings import IP, SENSORS

import requests

def server_response():
    """[summary]
    
    Function is monitoring Arduino's server with temparatures sensors.

    Returns:
        [json data type]: [boiler's tempartures in json data type]
    """
    data = requests.get(f'{IP}/t.json')
    
    json_data = data.json()

    if data.status_code == 200 and json_data is not None:
        return json_data
    
    else:
        print(f'Server does not response !!!')
        return server_response()

def json_data_validator():
    """[summary]

    Filtering jason data, to specify a boiler and feeder temps also bolier's status with all temperatures 

    Returns:
        [boiler_and_feeder_temps]: dict with boiler and feeder temp
        [boiler_ststus]: f-string with all bolier's sensors
    """
    json_data = server_response()

    boiler_status = ''

    boiler_and_feeder_temps = {}
    
    # YOU CAN USE ZIP FUNCTION !!!!
    for index, data in enumerate(json_data['thermos']):
        if data['t'] == 0.0:
            continue
        else:
            boiler_and_feeder_temps[SENSORS[index]] = data['t']
            boiler_status += f'{SENSORS[index]}: {data["t"]} \n'
        
    return boiler_status, boiler_and_feeder_temps
