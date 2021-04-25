import json, sys, time
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
    def __init__(self, dataset, empty_grid, filled_grid):
        pygame.display.set_caption('Cross Word')
        
        self.DATA = CRW_Dataset(dataset)
        self.WIDTH = 1500
        self.HEIGHT = 750 
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        self.SMALL_FONT = pygame.font.SysFont('Arial', 18)
        self.TEXT_FONT = pygame.font.SysFont('Arial', 30)
        self.BOLD_FONT = pygame.font.SysFont('Arial Bold', 50)
        self.CLUE_TEXT = pygame.font.SysFont('Arial', 18)
        self.CLOCK = pygame.time.Clock()

        self.GRID = empty_grid
        self.FILLED_GRID = filled_grid

        

    def ifValidInput(self, y, x, alphabet):
        if self.GRID[(y//50)][(x//50)] != '.':
           self.GRID[(y//50)][(x//50)] = alphabet 

    def play_game(self):
        dist = 50
        
        blue_rect = pygame.Rect(0, 0, 50, 50)
        main_run = True

        while main_run:
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
            
            for row, elem_list in enumerate(self.GRID):
                for col , elem in enumerate(elem_list):
                    if elem != '.' or elem != ' ':
                        text = self.TEXT_FONT.render(elem, True, (0, 0, 0))
                        self.SCREEN.blit(text, ((50*col) + 18, (50*row) + 13))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_run = False
                    sys.exit(0)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        blue_rect.y -= dist
                    elif event.key == pygame.K_DOWN:
                        blue_rect.y += dist
                    elif event.key == pygame.K_LEFT:
                        blue_rect.x -= dist
                    elif event.key == pygame.K_RIGHT:
                        if blue_rect.x >= 650:
                            blue_rect.x = 650
                        blue_rect.x += dist 

                    if event.key == pygame.K_RETURN:
                        green_rect = pygame.Rect(0, 0, 50, 50)
                        green_rect.center = (0, 0)
                        self.GRID = self.FILLED_GRID
                        for row, elem_list in enumerate(self.GRID):
                            for col , elem in enumerate(elem_list):
                                if elem != '.' or elem != ' ':
                                    green_rect.center = ((50*col)+25 , (50*row)+25)
                                    pygame.draw.rect(self.SCREEN, (0, 255, 0), green_rect, 3)   
                                    text = self.TEXT_FONT.render(elem, True, (0, 0, 0))
                                    self.SCREEN.blit(text, ((50*col) + 18, (50*row) + 13))
                                    pygame.display.update()
                                time.sleep(0.1)

                        

                    if event.key == pygame.K_a:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'A')

                    if event.key == pygame.K_b:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'B')

                    if event.key == pygame.K_c:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'C')

                    if event.key == pygame.K_d:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'D')

                    if event.key == pygame.K_e:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'E')

                    if event.key == pygame.K_f:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'F')

                    if event.key == pygame.K_g:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'G')

                    if event.key == pygame.K_h:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'H')

                    if event.key == pygame.K_i:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'I')

                    if event.key == pygame.K_j:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'J')

                    if event.key == pygame.K_k:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'K')

                    if event.key == pygame.K_l:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'L')

                    if event.key == pygame.K_m:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'M')

                    if event.key == pygame.K_n:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'N')

                    if event.key == pygame.K_o:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'O')

                    if event.key == pygame.K_p:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'P')

                    if event.key == pygame.K_q:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'Q')

                    if event.key == pygame.K_r:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'R')

                    if event.key == pygame.K_s:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'S')

                    if event.key == pygame.K_t:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'T')

                    if event.key == pygame.K_u:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'U')

                    if event.key == pygame.K_v:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'V')

                    if event.key == pygame.K_w:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'W')

                    if event.key == pygame.K_x:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'X')

                    if event.key == pygame.K_y:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'Y')

                    if event.key == pygame.K_z:
                        self.ifValidInput(blue_rect.y, blue_rect.x, 'Z')
                    if event.key == pygame.K_BACKSPACE:
                        self.ifValidInput(blue_rect.y, blue_rect.x, ' ')
                    
            
            pygame.draw.rect(self.SCREEN, (0, 0, 255), blue_rect, 3)
            pygame.draw.line(self.SCREEN, (0, 0, 0), (750+375, 0), (750+375, 750), width= 5)
            pygame.draw.line(self.SCREEN, (0, 0, 0), (750, 0), (750, 750), width= 5)
            pygame.draw.line(self.SCREEN, (0, 0, 0), (750, 50), (1500, 50), width= 5)

            acr_txt = self.BOLD_FONT.render('ACROSS', True, (0, 0, 0))
            self.SCREEN.blit(acr_txt, (780, 16))
            dn_txt = self.BOLD_FONT.render('DOWN', True, (0, 0, 0))
            self.SCREEN.blit(dn_txt, (1155, 16))

            idx = 1
            for clues in self.DATA.clues_across:
                clues = clues.strip()
                if len(clues) > 57:
                    first_char = clues[:57]
                    second_char = clues[57:]
                    fst_txt = self.CLUE_TEXT.render(first_char, True, (0, 0, 0))
                    self.SCREEN.blit(fst_txt, (755, 50+ (idx*17)))
                    idx+=1 
                    snd_txt = self.CLUE_TEXT.render(second_char, True, (0, 0, 0))
                    self.SCREEN.blit(snd_txt, (755, 50+ (idx*17)))
                    idx+=1
                else:
                    clu_txt = self.CLUE_TEXT.render(clues, True, (0, 0, 0))
                    self.SCREEN.blit(clu_txt, (755, 50+ (idx*17)))
                    idx+=1

            idx = 1
            for clues in self.DATA.cluses_down:
                clues = clues.strip()
                if len(clues) > 57:
                    first_char = clues[:57]
                    second_char = clues[57:]
                    fst_txt = self.CLUE_TEXT.render(first_char, True, (0, 0, 0))
                    self.SCREEN.blit(fst_txt, (750+380, 50+ (idx*17)))
                    idx+=1 
                    snd_txt = self.CLUE_TEXT.render(second_char, True, (0, 0, 0))
                    self.SCREEN.blit(snd_txt, (750+380, 50+ (idx*17)))
                    idx+=1
                else:
                    clu_txt = self.CLUE_TEXT.render(clues, True, (0, 0, 0))
                    self.SCREEN.blit(clu_txt, (750+380, 50+ (idx*17)))
                    idx+=1



            pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    with open('dataset.json', 'r') as f:
        dataset = json.load(f)

    ans_grid = [x for x in dataset['grid']]
    x = ''.join(ans_grid)

    empty_grid = []
    for i in x:
        if i != '.':
            l = i.replace(i, ' ')
            empty_grid.append(l)
        else: empty_grid.append(i)  

    actual_grid = [empty_grid[i:i+15] for i in range(0, len(empty_grid), 15)]
    filled_grid = [ans_grid[i:i+15] for i in range(0, len(ans_grid), 15)]

    crw = CrossWord_GUI(dataset, actual_grid, filled_grid)
    crw.play_game()


