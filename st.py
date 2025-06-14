# Importing streamlit
import streamlit as st

# Designing
st.title("AI Blogger")
st.subheader("Find the best restraunts and cafes near you")

# Place selectbox
with st.expander('Section 1 - Choose THe Place.'):
    places = ['Restaurant', 'Cafe', 'Both']
    place = st.selectbox('Where do you want to go?', places)

# Uber selectbox
Uber_options = [
    'Yes, call uber', 
    'No, show me location', 
    'Yes, call uber & show me location'
]
with st.sidebar:
    st.selectbox('Do you want use uber for delivery?', Uber_options)
    distance = st.slider(
    'What is the maximum distance for this place? (km)',
    min_value=1,
    max_value=30,
    value=10)

# Step 4: Checking the place
with st.expander('Section 2 - Choose your prefernences & Submit'):
    col1, col2 = st.columns(2)

    with  col1:
        if place != 'Cafe':
            meals = ['Breakfast', 'Lunch', 'Dinner', 'Dessert']
            meal = st.selectbox('What meal do you want?', meals)

            if meal == 'Breakfast':
                options = ['Egyptian(Foul & Ta3mia)','Eggs', 'Milk and Cheese', 'Pastries']

            elif meal == 'Lunch' or meal == 'Dinner':
                options = ['Fried Chicken','Beef', 'Pizza & Pasta (Italian)', 'Koshary']

            elif meal == 'Dessert':
                options = ['Waffle','Ice cream', 'Molten cake', 'Rice pudding']
                
            choice = st.selectbox('Choose What do you want to eat?', options)
        else:
            categories = ['Hot drinks', 'Cold Drinks', 'Desserts']
            category = st.selectbox('Choose A Category', categories)

            if category == 'Hot drinks':
                options = ['Tea', 'Hot chocolate', 'Coffee', 'Latte']
            elif category == 'Cold Drinks':
                options = ['Soda', 'Juice', 'Ice tea', 'Ice coffee']
            else:
                options = ['Waffle', 'Ice cream','Molten cake']

            choice = st.selectbox('Choose What Do You Want?', options)


    with col2:
        if st.button('Submit order'):
            st.success('Your order is placed successfully')
        else:
            st.warning('Hurry up! we will be closed within 30 minutes')
        

