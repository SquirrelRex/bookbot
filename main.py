def main ():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    #print(count_words(file_contents))
    #print(count_characters(file_contents))
    print_letters(count_characters(file_contents))


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_text = text.lower()
    character_count = {}
    for character in lower_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def print_letters(character_dict):
    for character in character_dict:
        if character.isalpha() == True:
            print(f"The '{character}' character was found {character_dict[character]} times")



if __name__ == "__main__":
    main()
