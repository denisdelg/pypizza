#!/usr/bin/env python3
import sys
import re
from collections import deque


def main():
    check_args(' '.join(sys.argv[1:]))
    board_size = get_board_size(sys.argv[1])
    dest_list = get_destination_coords(sys.argv[2:])
    grid = [[False for width in range(board_size[0])]
            for height in range(board_size[1])]
    path_coords = find_paths(grid, dest_list)
    path_dirs = build_direction_string(path_coords)
    print(path_dirs)


def find_paths(grid, destinations, start=(0, 0, '')):
    q = deque()
    path = []
    ret = []
    grid[start[0]][start[1]] = True
    for cur_dest in destinations:
        q.append([start])
        while len(q) > 0:
            path = q.popleft()
            node = path[-1]
            if node[0] == cur_dest[0] and node[1] == cur_dest[1]:
                grid = [[False for width in range(len(grid))]
                        for height in range(len(grid[0]))]
                path.append((node[0], node[1], 'D'))
                q.clear()
                start = (cur_dest[0], cur_dest[1], '')
                ret += path
                break
            grid[node[0]][node[1]] = True
            for neighbor in get_neighbors(node, grid):
                new_path = list(path)
                new_path.append(neighbor)
                q.append(new_path)
    return ret


def build_direction_string(path_list):
    ret = ''
    for cur_coord in path_list:
        if cur_coord[2] != '':
            ret += cur_coord[2]
    return ret


def get_neighbors(cur_coords, grid):
    ret = []
    translations = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dirs = ['W', 'E', 'S', 'N']
    for idx, trans in enumerate(translations):
        nX = cur_coords[0] + trans[0]
        nY = cur_coords[1] + trans[1]
        if nX >= 0 and nX < len(grid) and nY >= 0 and nY < len(grid[0]) and grid[nX][nY] == False:
            ret.append((nX, nY, dirs[idx]))

    return ret


def check_args(args):
    regex = r'^\d+x\d+ (\(\d+, *\d+\) *)+'
    matches = re.fullmatch(regex, args)
    if not matches:
        sys.exit('Usage: pizzabot.py boardsize (xCoord, yCoord)')
    return True


def get_board_size(args):
    ret = ()
    try:
        ret = tuple([int(n) for n in args.split('x', 2)])
    except Exception as error:
        print('Error in get_board_size: ' + repr(error))
    return ret


def get_destination_coords(args):
    ret = []
    try:
        for cur in args:
            cur = cur.replace(' ', '')
            cur = cur.replace('(', '')
            cur = cur.replace(')', '')
            w = cur.split(',', 2)
            ret.append((int(w[0]), int(w[1]), ''))
    except Exception as error:
        print('Error in get_destination_coords: ' + repr(error))

    return ret


if sys.version_info >= (3, 5):
    if __name__ == '__main__':
        main()
else:
    sys.exit('Error: This script requires Python 3.5 or greater')
