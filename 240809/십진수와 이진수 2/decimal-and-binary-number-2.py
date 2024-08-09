binary_str = input()


decimal_value = int(binary_str, 2)


multiplied_value = decimal_value * 17


result = bin(multiplied_value)[2:]
print(result)