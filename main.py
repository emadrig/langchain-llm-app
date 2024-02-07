import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Hamster","Snake"))
pet_color = st.sidebar.text_area(f"What is your pet {animal_type.lower()}'s color?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text(response["pet_name"])
