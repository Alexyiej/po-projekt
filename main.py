import tests 
import convert as conv

number = int(input("Enter a number: "))

tests.test_if_num_not_minus(number)
tests.test_if_num_not_0(number)
tests.test_converting_small_num()
tests.test_converting_bigger_num()
tests.test_converting_biggest_num()

hex_representation = conv.convert(number)
print(hex_representation)


