from time import perf_counter

def pairwise_compare(candidateA, candidateB, voters, cache):
    """
    Compare candidateA vs candidateB in a given profile (voters).
    Uses caching to avoid recomputation.
    """
    profile_key = profile_to_key(voters)
    cache_key = (profile_key, candidateA, candidateB)

    if cache_key in cache:
        return cache[cache_key]

    candidateA_wins = 0
    candidateB_wins = 0
    for preference in voters.values():
        if preference.index(candidateA) < preference.index(candidateB):
            candidateA_wins += 1
        else:
            candidateB_wins += 1

    if candidateA_wins == candidateB_wins:
        result = 0
    elif candidateA_wins > candidateB_wins:
        result = candidateA
    else:
        result = candidateB

    cache[cache_key] = result
    return result


def is_condorcet_winner(candidate, voters, candidates, cache):
    for other in candidates:
        if other == candidate:
            continue
        result = pairwise_compare(candidate, other, voters, cache)
        if result != candidate and result != 0:
            return False
    return True


def generate_swaps(voters):
    swapped_voters = []
    for voter, preferences in voters.items():
        for i in range(len(preferences) - 1):
            new_voters = {k: list(v) for k, v in voters.items()}
            new_preference = new_voters[voter]
            # adjacent swap
            new_preference[i], new_preference[i+1] = new_preference[i+1], new_preference[i]
            new_voters[voter] = new_preference
            swapped_voters.append(new_voters)
    return swapped_voters


def profile_to_key(voters):
    """
    Convert a profile (dict of voter -> preference list) into
    a hashable, sorted tuple of tuples.
    """
    return tuple(sorted((v, tuple(p)) for v, p in voters.items()))


def dodgson_score(candidate, voters, candidates):
    cache = {}  # pairwise comparison cache
    if is_condorcet_winner(candidate, voters, candidates, cache):
        return 0
    
    swaps = 0
    current_profiles = [voters]
    visited = {profile_to_key(voters)}  # track visited profiles
    
    while current_profiles:
        swaps += 1
        next_profiles = []
        for profile in current_profiles:
            for new_profile in generate_swaps(profile):
                pk = profile_to_key(new_profile)
                if pk in visited:
                    continue
                visited.add(pk)

                if is_condorcet_winner(candidate, new_profile, candidates, cache):
                    return swaps
                next_profiles.append(new_profile)
        current_profiles = next_profiles
    
    return float("inf")  # should not happen in valid elections


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

    print("\nTest 3: Dodgson Scores")
    scores = {c: dodgson_score(c, voters, candidates) for c in candidates}
    print("Dodgson scores:", scores)
    winner = min(scores, key=scores.get)
    print("Dodgson winner:", winner)
    
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    print(f"Program finished in {elapsed_time:.6f} seconds.")


if __name__ == "__main__":
    main()
