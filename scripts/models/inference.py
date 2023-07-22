import json
import joblib
import pandas as pd

model = joblib.load('./models/sc-model.joblib')
# config = json.load(open('./models/config.json'))

dt = {'host_response_rate': {2562: 100.0},
 'host_acceptance_rate': {2562: 100.0},
 'host_total_listings_count': {2562: 2.0},
 'neighbourhood': {2562: 45},
 'accommodates': {2562: 2},
 'bathrooms': {2562: 0.0},
 'bedrooms': {2562: 1.0},
 'beds': {2562: 1.0},
 'security_deposit': {2562: 287.61039657020365},
 'cleaning_fee': {2562: 15.0},
 'number_of_reviews': {2562: 14},
 'review_scores_rating': {2562: 97.0},
 'weighted_rating_score': {2562: 1358.0},
 'host_response_time_within a day': {2562: 0},
 'host_response_time_within a few hours': {2562: 0},
 'host_response_time_within an hour': {2562: 1},
 'host_is_superhost_t': {2562: 0},
 'host_identity_verified_t': {2562: 1},
 'property_type_Bed & Breakfast': {2562: 0},
 'property_type_Boat': {2562: 0},
 'property_type_Bungalow': {2562: 0},
 'property_type_Cabin': {2562: 0},
 'property_type_Camper/RV': {2562: 0},
 'property_type_Chalet': {2562: 0},
 'property_type_Condominium': {2562: 0},
 'property_type_Dorm': {2562: 0},
 'property_type_House': {2562: 1},
 'property_type_Loft': {2562: 0},
 'property_type_Other': {2562: 0},
 'property_type_Tent': {2562: 0},
 'property_type_Townhouse': {2562: 0},
 'property_type_Treehouse': {2562: 0},
 'property_type_Yurt': {2562: 0},
 'room_type_Private room': {2562: 1},
 'room_type_Shared room': {2562: 0},
 'bed_type_Couch': {2562: 0},
 'bed_type_Futon': {2562: 0},
 'bed_type_Pull-out Sofa': {2562: 0},
 'bed_type_Real Bed': {2562: 1},
 'cancellation_policy_moderate': {2562: 1},
 'cancellation_policy_strict': {2562: 0}}


data = pd.DataFrame(dt)
# data = pd.read_csv("./data/data.csv")
# data.columns = ["feat_" + str(col) for col in data.columns]


predictions = model.predict(data)  # or model.predict_proba(data)
