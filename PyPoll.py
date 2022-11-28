# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election base on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Perform  analysis
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)


# # Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
