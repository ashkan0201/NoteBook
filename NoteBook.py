# CB: ASHKAN

# Add the desired library.
from datetime import datetime   
import json5

# This class maintains a series of required values.
class Note:
    def __init__(self):
        self.Demo_ID = -1
        self.Title = None
        self.Comment = None
        self.Demo = {"Users":[]}

"""
Using the previous class, 
this class performs the main tasks such as creating a json file and generating an ID, 
getting the Title and comma, and saving information in the json file.
"""
class Repository:
    def __init__(self):
        self.Note = Note()
        # The location of the address of the json file.
        self.Json_File = "NoteBook.json"
        self.Json_Data = None
        self.Json_Dict = None
        self.Json_Remove = None
        self.Json_Remove_Index = None

    # Creating the Create function to Create a value in json.
    def Create(self):
        with open(self.Json_File, mode = "w") as Data:
            json5.dump(self.Note.Demo, Data)

    """
    Get_Title_And_Comment function to get the ID Created in 
    the previous function and the Title and Comment from the user.
    """
    def Get_Title_And_Comment(self):
        self.Note.Demo_ID += 1
        self.Note.Title = input("Title: ")
        self.Note.Comment = input("Comment: ")
        self.Json_Dict = {
            "ID" : self.Note.Demo_ID,
            "Title" : self.Note.Title,
            "Comment" : self.Note.Comment,
            "Registration_Time" :  datetime.today().ctime()
        }

        # Save function to Save the values ​​we got in the json file.
        def Save():
            with open(self.Json_File, mode = "r") as Data:
                self.Json_Data = json5.load(Data)
            self.Json_Data["Users"].append(self.Json_Dict)
            with open(self.Json_File, mode = "w") as Data:
                json5.dump(self.Json_Data, Data, indent = 4)
        return Save()

    # Remove_Item function to delete values ​​or all items or delete with ID
    def Remove_Item(self, With_ID):
        self.Del_Item = None
        self.Del_Item_With_ID = None

        with open(self.Json_File, mode = "r") as Data:
            self.Json_Remove = json5.load(Data)
            self.Del_Item = self.Json_Remove

        # If it was without ID
        if With_ID == None:
            with open(self.Json_File, mode = "w") as Data:
                json5.dump(self.Note.Demo, Data, indent = 4)
            return self.Del_Item

        # If it was with Idi
        elif With_ID != None:
            List_Of_ID = []
            try:
                for everything in self.Json_Remove["Users"]:
                    List_Of_ID.append(everything["ID"])
                if With_ID not in List_Of_ID:
                    raise

                for everything in self.Json_Remove["Users"]:
                    if everything["ID"] == With_ID:
                        self.Json_Remove_Index = self.Json_Remove["Users"].index(everything)
                        self.Del_Item_With_ID = self.Json_Remove["Users"].pop(self.Json_Remove_Index)
                        with open(self.Json_File, mode = "w") as Data:
                            json5.dump(self.Json_Remove, Data, indent = 4)
            except:
                print("This ID does not exist!")
            else:
                return self.Del_Item_With_ID

"""
This class is for displaying two modes of Data.
First mode: display all Data stored in json.
The second mode: displaying json Data based on the received ID.
"""
class View:
    def __init__(self):
        self.Method = Repository()
        self.Input_Id = None 

    # This function Shows the items in two modes, one without ID, which includes all items, and the other with ID.
    def Show_All(self, With_ID):
        with open(self.Method.Json_File, mode = "r") as Data:
            Show = json5.load(Data)
            
        # This function Shows all the items in the json file.
        if With_ID == None:
            return Show
        
        # This function is to Show the item based on ID.
        elif With_ID != None:
            try:
                List_Of_ID_V = []
                for everything in Show["Users"]:
                    List_Of_ID_V.append(everything["ID"])
                    if everything["ID"] == int(With_ID):
                        Result_Input = everything
                if With_ID not in List_Of_ID_V:
                    raise
            except:
                print("Your entry is either incorrect or there is no such ID!")
            else:
                return Result_Input

# NoteBook class is for creating and launching functions of previous classes.
class NoteBook:
    def __init__(self):
        self.Repo = Repository()
        self.View = View()
        self.Repo.Create()

    # This function causes the Get_Title_And_Comment function to be executed.
    def Enter_Item(self):
        self.Repo.Get_Title_And_Comment()

    # This function causes a function to display all items in json.
    def Give_Item(self, With_ID = None):
        """By giving a numerical value to With_ID, calculations can be checked based on that ID"""
        return self.View.Show_All(With_ID)

    # This function executes the Remove_Item function
    def Removing_Item(self, With_ID = None):
        """By giving a numerical value to With_ID, calculations can be checked based on that ID"""
        return self.Repo.Remove_Item(With_ID)

if __name__ == '__main__':
    Final = NoteBook()
