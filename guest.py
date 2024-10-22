def Total_Guest(n):
   
    if n <= 1:  # Base case for 1 guest
        return 1
    # Calculate the number of ways if the last guest attends alone
    way_single = Total_Guest(n-1)
    # Calculate the number of ways if the last two guests attend as a pair
    double_way = (n-1) * Total_Guest(n-2)
    # Total number of ways is the sum of both cases
    total = way_single + double_way
    return total

n = 4
answer = Total_Guest(n)
print(answer)
