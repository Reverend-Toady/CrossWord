import json, sys
import pygame
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
    def __init__(self, dataset, empty_grid):
        pygame.display.set_caption('Cross Word')
        
        self.DATA = CRW_Dataset(dataset)
        self.WIDTH = self.HEIGHT = 750 
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.SMALL_FONT = pygame.font.SysFont('Arial', 18)
        self.YEXT_FONT = pygame.font.SysFont('Arial', 24)
        self.CLOCK = pygame.time.Clock()

        self.GRID = empty_grid

    def ifValidInput(self, y, x, alphabet):
        if self.BOARD[(y//50)][(x//50)] != '.':
           self.BOARD[(y//50)][(x//50)] = alphabet 

    def play_game(self):
        dist = 50
        
        blue_rect = pygame.Rect(0, 0, 50, 50)
        run = True
        while run:
            self.CLOCK.tick(60)

            self.SCREEN.fill((255, 255, 255))

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
                        pygame.draw.rect(self.SCREEN, (0, 0, 0), pygame.Rect(50*col, 50*row, 50, 50))
                        
            row = 0
            index = 1
            for num in self.DATA.grid_num_list:
                
                if num != 0:
                    num_txt = self.SMALL_FONT.render(str(num), True, (0, 0, 0))
                    self.SCREEN.blit(num_txt, ((50*(index-1)+5), (50*row)+5))

                if index % 15 == 0:
                    row+=1
                    index = 0 
                
                index+=1 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        blue_rect.y -= dist
                    elif event.key == pygame.K_DOWN:
                        blue_rect.y += dist
                    elif event.key == pygame.K_LEFT:
                        blue_rect.x -= dist
                    elif event.key == pygame.K_RIGHT:
                        blue_rect.x += dist 

                    if event.key == pygame.K_a:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'A')

            
            pygame.draw.rect(self.SCREEN, (0, 0, 255), blue_rect, 3)


            pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    with open('dataset.json', 'r') as f:
        dataset = json.load(f)

    x = ''.join([x for x in dataset['grid']])
    empty_grid = []
    for i in x:
        if i != '.':
            l = i.replace(i, ' ')
            empty_grid.append(l)
        else: empty_grid.append(i)  

    actual_grid = [empty_grid[i:i+15] for i in range(0, len(empty_grid), 15)]

    crw = CrossWord_GUI(dataset, actual_grid)
    crw.play_game()


