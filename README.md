# [Link to Webapp](https://ds-project.onrender.com/)

# App For Inference and Shap

* This is a flask app that serves inference on review dataset ([for reference check 1](https://github.com/sachinraina112/reviews-seattle-airbnb)).
* This is a dummy app for visualizing shap values from trained model listed in 1 using Plotly. The application 
takes an user input in form of a json(Example refer below) and gives top ten features contributing most to prediction.

## Getting Started 

This flask app can be used as a template for visualizing your own data. Use
the template to enhance your professional portfolio. 

## Prerequisites

To install the flask app, you need:
- python3
- python packages in the requirements.txt file
 
 Install the packages with
``` 
 pip install -r requirements.txt
```

## Installing

* On a MacOS/linux system/Windows, installation is easy. Open a terminal, and go into 
the directory with the flask app files (app directory)
* Add following line `app.run(host='0.0.0.0', port=3001, debug=True)` to file routes.py.
* Run `python app/routes.py` in the terminal from app directory.

## Example
````
{"dt_" : {"host_response_rate": 10000.0,
 "host_acceptance_rate": 10000.0,
 "host_total_listings_count": 2.0,
 "neighbourhood": 45,
 "accommodates": 20000,
 "bathrooms": 0.0,
 "bedrooms": 1.0,
 "beds": 0.0,
 "security_deposit": 287.61039657020365,
 "cleaning_fee": 15.0,
 "number_of_reviews": 14000,
 "review_scores_rating": 9700.0,
 "weighted_rating_score": 135800.0,
 "host_response_time_within a day": 0,
 "host_response_time_within a few hours": 0,
 "host_response_time_within an hour": 1,
 "host_is_superhost_t": 0,
 "host_identity_verified_t": 1,
 "property_type_Bed & Breakfast": 14000,
 "property_type_Boat": 0,
 "property_type_Bungalow": 0,
 "property_type_Cabin": 0,
 "property_type_Camper/RV": 0,
 "property_type_Chalet": 0,
 "property_type_Condominium": 0,
 "property_type_Dorm": 0,
 "property_type_House": 1,
 "property_type_Loft": 0,
 "property_type_Other": 0,
 "property_type_Tent": 0,
 "property_type_Townhouse": 0,
 "property_type_Treehouse": 10000,
 "property_type_Yurt": 0,
 "room_type_Private room": 1,
 "room_type_Shared room": 0,
 "bed_type_Couch": 0,
 "bed_type_Futon": 0,
 "bed_type_Pull-out Sofa": 0,
 "bed_type_Real Bed": 1,
 "cancellation_policy_moderate": 10000,
 "cancellation_policy_strict": 0}}

````
Just go to [Link to Webapp](https://ds-project.onrender.com/)
and enter above json in search tab.
