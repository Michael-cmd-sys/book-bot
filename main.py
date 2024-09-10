def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("-"*42)
    print("Character counts in text: ")
    charMap = create_char_map(text)
    print_charMap(charMap)
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    # print(f"words: {words}")
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def create_char_map(text : str) -> dict[str, int]:
    charMap = dict()
    
    for char in text:
        char = char.lower()
        if not char.isalpha():
            continue
        elif char in charMap :
            charMap[char] += 1
        else:
            charMap[char] = 1
            
    return charMap


def print_charMap(charMap: dict[str, int]) -> None:
    ordered_keys = sorted(charMap.keys())
    for char in ordered_keys:
        print(f"The {char} character was found {charMap[char]} times")
        
main()
