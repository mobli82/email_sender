#!/usr/bin/python3

from email_observer.email_address import EmailAddress
from email_observer.email_sender_observer import EmailSender

from settings import EMAIL_ADDRESS, EMAIL_AUTH, SLEEP_TIME

from utils import check_temparatures, read_email

import time


def run():

    my_email = EmailAddress(EMAIL_ADDRESS, EMAIL_AUTH)

    emails_box = EmailSender()

    emails_box.add_email(my_email)

    while True:
        IS_EMAIL_TO_SEND_FLAG = read_email()

        boiler_temp, feeder_temp, temperatures = check_temparatures()

        if boiler_temp >= 60 or feeder_temp >= 40 or IS_EMAIL_TO_SEND_FLAG == True:
            emails_box.dispach_message(boiler_temp, feeder_temp, temperatures)
            
    
        time.sleep(SLEEP_TIME)

        


if __name__ == '__main__':
    run()