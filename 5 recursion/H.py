def check_pos(x, y, maze):
    if maze[y][x] == '.':
        space = 1
        maze[y][x] = '*'
        if 0 <= y - 1:
            space += check_pos(x, y - 1, maze)
        if 0 <= x - 1:
            space += check_pos(x - 1, y, maze)
        if x + 1 <= len(maze[1]) - 1:
            space += check_pos(x + 1, y, maze)
        if y + 1 <= len(maze) - 1:
            space += check_pos(x, y + 1, maze)
        return space
    else:
        return 0

if __name__ == "__main__":
    n = int(input())
    maze = [list(input()) for i in range(n)]
    y, x = map(int, input().split())
    print(check_pos(x - 1, y - 1, maze))