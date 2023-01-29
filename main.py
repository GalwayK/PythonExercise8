import re

def find_words():
    with open("files/miracle_in_the_andes.txt", "r", encoding='utf-8') as file:
        book = file.read()
    book = book.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ")
    pattern = re.compile(" [A-Za-z]+[A-Za-z] ")
    words = re.findall(pattern, book.lower())

    first = ""
    first_count = 0
    second = ""
    second_count = 0
    third = ""
    third_count = 0
    unique_words = []

    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    print(unique_words)

    for word in unique_words:
        print(word)
        count = book.lower().count(word)
        if count > first_count:
            print(f"Found first word: {word}")
            first = word
            print(first)
            first_count = count
        elif count > second_count:
            print(f"Found second word: {word}")
            second = word
            print(second)
            second_count = count
        elif count > third_count:
            print("Found third word.")
            third = word
            print(third)
            third_count = count

    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Third: {third}")


def find_love_para():
    with open("files/miracle_in_the_andes.txt", "r", encoding='utf-8') as file:
        book = file.read()
    print(book)


find_love_para()