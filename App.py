from cmath import rect
from sys import exit
import pygame
import threading
from entity.base.Entity import Entity

class App:
	def __init__(self) -> None:
		self.__root = threading.Thread(target=self.__start)
		self.__clock = pygame.time.Clock()
		self.__screen = None
		self.__objects = []

		self.width = 0
		self.height = 0

	def run(self) -> None:
		self.__root.start()
	
	def add_object(self, object:Entity) -> None:
		self.__objects.append(object)

	def build(self) -> None:
		pass

	def __upload(self) -> None:
		for object in self.__objects:
			object.update()
			self.__screen.blit(object.source, object.root)

	def __start(self) -> None:
		pygame.init()
		self.__screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption('Titulo')

		self.build()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
		    
			self.__upload()
			pygame.display.update()
			self.__clock.tick(60)
