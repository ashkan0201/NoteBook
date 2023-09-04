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

    """
    GET_TITLE_AND_COMMENT function to get the ID created in 
    the previous function and the title and comment from the user.
    """
    def GET_TITLE_AND_COMMENT(self):
        self.GET_ID()
        self.Note.TITLE = input("TITLE: ")
        self.Note.COMMENT = input("COMMENT: ")
        self.Json_Dict = {
            "ID" : self.Note.ID,
            "TITLE" : self.Note.TITLE,
            "COMMENT" : self.Note.COMMENT
        }

        # save function to save the values ​​we got in the json file.
        def SAVE():
            with open(self.Json_File, mode = "r") as DATA:
                self.Json_Data = json5.load(DATA)
            self.Json_Data["Users"].append(self.Json_Dict)
            with open(self.Json_File, mode = "w") as DATA:
                json5.dump(self.Json_Data, DATA, indent = 4)
        return SAVE()

"""
This class is for displaying two modes of data.
First mode: display all data stored in json.
The second mode: displaying json data based on the received ID.
"""
class VIEW:
    def __init__(self):
        self.Method = REPOSITORY()
        self.Input_Id = None 

    # This function shows all the items in the json file.
    def SHOW_ALL(self):
        with open(self.Method.Json_File, mode = "r") as DATA:
            SHOW = json5.load(DATA)
        return SHOW
    
    # This function is to show the item based on ID.
    def SHOW_WITH_ID(self, ID):
        with open(self.Method.Json_File,  mode = "r") as DATA:
            SHOW = json5.load(DATA)
        try:
            Result_Input = SHOW["Users"][int(ID)]
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
    def ENTER_TITLE_AND_COMMENT(self):
        self.REPO.GET_TITLE_AND_COMMENT()

    # This function causes a function to display all items in json.
    def GIVE_ALL_ITEM(self):
        return self.VIEW.SHOW_ALL()
    
    # This function causes a function to display all items in json based on ID.
    def GIVE_ITEM_WITH_ID(self, ID):
        return self.VIEW.SHOW_WITH_ID(ID)
    
if __name__ == '__main__':
    FINAL = REPOSITORY()
