from address import extract_city, extract_state, extract_zipcode
import pytest

"""525 S Center St, Rexburg, ID 83460"""

def test_extract_city():

    city = extract_city("525 S Center St, Rexburg, ID 83460")
    assert isinstance(city, str)

        # Assert the parts of the name
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"

def test_extract_state():

    state = extract_state("525 S Center St, Rexburg, ID 83460")
    assert isinstance(state, str)

        # Assert the parts of the name
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"


def test_extract_zipcode():

    city = extract_zipcode("525 S Center St, Rexburg, ID 83460")
    assert isinstance(city, str)

        # Assert the parts of the name
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"


pytest.main(["-v", "--tb=line", "-rN", __file__])