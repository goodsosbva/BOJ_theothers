def solution(bishops):
    board = [[0 for _ in range(8)] for _ in range(8)]
    
    def pos_to_indices(pos):
        return ord(pos[0]) - ord('A'), int(pos[1]) - 1

    for bishop in bishops:
        x, y = pos_to_indices(bishop)
        board[x][y] = 1  
        
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                board[nx][ny] = 1
                nx += dx
                ny += dy
    
    safe_count = sum(row.count(0) for row in board)
    
    return safe_count

print(solution(["D5"]))         
print(solution(["D5", "E8", "G2"]))  
