import sys
from stats import get_num_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    count = get_num_words(book_text)
    character_count = count_characters(book_text)
    
    report = f"""
============ BOOKBOT ============
Analyzing book found at {filepath}
----------- Word Count ----------
Found {count} total words
--------- Character Count -------
    """
    
    for key in character_count:
        if key.isalpha():
            report += f"{key}: {character_count[key]}\n"
    
    report += "============= END ==============="
    print(report)
    
main()