import pygame
import sys
from board import Board
from time import sleep
pygame.init()
SCREEN_X = 1000
SCREEN_Y = 1000
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
screen.fill((100, 150, 200))


class Main():
	def __init__(self):
		self.board = Board(4, 4)
		self.game_is_not_over = True

	def click(self, coord):
		click_x, click_y = coord
		rect_x = (click_x - self.board.offset_x)//self.board.cell_x
		rect_y = (click_y - self.board.offset_y)//self.board.cell_y
		if rect_x < self.board.x and rect_y < self.board.y:
			if self.board.cells[rect_y][rect_x] == 0:
				self.move(rect_x, rect_y)

	def move(self, rect_x, rect_y):
		if self.board.gamer == 'null':
			self.board.cells[rect_y][rect_x] = 'o'
			self.board.gamer = 'cross'
		elif self.board.gamer == 'cross':
			self.board.cells[rect_y][rect_x] = 'x'
			self.board.gamer = 'null'
		if self.board.are_3_in_line():
			self.game_is_not_over = False
def quit():
	pygame.quit()
	sys.exit()

main = Main()

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.MOUSEBUTTONUP and main.game_is_not_over:
			main.click(event.pos)
		elif event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit()

	screen.fill((100, 150, 200))
	main.board.draw(screen)
	pygame.display.update()

	if main.game_is_not_over == False:
		sleep(3)
		main = Main()

