from email.message import EmailMessage
from email_messages import MESSAGESS_BOILER, MESSAGESS_FEDDER

from imap_tools import AND
from imap_tools import MailBox

from settings import EMAIL_TO, SENSORS
from server_resp import json_data_validator


import smtplib

class EmailAddress:
    def __init__(self, address, password):
        self.address = address
        self.password = password
    
    def message(self, message:str, subject:str):
        """[summary]
        Function is creating EmailMessage object

        Args:
            message ([str]): [description]
            subject ([str]): [description]

        Returns:
            [EmailMessage object]: [returns email message object with subject and content ]
        """
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.address
        msg['To'] = EMAIL_TO

        msg.set_content(message)

        return msg

    def send_email(self,content:EmailMessage):
        """[summary]
        Function is logging in to goole email address and sending and email

        Args:
            content ([EmailMessage object]): [content for send to user]
        """

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(self.address, self.password)

            smtp.send_message(content)

    def content_and_subject_to_send(self, b_temp:int, f_temp:int, temps:str):
        """[summary]
        Function is creating content, subject and sending an email to user 

        Args:
            b_temp ([int]): [boiler temp]
            f_temp ([int]): [feeder temp]
            temps ([str]): [rest of temeratures]
        """
        subject_1 = f'{SENSORS[0]} {MESSAGESS_BOILER[b_temp]}'
        subject_2 = f'{SENSORS[2]} {MESSAGESS_FEDDER[f_temp]}'

        subject = f'{subject_1} - {subject_2}'
        content = f'{temps}'

        print(f'subject {subject}')
        msg = self.message(content, subject)

        self.send_email(msg)
