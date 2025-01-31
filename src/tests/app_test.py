import pytest
import streamlit as st
from app import place_order, get_wallet_balance, food_items

def test_wallet_debit():
    st.session_state.user_wallet = 100
    place_order(food_items[0], "Pickup")
    assert get_wallet_balance() == 90

def test_wallet_debit_insufficient_funds():
    st.session_state.user_wallet = 5
    with pytest.raises(ValueError, match="Insufficient funds"):
        place_order(food_items[1], "Pickup")

def test_wallet_credit():
    st.session_state.user_wallet = 100
    st.session_state.user_wallet += 50
    assert get_wallet_balance() == 150

def test_place_order_pickup():
    st.session_state.user_wallet = 100
    success, total_cost = place_order(food_items[2], "Pickup")
    assert success
    assert get_wallet_balance() == 50
    assert total_cost == 50

def test_place_order_delivery():
    st.session_state.user_wallet = 100
    success, total_cost = place_order(food_items[2], "Delivery")
    assert success
    assert get_wallet_balance() == 40
    assert total_cost == 60

def test_place_order_insufficient_funds():
    st.session_state.user_wallet = 50
    with pytest.raises(ValueError, match="Insufficient funds"):
        place_order(food_items[1], "Delivery")