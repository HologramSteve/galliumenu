# def real():
#     print("so real!?!?!? (what the flip)")



class Function:
    def __init__(self, name, desc, executefunc):
        self.name = name # Function name
        self.description = desc # Function description
        self.executefunc = executefunc # The function to call when running

class Main:
    def __init__(self):
        self.name = "" # Package name
        self.author = "" # The package author
        self.functions = [Function("wiudjw", "qwer", real)] # Contains function classes
        self.version = "" # Package version