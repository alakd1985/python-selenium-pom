# Valid credentials
VALID_USERNAME = "Admin"
VALID_PASSWORD = "admin123"

# Negative test credentials

# 1. Valid username + invalid password
VALID_USERNAME_INVALID_PASSWORD = {
    "username": VALID_USERNAME,
    "password": "admin1234"
}

# 2. Invalid username + valid password
INVALID_USERNAME_VALID_PASSWORD = {
    "username": "Admin1",
    "password": VALID_PASSWORD
}

# 3. Invalid username + invalid password
INVALID_USERNAME_INVALID_PASSWORD = {
    "username": "Admin1",
    "password": "admin1234"
}

# 4. Empty username + empty password
EMPTY_CREDENTIALS = {
    "username": "",
    "password": ""
}
