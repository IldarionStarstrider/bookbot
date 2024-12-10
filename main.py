def main(directory):
    with open(directory) as f:
        file_contents = f.read()
        return file_contents

#counts the number of words in the text.
def wordcounter(string):
    list_words = string.split()
    count = 0
    for word in list_words:
        count += 1
    return count

#counts the number of times a character is used in the text and delivers an alphabetized dictionary.
def charcounter(string):
    lowered_string = string.lower()
    dict = {}
    for character in lowered_string:
        if character in dict:
            dict[character] += 1
        elif character.isalpha():
            dict[character] = 1
    return dict

#cexpand the charcounter dictionary with char and num keys and adds them to a list.
def expand_dict(dict):
    new_list = []
    for k in dict:
        expanded_dict = {}
        expanded_dict["char"] = k
        expanded_dict["num"] = dict[k]
        new_list.append(expanded_dict)
    return new_list

#tells what to sort by
def sort_by(dict):
    return dict["num"]

#sorts the list from convert_dict on number of times.
def sort_list(list):
    list.sort(reverse=True, key=sort_by)
    return list

#creates a report of directory
def create_report(directory):
    string = main(directory)
    print(f"--- Begin report of {directory} ---")
    print(f"{wordcounter(string)} words found in the document")
    print("")
    print("")
    dict = charcounter(string)
    list = expand_dict(dict)
    list = sort_list(list)
    for d in list:
        print(f"The '{d["char"]}' character was found {d["num"]} times")
    print("--- End report ---")


create_report("books/frankenstein.txt")