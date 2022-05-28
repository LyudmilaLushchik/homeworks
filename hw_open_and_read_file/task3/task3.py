import os


BASE_PATH = os.getcwd()
INPUT_DIR_NAME = 'input_files'
RESULT_FILE_NAME = 'result_file.txt'
in_path = os.path.join(BASE_PATH, INPUT_DIR_NAME)
res_path = os.path.join(BASE_PATH, RESULT_FILE_NAME)


def read_func(file_path):
    files_list = os.listdir(file_path)
    read_files = []
    for file in files_list:
        with open(os.path.join(file_path, file), mode = 'rt', encoding = 'utf-8') as file_obj:
            data = file_obj.readlines()
            file_name = file
            read_file = file_name, (len(data), data)
            read_files.append(read_file)
            read_files.sort(key=lambda i: i[1])

    result = ''
    for item in read_files:
        content = ''
        for element in item[1][1]:
            content += str(element)
        result += f"{item[0]}\n{item[1][0]}\n{content}\n"
    return result


def write_func(read_func_list, file_path):
    with open(file_path, mode = 'wt', encoding = 'utf-8') as file_obj:
        file_obj.writelines(str(read_func_list))

write_func(read_func(in_path), res_path)