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
    group_list = []
    for line in input_list:
        if len(line.strip(LETTERS)) == 0:
            group_dict[line] = 0
    for name in group_dict:
        group_list.append(name)
    save_indexes(group_dict, input_list, group_list)


def save_indexes(group_dict, input_list, group_list):
    index_list = []
    for group in group_dict:
        index = input_list.index(group)
        index_list.append(index)
    split_list(index_list, group_dict, input_list, group_list)


def split_list(index_list, group_dict, input_list, group_list):
    for i in range(0, len(index_list)):
        start = index_list[i]
        if i < len(index_list) - 1:
            stop = index_list[i + 1]
            saved_list = input_list[start + 1:stop]
        else:
            saved_list = input_list[start + 1:]
        group_dict[group_list[i]] = saved_list
    print(input_list)
    print(group_dict)
    print(index_list)
    print(group_list)
    print(group_dict)
