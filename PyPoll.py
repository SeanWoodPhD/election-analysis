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

# Initialize a total vote counter.
total_votes = 0

# Initialize new list for candidate options.
candidate_options = []

# Declare an empty dictionary for candidate votes.
candidate_votes = {}

# Winning candidate and winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Perform  analysis
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Go through each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")

        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the perecentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list.
        for candidate_name in candidate_votes:

            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]

            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # Print the candidate name, vote count, and percentage of votes.
            # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            # Save the candidate results to our text file.
            txt_file.write(candidate_results)
            

            #Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_candidate_summary)

        txt_file.write(winning_candidate_summary)


# # Print the total votes.
# print(total_votes)

# # Print the candidate list.
# print(candidate_options)

# # Print candidates' votes.
# print(candidate_votes)

# # Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
