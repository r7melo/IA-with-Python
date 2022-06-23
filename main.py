from turtle import left
import pygame
from App import App
from entity.Snail import Snail
from entity.base.Entity import Entity
from entity.Play import Play

class AppMain(App):
	def __init__(self) -> None:
		super().__init__()

		self.play: Play

	def build(self) -> None:

		test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

		sky_surface = pygame.image.load('graphics/Sky.png').convert()
		sky_rect = sky_surface.get_rect()
		sky = Entity(sky_surface, sky_rect)

		ground_surface = pygame.image.load('graphics/ground.png').convert()
		ground_rect = ground_surface.get_rect(left=0, top=300)
		ground = Entity(ground_surface, ground_rect)

		score_surf = test_font.render('My game', False, "#ffffff")
		score_rect =  score_surf.get_rect(center = (400,50))
		score = Entity(score_surf, score_rect)

		snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
		snail_rect = snail_surface.get_rect(midbottom = (600, 300))
		snail = Snail(snail_surface, snail_rect)

		play_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
		play_rect = play_surf.get_rect(midbottom = (80,300))
		self.play = Play(play_surf, play_rect)


		self.add_object(sky)
		self.add_object(ground)
		self.add_object(score)
		self.add_object(snail)
		self.add_object(self.play)

	def keyboard(self, event) -> None:
		
		self.play.keyboard(event)




if __name__ == "__main__":
	app = AppMain()
	app.width = 800
	app.height = 400
	app.run()