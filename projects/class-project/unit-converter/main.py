import streamlit as st
from streamlit_option_menu import option_menu
def main():
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Settings'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
        selected
    


if __name__ == "__main__":
    main()