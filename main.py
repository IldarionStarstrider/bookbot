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
    print(count)
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
    print(dict)
    return dict





main()
wordcounter(main())
charcounter(main())