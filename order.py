class Order:
    """
    Represents an order placed by a customer, including the associated packet.

    Attributes:
        __order_id (str): Unique identifier for the order.
        __customer (Customer): Reference to the customer who placed this order.
        __packet (Packet): The packet containing the shipment details.
        __status (str): Current status of the order (e.g., 'Pending', 'Shipped', 'Delivered').
        __total_price (float): Total price for the entire order.
    """

    def __init__(self, order_id, customer, packet, status="Pending", total_price=0.0):
        self.__order_id = order_id
        self.__customer = customer
        self.__packet = packet
        self.__status = status
        self.__total_price = total_price

    # --- Getters ---
    def get_order_id(self):
        return self.__order_id

    def get_customer(self):
        return self.__customer

    def get_packet(self):
        return self.__packet

    def get_status(self):
        return self.__status

    def get_total_price(self):
        return self.__total_price

    # --- Setters ---
    def set_status(self, status):
        self.__status = status

    def set_total_price(self, price):
        self.__total_price = price

    # --- Example Methods ---
    def calculate_total_price(self):
        """
        Potentially combine product cost, shipping cost, etc.
        For now, it's a placeholder or an update to __total_price.
        """
        # e.g., self.__total_price = base_price + shipping_calculations
        pass

    def update_order_status(self, new_status):
        """
        Updates the order status, e.g., from 'Pending' to 'Shipped'.
        Could add validation logic to ensure correct transitions.
        """
        self.__status = new_status

    def __str__(self):
        """
        Return a user-friendly summary of the order.
        """
        return (
            f"Order [ID={self.__order_id}, Status={self.__status}, "
            f"Total Price={self.__total_price}, Customer={self.__customer.get_name()}]\n"
            f"  Packet: {self.__packet}\n"
        )
