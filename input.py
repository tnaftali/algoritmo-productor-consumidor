import validation

def insert_number(message):
    str_num = input(message)
    while not validation.is_valid_number(str_num):
        str_num = input('Please insert a valid integer positive number:\n')
    return int(str_num)