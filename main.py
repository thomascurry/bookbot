def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    print("--- Book Statistics ---")
    print(f"{count_words(file_contents)} words found in the document")
    for character in count_characters(file_contents):
        print(f"The '{character['char']}' character appears {character['count']} times in the document")
    print("-----------------------")

def sort_on(dict):
    return dict['count']

def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}

    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in characters:
                characters[lower_char] += 1
            else:
                characters[lower_char] = 1

    chracter_count = []
    for char, count in characters.items():
        chracter_count.append({'char': char, 'count': count})

    chracter_count.sort(key=sort_on, reverse=True)
    return chracter_count

main()
