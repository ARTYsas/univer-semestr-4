def build_prefix_table(pattern):
    """
    Build the prefix table for the given pattern.
    """
    m = len(pattern)
    prefix_table = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_table[length - 1]
            else:
                prefix_table[i] = 0
                i += 1

    return prefix_table


def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt search for the pattern in the text.
    """
    n = len(text)
    m = len(pattern)
    prefix_table = build_prefix_table(pattern)
    result = []

    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                result.append(i - j)
                j = prefix_table[j - 1]
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1

    return result


# Main program
def search_word_in_file(file_path, search_word):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

            # Convert both text and search_word to lowercase for case-insensitive search
            text = text.lower()
            search_word = search_word.lower()

            # Perform KMP search
            occurrences = kmp_search(text, search_word)

            if len(occurrences) == 0:
                print("The word was not found in the file.")
            else:
                print("Occurrences found at positions:")
                for pos in occurrences:
                    print(pos)
    except FileNotFoundError:
        print("File not found.")


# Get user input for file path and search word
file_path = input("Enter the path to the text file: ")
search_word = input("Enter the word to search for: ")

# Call the search function
search_word_in_file(file_path, search_word)
