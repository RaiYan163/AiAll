def custom_pruning(limit, index, is_max, scores, a_val, b_val):

    if limit == 3:
        return scores[index]

    if is_max:
        best_val = -1000  
        for i in range(0, 2):
            val = custom_pruning(limit + 1, index * 2 + i, False, scores, a_val, b_val)
            best_val = max(best_val, val)  
            a_val = max(a_val, best_val)  
            if b_val <= a_val:
                break
        return best_val

    else:
        best_val = 1000  
        for i in range(0, 2):
            val = custom_pruning(limit + 1, index * 2 + i, True, scores, a_val, b_val)
            best_val = min(best_val, val)  
            b_val = min(b_val, best_val)  
            if b_val <= a_val:
                break
        return best_val

if __name__ == "__main__":
    node_values = [3, 5, 6, 9, 1, 2, 0, -1]  
   
    print("Optimal value: ", custom_pruning(0, 0, True, node_values, -1000, 1000))