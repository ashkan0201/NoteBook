# CB: ASHKAN

# Add the desired library.
import json5

# This class maintains a series of required values.
class NOTE:
    def __init__(self):
        self.ID = None
        self.TITLE = None
        self.COMMENT = None
        self.DEMO = {"Users":[]}

"""
Using the previous class, 
this class performs the main tasks such as creating a json file and generating an ID, 
getting the title and comma, and saving information in the json file.
"""
class REPOSITORY:
    def __init__(self):
        self.Note = NOTE()
        # The location of the address of the json file.
        self.Json_File = "NoteBook.json"
        self.Json_Data = None
        self.Json_Dict = None

    # Creating the create function to create a value in json.
    def CREATE(self):
        with open(self.Json_File, mode = "w") as DATA:
            json5.dump(self.Note.DEMO, DATA)

    # Creating the get_id tab to get each person's ID.
    def GET_ID(self):
        with open(self.Json_File, mode = "r") as DATA:
            LEN_DICT = json5.load(DATA)
            self.Note.ID = len(LEN_DICT["Users"])