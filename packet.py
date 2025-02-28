class Packet:
    """
    Represents the shipped package itself, rather than individual items.

    Attributes:
        __packet_id (str): Unique identifier for the packet.
        __contents_description (str): Description of what's inside the packet.
        __weight (float): Weight of the entire packet in kilograms.
        __dimensions (str): Dimensions (LxWxH) of the packet.
        __shipping_method (str): Method of shipment (e.g., "Air", "Ground", "Express").
    """

    def __init__(self, packet_id, contents_description, weight, dimensions, shipping_method):
        self.__packet_id = packet_id
        self.__contents_description = contents_description
        self.__weight = weight
        self.__dimensions = dimensions
        self.__shipping_method = shipping_method

    # --- Getters ---
    def get_packet_id(self):
        return self.__packet_id

    def get_contents_description(self):
        return self.__contents_description

    def get_weight(self):
        return self.__weight

    def get_dimensions(self):
        return self.__dimensions

    def get_shipping_method(self):
        return self.__shipping_method

    # --- Setters ---
    def set_contents_description(self, description):
        self.__contents_description = description

    def set_weight(self, weight):
        self.__weight = weight

    def set_dimensions(self, dimensions):
        self.__dimensions = dimensions

    def set_shipping_method(self, shipping_method):
        self.__shipping_method = shipping_method

    # --- Example Stub Method ---
    def estimate_shipping_cost(self):
        """
        Placeholder for logic that calculates shipping cost
        based on weight/dimensions/shipping method.
        """
        pass

    def __str__(self):
        """
        Return a string representation of the packet details.
        """
        return (
            f"Packet [ID={self.__packet_id}, Contents='{self.__contents_description}', "
            f"Weight={self.__weight}kg, Dimensions={self.__dimensions}, "
            f"Method={self.__shipping_method}]"
        )
