from pathlib import Path
from colorama import Fore, Style
import sys

def print_folder(folder_path: str, level=0):
    p = Path(folder_path)

    if not p.exists():
        print(f"Path '{folder_path}' does not exist.")
        return

    for x in p.iterdir():
        indent = " " * (level * 4)  
        if x.is_dir():
            print(Fore.YELLOW + indent + f"[DIR] {x.name}" + Style.RESET_ALL)
            
            print_folder(x, level + 1)
        else:
            print(Fore.BLUE + indent + f"[FILE] {x.name}" + Style.RESET_ALL)

if __name__ == "__main__":
    
    if len(sys.argv) <= 1:
        print("No directory path provided.")
    else:
        folder_path = sys.argv[1]
        print_folder(folder_path)