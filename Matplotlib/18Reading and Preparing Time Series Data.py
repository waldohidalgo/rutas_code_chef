import pandas as pda

# Create sample data
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Sales': [100, 120, 110, 140, 130]
}

# Create the DataFrame
df = pda.DataFrame(data)

print(df.head())    # Dataframe before the conversion

# Convert 'Date' to datetime and set as index
df['Date'] = pda.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df.head())    # Dataframe after the conversion