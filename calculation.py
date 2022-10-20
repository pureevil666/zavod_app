input_text = ''
data_list = []


def give_data(data):
    global input_text
    input_text = data
    convert_data_to_list(input_text)


def convert_data_to_list(data):
    global data_list
    data_list = data.splitlines()
    print(data_list)
