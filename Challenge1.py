def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("K") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("éù$") == 0, "Special characters"
assert count_upper_case("Hello %Ké@") == 2, "2 upper case + special character"

print ("All the tests passed")