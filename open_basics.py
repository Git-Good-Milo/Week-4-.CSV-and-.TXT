
def open_read_file(file):

    try:
        opened_file = open(file, 'r')
        file_lines_list = opened_file.readlines()
        print(file_lines_list)

        for line in file_lines_list:
            print(line.rstrip('\n'))

        opened_file.close() # Otherwise file is locked and cant be changed

    except FileNotFoundError as errmsg:
        print("File can not be found. Please check your input")
        print(errmsg)
        raise

def open_read_file_using_with(file):
    try:
        with open(file, 'r') as open_file:
                for line in open_file.readlines():
                    print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print("File can not be found. Please check your input")
        print(errmsg)
        #raise
    finally:
        print('\n Execution complete')

def write_to_file(file, order_item):
    try:
        opened_file = open(file, 'w')
        opened_file.write(order_item)

        opened_file.close()
    except FileNotFoundError:
        print("File not found")

def append_to_file(file, order_item):
    try:
        opened_file = open(file, 'a')
        opened_file.write(order_item)

        opened_file.close()
    except FileNotFoundError:
        print("File not found")