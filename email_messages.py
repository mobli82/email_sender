from server_resp import json_data_validator
from settings import SENSORS

MESSAGESS_BOILER = {
    20: 'COLD ',
    30: 'TEMPERATORA OK ',
    40: 'TEMPERATURA OK ',
    50: 'TEMPERATURA OK ',
    60: 'TEMPERATURA HIGH',
    70: 'TEMPERATURA CRITICAL ',
    80: 'OVERHEATED !!!! ',
}

MESSAGESS_FEDDER = {
    10: 'COLD ',
    20: 'COLD ',
    30: 'TEMPERATORA HIGH ',
    40: 'TEMPERATURA CRITICAL ',
    50: 'OVERHEATED ',
}