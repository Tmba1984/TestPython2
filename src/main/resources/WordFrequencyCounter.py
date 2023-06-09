def count_word_frequency(file_name):
    for line in file_name:
        print(line)
    file_name.close()

if __name__ == "__main__":
    f = open("C:/Users/famMb/OneDrive/Dokumente/py_workspace/input.txt", "r")
    print('TTTTTTT')
    count_word_frequency(f)