import pygame

class Background():
	def __init__(self, game, imageFile, width, height, scrollX = 0, scrollY = 0):
		self.image = pygame.image.load(imageFile)
		self.screen = game.screen
		self.width = width
		self.height = height
		self.scrollAmountX = scrollX
		self.scrollAmountY = scrollY
		self.cWidth = self.screen.get_width()
		self.cHeight = self.screen.get_height()

		self.image = pygame.transform.scale(self.image, (self.width, self.height))

	def draw(self, offX = 0, offY = 0):

		externX = int(offX * self.scrollAmountX)
		externY = int(offY * self.scrollAmountY)	

		for ix in range((externX * -1), self.cWidth, self.width):
			for iy in range((externY * -1),self.cHeight, self.height):
				self.screen.blit(self.image, (ix, iy))

		
