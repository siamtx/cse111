from names import make_full_name, extract_family_name, extract_given_name
import pytest


# Testing the fullname function
def test_make_full_name():

    name = make_full_name("Sally",  "Brown")
    assert isinstance(name, str)

    # Assert the parts of the name
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Buck", "Rogers") == "Rogers; Buck"
    assert make_full_name("", "Brown") == "Brown; """
    assert make_full_name("sally", "Brown") == "Brown; sally"

# Testing the family name function
def test_extract_family_name():
    family = extract_family_name("Brown; Sally")
    assert isinstance(family, str)


    # Assert the parts of the name
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Brown; Sally") != "Sally"
    assert extract_family_name("Brown; "" ") == "Brown"
    assert extract_family_name("Rogers; Sally") == "Rogers"

# Testing the given name function
def test_extract_given_name():
    given = extract_given_name("Brown; Sally")
    assert isinstance(given, str)


    # Assert the parts of the name
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name(" ""; Sally") == "Sally"
    assert extract_given_name("Brown; sally") == "sally"
    assert extract_given_name("Brown; Robin") == "Robin"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
