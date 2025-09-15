def is_condorcet_winner(candidate, voters, candidates):
    for others in candidates:
        if others == candidate:
            continue
        result = pairwise_compare(candidate , others, voters)
        if result != candidate and result != 0:
            return False
    return True

def generate_swaps(voters):
    swapped_voters = []
    for voter, preferences in voters.items():
        for i in range(len(preferences) - 1):
            new_voters = {k: list(v) for k, v in voters.items()}
            new_preference = new_voters[voter]
            new_preference[i], new_preference[i+1] = new_preference[i+1], new_preference[i]
            new_voters[voter] = new_preference
            swapped_voters.append(new_voters)
    return swapped_voters

def dodgson_score(candidate, voters, candidates):
    if is_condorcet_winner(candidate, voters, candidates):
        return 0
    
    swaps = 0
    current_profiles = [voters]
    
    while True:
        swaps += 1
        next_profiles = []
        for profile in current_profiles:
            for new_profile in generate_swaps(profile):
                if is_condorcet_winner(candidate, new_profile, candidates):
                    return swaps
                next_profiles.append(new_profile)
        current_profiles = next_profiles
                  
def pairwise_compare(candidateA, candidateB, voters):
    candidateA_wins = 0
    candidateB_wins = 0
    for preference in voters.values():
        if preference.index(candidateA) < preference.index(candidateB):
            candidateA_wins += 1
        else:
            candidateB_wins += 1
    if candidateA_wins == candidateB_wins:
        return 0
    elif candidateA_wins > candidateB_wins:
        return candidateA
    else: 
        return candidateB
        
    
def main():
    def read_election_file(filename):
        candidates = []
        voters = {}

        with open(filename, 'r') as f:
            lines = f.readlines()
        
        candidates = lines[0].strip().split()

        for line in lines[1:]:
            parts = line.strip().split()
            if len(parts) < 2:
                continue  
            voter_id = int(parts[0])
            ranking = parts[1:]
            voters[voter_id] = ranking

        return candidates, voters


    filename = "election.txt" 
    candidates, voters = read_election_file(filename)

    print("Candidates:", candidates)
    print("Voters:")
    for voter, ranking in voters.items():
        print(voter, ranking)


    # pairwise_compare
    # print("Test 1: Pairwise Compare")
    # print("A vs B:", pairwise_compare("A", "B", voters)) 
    # print("B vs C:", pairwise_compare("B", "C", voters))
    # print("C vs A:", pairwise_compare("C", "A", voters)) 

    # # generate_swaps
    # print("\nTest 2: Generate Adjacent Swaps")
    # swapped_profiles = generate_swaps(voters)
    # for i, profile in enumerate(swapped_profiles, start=1):
    #     print(f"Profile {i}: {profile}")

    # Dodgson Scores
    print("\nTest 3: Dodgson Scores")
    scores = {c: dodgson_score(c, voters, candidates) for c in candidates}
    print("Dodgson scores:", scores)
    winner = min(scores, key=scores.get)
    print("Dodgson winner:", winner)
if __name__ == "__main__":
    main()
