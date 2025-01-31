import streamlit as st
from datetime import datetime

# Sample data for food items
food_items = [
    {"id": 1, "name": "Samosa", "price": 10.00},
    {"id": 2, "name": "Biryani", "price": 150.00},
    {"id": 3, "name": "Masala Dosa", "price": 50.00},
]

# Initialize user wallet balance in session state
if 'user_wallet' not in st.session_state:
    st.session_state.user_wallet = 500.00

# Initialize orders in session state
if 'orders' not in st.session_state:
    st.session_state.orders = []

def place_order(selected_item, delivery_option):
    delivery_cost = 10.00 if delivery_option == "Delivery" else 0.00
    total_cost = selected_item["price"] + delivery_cost
    if st.session_state.user_wallet >= total_cost:
        st.session_state.user_wallet -= total_cost
        order_details = {
            "name": selected_item["name"],
            "price": selected_item["price"],
            "delivery_cost": delivery_cost,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "delivery_option": delivery_option
        }
        st.session_state.orders.append(order_details)
        return True, total_cost
    else:
        raise ValueError("Insufficient funds")

def get_wallet_balance():
    return st.session_state.user_wallet

def display_wallet_balance():
    st.info(f"**Wallet Balance: ₹{st.session_state.user_wallet:.2f}**", icon="💰")

def main():
    st.sidebar.header("Bitezy 🍔🍕🍜")
    st.sidebar.write("""
        **Welcome to Bitezy!**
        
        Order your favorite food items from our menu.
        
        **Timings:**
        - Monday to Friday: 9 AM - 9 PM
        - Saturday and Sunday: 10 AM - 10 PM
        
        **Contact Us:**
        - Phone: +91 1234567890
        - Email: support@bitezy.com
    """)

    st.title("Bitezy 🍔🍕🍜")
    st.write("**Name: Dr.Naveen Kumar**")
    st.write("**Phone: +91 9876543210**")
   
    tab1, tab2, tab3, tab4 = st.tabs(["Menu", "Orders", "Add to Wallet", "Profile"])

    with tab1:
        st.header("Menu")
        selected_item = st.radio("Select an item", food_items, format_func=lambda item: f"{item['name']} - ₹{item['price']:.2f}")
        delivery_option = st.radio("Select Delivery Option", ("Delivery", "Pickup"))

        if st.button("Submit Order"):
            try:
                success, total_cost = place_order(selected_item, delivery_option)
                if success:
                    st.success(f"Successfully ordered {selected_item['name']}!")
                    if delivery_option == "Delivery":
                        st.info(f"Your order will be delivered in 20 minutes. Total cost: ₹{total_cost:.2f} (including ₹10.00 delivery cost).")
                    else:
                        st.info(f"You can pick up your order in 15 minutes. Total cost: ₹{total_cost:.2f}.")
            except ValueError as e:
                st.error(str(e))

    with tab2:
        st.header("Your Orders")
        if st.session_state.orders:
            st.table(st.session_state.orders)
        else:
            st.write("No orders placed yet.")

    with tab3:
        st.header("Add Amount to Wallet")
        amount = st.number_input("Enter amount to add", min_value=0.0, step=10.0)
        if st.button("Add Amount"):
            st.session_state.user_wallet += amount
            st.success(f"₹{amount:.2f} added to wallet!")

    with tab4:
        st.header("Profile")
        st.write("**Name:** Dr.Naveen Kumar")
        st.write("**Address:** Room Number 350, Pennar Hostel")
        st.write("**Phone:** +91 9876543210")
    
    display_wallet_balance()

if __name__ == "__main__":
    main()