def find_substring_in_wordlist(wordlist, name):
    # Initialize variables to store results
    count = 0
    indices = []

    # Iterate through each word in the wordlist
    for word in wordlist:
        if name in word:
            # If the name is a substring of the word, increment count
            count += 1
            # Find and append the indices of occurrences of name in the word
            word_indices = [i for i in range(len(word)) if word.startswith(name, i)]
            indices.append(word_indices)
        else:
            # If the name is not a substring, append 0
            indices.append(0)

    return (count, indices)

# Example usage:
wordlist = ["apple", "banana", "nameless", "nickname", "game"]
name = "name"

result = find_substring_in_wordlist(wordlist, name)
print("Number of words with '{}' as substring: {}".format(name, result[0]))
print("Indices of '{}' in each word: {}".format(name, result[1]))
