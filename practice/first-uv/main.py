import streamlit as st

def main():
    st.set_page_config(page_title="Weight on Different Planets", page_icon="🌍")
    st.title("Cosmo Weights")
    st.subheader("Enter your weight and get your weight on different planets")

    user_weight = st.number_input("Enter your current weight: ", min_value=0, max_value=1000, value=0, 
                                  )
 
    planet = st.text_input("Enter the planet name: ").strip().lower()

    gravity = {
        "mars": 0.378,
        "venus": 0.889,
        "mercury": 0.376,
        "jupiter": 2.36,
        "saturn": 1.081,
        "uranus": 0.815,
        "neptune": 1.14
    }


    def calculate_weight(user_weight, planet):
        if not planet:
            st.write("Please enter a planet name")
        elif planet in gravity:
            result = user_weight * gravity[planet]
            st.success(f"Your weight on {planet.capitalize()} is {result:.2f} kg")
     
        else:
            st.error("Invalid planet name. Please enter a valid planet.")
    
    calculate_weight(user_weight, planet)
if __name__ == "__main__":
    main()
