def remove_vowels(string):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in string:
        if char not in vowels:
            result += char
    
    return result


input_string = "Hello, World!"
output_string = remove_vowels(input_string)
print(output_string)
