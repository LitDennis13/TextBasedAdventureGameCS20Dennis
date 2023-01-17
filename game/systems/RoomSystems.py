from player import Player
from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear
import sys

from rooms.roomone import roomone
from rooms.roomtwo import roomtwo
from rooms.roomthree import roomthree
from rooms.roomfour import roomfour
from rooms.roomfive import roomfive
from rooms.roomsix import roomsix
from rooms.roomseven import roomseven
from rooms.roomeight import roomeight
from rooms.roomnine import roomnine
from rooms.roomten import roomten
from rooms.roomeleven import roomeleven
from rooms.roomtwelve import roomtwelve
from rooms.bossroom import bossroom
class roomsystems:
    def go_to_room(player):
        room = rooms
        room.room()
        player.total_health = room.return_total_health()
        player.health = room.return_health()
        player.inventory = room.return_inventory()
        player.room_number = room.return_room_number()
        player.sword_damage = room.return_sword_damage()
    def make_rooms(player):
        global rooms 
        if player.room_number == 0:
            rooms = roomone(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 1:
            rooms = roomtwo(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 2:
            rooms = roomthree(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 3:
            rooms = roomfour(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 4:
            rooms = roomfive(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 5:
            rooms = roomsix(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 6:
            rooms = roomseven(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 7:
            rooms = roomeight(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 8:
            rooms = roomnine(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 9:
            rooms = roomten(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 10:
            rooms = roomeleven(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 11:
            rooms = roomtwelve(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        elif player.room_number == 12:
            rooms = bossroom(player.name,player.health,player.total_health,player.inventory,player.sword_damage)
        else:
            clear()
            print("Congradulations you have finished the game\n")
            inputhandler.entercon()
            clear()
            sys.exit()