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

#counts the number of times each character is mentioned in the text.
def charcounter(string):







main()
wordcounter(main())