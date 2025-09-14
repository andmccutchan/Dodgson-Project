import itertools #helper library for more efficient pairwise looping.

def dodgson_rule(voters, candidates): 
    candidate_scores = {c: 0 for c in candidates}
    for a, b in itertools.combinations(candidates, 2):
        winner = pairwise_compare(a, b, voters)
        candidate_scores[winner] += 1
    for candidate, score in candidate_scores.items():
        if score == len(candidates) - 1:
            return candidate
        else: 
            return 0
            #here is where will compute dodgson scores     
                  
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
        
    

candidates = ["A", "B", "C", "D"]
voters = {
    1: ["A", "B", "C", "D"],
    2: ["A", "C", "D", "B"],
    3: ["A", "C", "B", "D"]
}

winner = dodgson_rule(voters, candidates)
if winner == 0:
    print("No winner")
else:
    print(winner)    
            
            


         
    