import pygame
class Board:
	def __init__(self, x, y, offset_x, offset_y):
		self.x = x
		self.y = y
		self.cells =[ [0 for i in range(x)] for i in range(y)]
		self.cell_x = 200
		self.cell_y = 200
		self.offset_x = offset_x
		self.offset_y = offset_y
		self.gamer = 'null'

	def draw(self, screen):
		print(self.cells)
		for i in range(self.y):
			for j in range(self.x):
				pygame.draw.rect(screen, (255, 255, 255), (self.cell_x*j+self.offset_x, self.cell_y*i+self.offset_y, self.cell_x-10, self.cell_y-10))
				if self.cells[i][j] == 'o':
					pygame.draw.circle(screen, (255, 0, 0), (self.cell_x*j+ self.offset_x + self.cell_x//2 - 5, self.cell_y*i+100 + self.cell_y//2 -5), self.cell_x//2 - 20, 10)
				elif self.cells[i][j] == 'x':
					pygame.draw.line(screen, (255, 0, 0),  [self.cell_x*j+self.offset_x, self.cell_y*i+self.offset_y], [self.cell_x*(j+1)+self.offset_x-10, self.cell_y*(i+1)+self.offset_y-10], 10)
					pygame.draw.line(screen, (255, 0, 0),  [self.cell_x*(j+1)+self.offset_x-10, self.cell_y*i+self.offset_y], [self.cell_x*j+self.offset_x, self.cell_y*(i+1)+self.offset_y-10], 10)

	def are_3_in_line(self):
		if self.gamer == 'null':
			var = 'x'
		else:
			var = 'o'
		for i in range(self.y):
			for j in range(self.x - 2):
				if all((self.cells[i][j] == var, self.cells[i][j+1] == var, self.cells[i][j+2] == var)):
					print(1)
					return True
		for i in range(self.y -2):
			for j in range(self.x):
				if all((self.cells[i][j] == var, self.cells[i+1][j] == var, self.cells[i+2][j] == var)):
					return True
		for i in range(self.y-2):
			for j in range(self.x - 2):
				if all((self.cells[i][j] == var, self.cells[i+1][j+1] == var, self.cells[i+2][j+2] == var)):
					return True
		for i in range(2, self.y):
			for j in range(2, self.x):
				if all((self.cells[i-2][j-2] == var, self.cells[i-1][j-1] == var, self.cells[i][j] == var)):
					return True
