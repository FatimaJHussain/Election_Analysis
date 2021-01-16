

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load =os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
   reader=csv.reader(election_data)
   # Read and print the header row.
   headers = next(reader)
   print(headers)
     #To do: perform analysis.
   for row in reader:
          print(reader)

