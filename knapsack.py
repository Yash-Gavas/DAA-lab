def knapsack(items, max_weight):
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if items[i-1][1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][1]] + items[i-1][2])
            else:
                dp[i][w] = dp[i-1][w]
    
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(items[i-1])
            w -= items[i-1][1]
    
    selected_items.reverse()
    return dp[n][max_weight], selected_items

def get_user_input():
    items = []
    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        item_id = int(input(f"Enter the ID for item {i + 1}: "))
        weight = int(input(f"Enter the weight for item {i + 1}: "))
        value = int(input(f"Enter the value for item {i + 1}: "))
        items.append((item_id, weight, value))
    max_weight = int(input("Enter the maximum weight for the knapsack: "))
    return items, max_weight

items, max_weight = get_user_input()
max_value, selected_items = knapsack(items, max_weight)
print("Maximum Value:", max_value)
print("Selected Items:", selected_items)
