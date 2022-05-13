import pygame
import pygame_menu
import lekcjia1
def zmianaRozdielczosci(nazwaPola,atrybut):
    lekcjia1.zmianaRozdielczosci=atrybut
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((400,400))
    pygame.display.set_caption("Menu Snake")
    menu = pygame_menu.Menu('Snake 3TI', 400, 400,theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("start gry",lekcjia1.main,background_color=(0,0,0))
    menu.add.selector("rozmiar ekranu",[('400x400',400),('600x600',600),('800x800',800)],onchange=zmianaRozdielczosci)
    menu.mainloop(OknoMenu)
    
main()

