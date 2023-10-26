import convert as conv

# tests
def test_if_num_not_minus(number):
    assert number >= 0 , "Number must be bigger than 0"
    
def test_if_num_not_0(number):
    assert number != 0 , "Number must be bigger than 0"
    
def test_converting_small_num():
    assert conv.convert(31) == "1F", "Error while converting small number"

def test_converting_bigger_num():
    assert conv.convert(4096) == "1000", "Error while converting bigger number"
    
def test_converting_biggest_num():
    assert conv.convert(1234567890123456789012345678901234567890) == "3A0C92075C0DBF3B8ACBC5F96CE3F0AD2", "Error while converting biggest number"