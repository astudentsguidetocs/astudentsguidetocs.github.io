# gpt word counter for all files
import os

def count_words_in_file(filepath):
    """Count the number of words in a given file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        return len(text.split())
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return 0

def main(folder_path):
    """Traverse all subdirectories and calculate word counts for .md files."""
    total_word_count = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                word_count = count_words_in_file(filepath)
                total_word_count += word_count
                print(f"{filepath}: {word_count} words")

    print(f"Total word count for all .md files: {total_word_count}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ").strip()
    if os.path.isdir(folder_path):
        main(folder_path)
    else:
        print("The provided path is not a valid directory.")
