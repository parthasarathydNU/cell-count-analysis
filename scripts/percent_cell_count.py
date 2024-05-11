# Importing required libraries
import pandas as pd

# Importing data
try:
    # Load the data
    data = pd.read_csv('data/cell-count.csv')

    # Display the first few rows of the data frame
    print("===============Succesfully loaded data:===============")
    print(data.head())

    # Basic Operation: Calculate the total number of samples
    total_samples = data.shape[0]
    print(f"Total  number of samples: {total_samples}")

    populations = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]

    # Calculate total count of each sample
    data['total_count'] = data[populations].sum(axis=1)

    # Prepare the output DataFrame
    output = pd.DataFrame()

    # Loop through each population to calculate percentage
    for population in populations:
        temp_df = pd.DataFrame()
        temp_df['sample'] = data['sample']
        temp_df['total_count'] = data['total_count']
        temp_df['population'] = population
        temp_df['count'] = data[population]
        temp_df['percentage'] = (data[population] / data['total_count']) * 100
        output = pd.concat([output, temp_df])

    # Updating the index values before saving as CSV
    output = output.reset_index(drop=True)

    # Save the processed data to a new CSV file
    output.to_csv("data/updated-cell-count.csv", index=False)

    print("===============Succesfully uploaded data to data/updated-cell-count.csv:===============")
    print(output.head())
except Exception as e:
    print(f"An error occured: {e}")
