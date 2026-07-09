import pandas as pd
import pickle as pk
import streamlit as st

# Load trained model
model = pk.load(open('model.pkl', 'rb'))

st.title(" Car Price Prediction")

# Load dataset
car_data = pd.read_csv(r'D:\python\datasets\Cardetails.csv')

# Extract brand name
def get_brand_name(car_name):
    return car_name.split()[0]

car_data['name'] = car_data['name'].apply(get_brand_name)

# -------------------- Mapping Dictionaries --------------------

brand_map = {
    'Maruti':1, 'Skoda':2, 'Honda':3, 'Hyundai':4, 'Toyota':5,
    'Ford':6, 'Renault':7, 'Mahindra':8, 'Tata':9, 'Chevrolet':10,
    'Datsun':11, 'Jeep':12, 'Mercedes-Benz':13, 'Mitsubishi':14,
    'Audi':15, 'Volkswagen':16, 'BMW':17, 'Nissan':18, 'Lexus':19,
    'Jaguar':20, 'Land':21, 'MG':22, 'Volvo':23, 'Daewoo':24,
    'Kia':25, 'Fiat':26, 'Force':27, 'Ambassador':28,
    'Ashok':29, 'Isuzu':30, 'Opel':31
}

fuel_map = {
    'Diesel':1,
    'Petrol':2,
    'LPG':3,
    'CNG':4
}

seller_map = {
    'Individual':1,
    'Dealer':2,
    'Trustmark Dealer':3
}

transmission_map = {
    'Manual':1,
    'Automatic':2
}

owner_map = {
    'First Owner':1,
    'Second Owner':2,
    'Third Owner':3,
    'Fourth & Above Owner':4,
    'Test Drive Car':5
}

# -------------------- User Inputs --------------------

name = st.selectbox("Select Car Brand", sorted(car_data['name'].unique()))

year = st.slider("Manufacturing Year", 1994, 2024, 2020)

km_driven = st.slider("Kilometers Driven", 0, 300000, 50000)

fuel = st.selectbox("Fuel Type", list(fuel_map.keys()))

seller_type = st.selectbox("Seller Type", list(seller_map.keys()))

transmission = st.selectbox("Transmission", list(transmission_map.keys()))

owner = st.selectbox("Owner", list(owner_map.keys()))

mileage = st.slider("Mileage (km/l)", 5, 40, 20)

engine = st.slider("Engine (CC)", 700, 5000, 1200)

max_power = st.slider("Max Power (BHP)", 20, 250, 80)

seats = st.slider("Seats", 2, 10, 5)

# -------------------- Prediction --------------------

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        'name': [brand_map[name]],
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel_map[fuel]],
        'seller_type': [seller_map[seller_type]],
        'transmission': [transmission_map[transmission]],
        'owner': [owner_map[owner]],
        'mileage': [mileage],
        'engine': [engine],
        'max_power': [max_power],
        'seats': [seats]
    })

    prediction = model.predict(input_df)

    st.success(f"Estimated Car Price: ₹ {prediction[0]:,.2f}")