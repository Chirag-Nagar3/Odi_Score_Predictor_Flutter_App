import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('pipe.pkl', 'rb'))

st.title("ODI Cricket Score Predictor")

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka',
    'Netherlands'
]

cities = ['Colombo',
          'London',
          'Mirpur',
          'Sydney',
          'Centurion',
          'Melbourne',
          'Abu Dhabi',
          'Rangiri',
          'Adelaide',
          'Birmingham',
          'Johannesburg',
          'Dubai',
          'Perth',
          'Auckland',
          'Karachi',
          'Hamilton',
          'Brisbane',
          'Wellington',
          'Cardiff',
          'Manchester',
          'Pallekele',
          'Lahore',
          'Cape Town',
          'Durban',
          'Sharjah',
          'Southampton',
          'Chandigarh',
          'Nottingham',
          'Port Elizabeth',
          'Christchurch',
          'Leeds',
          'Hambantota',
          'Napier',
          'Chester-le-Street',
          'Hobart',
          'Dhaka',
          'Mumbai',
          'Mount Maunganui',
          'Rawalpindi',
          'Nagpur',
          'Dunedin',
          'Bloemfontein',
          'Delhi',
          'Chittagong',
          'Hyderabad',
          'Pune',
          'Paarl',
          'Fatullah',
          'Chattogram',
          'Dambulla',
          'Kolkata',
          'Rajkot',
          'Jaipur',
          'Bristol',
          'Nelson',
          'Ahmedabad',
          'Ranchi',
          'Visakhapatnam',
          'Indore',
          'Kimberley',
          'Canberra',
          'Harare',
          'Kanpur',
          'Chennai',
          'Kandy',
          'Cuttack',
          'Cairns',
          'Trinidad',
          'Bangalore',
          'Amstelveen',
          'Grenada',
          'East London',
          'Potchefstroom',
          'Guwahati',
          'Multan',
          'Vadodara',
          'St Kitts',
          'Darwin',
          'Antigua',
          'Doha',
          'Guyana',
          'Faisalabad',
          'Gqeberha',
          'Gwalior',
          'Rotterdam',
          'Queenstown',
          'Belfast',
          'Barbados',
          'Peshawar',
          'Margao',
          'Jamaica',
          'Bengaluru',
          'Dublin',
          'Kochi',
          'Kuala Lumpur']

batting_team_col, bowling_team_col = st.columns(2)

with batting_team_col:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with bowling_team_col:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select City', sorted(cities))

current_score_col, over_done_col, wickets_fall_col = st.columns(3)

with current_score_col:
    current_score = st.number_input('Current Score')
with over_done_col:
    overs = st.number_input('Overs Done (Works for over > 5)')
with wickets_fall_col:
    wickets = st.number_input('Wickets Fall')

last_five_over_runs = st.number_input('Runs scored in last 5 Overs')

if st.button('Predict Score'):
    balls_left = 300 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score / overs

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'current_score': [current_score],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'crr': [crr],
        'last_five': [last_five_over_runs]
    })

    result = model.predict(input_df)
    st.header("Predicted Score : " + str(int(result[0])))
