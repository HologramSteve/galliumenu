## GalliuMenu
GalliuMenu, an extremely simple menu system for (future) my CLI tools.
It loads all files from the "modules" folder. And provides a neat menu choosing the menu's options.
Every module can provide some details, like the name, author, etc.
___
### Module layout
The script reads from the `Main` class.
The `Main` class must contain these properties:

- `name`: the module's name
- `author`: the module's author.
- `version`: the module's version
- `functions`: an array of the `Function` class, described below.
#### The `Function` class:
The `Function` class must contain the following properties:

- `name`: the function's name
- `description`: the function's description
-  `executefunc`: A python function which will be ran when the menu executes the `Function`.

**Here is a full example of a module file:**
```python
def nothing_func():
    print("Nothing.")


class Function:
    def __init__(self, name, desc, executefunc):
        self.name = name
        self.description = desc
        self.executefunc = executefunc

class Main:
    def __init__(self):
        self.name = "Nothingness"
        self.author = "Nobody"
        self.functions = [Function("nothing", "Does nothing.", nothing_func)]
        self.version = "1.0"
```
This will look like this in GalliuMenu:
```bash
GalliuMenu
----------------
Nothingness by Nobody
Version 1.0
----------------
Commands:
[1] nothing 'Does nothing.'
```

### License
> This project is licensed under the "IDGAF" license. Do whatever you
> want, but if you make something cool, I'd appreciate if you'd lmk on
> discord (`@hologramsteve`).

Thanks.
