def first_non_repeating_char(s):
    char_count = {}

    # count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # find the first non repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    return None


# usage
input_str = "programming"
result = first_non_repeating_char(input_str)

if result:
    print(f"first non repeating character in {input_str} is: {result}")
else:
    print(f"no non repeating character in {input_str}")
