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
		
	def print_board(self,d):
		vis = []
		for i in range(0,self.width):
			vis.append([])
			for j in range(0,self.width):
				vis[i].append(d[(i,j)])
			print vis[i]
		print ''
		
	def seed(self,x,y):
		self.board[(x,y)] = 1
			
	def live(self):
		step = {}
		
		
	def get_neighbors(self,b):
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
		
life = Game(10)

for i in range(0,3):
	for j in range(0,3):
		life.seed(i,j)
life.print_board(life.get_neighbors(life.board))	


	
# while 1:
	# for event in pygame.event.get():
		# if event.type == pygame.QUIT: sys.exit()


	# screen.fill(black)
	# screen.blit(ball, ballrect)
	# pygame.display.flip()