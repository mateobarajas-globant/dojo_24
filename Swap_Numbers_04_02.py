def SwapNumbers(head):
    if not head or len(head) < 2:
        return head
    
    for i in range (0, len(head)-1, 2):
        head[i], head[i+1]  = head[i+1], head[i]

    return head

head = [1,2,3,4,5,6]

n_head = SwapNumbers(head)

print(n_head)
