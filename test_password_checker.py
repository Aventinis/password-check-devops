from password_checker import is_valid_password

def test_password_checker():
    assert is_valid_password("Password123!") == True
    assert is_valid_password("password") == False
    assert is_valid_password("PASSWORD123") == False
    assert is_valid_password("Pass123") == False
    assert is_valid_password("Passw0rd!") == True
    assert is_valid_password("12345678") == False
    assert is_valid_password("!@#$%^&*()") == False
    assert is_valid_password("ValidPass1!") == True
    