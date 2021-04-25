import json
import pygame, sys
from pygame.locals import *


class CRW_Dataset:
    def __init__(self, dataset):
        self.row_str = ''.join([x for x in dataset['grid']])
        self.row_list = [self.row_str[i : i+15] for i in range(0, len(self.row_str), 15)]
        self.answers_across = dataset['answers']['across']
        self.answers_down = dataset['answers']['down']
        self.clues_across = dataset['clues']['across']
        self.cluses_down = dataset['clues']['down']
        self.grid_num_list = dataset['gridnums']

class CrossWord_GUI:
    def __init__(self, dataset):
        pygame.display.set_caption('Cross Word')
        
        self.DATA = CRW_Dataset(dataset)
        self.WIDTH = self.HEIGHT = 750 
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.SMALL_FONT = pygame.font.SysFont('ariel', 5)


    def play_game(self):
        
        self.SCREEN.fill((255, 255, 255))
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit

            num = 50
            for x in range(15):
                pygame.draw.line(self.SCREEN, (0, 0, 0), (num, 0), (num, 750), width= 3)
                num += 50
            num = 50
            for x in range(15):
                pygame.draw.line(self.SCREEN, (0, 0, 0), (0, num), (750, num), width= 3)
                num += 50

            for row, string in enumerate(self.DATA.row_list):
                for col, dot in enumerate(string):
                    if dot == '.':
                        pygame.draw.rect(self.SCREEN, (0, 0, 0), pygame.Rect(50*row, 50*col, 50, 50))
            
            row = 0
            for index, num in enumerate(self.DATA.grid_num_list, start= 1):
                if index % 15 == 0:
                    row+=1
                    if num != 0:
                        
                        num_txt = self.SMALL_FONT.render(str(num), False, (0, 0, 0))
                        num_txt_rect = num_txt.get_rect()
                        num_txt_rect.center = (50*row, 50*index)
                        self.SCREEN.blit(num_txt, num_txt_rect) 

            pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    with open('dataset.json', 'r') as f:
        dataset = json.load(f)

    crw = CrossWord_GUI(dataset)
    crw.play_game()

