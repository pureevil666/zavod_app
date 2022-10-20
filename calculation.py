LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
LETTERS = LETTERS + LETTERS.upper()
group_dict = {}

def give_data(data):
    input_text = data
    convert_data_to_list(input_text)


def convert_data_to_list(data):
    data_list = data.splitlines()
    print(data_list)
    create_groups(data_list)

def create_groups(input_list):
    global group_dict
    for line in input_list:
        if len(line.strip(LETTERS)) == 0:
            group_dict[line] = 0
    print(group_dict)
