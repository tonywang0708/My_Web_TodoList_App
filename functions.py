FILEPATH = "Todo List.txt"

def get_list(filepath=FILEPATH):
    """arg: filePath; return list of content from the given filepath """
    with open(filepath, 'r') as f:
        list1 = f.readlines()
    return list1


def write_list(list, filepath=FILEPATH):
    """ Write the given list to given file """
    with open(filepath, 'w') as f:
        f.writelines(list)

if __name__  == "__main__":
    print("hello")