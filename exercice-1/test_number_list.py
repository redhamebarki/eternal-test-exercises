def test_convert_to_integer():
    from number_list import convert_to_integer
    assert convert_to_integer([1,2.5,9.2,'hi']) == ([1,2,9])