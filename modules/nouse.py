def run_func():
    print("runnn!")




class Function:
    def __init__(self, name, desc, executefunc):
        self.name = name
        self.description = desc
        self.executefunc = executefunc

    def execute(self):
        self.executefunc()

class Main:
    def __init__(self):
        self.name = ""
        self.author = ""
        self.functions = [Function("run", "run stuff", run_func)]
        self.version = ""

    def execute(self, function):
        if function == "run":
            print("run!!")