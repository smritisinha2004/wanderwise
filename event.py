import streamlit as st
from datetime import datetime

with open('styles.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Dummy data for events (replace with your own data)
events = [
    {"name": "GO GOA GONE", "date": "2024-03-28", "location": "Goa"},
    {"name": "Trip to Wayanad", "date": "2024-04-01", "location": "Wayanad"},
    {"name": "Trip to Kashmir", "date": "2024-03-28", "location": "Kashmir"}
]

def create_event():
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Date", min_value=datetime.now())
    event_location = st.text_input("Location")
    event_description = st.text_area("Description")
    if st.button("Create Event"):
        # Code to save the event to a database or data structure
        st.success("Event created successfully!")

def display_events(events):
    st.write("Upcoming Events:")
    for idx, event in enumerate(events, start=1):
        st.write(f"{idx}. {event['name']} - {event['date']} - {event['location']}")

def filter_events(events, search_text, selected_date, selected_location):
    filtered_events = []
    for event in events:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d")
        if (not search_text or search_text.lower() in event["name"].lower()) and \
           (not selected_date or event_date == selected_date) and \
           (not selected_location or selected_location.lower() in event["location"].lower()):
            filtered_events.append(event)
    return filtered_events

def main():
    st.title("Holiday Event Planner")
    st.sidebar.title("Menu")
    menu_options = ["Create Event", "View Events"]
    selected_option = st.sidebar.selectbox("Select Option", menu_options)

    if selected_option == "Create Event":
        create_event()
    elif selected_option == "View Events":
        search_text = st.sidebar.text_input("Search Events")
        selected_date = st.sidebar.date_input("Select Date")
        selected_location = st.sidebar.text_input("Select Location")
        
        # Filter events based on search criteria
        filtered_events = filter_events(events, search_text, selected_date, selected_location)
        
        # Display filtered events
        display_events(filtered_events)

if __name__ == "__main__":
    main()
