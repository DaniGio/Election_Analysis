# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
#/Users/danielagioia/Desktop/Data/Election_Analysis

#Challenge: 
# determine the number of votes that were cast from each county 
# and the percentage of votes each county contributed to the election.
# Extend your use of for loops and conditionals with membership and logical operators.
# Scope and refactor code to provide additional information.
# Write data to an output file and print the file.


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0 
#Declare a new list
candidate_options = []
#Create a list of the counties
counties_list = []
#Declare a new Dictionary
candidate_votes = {}
counties_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largest_turnout = ""
county_count = 0
county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)


      # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count. This formula is the same as number = number + 1
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
           # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

             # Add a vote to that candidate's count. This formula is the same as number = number + 1
        candidate_votes[candidate_name] += 1

          # Print each row in the CSV file.
    # for row in file_reader:
        # Add to the total vote count. This formula is the same as number = number + 1
        # total_votes += 1
        # Print the conties name from each row
        county_name = row[1]
           # If the counties does not match any existing county...
        if county_name not in counties_list:
            # Add it to the list of counties.
            counties_list.append(county_name)

            # Begin tracking that counties's vote count. 
            counties_votes[county_name] = 0

             # Add a vote to that counties's count. This formula is the same as number = number + 1
        counties_votes[county_name] += 1


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

# Print the winning conties's results to the terminal.
    counties_votes_txt= (
        f"\nCounties Votes:\n")
    print(counties_votes_txt)
    txt_file.write(counties_votes_txt)
#Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the counties list.
    for county in counties_votes:
            #Retrieve votes count of a county.
        votes = counties_votes[county]
            # Calculate the percentage of votes.
        vote_percentage = round((int(votes) / int(total_votes) * 100),2)
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
       

        # Print each candidate's voter count and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)


     # Determine largest county counte
        # Determine if the votes is greater than the winning count.
        if (votes > county_count) and (vote_percentage > county_percentage):
            # And, set the winning_candidate equal to the candidate's name.
            county_count = votes
            county_percentage = vote_percentage
            largest_turnout = county



    largest_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
    print(largest_turnout_summary)
    # Save the largest_turnout_'s results to the text file.
    txt_file.write(largest_turnout_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = round((int(votes) / int(total_votes) * 100),2)
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count= votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate


# Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)













    




    