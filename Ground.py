from Block import Block

class Ground(Block):
	def __init__(self, game):
		spriteMaker = [["sprites/ground.png"] ] *60
		super().__init__(game, spriteMaker, 120, 40)
		self.posX = 0
		self.posY = 400
		self.rect.center = (self.posX, self.posY)
		
		
	def update(self, offsetX = 0, offsetY = 0):

		super().update(offsetX, offsetY)