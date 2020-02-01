# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
#/Users/danielagioia/Desktop/Data/Election_Analysis

# # Assign a variable for the file to load and the path.
# file_to_load = 'election_results.csv'

# # Open the election results and read the file.
# with open (file_to_load) as election_data:

#     #to do performance analysis.
#     print(election_data)

# #Add our dependencies.
# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#      # Write three counties to the file.
#      txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")

#to retrieve the first item from each row
# for row in file_reader:

#     print(row[0])

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
#Declare a new Dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

  # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #   # Print the header row.
    # headers = next(file_reader)
    # print(headers)

      # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count. This formula is the same as number = number + 1
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
           # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

         # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

             # 2. Add to the total vote count. This formula is the same as number = number + 1
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = round((int(votes) / int(total_votes) * 100),2)
        # # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate}: received {vote_percentage}% of the vote.") 

        # # To do: print out each candidate's name, vote count, and percentage of
        # # votes to the terminal.
        # print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count= votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    # winning_candidate_summary = (
    #     f"-------------------------\n"
    #     f"Winner: {winning_candidate}\n"
    #     f"Winning Vote Count: {winning_count:,}\n"
    #     f"Winning Percentage: {winning_percentage:.1f}%\n"
    #     f"-------------------------\n")
    # print(winning_candidate_summary)
    

    # # 3. Print the total votes.
    # print(total_votes)

    # print(candidate_options)

    # print(candidate_votes)

    # print (winning_candidate)
    
    # Print the final vote count to the terminal.
    candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    print(candidate_results)
      

    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    #  Save the candidate results to our text file.
    txt_file.write(candidate_results)
