def open_second(queue):
    total_items = sum(queue)
    estimated_time = (total_items // 5) * 1
    if total_items % 5 != 0:
        estimated_time += 1
    if estimated_time > 10:
        return True
    else:
        return False

queue = [15, 1, 7, 12] 
if open_second(queue):
    print("Open a second.")
else:
    print("Keep one.")
