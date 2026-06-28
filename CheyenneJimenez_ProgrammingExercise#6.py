import re

# Function that validates a phone number.
def validate_phone_number(phone_number):
    ' Return True if the phone number is valid.'
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return re.match(pattern, phone_number) is not None

# Function that validates a social security number.
def validate_ssn(ssn):
    ' Return True if the Social Security number is valid.'
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return re.match(pattern, ssn) is not None

# Function that validates zip code.
def validate_zip_code(zip_code):
    ' Return True if the zip code is valid.'
    pattern = r"^\d{5}(-\d{4})?$"
    return re.match(pattern, zip_code) is not None


def main():
    ' Get user input and display validation results.'
    # Ask user to enter phone number, social security number, and zip code.
    phone_number = input("Enter a phone number (XXX-XXX-XXXX): ")
    ssn = input("Enter a Social Security number (XXX-XX-XXXX): ")
    zip_code = input("Enter a zip code (XXXXX or XXXXX-XXXX): ")

    print()

    # Validates credentials entered by user.

    if validate_phone_number(phone_number):
        print("The phone number is valid.")
    else:
        print("The phone number is invalid.")

    if validate_ssn(ssn):
        print("The Social Security number is valid.")
    else:
        print("The Social Security number is invalid.")

    if validate_zip_code(zip_code):
        print("The zip code is valid.")
    else:
        print("The zip code is invalid.")


if __name__ == "__main__":
    main()