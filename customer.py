class Customer:
    """
    Represents a customer in the delivery management system.

    Attributes:
        __customer_id (str): Unique identifier for the customer.
        __name (str): The customer's full name.
        __email (str): Email address used for notifications.
        __address (str): Residential or shipping address.
        __phone (str): Contact phone number.
    """

    def __init__(self, customer_id, name, email, address, phone):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__address = address
        self.__phone = phone

    # --- Getters ---
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    # --- Setters ---
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    # --- Example Stub Method ---
    def validate_contact_details(self):
        """
        Checks if the customer's email and phone number are valid.
        E.g., ensure email has '@' and phone is numeric.
        """
        pass

    def __str__(self):
        """
        Return a user-friendly string representation of the customer.
        """
        return (
            f"Customer [ID={self.__customer_id}, Name={self.__name}, "
            f"Email={self.__email}, Address={self.__address}, Phone={self.__phone}]"
        )
