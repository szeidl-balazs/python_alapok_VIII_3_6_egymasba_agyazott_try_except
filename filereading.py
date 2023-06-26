#file name opener function to open the file and return the content:
def read_file(file_name):
    try:
        target_file = open(file_name)
        content = target_file.read()

    except OSError:
        print('Hiba a fájl kezelése közben!')

    else:
        return content               

    finally:
        target_file.close()



#file name asker function to ask for file name and return it:
def get_file_name():
    return input('Which file you want to open? ')

#printer function that calls the opener function which returns the content:
def print_content(file_name):
    
    print(read_file(file_name))

#call the name asker function that returns the name:
print_content(get_file_name())
