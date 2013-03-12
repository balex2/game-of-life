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
			
	def seed(self,x,y):
		self.board[(x,y)] = 1
			
	def live(self):
		neighbors = {}
		
		for i in self.board:
			count = 0
			if i[0] == 0 and i[1] == 0: #get neighbor count for corners
				
			if i[0] != 0 and i[1] != (self.width-1): #get neighbor count for central squares
				if self.board[(i[0]-1,i[1]-1)] == 1:
					count +=1
				if self.board[(i[0]-1,i[1])] == 1:
					count +=1
				if self.board[(i[0]-1,i[1]+1)] == 1:
					count +=1
				if self.board[(i[0],i[1]-1)] == 1:
					count +=1
				if self.board[(i[0],i[1]+1)] == 1:
					count +=1
				if self.board[(i[0]+1,i[1]-1)] == 1:
					count +=1
				if self.board[(i[0]+1,i[1])] == 1:
					count +=1
				if self.board[(i[0]+1,i[1]+1)] == 1:
					count +=1
			neighbors[i] = count
		
life = Game(10)
# for i in life.board:
	# if i[0] % 2 == 0 and i[1] % 2 == 0:
		# life.board[i] = 1
life.print_board()

	
# while 1:
	# for event in pygame.event.get():
		# if event.type == pygame.QUIT: sys.exit()


	# screen.fill(black)
	# screen.blit(ball, ballrect)
	# pygame.display.flip()