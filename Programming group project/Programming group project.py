

import pandas as pd
import numpy as np
from faker import Faker
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Initialize Faker for generating random names
fake = Faker()

def generate_advanced_data(num_students=50):
    destinations = ['Barcelona', 'Reykjavik', 'Tokyo', 'Cape Town', 'New York', 'Sydney']
    activities = ['Cooking Class', 'Dance Lessons', 'Historical Tours', 'Adventure Sports', 'Art Tours', 'Music & Theatre']
    accommodations = ['Local Stays', 'Eco Lodges', 'Luxury Hotels', 'Hostels', 'Boutique Hotels', 'Apartments']
    foods = ['Street Food', 'Fine Dining', 'Seafood Feasts', 'Vegan Eats', 'Dessert Tours', 'Cooking with Chefs']
    transports = ['Public Transit', 'Bicycles', 'Mini-Buses', 'Walking Tours', 'Boat Rides', 'Car Rentals']
    genders = ['Male', 'Female']
    budget = np.random.randint(500, 1500, num_students)  # Budget in USD
    weights = np.random.randint(1, 5, num_students)  # Preference weights

    data = {
        'Gender': np.random.choice(genders, num_students),
        'Student': [fake.unique.first_name() for _ in range(num_students)],
        'Destination': np.random.choice(destinations, num_students),
        'Activity': np.random.choice(activities, num_students),
        'Accommodation': np.random.choice(accommodations, num_students),
        'Food': np.random.choice(foods, num_students),
        'Transport': np.random.choice(transports, num_students),
        'Budget': budget,
        'PreferenceWeight': weights
    }
    return pd.DataFrame(data)

def create_database(df, dbname="ClassTrip.db"):
    conn = sqlite3.connect(dbname)
    df.to_sql('preferences', conn, if_exists='replace', index=False)
    conn.close()

def analyze_preferences_from_db(dbname="ClassTrip.db"):
    conn = sqlite3.connect(dbname)
    query = "SELECT * FROM preferences"
    df = pd.read_sql(query, conn)
    conn.close()

    sns.set(style="whitegrid")
    # Analyzing and visualizing preferences creatively
    categories = ['Destination', 'Activity', 'Accommodation', 'Food', 'Transport']
    for category in categories:
        plt.figure(figsize=(10, 5))
        sns.barplot(x=category, y='PreferenceWeight', data=df, estimator=sum, ci=None, palette='viridis')
        plt.title(f'Sum of Weights for {category}')
        plt.xticks(rotation=45)
        plt.show()

    return df['Destination'].value_counts().idxmax()

df = generate_advanced_data()
create_database(df)
top_destination = analyze_preferences_from_db()

# Proposing a trip
print(f"The chosen destination based on preferences is {top_destination}.")
print("Proposed trip details:")
print("- Destination:", top_destination)
print("- Duration: 7 days, starting June 15th, 2024.")
print("- Activities: Based on the top preferences, include a mix of cooking classes, historical tours, and cultural shows.")
print("- Accommodation: Luxury Hotels or Boutique Hotels, based on availability and preference.")
print("- Transportation: Arrange for Public Transit passes and Mini-Buses for group travel.")
print("- Food: Organize street food tours and a few fine dining experiences.")
