from sanitize import sanitize_phone_number

COMMAND_EXIT = ['good bye', 'close', 'exit']
contacts_dict = [{"name": "Artem", "phone": "+380504848484"},
                 {"name": "Ira", "phone": "+380501111111"},
                 {"name": "Diana", "phone": "+380502222222"},]


def input_error(func):
    def wrapper(x):
        try:
            result = func(x)
        except IndexError:
            return f'Give me name and phone please'
        return result
    return wrapper


def index_error(func):
    def wrapper(x):
        try:
            result = func(x)
        except IndexError:
            return f'Enter contact name'
        return result
    return wrapper


def hello_func(text=None):
    return f'How can I help you?'


@input_error
def add_func(text):
    global contacts_dict
    name = text[0].capitalize()
    phone = sanitize_phone_number(text[1])
    new_contact = {"name": name, "phone": phone}
    contacts_dict.append(new_contact)
    return f'add contact {name} - {phone}'


def show_all(text=None):
    result = 'Contacts list \n'
    for i in contacts_dict:
        result += 'name ' + i["name"] + ' phone ' + i["phone"] + "\n"
    return result


@input_error
def change_contact(list_contacts):
    global contacts_dict
    name = list_contacts[0].capitalize()
    phone = sanitize_phone_number(list_contacts[1])
    for i in contacts_dict:
        if i["name"] == name:
            i["phone"] = phone
            return f'contast {i["name"]} take new phone {i["phone"]}'
    return f'Not {name} in contact list'


@index_error
def phone_print(name):
    contact = name[0].capitalize().strip()
    for i in contacts_dict:
        if i["name"] == contact:
            return f'name: {contact} phone: {i["phone"]}'
    return f'Not {contact} in contact list'


COMMAND_DICT = {
    hello_func: "hello",
    add_func: "add",
    show_all: "show all",
    change_contact: "change",
    phone_print: "phone"
}


def select_command(text):
    for key, val in COMMAND_DICT.items():
        if val == text:
            return key
    return f'non command in list'


def parser_text(text):
    text = text.lower().strip()
    if text.startswith("show all"):
        return "show all", None
    else:
        user_text = text.split()
        return user_text[0], user_text[1:]


def main():

    while True:

        user_input = input('>>input>>')
        if user_input.lower().strip() in COMMAND_EXIT:
            print('Good bye!')
            break
        user_command, other_text = parser_text(user_input)
        result = select_command(user_command)
        if type(result) == str:
            print(result)
        else:
            print(result(other_text))


if __name__ == "__main__":
    main()
