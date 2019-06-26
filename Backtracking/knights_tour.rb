=begin
    Q: The knight is placed on the first block of an empty board and, moving according to the rules of chess, must visit each square exactly once. Write a program for the same
    URL: https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
=end

$n = 8


def print_result(board)
    $n.times do |i|
        $n.times do |j|
            print (board[i][j]).to_s + ", " 
        end
        print("\n")
    end
end

def valid_move?(x, y, board)
    x < 8 && x > -1 && y < 8 && y > -1 && board[x][y] == -1
end

def solve_util(x, y, move_number, x_moves, y_moves, board)
    if move_number == ($n*$n)
        return true
    end

    $n.times do |i|
        next_x = x + x_moves[i]
        next_y = y + y_moves[i]

        if valid_move?(next_x, next_y, board)
            board[next_x][next_y] = move_number

            if solve_util(next_x, next_y, move_number + 1, x_moves, y_moves, board)
                return true
            else
                board[next_x][next_y] = -1
            end
        end
    end

    false
end

def track
    # Create a 2D array of 8*8 and initialize with -1
    board = Array.new($n, -1) { |item| Array.new($n, -1) }
    
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # Initial block
    board[0][0] = 0

    if !solve_util(0, 0, 1, x_moves, y_moves, board)
        p "Could not solve the problem"
    else
        print_result(board)
    end
end


track