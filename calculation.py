LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
LETTERS = LETTERS + LETTERS.upper()
group_dict = {}


def give_data(data):
    input_text = data
    convert_data_to_list(input_text)


def convert_data_to_list(data):
    data_list = data.splitlines()
    create_groups(data_list)


def create_groups(input_list):
    global group_dict
    for line in input_list:
        if len(line.strip(LETTERS)) == 0:
            group_dict[line] = 0
    save_indexes(group_dict, input_list)


def save_indexes(group_dict, input_list):
    print(input_list)
    print(group_dict)
    index_list = []
    for group in group_dict:
        index = input_list.index(group)
        index_list.append(index)
    print(index_list)
