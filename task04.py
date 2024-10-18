def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args,contacts):
    if len(args) == 2:
        name, phone = args
        contacts [name] = phone
        return "Contact added"
    return "Error: Command should be in the format add [name] [phone]"

def change_contact(args, contacts):
    if len (args) == 2:
        name, phone = args
        if name in contacts:
            contacts [name] = phone
            return "Contact updated"
        return "Error: Contact not found"
    return"Error: Command should be in the format 'change [name] [new phone]'."
        
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return f"{name}: {contacts[name]}"
        return "Error:contact not found "
    return "Error: Command should be in the format'contacts[name]'."

def show_all(contacts):
    if contacts:
         return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "No contacts available."
def main():
    contacts = {}
    print("Welcome to the assistant bot!") 
    while True :
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close" ,"exit"]:
            print("Good buy!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print (show_all(contacts))
        else:
            print("Invalid command")
            if __name__ == "__ main __":
                main()









