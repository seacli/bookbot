import string

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(content):
    # clean = content.translate(str.maketrans('', '', string.punctuation))
    # return len(clean.split())
    return len(content.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    

if __name__ == "__main__":
    main()