from time import perf_counter

def heuristic(voters, candidates):
    candidate_scores = {c: 0 for c in candidates}
    for pref in voters.values():
        for idx, cand in enumerate(pref): 
            candidate_scores[cand] += idx
    return min(candidate_scores.keys()) 
            
        
    
def main():
    start_time = perf_counter()
    
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

    # # Dodgson Scores
    # print("\nTest 3: Dodgson Scores")
    # scores = {c: dodgson_score(c, voters, candidates) for c in candidates}
    # print("Dodgson scores:", scores)
    # winner = min(scores, key=scores.get)
    # print("Dodgson winner:", winner)
    
    heu = heuristic(voters, candidates)
    print("Dodgson:", heu)
    
    end_time = perf_counter()
    elapsed_time = end_time - start_time

    print(f"Program finished in {elapsed_time:.6f} seconds.")
    
if __name__ == "__main__":
    main()
