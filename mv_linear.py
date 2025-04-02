import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data (1000 samples)
size = np.random.randint(500, 5000, 1000)  # House Size in sq ft
bedrooms = np.random.randint(1, 6, 1000)   # Number of Bedrooms
location = np.random.randint(1, 11, 1000)  # Location Score (1-10)
age = np.random.randint(1, 51, 1000)       # Age of House in Years

# Generate House Prices with some noise
price = (size * 300) + (bedrooms * 50000) + (location * 20000) - (age * 2000) + np.random.randint(-20000, 20000, 1000)

# Create DataFrame
df = pd.DataFrame({"Size": size, "Bedrooms": bedrooms, "Location": location, "Age": age, "Price": price})

# Save to CSV
csv_filename = "house_price_data.csv"
df.to_csv(csv_filename, index=False)

print(f"✅ Dataset saved as '{csv_filename}' with {df.shape[0]} rows and {df.shape[1]} columns.")
