import pygame, os, sys
from pygame.locals import *

#spriteGroup = pygame.sprite.OrderedUpdates()
#screenRefresh = True # complements newSprite

g_walls = [] # contain wall
g_doors_solid = []
g_doors_interact = []
g_examine_solid = []
g_examine = []
g_characters_solid = []
g_characters = []

characters_mad = 0 # if characters_mad becomes 3 .... bad end
total_characters = 7

money = 0 # 100 is 1 dollar
playername = None

h_player = [
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,10),(4,10),(4,10),(4,10),(4,10),(4,11),(4,10),(4,10),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,3),(4,12),(4,12),(4,12),(4,12),(4,12),(4,12),(4,12),(4,12),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,12),(4,12),(4,12),(4,12),(4,12),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,14),(4,12),(4,12),(4,12),(4,12),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,12),(4,12),(4,13),(4,12),(4,12),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,12),(4,12),(4,12),(4,12),(4,12),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)]
]

h_farmer = [
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,18),(4,18),(4,18),(4,18),(4,18),(4,18),(4,18),(4,18),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,4),(4,17),(4,17),(4,17),(4,17),(4,17),(4,17),(5,0),(4,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,17),(4,17),(4,17),(4,17),(4,17),(4,17),(4,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,17),(4,17),(4,17),(4,17),(4,17),(4,17),(4,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,17),(4,17),(4,17),(4,17),(4,17),(4,17),(5,1),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,17),(4,17),(4,17),(4,17),(4,19),(4,17),(4,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)]
]

h_grandma = [
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(5,3),(5,3),(5,3),(5,3),(5,3),(5,3),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,3),(5,4),(5,4),(5,5),(5,6),(5,4),(5,4),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,5),(5,4),(5,4),(5,4),(5,4),(5,4),(5,4),(5,4),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(5,4),(5,4),(5,4),(5,4),(5,4),(5,4),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(5,4),(5,4),(5,4),(5,4),(5,4),(5,4),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(5,4),(5,4),(5,4),(5,4),(5,4),(5,7),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)]
]

h_cool = [
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(5,8),(5,8),(5,8),(5,8),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,8),(4,2),(4,0),(4,0),(4,0),(4,0),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,6),(4,0),(5,8),(4,0),(4,0),(4,0),(4,0),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,0),(4,0),(4,0),(4,0),(4,0),(4,0),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,0),(4,0),(4,0),(4,0),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(5,9),(4,0),(4,0),(5,10),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,0),(4,0),(4,0),(4,0),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)]
]

h_groc = [
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(6,7),(6,7),(6,7),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(5,11),(5,11),(5,11),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(5,11),(5,11),(5,11),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(6,7),(6,7),(5,11),(5,11),(6,7),(6,7),(6,7),(5,12),(6,7),(6,7),(5,13),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,7),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,11),(5,11),(5,11),(5,14),(5,14),(5,14),(5,11),(5,11),(5,11),(5,11),(5,11),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,11),(5,15),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(5,11),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)]
]

h_gas = [
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,3),(5,3),(5,3),(5,3),(5,3),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,18),(5,17),(5,17),(5,19),(5,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,17),(5,17),(5,17),(5,17),(5,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,17),(5,17),(5,17),(5,17),(5,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,8),(5,17),(5,17),(5,17),(6,0),(5,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,17),(5,17),(5,17),(5,17),(5,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,17),(6,0),(6,0),(6,0),(5,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,17),(5,17),(5,17),(5,17),(5,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(5,17),(5,17),(5,17),(5,17),(5,17),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)]
]

h_doc = [
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(6,1),(6,1),(4,2),(6,2),(6,1),(6,5),(6,1),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(6,6),(6,6),(4,2),(6,6),(6,6),(6,6),(6,3),(6,1),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(6,1),(6,6),(6,4),(6,1),(6,6),(6,6),(6,6),(6,6),(6,3),(6,5),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,9),(6,6),(6,6),(6,6),(6,6),(6,6),(6,6),(6,6),(6,6),(6,6),(6,3),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(6,6),(6,6),(6,6),(6,6),(6,6),(6,3),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(6,6),(6,6),(6,6),(6,6),(6,6),(6,3),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)],
    [(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2),(4,2)]
]

mainmap0 = [
    [(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0)],
    [(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(0,7),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8)],
    [(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(0,12),(1,7),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,7),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,11),(1,8),(0,0),(0,0),(2,4),(2,5),(0,0),(0,0),(0,1),(0,0),(0,0),(0,0)],
    [(1,7),(0,17),(0,18),(4,16),(2,0),(2,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,1),(3,4),(3,5),(0,0),(0,0),(1,1),(0,1),(0,0),(0,0)],
    [(1,7),(0,19),(1,19),(0,0),(3,0),(3,1),(4,15),(0,0),(0,0),(0,0),(0,0),(1,1),(0,5),(0,0),(0,0),(0,0),(0,0),(1,1),(0,0),(0,0)],
    [(1,7),(1,17),(1,18),(0,0),(1,5),(0,2),(0,2),(0,2),(0,2),(0,2),(0,2),(0,2),(1,2),(0,2),(0,6),(0,2),(0,2),(0,2),(0,2),(0,2)],
    [(1,7),(0,0),(5,2),(0,0),(0,5),(0,13),(0,16),(0,14),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,5),(2,6),(2,7),(0,0),(0,0),(0,0)],
    [(1,7),(2,2),(2,3),(0,0),(0,5),(0,15),(1,12),(1,16),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,5),(3,6),(3,7),(0,0),(0,0),(0,0)],
    [(1,7),(3,2),(3,3),(0,2),(1,4),(1,13),(1,15),(1,14),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,3),(0,2),(1,4),(0,0),(0,0),(0,0)],
    [(1,7),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1)],
    [(1,7),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1)]
]

mainmap1 = [
    [(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,11),(1,7),(0,1),(2,17),(2,18),(0,9),(0,10),(0,1),(0,1),(0,1),(0,1),(0,1)],
    [(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,8),(0,11),(1,8),(1,1),(3,17),(3,18),(3,19),(2,19),(1,1),(1,1),(1,1),(1,1),(1,1)],
    [(0,0),(0,0),(0,1),(0,0),(4,0),(4,1),(4,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,9),(0,10),(0,0),(0,0),(0,0),(0,0),(0,1)],
    [(0,0),(0,0),(1,1),(0,0),(4,0),(4,0),(4,0),(0,0),(0,1),(0,0),(0,0),(0,0),(0,0),(1,9),(1,10),(3,16),(3,16),(2,11),(2,12),(1,1)],
    [(0,0),(0,0),(0,0),(0,0),(0,5),(0,0),(0,0),(0,0),(1,1),(0,0),(5,16),(0,0),(0,0),(0,9),(0,10),(3,16),(3,16),(3,11),(3,12),(0,1)],
    [(0,0),(0,0),(0,0),(0,0),(0,5),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,9),(1,10),(2,16),(3,15),(3,15),(3,15),(1,1)],
    [(0,2),(0,2),(0,2),(0,2),(1,2),(0,6),(0,2),(0,2),(0,2),(0,2),(0,2),(0,2),(0,2),(0,9),(0,10),(0,2),(0,3),(0,0),(0,0),(0,1)],
    [(0,0),(0,0),(0,1),(0,0),(0,0),(0,5),(2,8),(2,9),(2,10),(0,0),(0,0),(0,0),(0,0),(1,9),(1,10),(0,0),(0,5),(2,13),(2,14),(1,1)],
    [(0,0),(0,0),(1,1),(0,0),(0,0),(0,5),(3,8),(3,9),(3,10),(0,0),(0,0),(0,0),(2,15),(0,9),(0,10),(0,0),(0,5),(3,13),(3,14),(0,1)],
    [(0,0),(0,0),(0,0),(0,0),(0,0),(1,3),(0,2),(1,4),(0,0),(0,0),(0,0),(0,0),(0,0),(1,9),(1,10),(0,0),(1,3),(1,4),(0,0),(1,1)],
    [(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,9),(0,10),(0,1),(0,1),(0,1),(0,1),(0,1)],
    [(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,9),(1,10),(1,1),(1,1),(1,1),(1,1),(1,1)]
]

maps = [mainmap0,mainmap1,h_player,h_farmer,h_grandma,h_cool,h_groc,h_gas,h_doc]

gas_talk = None
gas_play = None
cop_talk = None
cop_play = None
granny_talk = None
granny_play = None
coolguy_talk = None
coolguy_play = None
grocer_talk = None
grocer_play = None
farmer_talk = None
farmer_play = None
doctor_talk = None
doctor_play = None
family_talk = None
family_play = None

