def practice02_03():
    import re
    strings = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material in this guide, 
    then the Python Mentors group is available to help guide new contributors through the process"""
    converted_strings = ''
    word = ''
    word_list = []
    set_like_list = [0]
    for i in range(0, len(strings)):
        word += strings[i]
        if strings[i] == ' ' or strings[i] == '.' or strings[i] == ',' or strings[i] == '\n' or i == len(strings):
            converted_strings += word.upper()
            word = ''
    strings = ''

    for i in range(0, len(converted_strings)):

        if converted_strings[i] != '.' and converted_strings[i] != ','\
                and converted_strings[i] != '\n':
            strings += converted_strings[i]

    for i in range(0, len(strings)):

        if strings[i] != ' ':
            word += strings[i]
        else :
            word_list.append(word)
            word = ''
    for i in range(0, len(word_list)):
        for j in range(i+1, len(word_list)) :
            if word_list[i] != word_list[j]:
                set_like_list.append(word_list[i])
    print(word_list)



practice02_03()
