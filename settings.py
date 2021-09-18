import os

EMAIL_ADDRESS = os.environ.get('EMAIL')
EMAIL_PASSWORD = os.environ.get('PSQL')
EMAIL_AUTH = os.environ.get('LUCJAN')
EMAIL_TO = os.environ.get('EMAIL_TO')
IP = os.environ.get('IP_SERVER')
IMAP_SERVER = 'imap.gmail.com'

SENSORS = ['BOILER', 'BOILERS_RETURN', 'FEEDER', ' ', ' ', 'CWU', ' ', ' ', 'CO', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

SLEEP_TIME = 15