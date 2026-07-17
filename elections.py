# Function to count seats won by each party
def count_seats(filename):
    party_count = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            # Skip empty lines
            if line == "":
                continue

            data = line.split()

            # Skip headings or invalid rows
            if not data[0].isdigit():
                continue

            # Winner's party is the 5th item from the end:
            # ... Winner Gender Party WinnerVotes Runner RunnerGender RunnerParty RunnerVotes
            winner_party = data[-6]

            if winner_party in party_count:
                party_count[winner_party] += 1
            else:
                party_count[winner_party] = 1

    return party_count


# Store results for all years
results = {
    "2004": count_seats("elections2004.txt"),
    "2009": count_seats("elections2009.txt"),
    "2014": count_seats("elections2014.txt")
}

# Print in the required format
print("(")
for year, parties in results.items():
    print(f"'{year}':(", end="")
    first = True
    for party, seats in parties.items():
        if not first:
            print(",", end="")
        print(f"'{party}':{seats}", end="")
        first = False
    print("),")
print(")")