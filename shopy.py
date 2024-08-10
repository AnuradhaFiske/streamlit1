import streamlit as st

# Sample product data
cosmetics = {
    "Lipstick": 15.00,
    "Mascara": 20.00,
    "Foundation": 30.00,
    "Eyeliner": 10.00
}

skincare = {
    "Face Cream": 25.00,
    "Sunscreen": 20.00,
    "Cleanser": 18.00,
    "Toner": 15.00
}

def display_products(category, products):
    st.subheader(f"{category} Products")
    cart = []

    for product, price in products.items():
        if st.checkbox(f"{product} - ${price:.2f}", key=product):
            cart.append((product, price))

    return cart

def main():
    st.title("Shopping App")

    st.sidebar.title("Categories")
    category = st.sidebar.radio("Select a category", ["Cosmetics", "Skin Care"])

    if category == "Cosmetics":
        selected_products = display_products("Cosmetics", cosmetics)
    else:
        selected_products = display_products("Skin Care", skincare)

    if selected_products:
        st.subheader("Your Cart")
        total_price = 0.0
        for product, price in selected_products:
            st.write(f"{product} - ${price:.2f}")
            total_price += price
        st.write(f"Total Price: ${total_price:.2f}")
    else:
        st.write("Your cart is empty.")

if __name__ == "__main__":
    main()
