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

