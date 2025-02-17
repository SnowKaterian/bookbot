def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)

    print_report(book_path, num_words, char_count)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
	text = text.lower()
	char_count = {}
	for char in text:
		if char.isalpha():
			if char in char_count:
				char_count[char] += 1
			else:
				char_count[char] = 1
	return char_count

def print_report(book_path, num_words, char_count):
	print(f"--- Begin report of {book_path} ---")
	print(f"{num_words} words found in the document\n")

	sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

	for char, count in sorted_char_count:
		print(f"The '{char}' character was found {count} times")

	print("--- End Report ---")

main()
