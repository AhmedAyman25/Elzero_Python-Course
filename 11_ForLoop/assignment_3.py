# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
A,B,C = 100,80,40
total_points = 0
for rank_key, rank_value in my_ranks.items():
    if rank_value == 'A':
        print(f"My Rank in {rank_key} Is A And This Equal {A} Points")
        total_points += A
    elif rank_value == 'B':
        print(f"My Rank in {rank_key} Is A And This Equal {B} Points")
        total_points += B
    elif rank_value == 'C':
        print(f"My Rank in {rank_key} Is A And This Equal {C} Points")
        total_points += C
print(f"Total Points Is {total_points}")
