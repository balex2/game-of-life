# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


import sys, pygame, math

pygame.init()
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()
num_squares = int(raw_input("Enter number of squares: "))
#num_squares = 20
#box_size = int(raw_input("Enter size of box in pixels: "))
box_size = 20

print "Click a square to 'seed' it then press 'Space' to begin simulation"

size = width, height = box_size*num_squares, box_size*num_squares

black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)


class game(object):

	board = {}
	start = False
	
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
		
	def get_rects(self):
		rects = []
		for i in self.board:
			if self.board[i] == 1:
				rects.append((i[0]*box_size,i[1]*box_size,box_size,box_size))
		return rects
		
	def seed(self,x,y):
		self.board[(x,y)] = 1 - self.board[(x,y)]
		print "Cell (%s,%s) selected." % (x+1,y+1)
			
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
		

		
life = game(num_squares)
	
while 1:
	clock.tick(60)
	pygame.time.delay(300)
	screen.fill(white)
	
	for k in life.get_rects():
		pygame.draw.rect(screen,black,k)
	for j in range(1,num_squares):
		pygame.draw.line(screen, black, (j*box_size,0), (j*box_size,width), 1)
	for j in range(1,num_squares):
		pygame.draw.line(screen, black, (0,j*box_size), (width,j*box_size), 1)

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN: 
			if life.start == False:
				u = math.ceil(pygame.mouse.get_pos()[0]/box_size)
				v = math.ceil(pygame.mouse.get_pos()[1]/box_size)
				life.seed(u,v)
			else:
				print 'Simulation has already started.'
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				life.start = True
				
	if life.start == True:
		life.live()
		
	pygame.display.flip()