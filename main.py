def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

#counts the number of words in the text.
def wordcounter(string):
    list_words = string.split()
    count = 0
    for word in list_words:
        count += 1
    return count

#counts the number of times a character is used in the text.
def charcounter(string):
    lowered_string = string.lower()
    dict = {}
    for character in lowered_string:
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict

#converts the charcounter dictionary to a list of dictionaries.
def convert_dict(dict):
    new_list = []
    for k, v in dict:
        
    print(new_list)





#creates a report of frankenstein.txt
#def create_report(string):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcounter(string)} words found in the document")
    dict = charcounter(string)
    for key in dict:
        print(f"The {key} character was found {dict[key]} times")







convert_dict(charcounter(main()))

#create_report(main())