def update_words(playername):
    global gas_talk, gas_play, cop_talk, cop_play, granny_talk, granny_play, coolguy_talk, coolguy_play, grocer_talk, grocer_play, farmer_talk, farmer_play, doctor_talk, doctor_play, family_talk, family_play
    gas_talk = ['Hi, welcome to Quickstop. How can I help?',
                    'Most boring shift of my life. Can\'t wait to go home. (+1)',
                    'Uh hi. Okay. (+0)',
                    'I’m not giving you 20 cents.(-1)',
                    'Is there something else I can do for you?',
                    'Yeah, I didn’t really aspire to work as a cashier, it just pays the rent you know? (+1)',
                    'Yeah they’re like 25 cents … you don’t seem like you have the money for it. (+0)',
                    'You’re really starting to get on my nerves. (-1)',
                    'Anything else you have to say?',
                    'A marine biologist, hah, but that trying to learn that was a bit too rigorous for me. (+1)',
                    'Yeah, my manager is usually here but he’s taking a break today. (+0)',
                    'There is no incentive for me to give any money to you (-1)',
                    'I’ve made up my mind.',
                    'You are really determined for that money, but you’re also the highlight of my day.',
                    'I came into shift today thinking it was going to be another normal day, and then you show up and make me think about my dreams and aspirations.',
                    'Thanks for changing my mind. Once I get enough money to leave town, I’m going to travel and think about my life. Here’s your 20 cents.',
                    'You’re pretty weird.',
                    'But that’s okay I guess.',
                    'Here’s 20 cents for you to spend on whatever, have fun.',
                    'You are really annoying.',
                    'You really want that 20 cents.',
                    'Well here’s something: get out of my store right now. I don’t want to see your face again.'
                    ]

    gas_play = ['Hey dude, how are ya?',
                'Hi.',
                'Give me 20 cents.',
                'You seem like you rather would be doing something else.',
                'Hey how much are for the potato chips?',
                'I’m going to stand here until you give me 20 cents.',
                'What do you really want to work as?',
                'Aren’t there any other workers here?',
                'Look it’s just 20 cents, you have a cash register full of money.'
                ]

    cop_talk = ['Hey, its ... '+playername+' is it?',
                'You been here for a while and I still forget your name sometimes. (+1)',
                'Your neighborhood cop, although work has been very slow lately. (0)',
                'I’m not a walking atm, why don’t you ask someone else? (-1)',
                'How is your farm going?',
                'You’ve been a farmer for 3 years, what went wrong..?. (+1)',
                'Huh? Your crop field is empty and you insist it’s fine? (0)',
                'Woah,'+playername+' we’ve barely just talked and you’re telling me your life story. (-1)',
                'What do you plan to do about your farm scenario then?',
                'Yeah, you should try moving to the city or something – there should be some opportunities there. (+1)',
                '...You sure about that? (0)',
                'You’ve been at this for 3 years and it hasn’t worked … you need to change your strategy. (-1) ',
                'Hm.',
                'I’ve been there. Put a lot of work into something and now I have to face the realization it won’t work.',
                'That feeling sucks, it took me a long time to get out of that rut.',
                'You should try leaving this for a while, and then when you can, pick up farming later. Here is 20 cents.',
                'You’re being evasive about your current situation.',
                'I’m no farmer … but you should try seeking some assistance.',
                'Here is 20 cents, maybe it can do something for you.',
                'You’re a terrible farmer. You need to realize that.',
                'Now I also know why I barely ever talk to you these past 3 years.',
                'Just go, you’re bothering me.'
                ]

    cop_play = ['Yeah.',
                'And you are..?',
                'Do you have any money to spare?',
                'It’s pretty bad.',
                'It’s fine.',
                'Terrible. There is no crop yield and I’m barely making any money as a farmer. I think I need to rethink my profession.',
                'Give up, for now. I don’t have the resources to handle this problem.',
                'Nothing, I can manage my current situation.',
                'I just need some money to get the farm working again.'
                ]

    granny_talk = ['Hi '+playername+', would you like to try out my lemon cakes?',
                'Just give them a few minutes, they’re still cooking (+1)',
                'Ah alright, you seem to be in a hurry just now (0)',
                'Huh, a change in taste? You seem to like them last week (-1)',
                'You came to talk about something?',
                'I’m always here for you. (+1)',
                'I’m doing alright sweetie. Although I’d like to know more about how you are doing (0)',
                'Everybody needs money nowadays … (-1)',
                'Well by the look of your face, it’s your farm again.',
                'My, my. This must be serious then. (+1)',
                'I’m sorry that your farm hasn’t being running that well. (0)',
                'I’m just trying to address the problem (-1)',
                '(sigh)',
                'I remember when you just arrived in town. I just met you for the first time.',
                'You have been running away from something, and you tried to start anew but you couldn’t.',
                'You should try to reconnect with your parents, then you can move on. Here is 20 cents.',
                'Well, if your farm isn’t working.',
                'Then maybe it’s the time for you to try something else.',
                'Here is your money, I hope you find what you need.',
                'You seem in quite a bad mood today.',
                'I don’t know what I can do for you.',
                'I’m sorry, you should come back tomorrow once you feel better.'
                ]

    granny_play = ['I would love to.',
                'No thank you.',
                'I don’t like lemon cakes.',
                'I just need some support.',
                'How are you doing?',
                'I need 20 cents.',
                'I’m trying to call my parents, can you please lend me 20 cents for a payphone?',
                'Yeah...',
                '...'
                ]

    coolguy_talk = ['Who are you? Why are you in my house?',
                'You came to invade the privacy of my home just to say hi? (-1)',
                'Huh. (0)',
                'Hah! Straight to the point. (+1)?',
                'Well, what’s your problem?',
                'And now you want to cry into my arms or something? (-1)',
                'Ah, the usual (0).',
                'Oh I’m so scared! This random person just walked in my house and start making threats! (+1)',
                'Anything else?',
                'And I don’t want to be your friend. (-1)',
                'Yeah. I guess.(0)',
                'Going for the low blows huh? You are one angry person. (+1)',
                'Let me get this straight:',
                'You really sentimental and stuff.',
                'That sorta thing bores me.',
                'Get out of my house.',
                'You just walked inside my house without knocking.',
                'And we just had the weirdest conversation, that’s okay I guess.',
                'Here’s your 20 cents. Bugger off.',
                'In this boring town, you’re the only entertaining soul with a fiery attitude. You seem cool.',
                'I’d like to know more about you later, since you seem like you gotta do something now.',
                'Here’s the money, talk to ya later.'
                ]

    coolguy_play = ['I haven’t met you before, I’m'+playername+'.',
                'I’m just looking around.',
                'GIVE ME 20 CENTS.',
                'Everything, it’s all terrible and my farm that I have been running for 3 years isn’t doing that well.',
                'Life sucks.',
                'Dealing with the authorities after I beat you up if you don’t give me the money.',
                'You seem pretty cool.',
                'Do you have any spare change?',
                'You’re not cool.'
                ]

    grocer_talk = ['Welcome to the grocery,'+playername+'!',
                'It’s been doing great! But business today is usually slow. (+1)',
                'I’m going to assume that you’re not going to buy anything.(0)',
                'And when can I expect you to return it? (-1)',
                'Do you want some fresh pizza?',
                'I don’t know why you like my low quality pizza .. Wouldn’t you be a bit more picky since you’re previously a pizza chef? (+1)',
                'More for me (0)',
                'As a small business, every single penny counts. (-1)',
                'Anything going on lately?',
                'Your purchase of all that fertilizer reflects that (+1)',
                'Same. (0)',
                'Go take out a loan or something. (-1)',
                'Say..',
                'You told me a while back that you left home because you didn’t want to be a pizza chef.',
                'I think it’s a time for a change in career. You’re not really a good farmer.',
                'There are plenty of other careers out there that isn’t a chef. Here is some money to help you.',
                'You have some troubles.',
                'And I have a business to run.',
                'Here is your 20 cents, just give me 20 cents later when you can afford to.',
                'You are a parrot spouting the same line over and over again.',
                'I don’t know how other people can stand you.',
                'Please get out of my store, and don’t come back until you changed your whole attitude.'
                ]

    grocer_play = ['How has your business been doing?',
                'Howdy.',
                'Do you have 20 cents you can lend me?',
                'Sure!',
                'No thank you.',
                'it’s only 20 cents, that’s not a large amount.',
                'Having some farm-related troubles.',
                'Just the usual.',
                'I’m 20 cents short.'
                ]

    farmer_talk = ['Hey neighbor, back for some farming tips?',
                'Go buy some actual farming equipment. (+1)',
                'Ok (0)',
                'I would if you didn’t say it like that so rudely. (-1)',
                'Do you have something else to ask me?',
                'I think the soil is actually perfect, it is just that your crop might not be suitable for this soil.',
                'It’s my crop yield for this month! (0)',
                'I do work the field. It’s just every time you’re busy, I’m working (-1)',
                'Do you enjoy being a farmer?',
                'That’s the spirit... (+1)',
                'Look, being a farmer takes a lot of skill (0)',
                'Simmer down, okay? Are you jealous or something? (-1)',
                'Weeeeeelll..',
                'You’re a good person. Ever since you arrived, I took you under my wing and taught you my ways.',
                'You are determined to be a farmer. You are chipper and you don’t let things get you down.',
                'But I think it’s for the best that you should do something else. You aren’t meant to be a farmer … here is the money.',
                'You arrived here 3 years ago, with literally no farming experience.',
                'I was raised in the farm lifestyle, casted by it, molded by it.',
                'While you are improving, it’s not enough improvement to sustain yourself … here is 20 cents for your troubles.',
                'I’m a bit busy right now.',
                'You just entered my house and started pestering me.',
                'Leave my home, and you can return when you calmed down.'
                ]

    farmer_play = ['Yeah.',
                'No, I’m just here to chat.',
                'Can you give me 20 cents?',
                'How can I improve the soil conditions?',
                'Why is there a pile of hay in the corner?',
                'When do you work the field? I NEVER see you working the field.',
                'Yeah! There may be some issues with my farm, but I believe I can work through it.',
                'Not so much now, it’s hard to enjoy something that you’re not good at.',
                'WHY IS YOUR FARM PROSPERING WHILE MINE IS FAILING?!'
                ]

    doctor_talk = ['Hello '+playername+'. How are you?',
                'You seem very chipper (0)',
                'Well I hope that medication I’ve prescribed to you is working (+1)',
                'I don’t think I can help you in that regard (-1)',
                'Well let’s get straight to business, what do you want?',
                'I’m not one for small talk … it’s just time wasted (0)',
                'You would ask someone who is knowledgeable in farming? (+1)',
                'Go to the bank in the nearest town or something (-1)',
                'You aren’t here for an appointment … anything else you have to say?',
                'Mhm. (0)',
                'I’m not a pharmacist … so go to the nearest town here (+1)',
                'That is not even a full sentence (-1)',
                'Here is my ‘diagnosis’ of you.',
                'You have an awfully cheery personally.',
                'You like small talk, but it seems like you’re being evasive and hiding a problem.',
                'I don’t care enough to ask. Here is 20 cents, and please leave.',
                'You are stressed, and your failing farm is ailing you.',
                'You’re trying to go around to people to ask for money to help you.',
                'Well, here is 20 cents for your efforts.',
                'You want money.',
                'I’m annoyed by you. I’m not giving you the money.',
                'You will leave my office and not bother me for the rest of this month.'
                ]

    doctor_play = ['I’m doing fine! Thank you.',
                'Having some headaches lately.',
                'My wallet feels a bit light.',
                'Well I just want to know you better.',
                'Advice. How do I manage my failing farm?',
                'Money.',
                'I like the color theme of this room.',
                'Where do I go to refill my prescription medicine?',
                '20 cents.'
                ]

    family_talk = ['Hello … is this '+playername+'? This is your father speaking. Your mother is here as well.',
                    'We’ve been trying to find you, but you never called back after you left home. (+1)',
                    'You should be! We were worried sick about you. (0)',
                    'You don’t sound very excited to talk to your pops again (-1)',
                    'There is so much to say ...',
                    'That’s what I partially suspected as well … Let me guess, a farmer? (+1)',
                    'Well don’t worry about that, we have enough money to cover your costs (0)',
                    'It was continuing our legacy! Like you, I was born into it. It’s what our family is known for. (-1)',
                    'Can you please come home?',
                    'I’ve taken some time to reflect upon that after you left … (+1)',
                    'The words I never though I hear … I’m bursting with joy right now! (0)',
                    'Now you’re talking about this whole ‘feeling’ thing again. Did you know you never respected our feelings as well?! (-1)',
                    '(sigh) '+playername+'...',
                    'Although I don’t necessarily agree with your choice, I respect it.',
                    'Your mother and I will support you no matter what you aspire to be.',
                    'Please come home, we can talk about your adventure once you arrive.',
                    'Well now that you’re returning, you seem hesitant about being a pizza chef.',
                    'We’ll show you how important being a pizza chef really is. Maybe you’ll even learn to enjoy it!',
                    'Come home soon, your mother and I are very excited to see you again.',
                    'You could have been the greatest pizza chef. You had my and your mother’s support!',
                    'Instead you go and become a farmer, at which you are terrible at. And you ended the our family’s great pizza lineage.',
                    'Since you’re so adamant on doing whatever you want ... We’re disowning you; don’t contact us again.'
                    ]

    family_play = ['Hi dad, it’s been a long time.',
                    'Hey dad, I’m sorry for not contacting you or mom for this long.',
                    'Father.',
                    'I ran away from home because I really wanted to pursue my own dreams.',
                    'I’m in some financial trouble at the moment.',
                    'Why do you want me to be a pizza chef so much?',
                    'I’ll return home for now … but please understand I don’t want to be a pizza chef.',
                    'I’ll return home and be a pizza chef.',
                    'Why should I? I never wanted to be a pizza chef and you and mom also ignored my feelings! '
                    ]


c_intro = ['Well, that’s it.',
            'I\'ve paid my monthly rent and now I\'m debt free!',
            'There is only one problem though ...',
            'I have absolutely no money. My only source of income – the farm – is doing very poorly.',
            'I don’t think I can really manage being a farmer for another month.',
            '[gestures to phone number on desk] I should probably call my family back home. They can probably help with my financial situation.',
            'I’ve ran away from home 3 years earlier .. Because they wanted me to become a pizza chef and I didn’t.',
            'But I don’t really have much of a choice now ...',
            'I don’t have a home phone or even a cell phone. There is a public payphone though.',
            'I can try asking around for some money. I’m sure my neighbors would help.',
            'I just got to be sure that I don’t get on neighbors’ bad sides, otherwise they won’t help me.',
            'Well whatever I do, I just need some money for the payphone.'
            ]

c_travel = ['I didn’t want to call my parents ...',
            'If they didn’t support me then, what would make them support me now?',
            'Only thing I can do is move forward',
            'There is bound to be opportunity elsewhere.'
            ]

c_statusquo = ['Well I didn’t get enough money for a payphone or to leave town.',
                'Talking to my parents wouldn’t had helped me anyways ...',
                'I guess I can try to get my farm in working order again.',
                'All I can do is wait.'
                ]

c_hangup = ['At least I told my parents how I felt ... that felt somewhat nice.',
            'But I just don’t understand why they won’t support me ... why can\' they accept me for who I am?',
            'I just need to continue, I can’t linger on my parents forever.',
            'Back to the farm then. Or will I leave the town? I guess I can go anywhere as long as it\'s forward'
            ]

c_familychef = ['I guess now I\'ll pack up and return home. Parents paid for my flight too.',
                'The only way I can see my parents smile again is to become a pizza chef.',
                'I don’t want to be a pizza chef, but I can’t stay a farmer forever.',
                'This is okay, I think I can make it work.'
                ]

