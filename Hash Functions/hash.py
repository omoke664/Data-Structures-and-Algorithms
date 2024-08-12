def hash_function(input_string):
    summation = sum(ord(ch) for ch in input_string)
    return summation % 10

print(hash_function('Hello'))
print(hash_function('world'))