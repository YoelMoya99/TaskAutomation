import json

class Config:

    def __init__(self):
        self.file_name = '.local_config.json'
        self.width = 3
        self.number_size = 12
        self.something_else = 11

    def update_values(self):

        with open(self.file_name, 'w', encoding = 'utf-8') as file:


