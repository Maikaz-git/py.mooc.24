# Write your solution here
def who_won(game_board: list)->int:
    count_1s = 0
    count_2s = 0
    for i in range(len(game_board)):
        for piece in game_board[i]:
            if piece == 1:
                count_1s += 1
            elif piece == 2 :
                count_2s += 1

    if count_1s > count_2s:
        return 1
    elif count_2s > count_1s:
        return 2
    else:
        return 0

if __name__=="__main__":
    print(who_won(game_board=[[1, 2, 1], [0, 3, 4], [1, 0, 0]])) 