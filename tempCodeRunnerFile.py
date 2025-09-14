# pairwise_compare
# print("=== Test 1: Pairwise Compare ===")
# print("A vs B:", pairwise_compare("A", "B", voters)) 
# print("B vs C:", pairwise_compare("B", "C", voters))
# print("C vs A:", pairwise_compare("C", "A", voters)) 

# # generate_swaps
# print("\n=== Test 2: Generate Adjacent Swaps ===")
# swapped_profiles = generate_swaps(voters)
# for i, profile in enumerate(swapped_profiles, start=1):
#     print(f"Profile {i}: {profile}")

# # is_condorcet_winner 
# print("\n=== Test 3: Condorcet Winner Check ===")
# for candidate in candidates:
#     print(f"{candidate} is Condorcet winner? {is_condorcet_winner(candidate, voters, candidates)}")

# # Dodgson Scores
# print("\n=== Test 4: Dodgson Scores ===")
# scores = {c: dodgson_score(c, voters, candidates) for c in candidates}
# print("Dodgson scores:", scores)
# winner = min(scores, key=scores.get)
# print("Dodgson winner:", winner)