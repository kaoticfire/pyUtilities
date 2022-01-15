from collections import Counter


# Method One
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    freq1 = check_n_add(s1)
    freq2 = check_n_add(s2)
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


def check_n_add(word: str):
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


# Method Two
def comparison(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


# Method Three
def sorted_comparison(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    word_one = 'SALESMAN'
    word_two = 'NAMELESS'
    if are_anagrams(word_one, word_two) and comparison(word_one, word_two) and sorted_comparison(word_one, word_two):
        print(f'{word_one} & {word_two} are anagrams')
    else:
        print(f'{word_one} & {word_two} are not anagrams')