c_reunion = ['I can’t believe my parents actually support me.',
                'Maybe I was mistaken after all .. It was just a huge misunderstanding.',
                'I need to get home as soon as possible to see my parents in person.',
                'Then I can talk about them about my farming situation … it’s time to go.'
                ]


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller ; useful for opening images """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = ""
    finally:
        return os.path.join(base_path, relative_path)

def load_font(main_folder, file_folder):
    ''' just loads the font '''
    r_path = resource_path(main_folder)
    full_path = os.path.join(r_path,file_folder)
    return full_path

def renderTextCenteredAt(text:str, font:str, colour, x:int, y:int, screen, allowed_width:int):
    ''' helper function that does text wrapping '''
    var = 0
    # first, split the text into words
    words = text.split()
    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them
    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)
        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset
        var = tx
        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))
        y_offset += fh

    return tx

def monolog(display_surface,body:str,name:str=None,size=26):
    ''' when somebody be preachin '''
    condition = True
    dialog_ = pygame.Rect(0,528,1280,192)
    font = pygame.font.Font(load_font('game_assets','arial.ttf'),size)
    space_font = pygame.font.Font(load_font('game_assets','arial.ttf'),20)
    while condition:
        pygame.display.flip() # update full display surface to screen
        pygame.draw.rect(display_surface,(230,230,230),dialog_)
        if name:
            full_dialog = "["+name+"]: "+body
        else:
            full_dialog = body
        renderTextCenteredAt(full_dialog,font,(0,0,0),640,560,display_surface,1152)
        renderTextCenteredAt('Press space to continue',space_font,(0,0,0),640,680,display_surface,1152)
        #words = font.render(full_dialog, True, (0, 0, 0),(230,230,230))
        #advice = font.render('press space to continue',True,(0,0,0),(230,230,230))
        #display_surface.blit(words,(0,528))
        #display_surface.blit(advice,(640,656))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    condition = False
            elif event.type == pygame.QUIT:
                condition = False
                pygame.quit()

def choice(display_surface,choices:list,size=26,pointer=None,controlclass=None):
    ''' preferably takes in a list of elements ... 3 at most ; 2 at least '''
    condition = True
    dialog_ = pygame.Rect(0,528,1280,192)
    font = pygame.font.Font(load_font('game_assets','arial.ttf'),size)
    space_font = pygame.font.Font(load_font('game_assets','arial.ttf'),20)
    choice_num = 1
    while condition:
        pygame.display.flip() # update full display surface to screen
        pygame.draw.rect(display_surface,(230,230,230),dialog_)
        initial_offset_y = 544
        leftmost_nums = [] # get a list of the leftmosts
        for choice in choices:
            full_dialog = choice
            leftmost_num_temp = renderTextCenteredAt(full_dialog,font,(0,0,0),640,initial_offset_y,display_surface,1152)
            leftmost_nums.append(leftmost_num_temp)
            initial_offset_y += 40
        renderTextCenteredAt('Press space to continue',space_font,(0,0,0),640,680,display_surface,1152)
        display_surface.blit(pointer,updatepointer(choice_num,'dialogchoice',leftmost_nums))
        #words = font.render(full_dialog, True, (0, 0, 0),(230,230,230))
        #advice = font.render('press space to continue',True,(0,0,0),(230,230,230))
        #display_surface.blit(words,(0,528))
        #display_surface.blit(advice,(640,656))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    condition = False
                    return choice_num
                elif event.key == K_UP or event.key == K_w:
                    choice_num -= 1
                elif event.key == K_DOWN or event.key == K_s:
                    choice_num += 1
                if choice_num < 1: # constrain to 1 <= x <= 3
                    choice_num = len(choices)
                elif choice_num > len(choices):
                    choice_num = 1
            elif event.type == pygame.QUIT:
                condition = False
                pygame.quit()

def countdisplay(display_surface,image_surface,x,y):
    display_surface.blit(image_surface,(x,y))
    font = pygame.font.Font(load_font('game_assets','arial.ttf'),20)
    l_money = "$"+str(money//100)+"."+str(money%100)
    center_x = x + image_surface.get_width()//2
    center_y = y + image_surface.get_height()//2
    renderTextCenteredAt(l_money,font,(0,0,0),center_x,center_y,display_surface,60)

def updatepointer(mode_int:int,mode:str,xposition:list=None): # just updates the position of the pointer in the main menu 
    ''' only serves to change position of pointer on main menu'''
    if mode == 'menu':
        if mode_int == 1:
            return (370,264)
        elif mode_int == 2:
            return (370,384)
        elif mode_int == 3:
            return (370,494)
        elif mode_int == 4:
            return (370,620)
    elif mode == 'dialogchoice': # uses self._screen.blit(self._pointer,updatepointer(self._controlclass._mode,'dialogchoice')) # renders image
        if mode_int == 1:
            return (xposition[0]-96,550)
        elif mode_int == 2:
            return (xposition[1]-96,590)
        elif mode_int == 3:
            return (xposition[2]-96,630)

def tick_clock(): # helper function in getting frames
    ''' get the ticks of the clock '''
    current_time = pygame.time.get_ticks()
    return current_time

#def showSprite(sprite):
#    ''' adds the sprite to sprite group '''
#    spriteGroup.add(sprite)

def load_image_clear(main_folder,file_folder):
    ''' loads an image, given main_folder path and file_folder (name.format); any image will do '''
    # using os.path.join(folder_location, file_name)
    # convert_alpha() allows for transparency
    r_path = resource_path(main_folder) # this will allow the game to work in development / when it's published
    full_path = os.path.join(r_path,file_folder)
    try:
        image = pygame.image.load(full_path)
        image = image.convert_alpha()
        return image
    except Exception as error:
        print ('Cannot load image:', full_path)
        raise SystemExit(str(error))

def load_tile_table(filename, width, height):
    ''' parses png image that is a tile map .. note that this doesnt work for tilemaps with any spaces '''
    image = load_image_clear('game_assets',filename)
    image = image.convert_alpha() # for transparency purposes ...
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width//width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height//height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect)) # gets an image from the bigger image
    return tile_table

class Wall(object):
    ''' basic walls '''
    def __init__(self, pos):
        rect = pygame.Rect(pos[0], pos[1], 64, 64)
        g_walls.append(rect)

class Door(object):
    ''' door objects '''
    def __init__(self, pos, destination, name, newpos):
        self._dest = destination
        self._newpos = newpos
        self._name = name
        self.rect = pygame.Rect(pos[0]-32,pos[1]-32, 128,128)
        g_doors_interact.append(self)
        solid = pygame.Rect(pos[0], pos[1], 64, 64)
        g_doors_solid.append(solid)

class Examine(object):
    ''' examinable objects '''
    def __init__(self, pos,flavor):
        self._text = flavor
        self.rect = pygame.Rect(pos[0], pos[1], 64, 64)
        self.rect = pygame.Rect(pos[0]-32,pos[1]-32, 128,128)
        g_examine.append(self)
        solid = pygame.Rect(pos[0], pos[1], 64, 64)
        g_examine_solid.append(solid)

class Char(object):
    ''' characters !'''
    def __init__(self, char_talk:list, you_talk:list, personality:str, name_:str, type:str, pos:tuple,image_surf=None):
        self._x = pos[0]
        self._y = pos[1]
        if type == 'tile':    
            self.rect = pygame.Rect(pos[0]-32,pos[1]-32, 128,128)
            solid = pygame.Rect(pos[0], pos[1], 64, 64)
            g_characters.append(self)
            g_characters_solid.append(solid)
        else:
            self.rect = pygame.Rect(pos[0]-32,pos[1]-32, image_surf.get_width()+64,image_surf.get_height()+64)
            solid = pygame.Rect(pos[0], pos[1], image_surf.get_width(), image_surf.get_height())
            g_characters.append(self)
            g_characters_solid.append(solid)
        self._chartalk = char_talk
        self._youtalk = you_talk
        self._talked = False
        self._mood = 0
        self._trait = personality # 'red','blue','green'
        self._choices = {'green':1,'blue':2,'red':3}
        self._name = name_
        self._image = image_surf

    def converse(self, surface_,point,cclass,app=None):
        if not self._talked:
            self._talked = True
            # conversation 1
            monolog(surface_,self._chartalk[0],self._name)
            c1 = choice(surface_,self._youtalk[0:3],pointer=point,controlclass=cclass)
            if c1 == 1:
                monolog(surface_,self._chartalk[1],self._name)
            elif c1 == 2:
                monolog(surface_,self._chartalk[2],self._name)
            else:
                monolog(surface_,self._chartalk[3],self._name)
            if c1 == 3 and self._trait == 'green': self._mood -=1
            elif c1 == 1 and self._trait == 'red': self._mood -=1
            elif c1 == 3 and self._trait == 'blue': self._mood -=1
            elif c1 == self._choices[self._trait]: 
                if self._trait == 'red':
                    self._mood -= 1
                else:
                    self._mood +=1
            # conversation 2
            monolog(surface_,self._chartalk[4],self._name)
            c2 = choice(surface_,self._youtalk[3:6],pointer=point,controlclass=cclass)
            if c2 == 1:
                monolog(surface_,self._chartalk[5],self._name)
            elif c2 == 2:
                monolog(surface_,self._chartalk[6],self._name)
            else:
                monolog(surface_,self._chartalk[7],self._name)
            if c2 == 3 and self._trait == 'green': self._mood -=1
            elif c2 == 1 and self._trait == 'red': self._mood -=1
            elif c2 == 3 and self._trait == 'blue': self._mood -=1
            elif c2 == self._choices[self._trait]:
                if self._trait == 'red':
                    self._mood -= 1
                else:
                    self._mood +=1
            # conversation 3
            monolog(surface_,self._chartalk[8],self._name)
            c3 = choice(surface_,self._youtalk[6:9],pointer=point,controlclass=cclass)
            if c3 == 1:
                monolog(surface_,self._chartalk[9],self._name)
            elif c3 == 2:
                monolog(surface_,self._chartalk[10],self._name)
            else:
                monolog(surface_,self._chartalk[11],self._name)
            if c3 == 3 and self._trait == 'green': self._mood -=1
            elif c3 == 1 and self._trait == 'red': self._mood -=1
            elif c3 == 3 and self._trait == 'blue': self._mood -=1
            elif c3 == self._choices[self._trait]:
                if self._trait == 'red':
                    self._mood -= 1
                else:
                    self._mood +=1
            # end result
            monolog(surface_,self._chartalk[12],self._name)
            if self._mood == 3:
                monolog(surface_,self._chartalk[13],self._name)
                monolog(surface_,self._chartalk[14],self._name)
                monolog(surface_,self._chartalk[15],self._name)
            elif self._mood >= 0:
                monolog(surface_,self._chartalk[16],self._name)
                monolog(surface_,self._chartalk[17],self._name)
                monolog(surface_,self._chartalk[18],self._name)
            elif self._mood < 0:
                monolog(surface_,self._chartalk[19],self._name)
                monolog(surface_,self._chartalk[20],self._name)
                monolog(surface_,self._chartalk[21],self._name)
            if self._name != 'Your dad' and self._name != 'Gate':
                self.determine()
            else:
                self.ending(surface_,app._cutscenes)
        else:
            if self._mood == 3:
                monolog(surface_,self._chartalk[15],self._name)
            elif self._mood >= 0:
                monolog(surface_,self._chartalk[18],self._name)
            elif self._mood < 0:
                monolog(surface_,self._chartalk[21],self._name)

    def determine(self):
        # finds out if the character will give you money or not
        global money, characters_mad, total_characters
        if self._mood >= 0 and self._trait == 'green':
            money+=20
        elif self._mood >= 0 and self._trait == 'blue':
            money+=20
        elif self._mood <= 0 and self._trait == 'red':
            money+=20
        elif self._mood < 0 and self._trait == 'green' or self._mood < 0 and self._trait == 'blue':
            characters_mad += 1
        elif self._mood > 0 and self._trait == 'red':
            characters_mad += 1
        total_characters -= 1
        # otherwise you don't get the money :)
    
    def ending(self, surface_, image_endings:list): # only for the gate and for the payphone
        lecture = False
        while True:
            surface_.fill([125,125,125])
            if not lecture:
                if self._mood == 3:
                    for text in c_reunion:
                        monolog(surface_,text)
                elif self._mood >= 0:
                    for text in c_familychef:
                        monolog(surface_,text)
                else:
                    for text in c_hangup:
                        monolog(surface_,text)
                lecture = True
            else:
                if self._mood == 3:
                    surface_.blit(image_endings[5],(0,0))
                elif self._mood >= 0:
                    surface_.blit(image_endings[4],(0,0))
                else:
                    surface_.blit(image_endings[3],(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    condition = False
                    pygame.quit()
            pygame.display.flip()
            
        # do something with mood here to calculate and show the endings

class Level:
    ''' manages all tile stuff '''
    def __init__(self,filename, width, height, currentmap):
        self._ttable = load_tile_table(filename, width, height)
        self._cmap = currentmap

    def getspritemap(self):
        return self._ttable

    #def getrect(self,ty:int,tx:int):
    #    return self._ttable[ty][tx].get_rect()

    def getlevel(self):
        return self._cmap


class newSprite(pygame.sprite.Sprite):
    ''' makes a sprite, splits up a spritesheet walkcycle into multiple pics '''
    def __init__(self, filename, frames=1):
        # DO NOT MESS WITH THIS __init__ IT IS MAGIC
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = load_image_clear('game_assets',filename)
        self.originalWidth = img.get_width() // frames
        self.originalHeight = img.get_height()
        frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
        x = 0
        for frameNo in range(frames):
            frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
            frameSurf.blit(img, (x, 0))
            self.images.append(frameSurf.copy())
            x -= self.originalWidth
        self.image = pygame.Surface.copy(self.images[0])

        self.currentImage = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1

    def addImage(self, filename):
        self.images.append(load_image_clear('game_assets',filename))

    #def move(self, xpos, ypos, centre=False):
    #    if centre:
    #        self.rect.center = [xpos, ypos]
    #    else:
    #        self.rect.topleft = [xpos, ypos]

    def changeImage(self, index):
        self._currentImage = index
        if self.angle == 0 and self.scale == 1:
            self.image = self.images[index]
        else:
            self.image = pygame.transform.rotozoom(self.images[self.currentImage], -self.angle, self.scale) # I have no idea how this works nor will I want to test it
        oldcenter = self.rect.center
        self.rect = self.image.get_rect()
        originalRect = self.images[self.currentImage].get_rect()
        self.originalWidth = originalRect.width
        self.originalHeight = originalRect.height
        self.rect.center = oldcenter
        self.mask = pygame.mask.from_surface(self.image)
        #if screenRefresh:
        #    updateDisplay()

class Player_avatar(newSprite):
    ''' player class for managing player object '''
    def __init__(self,filename, frames=1):
        super().__init__(filename, frames)
        self._x,self._y = (400,400)
        self.rect.x = self._x
        self.rect.y = self._y
        self._interactbool = False
        self._possibledest = None
        self._destname = None
        self._newpos = None
        self._talkcharacter = None
        self._flavortext = None

    def getCoordinates(self):
        return self._x,self._y

    def move(self,direction:str,facing:str,num_pixels:int,frame_num:int): # perhaps manage collision here as well :>
        # implement non cardinal directions?
        if direction: # if the key is pressed or being pressed.
            if direction == 'left': # the four main directions, north, east, south, west.
                super().changeImage(3*8+frame_num)
                self._x -= num_pixels
                self.rect.x -= num_pixels
            elif direction == 'right':
                super().changeImage(2*8+frame_num)
                self._x += num_pixels
                self.rect.x += num_pixels
            elif direction == 'up':
                super().changeImage(1*8+frame_num)
                self._y -= num_pixels
                self.rect.y -= num_pixels
            elif direction == 'down':
                super().changeImage(0+frame_num)
                self._y += num_pixels
                self.rect.y += num_pixels

            # HANDLING COLLISION HERE.

            for wall in g_walls+g_doors_solid+g_examine_solid+g_characters_solid: # everything that is a solid
                if self.rect.colliderect(wall):
                    #print(wall.rect.x,wall.rect.y)
                    if direction == 'right': # Moving right; Hit the left side of the wall
                        self._x -= num_pixels
                        self.rect.x -= num_pixels
                    if direction == 'left': # Moving left; Hit the right side of the wall
                        self._x += num_pixels
                        self.rect.x += num_pixels
                    if direction == 'down': # Moving down; Hit the top side of the wall
                        self._y -= num_pixels
                        self.rect.y -= num_pixels
                    if direction == 'up': # Moving up; Hit the bottom side of the wall
                        self._y += num_pixels
                        self.rect.y += num_pixels
            
            self._interactbool = False
            self._possibledest = None
            self._destname = None
            self._newpos = None
            self._talkcharacter = None
            self._flavortext = None

            for door in g_doors_interact: # ... 'hitbox detection'
                if self.rect.colliderect(door.rect):
                    self._interactbool = True
                    self._possibledest = door._dest
                    self._destname = door._name
                    self._newpos = door._newpos

            for char in g_characters:
                if self.rect.colliderect(char.rect):
                    self._interactbool = True
                    self._talkcharacter = char

            for ex in g_examine:
                if self.rect.colliderect(ex.rect):
                    self._interactbool = True
                    self._flavortext = ex._text

        else: # to arrange the character in right orientation after moving
            if facing == 'left': # the four main directions, north, east, south, west.
                super().changeImage(3*8)
            elif facing == 'right':
                super().changeImage(2*8)
            elif facing == 'up':
                super().changeImage(1*8)
            elif facing == 'down':
                super().changeImage(0)

    def getrect(self):
        return self.rect
        
class Controls:
    ''' player controls '''
    global g_walls, g_examine, g_characters, g_doors_solid, g_doors_interact

    def __init__(self):
        self._pdirection = None # used to see if moving
        self._facing = None # used to make a character face direction after moving
        self._pressedkeys = (None,None)
        self._iscollide = False
        self._mode = 1 # mode = [0,1,2,3,4] ; 0 = menu, 1 = play, 2 = credit, 3 = debug, 4 = quit
        self._instructions = 1 # 1 instruction ... 2 disclaimer ...

    def on_key_down(self, mode:str, event, player:Player_avatar, playername:str=None, point=None, surface=None, app=None): # when a key is pressed
        if mode == 'Debug' or mode == 'Play':
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self._pdirection = 'left'
                self._facing = 'left'
                self._pressedkeys = ('a','left')
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self._pdirection = 'right'
                self._facing = 'right'
                self._pressedkeys = ('d','right')
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self._pdirection = 'down'
                self._facing = 'down'
                self._pressedkeys = ('s','down')
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self._pdirection = 'up'
                self._facing = 'up'
                self._pressedkeys = ('w','up')
            elif event.key == pygame.K_SPACE and player._interactbool:
                if type(player._possibledest)==int and 0<=player._possibledest:
                    if mode == 'Debug':
                        monolog(surface,'Do you want to go '+player._destname+'?')
                        tempc = choice(surface,['Yes','No'],pointer=point,controlclass=self)
                        if tempc == 1:
                            monolog(surface,'This is just a test door; it doesnt work in debug.')
                    else: # it's play mode
                        monolog(surface,'Do you want to go '+player._destname+'?')
                        tempc = choice(surface,['Yes','No'],pointer=point,controlclass=self)
                        if tempc == 1:
                            app._area = player._possibledest
                            g_walls.clear()
                            g_doors_solid.clear()
                            g_doors_interact.clear()
                            g_examine_solid.clear()
                            g_examine.clear()
                            g_characters_solid.clear()
                            g_characters.clear()
                            player._x = player._newpos[0]
                            player.rect.x = player._x
                            player._y = player._newpos[1]
                            player.rect.y = player._y
                            player._interactbool = False
                            player._destname = None
                            player._possibledest = None
                            player._newpos = None
                            app._loadarea = False
                elif player._talkcharacter:
                    if player._talkcharacter._name == 'Your dad':
                        if money < 100:
                            monolog(surface,'I need $1 to use this payphone. I should try talking to the people in this town.')
                        else:
                            monolog(surface,'I have enough for the payphone. Do I really want to call my parents? Maybe I can leave town by paying $1 for the cop to raise the crossing gate...')
                            tempc = choice(surface,['Yes, call my parents.','No, I need to think about this.'],pointer=point,controlclass=self)
                            if tempc == 1:
                                player._talkcharacter.converse(surface,point,self,app)
                                player._interactbool = False
                                player._talkcharacter = None
                
                    elif player._talkcharacter._name == 'Gate':
                        if money < 100:
                            monolog(surface,'I need $1 to pay the toll to lift this gate and to leave town. I should try talking to the people in this town.')
                        else:
                            monolog(surface,'Do I really want to leave town ..? I can still call my parents.')
                            tempc = choice(surface,['Leave town.','No, I need to think about this.'],pointer=point,controlclass=self)
                            if tempc == 1:
                                lecture = False
                                while True:
                                    surface.fill([125,125,125])
                                    if not lecture:
                                        for text in c_travel:
                                            monolog(surface,text)
                                        lecture = True
                                    else:
                                        surface.blit(app._cutscenes[1],(0,0))
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            condition = False
                                            pygame.quit()
                                    pygame.display.flip()
                    else:
                        monolog(surface,'Do you want to talk with '+player._talkcharacter._name+'?')
                        tempc = choice(surface,['Yes','No'],pointer=point,controlclass=self)
                        if tempc == 1:
                            player._talkcharacter.converse(surface,point,self)
                            player._interactbool = False
                            player._talkcharacter = None
                
                elif player._flavortext:
                    monolog(surface,player._flavortext,playername)
    
            if mode == 'Debug':
                if event.key == pygame.K_q: # deleter
                    g_walls.clear()
                    g_doors_solid.clear()
                    g_doors_interact.clear()
                    g_examine_solid.clear()
                    g_examine.clear()
                    g_characters_solid.clear()
                    g_characters.clear()
                    
        elif mode == 'Menu':
            if self._mode < 1: # constrain to 1 <= x <= 4
                self._mode = 4
            elif self._mode >4:
                self._mode = 1

            if event.key == pygame.K_SPACE:
                return self._mode # 4 is quit
            else:
                return None

        elif mode == 'Credits':
            if event.key == pygame.K_SPACE:
                self._mode = 1
                return 0 
            else:
                return None

        elif mode == 'Instructions':
            if event.key == pygame.K_SPACE:
                self._instructions += 1
                if self._instructions >= 3:
                    return 0
                else:
                    return None 
            else:
                return None

    def on_key_up(self, mode:str, event, player:Player_avatar): # whenver a key is released
        if mode == 'Debug' or mode == 'Play':
            key_released = pygame.key.name(event.key)
            if key_released in self._pressedkeys: # if you pressed two keys at once .. and release the first key, then char will not stop
                self._pdirection = None

    def getdir(self):
        return self._pdirection

    def getfacing(self):
        return self._facing

class Application:
    ''' main class for defining the specifics of the game '''

    def __init__(self): # initializes variables
        ''' character name '''
        #global playername
        self._playername = "Adrian"
        #playername = self._playername
        update_words(self._playername)

        self._running = True
        self._screen = None # display window, that is a surface object
        self.size = (self.weight, self.height) = (1280, 720) # 640, 400 small ; 1280, 720 med; 1920, 1080 large
        self._gameicon = None
        self._modes = ['Menu','Play','Credits','Debug','Quit','Instructions']
        self._chosenmode = 5 # index of _modes
        self._area = 0
        self._loadarea = False

        # area 1, area 2 main ; area 3+ are just the rooms (7 for the 7 rooms: player, farmer, coolguy,grandma,grocer,cashier,doctor)
        self._controlclass = Controls()     

    def on_init(self): # initialization of window
        pygame.init() # initializes pygame modules
        pygame.display.set_caption('Money for a payphone ver 1.0') # set application name, need to call this before displaying mode
        self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF) # | is a bitwise OR.
        self._clock = pygame.time.Clock()
        self._running = True

        # screens
        self._instructions = load_image_clear('game_assets','instructions.png')
        self._disclaimer = load_image_clear('game_assets','disclaimer.png')
        self._menuscreen = load_image_clear('game_assets','title_screen.png')
        self._creditsscreen = load_image_clear('game_assets','credits.png')
        self._namescreen = load_image_clear('game_assets','name_enter.png')

        a = load_image_clear('game_assets','cutscene_1_intro.png')
        b = load_image_clear('game_assets','cutscene_2_travel.png')
        c = load_image_clear('game_assets','cutscene_3_statusquo.png')
        d = load_image_clear('game_assets','cutscene_4_hangup.png')
        e = load_image_clear('game_assets','cutscene_5_chef.png')
        f = load_image_clear('game_assets','cutscene_6_familyreunion.png')
        self._cutscenes = [a,b,c,d,e,f]
        # game play visuals
        self._gameicon = load_image_clear('game_assets','circle_char_icon.png')
        self._pointer = load_image_clear('game_assets','pointer.png')
        self._bubble = load_image_clear('game_assets','quote_bubble.png')
        self._mcounter = load_image_clear('game_assets','counter.png')

        # characters
        self._playerchar = Player_avatar('Circle_char_walkcycle.png',32)
        self._farmer = load_image_clear('game_assets','farmer_char.png')
        self._grandma = load_image_clear('game_assets','grandma_char.png')
        self._coolguy = load_image_clear('game_assets','coolguy_char.png')
        self._grocer = load_image_clear('game_assets','grocer_char.png')
        self._attendantchar = load_image_clear('game_assets','attendant_char.png')
        self._doctor = load_image_clear('game_assets','doc_char.png')

        # game settings and main loop
        pygame.display.set_icon(self._gameicon)
        self._levelclass = Level('master_map.png',64,64,mainmap0)
        self._table = self._levelclass.getspritemap()
        #showSprite(self._playerchar)

        # just for debug
        self._debugdebounce = False
        self._loadintro = False
        self._chosename = False

    def on_event(self, event): # checks if event == quit, meaning if we exited.
        mode = self._modes[self._chosenmode]
        if event.type == pygame.QUIT:
            self._running = False
        elif mode == 'Debug':
            if event.type == KEYDOWN:
                self._controlclass.on_key_down(mode,event,self._playerchar,playername,self._pointer,self._screen,self)
            elif event.type == KEYUP:
                self._controlclass.on_key_up(mode,event,self._playerchar)
        elif mode == 'Menu':
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_s:
                    self._controlclass._mode += 1
                elif event.key == K_UP or event.key == K_w:
                    self._controlclass._mode -= 1
                possible_mode = self._controlclass.on_key_down(mode,event,self._playerchar)
                if possible_mode:
                    if possible_mode == 4:
                        self._running = False
                    else:
                        self._chosenmode = possible_mode
        elif mode == 'Credits' or mode == 'Instructions':
            if event.type == KEYDOWN:
                possible_mode = self._controlclass.on_key_down(mode,event,self._playerchar)
                if possible_mode==0:
                    self._chosenmode = possible_mode
        elif mode == 'Play':
            if event.type == KEYDOWN:
                self._controlclass.on_key_down(mode,event,self._playerchar,playername,self._pointer,self._screen,self)
            elif event.type == KEYUP:
                self._controlclass.on_key_up(mode,event,self._playerchar)

    def on_cleanup(self): # exits the program
        pygame.quit()

    def on_loop(self,frame): # updating values; 
        self._playerchar.move(self._controlclass.getdir(),self._controlclass.getfacing(),5,frame) # moves player if player is in moving state.
        if self._chosenmode == 1: # if we are in play mode
            if self._area == 0:
                playx,playy = self._playerchar.getCoordinates()
                if playx > 1264:
                    g_walls.clear()
                    g_doors_solid.clear()
                    g_doors_interact.clear()
                    g_examine_solid.clear()
                    g_examine.clear()
                    g_characters_solid.clear()
                    g_characters.clear()
                    self._area = 1
                    self._playerchar._x = 32
                    self._playerchar.rect.x = self._playerchar._x
                    self._loadarea = False
                
            elif self._area == 1:
                playx,playy = self._playerchar.getCoordinates()
                if playx < 16:
                    g_walls.clear()
                    g_doors_solid.clear()
                    g_doors_interact.clear()
                    g_examine_solid.clear()
                    g_examine.clear()
                    g_characters_solid.clear()
                    g_characters.clear()
                    self._area = 0
                    self._playerchar._x = 1216
                    self._playerchar.rect.x = self._playerchar._x
                    self._loadarea = False
                #elif playy < 32:
                #    print('cannot go up')
                #    self._playerchar._y += 10
                #    self._playerchar.rect.y = self._playerchar._y
                elif playy > 688:
                    self._playerchar._y -= 100
                    self._playerchar.rect.y = self._playerchar._y
            elif characters_mad == 3: # bad ending
                monolog(self._screen,'. . .')
                monolog(self._screen,'I think I made too many people frustrated with me. I won\'t be able to get $1 from the rest of these people in town! Dangit.')
                lecture = False
                while True:
                    self._screen.fill([125,125,125])
                    if not lecture:
                        for text in c_statusquo:
                            monolog(self._screen,text)
                        lecture = True
                    else:
                        self._screen.blit(self._cutscenes[2],(0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            condition = False
                            pygame.quit()
                    pygame.display.flip()

    def on_render(self,frame): # rendering and loading images
        mode = self._modes[self._chosenmode]
        if mode=='Debug':
            self._screen.fill([255,255,255]) # white background ; for testing surfaces
            dialog = False
            if not self._debugdebounce: 
                self._debugdebounce = True
                Wall((200,100))
                Wall((200,164))
                Door((500,500),0,'in this green square that is supposed to be a door',(0,0))
                Char(gas_talk,gas_play,'green','Attendant','image',(700,400),self._attendantchar)
                Examine((900,200),'This is a green square. That is all.')
                monolog(self._screen,'This is the debug menu where I test stuff. Some things may not work properly here (like the door).','debug_menu')

            # draw hitbox area before drawing solid area
            for door_obj in g_doors_interact:
                pygame.draw.rect(self._screen, (255, 0, 0), door_obj.rect)

            for char_obj in g_characters:
                pygame.draw.rect(self._screen, (0, 0, 255), char_obj.rect)

            for ex_obj in g_examine:
                pygame.draw.rect(self._screen, (0, 0, 255), ex_obj.rect)

            for wall in g_walls+g_doors_solid+g_examine_solid+g_characters_solid:
                pygame.draw.rect(self._screen, (0, 255, 0), wall)    
            
            for character in g_characters:
                if character._name == 'Attendant':
                    self._screen.blit(self._attendantchar,(character._x,character._y))
                elif character._name == 'Farmer':
                    self._screen.blit(self._farmer,(character._x,character._y))
                elif character._name == 'Grandma':
                    self._screen.blit(self._grandma,(character._x,character._y))
                elif character._name == 'Coolguy':
                    self._screen.blit(self._coolguy,(character._x,character._y))
                elif character._name == 'Grocer':
                    self._screen.blit(self._grocer,(character._x,character._y))
                elif character._name == 'Doctor':
                    self._screen.blit(self._doctor,(character._x,character._y))

            self._screen.blit(self._playerchar.image,(self._playerchar.getCoordinates())) # renders image

            if self._playerchar._interactbool:
                tempx, tempy = self._playerchar.getCoordinates()
                self._screen.blit(self._bubble,(tempx,tempy-64))

            #spriteGroup.clear(self._playerchar.image, self._screen)
            countdisplay(self._screen,self._mcounter,0,0)
        elif mode=='Menu':
            self._screen.blit(self._menuscreen,(0,0)) # renders image
            self._screen.blit(self._pointer,updatepointer(self._controlclass._mode,'menu')) # renders image
        elif mode=='Credits':
            self._screen.blit(self._creditsscreen,(0,0)) # renders image
        elif mode=='Instructions':
            if self._controlclass._instructions == 1:
                self._screen.blit(self._disclaimer,(0,0))
            else:
                self._screen.blit(self._instructions,(0,0))

        elif mode=='Play':
            self._screen.fill([125,125,125]) # gray background ; for testing surfaces

            if not self._chosename: # asks for your name
                temp_name = ""
                temp_font = pygame.font.Font(load_font('game_assets','arial.ttf'),26)
                monolog(self._screen,'Enter your first name. Only use alphabetical characters. First letter will be automatically capitalized. Press space to confirm name, and press backspace to delete characters.')
                while_loop = True
                while while_loop:
                    pygame.display.flip()
                    self._screen.blit(self._namescreen,(0,0))
                    if len(temp_name)>=1:
                        renderTextCenteredAt(temp_name,temp_font,(0,0,0),600,270,self._screen,600)
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_SPACE:
                                monolog(self._screen,'Are you sure this is your name?')
                                temp_choice = choice(self._screen,['Yes','No'],pointer=self._pointer,controlclass=self._controlclass)
                                if temp_choice == 1:
                                    self._playername = temp_name
                                    update_words(temp_name)
                                    while_loop = False
                                    self._chosename = True
                            elif event.type == pygame.QUIT:
                                while_loop = False
                                self._chosename = True
                                pygame.quit()
                            elif 97<=event.key<=122:
                                if len(temp_name)<10:
                                    temp_name = temp_name + pygame.key.name(event.key)
                                    if len(temp_name)==1:
                                        temp_name = temp_name[0].upper()
                                else:
                                    monolog(self._screen,'You have reached the max characters. Press backspace to delete characters.')
                            elif event.key==8: # backspace
                                temp_name = temp_name[:-1]

            if not self._loadintro:
                self._screen.blit(self._cutscenes[0],(0,0))
                for phrase in c_intro:
                    monolog(self._screen,phrase)
                self._loadintro = True

            if not self._loadarea:
                # set collision rectangles ... special objects and characters
                obstacles = [(0,1),(0,7),(0,8),(0,11),(0,12),
                            (1,0),(1,1),(1,7),(1,8),(1,11),
                            (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(2,12),(2,13),(2,14),(2,17),(2,18),
                            (3,1),(3,2),(3,5),(3,6),(3,8),(3,10),(3,11),(3,12),(3,14),(3,18),(3,19),
                            (4,2),(4,10),(4,18),
                            (5,3),(5,5),(5,8),(5,12),(5,13),(5,19),
                            (6,1),(6,4),(6,5),(6,7)
                            ]
                            
                l_doors = [(2,11),(3,0),(3,3),(3,4),(3,7),(3,9),(3,13),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9)]
                characters = [(2,19),(3,17),(4,1)] #(2,19) will be place to exit town
                examine = [(2,15),(2,16),(4,11),(4,13),(4,14),(4,15),(4,16),(4,19),(5,0),(5,1),(5,2),(5,6),(5,7),(5,9),(5,10),(5,14),(5,15),(5,16),(5,18),(6,0),(6,2),(6,3)]
                self._loadarea = True
                for x, row in enumerate(maps[self._area]):
                    for y, tile_val in enumerate(row):
                        if tile_val in obstacles:
                            Wall((y*64,x*64))
                            #print('wall at!'+str(y*64)+' '+str(x*64))
                        elif tile_val in l_doors:
                            if tile_val == (2,11):
                                Door((y*64,x*64),7,'in the gas station',(256,256))
                            elif tile_val == (3,0):
                                Door((y*64,x*64),2,'in your house',(256,256))
                            elif tile_val == (3,3):
                                Door((y*64,x*64),3,'in the farmer\'s house',(256,256))
                            elif tile_val == (3,4):
                                Door((y*64,x*64),4,'in the grandma\'s house',(256,256))
                            elif tile_val == (3,7):
                                Door((y*64,x*64),5,'in the cool guy\'s house',(256,256))
                            elif tile_val == (3,9):
                                Door((y*64,x*64),6,'in the grocery',(260,260))
                            elif tile_val == (3,13):
                                Door((y*64,x*64),8,'in the doctor\'s office',(256,256))
                            elif tile_val == (4,3): 
                                Door((y*64,x*64),0,'outside',(256,384))
                            elif tile_val == (4,4):
                                Door((y*64,x*64),0,'outside',(192,576))
                            elif tile_val == (4,5):
                                Door((y*64,x*64),0,'outside',(768,320))
                            elif tile_val == (4,6):
                                Door((y*64,x*64),0,'outside',(1024,576))
                            elif tile_val == (4,7):
                                Door((y*64,x*64),1,'outside',(448,576))
                            elif tile_val == (4,8):
                                Door((y*64,x*64),1,'outside',(1024,192))
                            elif tile_val == (4,9):
                                Door((y*64,x*64),1,'outside',(1088,576))
                        elif tile_val in examine:
                            if tile_val == (2,15):
                                Examine((y*64,x*64),'this \'doctor\' sign is pointing to the doctor\'s office across the street')
                            elif tile_val == (2,16):
                                Examine((y*64,x*64),'a gas pump, there is only one setting … \'premium\'')
                            elif tile_val == (4,11):
                                Examine((y*64,x*64),'well the one thing I can admire is the view')
                            elif tile_val == (4,13):
                                Examine((y*64,x*64),'yeah that\'s my bed. Comfortable as a stone slate')
                            elif tile_val == (4,14):
                                Examine((y*64,x*64),'this is where I keep all 3 of my belongings, I have my parent\'s phone number on the desk')
                            elif tile_val == (4,15):
                                Examine((y*64,x*64),'when is my weekly newspaper going to arrive')
                            elif tile_val == (4,16):
                                Examine((y*64,x*64),'I can put 30 bags of these into my garden and my garden is still dead')
                            elif tile_val == (4,19):
                                Examine((y*64,x*64),'despite this rugged appearance, this mattress is very, very comfortable')
                            elif tile_val == (5,0):
                                Examine((y*64,x*64),'I am a bit jealous of his crop yield')
                            elif tile_val == (5,1):
                                Examine((y*64,x*64),'my neighbor is a certified farmer, he taught me everything I know')
                            elif tile_val == (5,2):
                                Examine((y*64,x*64),'I\'m not snooping in my neighbor’s mail')
                            elif tile_val == (5,6):
                                Examine((y*64,x*64),'not only is this a couch, but it is a bed as well')
                            elif tile_val == (5,7):
                                Examine((y*64,x*64),'this plant is nice')
                            elif tile_val == (5,9):
                                Examine((y*64,x*64),'this TV is tuned to some sports channel')
                            elif tile_val == (5,10):
                                Examine((y*64,x*64),'I had a couch like that once. It’s gone now')
                            elif tile_val == (5,14):
                                Examine((y*64,x*64),'yeah all the usual stuff is on sale – like asparagus')
                            elif tile_val == (5,15):
                                Examine((y*64,x*64),'It says .. "everything is 1 cent cheaper".')
                            elif tile_val == (5,16):
                                Examine((y*64,x*64),'holds the mail for everybody here who doesn’t have a mailbox')
                            elif tile_val == (5,18):
                                Examine((y*64,x*64),'smile, you’re on camera')
                            elif tile_val == (6,0):
                                Examine((y*64,x*64),'junk food and whatever')
                            elif tile_val == (6,2):
                                Examine((y*64,x*64),'I don’t need to look at this to know that I’m 20/20 vision')
                            elif tile_val == (6,3):
                                Examine((y*64,x*64),'why is there curtains, this isn\'t a hospital, but a doctor\'s office')
                            
                            
                        elif tile_val in characters: # these characters are tiles
                            if tile_val == (2,19):
                                Char(None,None,None,'Gate','tile',(y*64,x*64))
                            elif tile_val == (3,17):
                                Char(cop_talk,cop_play,'green','Cop','tile',(y*64,x*64))
                            elif tile_val == (4,1):
                                Char(family_talk,family_play,'green','Your dad','tile',(y*64,x*64))
            
                if self._area == 3: # placing characters who are images
                    Char(farmer_talk,farmer_play,'green','Farmer','image',(400,400),self._farmer)
                elif self._area == 4:
                    Char(granny_talk,granny_play,'green','Neighborhood grandma','image',(400,400),self._grandma)
                elif self._area == 5:
                    Char(coolguy_talk,coolguy_play,'red','Cool guy','image',(450,250),self._coolguy)
                elif self._area == 6:
                    Char(grocer_talk,grocer_play,'green','Grocer','image',(500,120),self._grocer)
                elif self._area == 7:
                    Char(gas_talk,gas_play,'green','Attendant','image',(512,128),self._attendantchar)
                elif self._area == 8:
                    Char(doctor_talk,doctor_play,'blue','Doctor','image',(576,320),self._doctor)

            # collision map
            
            for wall in g_walls:
                pygame.draw.rect(self._screen, (0, 255, 0), wall)

            # render the tiles

            for x, row in enumerate(maps[self._area]):
                for y, tile_val in enumerate(row):
                    tile_x, tile_y = tile_val
                    self._screen.blit(self._table[tile_y][tile_x], (y*64, x*64))
            
            # render + make characters ...

            for character in g_characters:
                if character._name == 'Attendant':
                    self._screen.blit(self._attendantchar,(character._x,character._y))
                elif character._name == 'Farmer':
                    self._screen.blit(self._farmer,(character._x,character._y))
                elif character._name == 'Neighborhood grandma':
                    self._screen.blit(self._grandma,(character._x,character._y))
                elif character._name == 'Cool guy':
                    self._screen.blit(self._coolguy,(character._x,character._y))
                elif character._name == 'Grocer':
                    self._screen.blit(self._grocer,(character._x,character._y))
                elif character._name == 'Doctor':
                    self._screen.blit(self._doctor,(character._x,character._y))

            #spriteRects = spriteGroup.draw(self._playerchar.image)
            #self._playerchar.changeImage(frame)
            self._screen.blit(self._playerchar.image,(self._playerchar.getCoordinates())) # renders image
            #spriteGroup.clear(self._playerchar.image, self._screen)

            countdisplay(self._screen,self._mcounter,0,0)

            if self._playerchar._interactbool:
                tempx, tempy = self._playerchar.getCoordinates()
                self._screen.blit(self._bubble,(tempx,tempy-64))

        pygame.display.flip() # update full display surface to screen

    def on_execute(self): # main loop function
        if self.on_init() == False:
            self._running = False
        
        next_frame = tick_clock()
        frame = 0
        while (self._running):
            if tick_clock() > next_frame: # only for the player character walkcycle
                frame = (frame+1)%8
                next_frame += 80
            #print(next_frame,tick_clock()) # prints time
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop(frame)
            self.on_render(frame)
            self._clock.tick(60) # speed of game

        self.on_cleanup()

if __name__ == "__main__" :
    theApp = Application()
    theApp.on_execute()