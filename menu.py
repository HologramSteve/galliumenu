print("[*] Loading menu...")

# More imports
import os
import importlib

def reset():
    os.system("cls")

def loadModules():
    modules = []

    raw = os.listdir("modules")
    for module in raw:
        module_name = module[:-3]
        if not module.endswith(".py"):
            print("[!] Warning: invalid file detected")
            continue


        try:
            module = importlib.import_module("modules." + module_name)
        except:
            print(f"[-] Error loading module '{module}'")
            continue

        if hasattr(module, 'Main'):
            main_class = getattr(module, 'Main')
            modules.append(main_class)
        else:
            print(f"[!] Warning: module {module_name} misses the Main class.")

    return modules

ans = input("[*] Do you want to load modules in the 'module' folder? Never trust random files! (y/n)\n> ")

if ans.lower() == "y":
    modules = loadModules()
    print(f"[+] Loaded {len(modules)} modules")
else:
    modules = []

def renderMenu():
    print("GalliuMenu\n----------------")
    i = 0
    command_list = []
    for module_raw in modules:
        try:
            module = module_raw()
        except:
            print(f"[x] Error loading a module")
            continue
        print(f"{module.name} by {module.author}\nVersion {module.version}\n----------------\nCommands:")
        msg = ""
        for func_raw in module.functions:
            func = func_raw.__dict__
            i += 1
            msg = msg + f"[{i}] {func['name']} '{func['description']}'\n"
            command_list.append(func['executefunc'])
        print(msg)
    return command_list

# Main
def main(): 	
    command_list = renderMenu()
    if len(command_list) == 0:
        print("[x] No commands loaded, exiting...")
        return
    ans = int(input("> "))
    print(f"[*] Executing function {ans}")
    if ans > len(command_list):
        print("[-] Invalid command id")
    else:
       try:
           command_list[ans - 1]()
       except (e):
        print("[!] Error executing!")
    input()
    reset()
    main()
    
main()