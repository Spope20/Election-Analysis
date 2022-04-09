# Retrevie Data
import csv
import random
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize variables needed for pypolls
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Opens the election results csv in read mode
with open(file_to_load) as election_data:
    print(election_data)

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print header row
    headers = next(file_reader)
    print(headers)

    # loop through the csv to retieve data
    for row in file_reader:
        # add upp the number of votes recieved
        total_votes += 1

        # find all candidate
        candidate_name = row[2]

        # test if candidate is already accounted for
        if candidate_name not in candidate_options:
            # add candidate to list
            candidate_options.append(candidate_name)

            # creates a new entry to tally votes
            candidate_votes[candidate_name] = 0
        
        # add up the number of votes for each candidate
        candidate_votes[candidate_name] += 1

# save poll results

with open(file_to_save, 'w') as txt_file:
    election_results = (f"\nElection Results\n"
                        f"-------------------------\n"
                        f"Total Votes: {total_votes:,}\n"
                        f"-------------------------\n")

    print(election_results, end="")

    # save the file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # votes to termina;.
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
    
    #print(winning_Candidate_summary)


