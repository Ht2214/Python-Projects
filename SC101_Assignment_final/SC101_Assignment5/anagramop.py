import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
Dic_list = {}                 # Dictionary would be faster


def main():
    """
    TODO:
    """
    start = time.time()
    read_dictionary()

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    result = find_anagrams("tesla")
    print(str(len(result)) + " anagrams: ", end='')
    print(result)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global Dic_list
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line[0]+str(len(line)) in Dic_list:
                Dic_list[line[0]+str(len(line))].append(line)
            else:
                Dic_list[line[0]+str(len(line))] = [line]

def find_anagrams(s):
    """
    :param s:
    :return: the list that contain anagrams
    """
    result = []
    find_anagrams_helper(s, "", len(s), result)
    return result


def find_anagrams_helper(s, current_s, size, lst):
    global Dic_list
    if size == len(current_s) and current_s in Dic_list[current_s[0]+str(size)]:
        if current_s not in lst:
            print('Find anagram for: ' + current_s)
            print('Searching...')
            lst.append(current_s)
    else:
        count = -1
        for char in s:
            # buggy
            count += 1 # indicate the index of char in s
            if char in current_s and char not in s[count + 1:]:
                continue
            if len(current_s) > 1 and not has_prefix(current_s, size):
                # short circuit evaluation
                break
            current_s += char
            find_anagrams_helper(s, current_s, size, lst)
            current_s = current_s[:-1]


def has_prefix(sub_s, size):
    """
    :param sub_s:
    :return:
    """
    global Dic_list
    for word in Dic_list[sub_s[0]+str(size)]:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()