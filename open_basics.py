
def open_read_file(file):

    try:
        opened_file = open(file, 'r')
        file_lines_list = opened_file.readlines()
        print(file_lines_list)

        for line in file_lines_list:
            print(line.rstrip('\n'))

        opened_file.close() # Otherwise file isl locked and cant be changed

    except FileNotFoundError as errmsg:
        print("File can not be found. Please check your input")
        print(errmsg)
        raise


# except SyntaxError as errmsg:
#     print("There has been a syntax error", errmsg)


# except:
#     print("There has been an error. PANIC!!!!")