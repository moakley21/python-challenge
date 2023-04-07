import os
import csv

total_votes = 0
candidates = {}
win_votes = 0

py_poll_csv = os.path.join('Resources', 'election_data.csv')

with open(py_poll_csv) as csvfile:
    pypoll = csv.reader(csvfile, delimiter =',')
    next(pypoll)

    for row in pypoll:
        total_votes += 1

        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    
   
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

   
    for candidate in candidates:
        votes = candidates[candidate]
        percentage = (votes/total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")


        if votes > win_votes:
            win_votes = votes
            winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


op_path = os.path.join("analysis","election_results.txt")

with open(op_path, "w") as txt:
    txt.write("Election Results\n")
    txt.write("-------------------------\n")
    txt.write(f"Total Votes: {total_votes}\n")
    txt.write("-------------------------\n")

    for candidate in candidates:
        votes = candidates[candidate]
        percentage = round((votes / total_votes) * 100, 3)
        txt.write(f"{candidate}: {percentage}% ({votes})\n")

    txt.write("-------------------------\n")
    txt.write(f"Winner: {winner}\n")
    txt.write("-------------------------\n")