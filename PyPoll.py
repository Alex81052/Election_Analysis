# Add our dependencies
import csv
import os 
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path. 
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the csv file.
    #for row in file_reader:
        #print(row)
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
#Using the with statement open the file as text file.
#outfile = open(file_to_save, "w")
#with open(file_to_save, "w") as txt_file:
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
    #txt_file.write("Hello World")
    #txt_file.write("Araphoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Counties_in_the_Election")
    #txt_file.write("Counties_in_the_Election\n------------------------\nArapahoe\nDenver\nJefferson")      
# Close the file
#outfile.close()
 

#election_data = open(file_to_load, 'r')


    #To do: read and analyze the data here.
    #print(election_data)
#Close the file.
#election_data.close() 
# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote 