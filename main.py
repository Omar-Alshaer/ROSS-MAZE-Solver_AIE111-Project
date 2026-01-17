#=========================
# main.py
#=========================


import sys
import pygame
from grid import GRID, ROWS, COLS, CELL_SIZE, get_start, get_goal, reset_grid
from bfs import bfs

WIDTH = COLS * CELL_SIZE + 120
HEIGHT = ROWS * CELL_SIZE + 180

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 150, 255)
YELLOW = (255, 255, 0)
BG = (30, 30, 30)

def get_cell_from_mouse(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    if 0 <= row < ROWS and 0 <= col < COLS:
        return row, col
    return None

def draw_grid(screen, font, visited_set, path_set, info_text=""):
    screen.fill(BG)
    
    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL_SIZE
            y = r * CELL_SIZE
            cell_value = GRID[r][c]
            
            color = WHITE
            if cell_value == 1:
                color = BLACK
            elif cell_value == 2:
                color = GREEN
            elif cell_value == 3:
                color = RED
            
            if (r, c) in visited_set and cell_value not in (2, 3):
                color = BLUE
            if (r, c) in path_set and cell_value not in (2, 3):
                color = YELLOW
            
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GREY, rect, 1)
    
    font_title = pygame.font.Font(None, 32)
    title = font_title.render("ROSS MAZE Solver", True, WHITE)
    screen.blit(title, (20, ROWS * CELL_SIZE + 10))
    
    instructions = [
        "Left Click: Wall  |  Right Click: Clear",
        "S Key: Set Start | G Key: Set Goal",
        "SPACE: Run BFS   |  R: Reset"
    ]
    
    y_offset = ROWS * CELL_SIZE + 50
    for instruction in instructions:
        text = font.render(instruction, True, WHITE)
        screen.blit(text, (20, y_offset))
        y_offset += 25
    
    if info_text:
        info_text_obj = font.render(info_text, True, YELLOW)
        screen.blit(info_text_obj, (20, y_offset + 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BFS Maze Solver - AIE111 Final Project")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 18)
    
    visited_order, path = [], []
    visited_index = 0
    path_index = 0
    running_bfs = False
    show_path = False
    visited_set = set()
    path_set = set()
    info_text = ""
    
    running = True
    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                elif event.key == pygame.K_r:
                    reset_grid()
                    visited_order = []
                    path = []
                    visited_index = 0
                    path_index = 0
                    visited_set.clear()
                    path_set.clear()
                    running_bfs = False
                    show_path = False
                    info_text = ""
                
                elif event.key == pygame.K_SPACE and not running_bfs and not show_path:
                    start = get_start()
                    goal = get_goal()
                    if not start or not goal:
                        info_text = "Set Start (S) and Goal (G) first!"
                    else:
                        visited_order, path = bfs(GRID, start, goal)
                        visited_index = 0
                        path_index = 0
                        visited_set.clear()
                        path_set.clear()
                        running_bfs = True
                        info_text = ""
                
                elif event.key == pygame.K_s:
                    pos = pygame.mouse.get_pos()
                    cell = get_cell_from_mouse(pos)
                    if cell:
                        r, c = cell
                        if GRID[r][c] != 1:
                            old_start = get_start()
                            if old_start:
                                GRID[old_start[0]][old_start[1]] = 0
                            GRID[r][c] = 2
                
                elif event.key == pygame.K_g:
                    pos = pygame.mouse.get_pos()
                    cell = get_cell_from_mouse(pos)
                    if cell:
                        r, c = cell
                        if GRID[r][c] != 1:
                            old_goal = get_goal()
                            if old_goal:
                                GRID[old_goal[0]][old_goal[1]] = 0
                            GRID[r][c] = 3
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cell = get_cell_from_mouse(event.pos)
                if cell:
                    r, c = cell
                    if event.button == 1:
                        if GRID[r][c] == 0:
                            GRID[r][c] = 1
                        elif GRID[r][c] == 1:
                            GRID[r][c] = 0
                    elif event.button == 3:
                        if GRID[r][c] == 1:
                            GRID[r][c] = 0
        
        if running_bfs:
            if visited_index < len(visited_order):
                visited_set.add(visited_order[visited_index])
                visited_index += 1
            else:
                running_bfs = False
                show_path = True
                info_text = f"BFS Complete | Visited: {len(visited_order)} | Path: {len(path)}"
        
        elif show_path:
            if path_index < len(path):
                path_set.add(path[path_index])
                path_index += 1
            else:
                show_path = False
        
        draw_grid(screen, font, visited_set, path_set, info_text)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
