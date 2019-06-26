=begin
    Q: Start from top left(0,0) in maze, and continue till bottom right(n-1, n-1). You can only move forward and down.
    URL: https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
=end

def valid_move?(x, y, maze)
    x >= 0 && x < maze.size && y >= 0 && y < maze.size && maze[x][y] == 1
end

def print_result(arr, n)
    n.times do |i|
        n.times do |j|
            print (arr[i][j]).to_s + ", " 
        end
        print("\n")
    end
    print("\n")
end

def track(maze)
    n = maze.size # Since it is an n*n matrix

    maze[0][0] = "S"



    if traverse(0, 0, maze)
        p "Maze traversed"
        print_result(maze, n)
        return true
    else
        p "Not traversed"
        print_result(maze, n)
        return false
    end
end

def traverse(x, y, maze)
    print_result(maze, maze.size)

    return true if(x == maze.size - 1 && y == maze.size - 1)

    down_x = x + 1
    down_y = y

    right_x = x
    right_y = y + 1

    if valid_move?(down_x, down_y, maze) || valid_move?(right_x, right_y, maze)
        # Move down first, and if that is not possible, move right
        if valid_move?(down_x, down_y, maze)
            maze[down_x][down_y] = "-"
            if !traverse(down_x, down_y, maze)
                maze[down_x][down_y] = 0
                return traverse(x, y, maze)
            else
                return true
            end
        else
            maze[right_x][right_y] = "-"
            if !traverse(right_x, right_y, maze)
                maze[right_x][right_y] = 0
                return traverse(x, y, maze)
            else
                return true
            end
        end
    else
        return false
    end
end


maze = [
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 1]
] 

track(maze)