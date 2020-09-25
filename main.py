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
			self.game_is_not_over = 1 - self.board.are_3_in_line('o')

		elif self.board.gamer == 'cross':
			self.board.cells[rect_y][rect_x] = 'x'
			self.board.gamer = 'null'
			self.game_is_not_over = 1 - self.board.are_3_in_line('x')
		self.ii_move()


	def ii_move(self):
		#ищем, куда походить, чтобы победить за ход
		for i in range(self.board.y):
			for j in range(self.board.x):
				if self.board.cells[i][j] == 0:
					self.board.cells[i][j] = 'o'
					if self.board.are_3_in_line('o') == 1:
						self.board.gamer = 'cross'
						self.game_is_not_over = False
						return 0
					else:
						self.board.cells[i][j] = 0
		#мешаю победить противнику
		for i in range(self.board.y):
			for j in range(self.board.x):
				if self.board.cells[i][j] == 0:
					self.board.cells[i][j] = 'x'
					if self.board.are_3_in_line('x') == 1:
						self.board.cells[i][j] = 'o'
						self.board.gamer = 'cross'

						return 0
					else:
						self.board.cells[i][j] = 0
		#хоть как-то походить надо же
		for i in range(self.board.y):
			for j in range(self.board.x):
				if self.board.cells[i][j] == 0:
					self.board.cells[i][j] = 'o'
					self.board.gamer = 'cross'

					return 0


def quit():
	pygame.quit()
	sys.exit()

main = Main()

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.MOUSEBUTTONUP and main.game_is_not_over and main.board.gamer == 'cross':
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

