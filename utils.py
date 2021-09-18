from settings import SENSORS

from email.message import EmailMessage
import smtplib
from server_resp import json_data_validator

from imap_tools import AND
from imap_tools import MailBox
from settings import EMAIL_ADDRESS
from settings import EMAIL_AUTH
from settings import EMAIL_TO
from settings import IMAP_SERVER

def check_temparatures():
    """[summary]
    Function is checking boilers temperatures 
    
    Returns:
        temp_boiler:int [returns boiler temperature]
        temp_feeder:int [returns feeder temperature]
        temperatures:int [returns CWU and RETURN temperatures]

    """
    boiler, feeder = SENSORS[0], SENSORS[2]
    temperatures, temp_range = json_data_validator()

    temp_boiler = int(str(temp_range[boiler])[0]) * 10
    temp_feeder = int(str(temp_range[feeder])[0]) * 10
    
    # print(f'boiler temp {temp_boiler} feeder temp {temp_feeder}')
    return temp_boiler, temp_feeder, temperatures

def read_email():
    """[summary]
    Function is changing FLAG status to TRUE when user send an email with subject == Status
    (mapping INBOX folder)

    Returns:
        FLAG:bool -> []
    """
    FLAG = False

    mb = MailBox(IMAP_SERVER).login(EMAIL_ADDRESS, EMAIL_AUTH)

    messeges = mb.fetch(criteria=AND(seen=False, from_=EMAIL_TO), 
                        mark_seen=False, 
                        bulk=True)
    
    for msg in messeges:
        if msg.from_ == EMAIL_TO and msg.subject == 'Status':
            FLAG = True
    
    mb.logout()

    return FLAG