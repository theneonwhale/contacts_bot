contacts = {}


def parser(command_input):
    parsed_input = command_input.lower().strip().split()
    return parsed_input


def input_error(func):
    def inner(data):
        if func.__name__ in ('add', 'change'):
            try:
                return func(data)
            except:
                return 'With this command you should enter contact name and phone number.'
        if func.__name__ in ('phone'):
            try:
                return func(data)
            except:
                return 'With this command you should enter contact name.'
    return inner


def hello():
    return 'How can I help you?'

@input_error
def add(data):
    if data[0] not in contacts.keys():
        contacts[data[0]] = data[1]
        message = f'Contact {data[0].title()} with phone {data[1]} was successfully added.'
        return message
    else:
        return 'Contact already exists.'

@input_error
def change(data):
    if data[0] in contacts.keys():
        contacts[data[0]] = data[1]
        message = f'Contact {data[0].title()} was successfully updated with phone {data[1]}.'
        return message
    else:
        return 'There is no such contact.'

@input_error
def phone(data):
    if data[0] in contacts.keys():
        return f'{contacts[data[0]]}'
    else:
        return 'There is no such contact.'

def show():
    if len(contacts):
        contacts_data = []
        for contact in contacts:
            contact_data = f"{contact.title()}: {contacts[contact]}\n"
            contacts_data.append(contact_data)
        return ''.join(contacts_data)
    else:
        return 'There are no any contacts.'

def close():
    return 'Good bye!'


commands = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show,
    'close': close
}


def main():
    while True:
        command_input = input("Enter command and data: ")

        if command_input in ('hello', 'show all'):
            print(commands.get(command_input)())
            continue

        if command_input in ('good bye', 'close', 'exit'):
            print(commands.get('close')())
            break

        parsed_input = parser(command_input)
        command = parsed_input[0]

        if command not in commands.keys():
            print('There is no such command.')
            continue

        data = parsed_input[1:]
        method = commands.get(command)
        print(method(data))


if __name__ == '__main__':
    main()
