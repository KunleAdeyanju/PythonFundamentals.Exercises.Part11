from enum import Enum

class Alive_status(Enum):
    alive = 1
    deceased = 0

class Person():
    def __init__(self, first_name, last_name, dob, status: Alive_status):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.status =  status

    def update_first_name(self, name: str):
        self.first_name = name

    def update_last_name(self, name: str):
        self.last_name = name

    def update_dob(self, dob):
        self.dob = dob
    
    def update_status(self, status):
        self.status = status



        
        
       
