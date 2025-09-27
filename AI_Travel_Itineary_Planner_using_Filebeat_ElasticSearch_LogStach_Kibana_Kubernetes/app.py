from src.core.planner import TravelPlanner
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="AI Travel Planner")
st.title('AI Travel Itinerary Planner')
st.write('Plan your day trips by entering your City and Intrests')

with st.form('Planner form'):
    city= st.text_input('Enter the city name for your trip')
    interests= st.text_input('Enter your interests')
    submitted= st.form_submit_button('Generate Itinerary')

    if submitted:
        if city and interests:
            planner= TravelPlanner()
            planner.set_city(city)
            planner.set_intrests(interests)
            itinerary= planner.create_itinerary()

            st.subheader("📄 Your Itinerary")
            st.markdown(itinerary)
        else:
            st.warning('Please fill city and intrest to move forward')