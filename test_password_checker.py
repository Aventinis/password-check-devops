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


def test_password_length():
    assert is_valid_password("Short1!") == False
    assert is_valid_password("LongEnough1!") == True

def test_password_character_requirements():
    assert is_valid_password("NoNumbers!") == False
    assert is_valid_password("nouppercase1!") == False
    assert is_valid_password("NOLOWERCASE1!") == False
    assert is_valid_password("NoSpecialChar1") == False
    assert is_valid_password("ValidPass1!") == True