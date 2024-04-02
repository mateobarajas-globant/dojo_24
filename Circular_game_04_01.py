def findTheWinner(n, k):
    player = list(range(1, n + 1))
    i = 0
    
    while len(player) > 1:
        i = (i + k - 1) % len(player)
        player.pop(i)
    
    return player[0]

n = 5
k = 2
print(findTheWinner(n, k))