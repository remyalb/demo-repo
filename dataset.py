import pandas as pd

# Creating a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}
df = pd.DataFrame(data)
# Displaying the dataset
df.head(1)
