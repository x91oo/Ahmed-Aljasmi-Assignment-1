# main.py
from customer import Customer
from packet import Packet
from order import Order
from deliverynote import DeliveryNote

def main():
    # Create a Customer
    cust = Customer(
        customer_id="CUST-001",
        name="Jane Doe",
        email="jane.doe@example.com",
        address="100 Maple Street, Cityville",
        phone="555-1234"
    )

    # Create a Packet
    pkt = Packet(
        packet_id="PKT-100",
        contents_description="Assorted Documents",
        weight=2.5,
        dimensions="30x20x5 cm",
        shipping_method="Express"
    )

    # Create an Order linking the Customer and the Packet
    order = Order(
        order_id="ORD-ABC123",
        customer=cust,
        packet=pkt,
        status="Pending",
        total_price=150.00
    )

    # Update Order status
    order.update_order_status("Shipped")

    # Create a DeliveryNote referencing the Order
    note = DeliveryNote(
        note_id="DN-2025-001",
        order=order,
        delivery_date="2025-03-10",
        recipient_signature="Jane Doe",
        courier_service="FastShip"
    )

    # Print the DeliveryNote (which includes the Order details)
    print(note)

if __name__ == "__main__":
    main()
