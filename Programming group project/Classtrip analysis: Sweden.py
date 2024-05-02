import pandas as pd
import numpy as np
from faker import Faker
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize Faker for generating random names
fake = Faker()

def generate_data(num_students=50):
    # Enforcing controlled randomness for preferences
    accommodations = ['Small Houses by the Lake'] * int(num_students * 0.6) + \
                     np.random.choice(['Luxury Hotels', 'Hostels', 'Boutique Hotels', 'Apartments'],
                                      size=int(num_students * 0.4), replace=True).tolist()
    np.random.shuffle(accommodations)

    foods = ['Traditional Swedish Food'] * int(num_students * 0.5) + \
            ['Cooking with Chefs'] * int(num_students * 0.2) + \
            np.random.choice(['Street Food', 'Fine Dining', 'Seafood Feasts', 'Vegan Eats', 'Dessert Tours'],
                             size=num_students - int(num_students * 0.7), replace=True).tolist()
    np.random.shuffle(foods)

    activities = ['Poker Games'] * int(num_students * 0.4) + \
                 np.random.choice(['Fishing', 'Barbecue Grilling', 'Boat Driving', 'Hiking', 'Wildlife Watching',
                                   'Canoeing', 'Sightseeing', 'Clubbing'],
                                  size=num_students - int(num_students * 0.4), replace=True).tolist()
    np.random.shuffle(activities)

    transports = np.random.choice(['Cars', 'Ferry', 'Bicycles', 'Walking Tours', 'Public Transit', 'Private Coaches'],
                                  num_students, replace=True)

    data = {
        'Student': [fake.unique.first_name() for _ in range(num_students)],
        'Accommodation': accommodations,
        'Food': foods,
        'Activity': activities,
        'Transport': transports
    }
    return pd.DataFrame(data)

df = generate_data()

# Visualization of data
def visualize_data(df):
    # Pie charts for accommodations and food preferences
    for category in ['Accommodation', 'Food', 'Activity']:
        plt.figure(figsize=(8, 8))
        counts = df[category].value_counts()
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
        plt.title(f'{category} Preferences')
        plt.show()

    # Bar chart for transportation preferences
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Transport', palette='viridis')
    plt.title('Transportation Preferences')
    plt.xticks(rotation=45)
    plt.show()

visualize_data(df)

# Final trip solution based on the preferences
print("Finalized trip details:")
print("- Destination: Small Town by a Lake in Sweden")
print("- Duration: 5 days")
print("- Activities: Fishing, Barbecue Grilling, Boat Driving, Sightseeing, Clubbing, and Poker Games")
print("- Accommodation: Small Houses next to the Lake")
print("- Transportation: Mainly Cars, with arrival via Ferry")
print("- Food: A mix of Traditional Swedish Food, Taco Evening, and Cooking with Chefs")
