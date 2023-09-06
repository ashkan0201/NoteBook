# CB: ASHKAN

# Add the desired library.
from datetime import datetime   
import json5

# This class maintains a series of required values.
class NOTE:
    def __init__(self):
        self.DEMO_ID = -1
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
        self.Json_Remove = None
        self.Json_Remove_Index = None

    # Creating the create function to create a value in json.
    def CREATE(self):
        with open(self.Json_File, mode = "w") as DATA:
            json5.dump(self.Note.DEMO, DATA)

    """
    GET_TITLE_AND_COMMENT function to get the ID created in 
    the previous function and the title and comment from the user.
    """
    def GET_TITLE_AND_COMMENT(self):
        self.Note.DEMO_ID += 1
        self.Note.TITLE = input("TITLE: ")
        self.Note.COMMENT = input("COMMENT: ")
        self.Json_Dict = {
            "ID" : self.Note.DEMO_ID,
            "TITLE" : self.Note.TITLE,
            "COMMENT" : self.Note.COMMENT,
            "REGISTRATION_TIME" :  datetime.today().ctime()
        }

        # save function to save the values ​​we got in the json file.
        def SAVE():
            with open(self.Json_File, mode = "r") as DATA:
                self.Json_Data = json5.load(DATA)
            self.Json_Data["Users"].append(self.Json_Dict)
            with open(self.Json_File, mode = "w") as DATA:
                json5.dump(self.Json_Data, DATA, indent = 4)
        return SAVE()

    # REMOVE_ITEM function to delete values ​​or all items or delete with ID
    def REMOVE_ITEM(self, WITH_ID):
        self.DEL_ITEM = None
        self.DEL_ITEM_WITH_ID = None

        with open(self.Json_File, mode = "r") as DATA:
            self.Json_Remove = json5.load(DATA)
            self.DEL_ITEM = self.Json_Remove

        # If it was without ID
        if WITH_ID == None:
            with open(self.Json_File, mode = "w") as DATA:
                json5.dump(self.Note.DEMO, DATA, indent = 4)
            return self.DEL_ITEM

        # If it was with Idi
        elif WITH_ID != None:
            LIST_OF_ID = []
            try:
                for everything in self.Json_Remove["Users"]:
                    LIST_OF_ID.append(everything["ID"])
                if WITH_ID not in LIST_OF_ID:
                    raise

                for everything in self.Json_Remove["Users"]:
                    if everything["ID"] == WITH_ID:
                        self.Json_Remove_Index = self.Json_Remove["Users"].index(everything)
                        self.DEL_ITEM_WITH_ID = self.Json_Remove["Users"].pop(self.Json_Remove_Index)
                        with open(self.Json_File, mode = "w") as DATA:
                            json5.dump(self.Json_Remove, DATA, indent = 4)
            except:
                print("This ID does not exist!")
            else:
                return self.DEL_ITEM_WITH_ID

"""
This class is for displaying two modes of data.
First mode: display all data stored in json.
The second mode: displaying json data based on the received ID.
"""
class VIEW:
    def __init__(self):
        self.Method = REPOSITORY()
        self.Input_Id = None 

    # This function shows the items in two modes, one without ID, which includes all items, and the other with ID.
    def SHOW_ALL(self, WITH_ID):
        with open(self.Method.Json_File, mode = "r") as DATA:
            SHOW = json5.load(DATA)
            
        # This function shows all the items in the json file.
        if WITH_ID == None:
            return SHOW
        
        # This function is to show the item based on ID.
        elif WITH_ID != None:
            try:
                LIST_OF_ID_V = []
                for everything in SHOW["Users"]:
                    LIST_OF_ID_V.append(everything["ID"])
                    if everything["ID"] == int(WITH_ID):
                        Result_Input = everything
                if WITH_ID not in LIST_OF_ID_V:
                    raise
            except:
                print("Your entry is either incorrect or there is no such ID!")
            else:
                return Result_Input

# NOTEBOOK class is for creating and launching functions of previous classes.
class NOTEBOOK:
    def __init__(self):
        self.REPO = REPOSITORY()
        self.VIEW = VIEW()
        self.REPO.CREATE()

    # This function causes the GET_TITLE_AND_COMMENT function to be executed.
    def ENTER_ITEM(self):
        self.REPO.GET_TITLE_AND_COMMENT()

    # This function causes a function to display all items in json.
    def GIVE_ALL_ITEM(self, WITH_ID = None):
        return self.VIEW.SHOW_ALL(WITH_ID)

    # This function executes the REMOVE_ITEM function
    def REMOVING_ITEM(self, WITH_ID = None):
        return self.REPO.REMOVE_ITEM(WITH_ID)

if __name__ == '__main__':
    FINAL = NOTEBOOK()
