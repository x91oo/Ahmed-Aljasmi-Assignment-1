class DeliveryNote:
    """
    Represents a delivery note or receipt for a completed or shipped order.

    Attributes:
        __note_id (str): Unique identifier for the delivery note.
        __order (Order): The order associated with this delivery note.
        __delivery_date (str): Actual or expected delivery date.
        __recipient_signature (str): Name or signature of the recipient upon delivery.
        __courier_service (str): Optional field for the courier or service used.
    """

    def __init__(self, note_id, order, delivery_date, recipient_signature, courier_service="Courier"):
        self.__note_id = note_id
        self.__order = order
        self.__delivery_date = delivery_date
        self.__recipient_signature = recipient_signature
        self.__courier_service = courier_service

    # --- Getters ---
    def get_note_id(self):
        return self.__note_id

    def get_order(self):
        return self.__order

    def get_delivery_date(self):
        return self.__delivery_date

    def get_recipient_signature(self):
        return self.__recipient_signature

    def get_courier_service(self):
        return self.__courier_service

    # --- Setters ---
    def set_delivery_date(self, date):
        self.__delivery_date = date

    def set_recipient_signature(self, signature):
        self.__recipient_signature = signature

    def set_courier_service(self, service):
        self.__courier_service = service

    # --- Example Stub Method ---
    def generate_note_details(self):
        """
        Creates a more detailed string or PDF summarizing the entire delivery.
        Could include order details, packet weight, etc.
        """
        pass

    def __str__(self):
        """
        Return a concise representation of the delivery note.
        """
        customer = self.__order.get_customer()
        return (
            "Delivery Note\n"
            "-------------\n"
            f"Note ID: {self.__note_id}\n"
            f"Delivery Date: {self.__delivery_date}\n"
            f"Courier Service: {self.__courier_service}\n"
            f"Recipient Signature: {self.__recipient_signature}\n\n"
            f"Order Details:\n{self.__order}\n"
            f"Ship To: {customer.get_name()}, {customer.get_address()}\n"
        )
