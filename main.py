import pygame
import sys
from board import Board
pygame.init()
SCREEN_X = 1000
SCREEN_Y = 1000
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
screen.fill((100, 150, 200))
game_is_not_over = True
offset_x = 100
offset_y = 100
board = Board(4, 4, offset_x, offset_y)
global gamer
gamer = 'cross'


def click(event):
	global gamer
	click_x, click_y = event.pos
	rect_x = (click_x - offset_x)//board.cell_x
	rect_y = (click_y - offset_y)//board.cell_y
	if rect_x < board.x and rect_y < board.y:
		if board.cells[rect_y][rect_x] == 0:
			if gamer == 'null':
				board.cells[rect_y][rect_x] = 'o'
				gamer = 'cross'
			elif gamer == 'cross':
				board.cells[rect_y][rect_x] = 'x'
				gamer = 'null'
			if are_3_in_line():
				quit()

def are_3_in_line():
	if gamer == 'null':
		var = 'x'
	else:
		var = 'o'
	for i in range(board.y):
		for j in range(board.x - 2):
			if all((board.cells[i][j] == var, board.cells[i][j+1] == var, board.cells[i][j+2] == var)):
				print(1)
				return True
	for i in range(board.y -2):
		for j in range(board.x):
			if all((board.cells[i][j] == var, board.cells[i+1][j] == var, board.cells[i+2][j] == var)):
				return True
	for i in range(board.y-2):
		for j in range(board.x - 2):
			if all((board.cells[i][j] == var, board.cells[i+1][j+1] == var, board.cells[i+2][j+2] == var)):
				return True
	for i in range(2, board.y):
		for j in range(2, board.x):
			if all((board.cells[i-2][j-2] == var, board.cells[i-1][j-1] == var, board.cells[i][j] == var)):
				return True



def quit():
	pygame.quit()
	sys.exit()

while game_is_not_over:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.MOUSEBUTTONUP:
			click(event)


		elif event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit()

	screen.fill((100, 150, 200))
	board.draw(screen)
	pygame.display.update()

