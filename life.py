# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


import sys, pygame

pygame.init()
pygame.display.set_caption('Game of Life')
size = width, height = 400, 400

black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)


class Game(object):

	board = {}
	
	def __init__(self,width):
		self.width = width
		
		for i in range(0,width):
			for j in range(0,width):
				self.board[(i,j)] = 0
		
	def print_board(self):
		vis = []
		for i in range(0,self.width):
			vis.append([])
			for j in range(0,self.width):
				vis[i].append(self.board[(i,j)])
			print vis[i]
		print ''
		
	def seed(self,x,y):
		self.board[(x,y)] = 1
			
	def live(self):
	
		def get_neighbors(b):
			neighbors = {}
			
			for k in b:
				count = 0
				
				for x in range(-1,2):
					for y in range(-1,2):
						try:
							if b[((k[0]+x),(k[1]+y))] == 1 and not(x==0 and y==0):
								count+=1
						except KeyError:
							pass
				neighbors[k] = count
			
			return neighbors
	
		step = {}
		neighbors = get_neighbors(self.board)
		for i in self.board:
			if self.board[i]==1 and (neighbors[i] < 2 or neighbors[i] > 3):
				step[i] = 0
			elif self.board[i]==1 and neighbors[i] < 4:
				step[i] = 1
			elif self.board[i]==0 and neighbors[i] == 3:
				step[i] = 1
			else:
				step[i] = 0
		self.board = step
		

		
life = Game(10)

for i in range(1,4):
	life.seed(2,i+2)
	
life.print_board()

for i in range(0,5):
	life.live()
	life.print_board()


	
# while 1:
	# for event in pygame.event.get():
		# if event.type == pygame.QUIT: sys.exit()


	# screen.fill(black)
	# screen.blit(ball, ballrect)
	# pygame.display.flip()