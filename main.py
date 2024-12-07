books_directory = "books/"


def count_words(text):
    words = text.split()
    print(len(words))


def unique_characters(text):
    hm = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in hm:
            hm[char] = 0
        hm[char] = hm[char] + 1
    return hm


def print_character_report(character_counts):
    sorted_dict = dict(
        sorted(character_counts.items(),
               key=lambda item: item[1], reverse=True)
    )
    for char in sorted_dict:
        if char.isalpha():
            print(f"The '{char}' was found {character_counts[char]} times")


def main():
    with open(f"{books_directory}/frankenstein.txt") as f:
        file_contents = f.read()

    count_words(file_contents)
    character_counts = unique_characters(file_contents)
    print_character_report(character_counts)


main()
