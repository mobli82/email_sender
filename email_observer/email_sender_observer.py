from settings import SENSORS, SLEEP_TIME, EMAIL_ADDRESS, EMAIL_TO

class EmailSender:
    def __init__(self):
        self.emails = set()
    
    def add_email(self, email):
        """
        Function is registering an email adress
        
        Keyword arguments:

        email: is an object with email addres to send
        
        """
        
        self.emails.add(email)

    def del_email(self, email):
        """
        Function is deleting an email adress
        
        Keyword arguments:

        Args:
            email ([EmailAddress object]): is an object with email addres to send
        
        """
        if email not in self.emails:
            return None

        self.emails.remove(email)
    
    def dispach_message(self, b_temp:int, f_temp:int, temps:str):
        """[summary]
        Function is bulk dispachting message for all emails 
        
        Args:
            b_temp ([int]): [boiler temperature]
            f_temp ([int]): [feedder temperature]
            temps ([str]): [all boiler's tempertures]
        """

        for address in self.emails:
            address.content_and_subject_to_send(b_temp, f_temp, temps)
    
