def square_area(num):
    num = num**2
    return num

def test_square_area_8():
    result = square_area(8)
    assert result == 64