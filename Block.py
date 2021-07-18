from Spritesheet import Spritesheet

class Block(Spritesheet):
	def __init(self, imageFile, xSize, ySize):
		super().__init__(imageFile, xSize, ySize)	
		self.isLeft = False
		self.isRight = False
		self.isAbove = False
		self.isBelow = False
	
	# 	collideswith(Sprite) - checks for collision with another sprite, pushes sprite back because it's a block
	def collidesWith(self, sprite):
		collision = False
	

		# assume collision
		collision = self.rect.colliderect(sprite)

		#print(collision)
		if collision:
			#print("collision?")
			sprite.x, sprite.y = sprite.rect.center
			self.x, self.y = self.rect.center

			# check borders
			left = int(self.x - (self.width / 2))
			top = int(self.y - (self.height / 2))
			right = int(self.x + (self.width / 2))
			bottom = int(self.y + (self.height / 2))
			spriteLeft = int(sprite.x - (sprite.width / 2))
			spriteTop = int(sprite.y - (sprite.height / 2))
			spriteRight = int(sprite.x + (sprite.width / 2))
			spriteBottom = int(sprite.y + (sprite.height / 2))
				
			

				

			# calculate amounts
			amountLeft = left - spriteRight
			amountAbove = top - spriteBottom
			amountRight = spriteLeft - right
			amountBelow = spriteTop - bottom
				
			# amountLeft is highest
			if (amountLeft > amountRight and amountLeft > amountAbove and amountLeft > amountBelow):
				self.isLeft = True
				self.isRight = False
				self.isAbove = False
				self.isBelow = False
			elif (amountRight > amountBelow and amountRight > amountAbove):
				self.isRight = True
				self.isLeft = False
				self.isAbove = False
				self.isBelow = False				
			elif (amountBelow > amountAbove):
				self.isBelow = True
				self.isLeft = False
				self.isAbove = False
				self.isRight = False				
			else:
				self.isAbove = True
				self.isLeft = False
				self.isBelow = False
				self.isRight = False				
				
				
			#move the sprite back
			if collision == True:
				if self.isBelow and (bottom > spriteTop):
					sprite.posY = (sprite.posY + (bottom - spriteTop))
				elif self.isAbove and (top < spriteBottom):
					sprite.posY = (sprite.posY - (spriteBottom - top))
					sprite.dy = 0				
				elif self.isLeft and (left < spriteRight):
					sprite.x = (sprite.posX - (spriteRight - left))
					sprite.dx = 0				
				elif self.isRight and (right > spriteLeft):
					sprite.x = (sprite.posX + (right - spriteLeft))	
					sprite.dx = 0						
						

			
		return collision
		
		
	# returns true if the bottom of one sprite is on top of a block
	def standingOn(self, sprite):	
		left = int(self.x - (self.width / 2))
		top = int(self.y - (self.height / 2))
		right = int(self.x + (self.width / 2))
		spriteLeft = int(sprite.x - (sprite.width / 2))
		spriteRight = int(sprite.x + (sprite.width / 2))
		spriteBottom = int(sprite.y + (sprite.height / 2))
		standing = False		
		
		# we need a NOR
		if not ((left > spriteRight) and (right < spriteLeft)):
			if top == spriteBottom:
				standing = True
			
		return standing			