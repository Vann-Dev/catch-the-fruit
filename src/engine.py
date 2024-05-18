from src.lib.queue import Queue
from src.map import Map
from src.player import Player
from src.interface import Interface
import time
import msvcrt
import os
from threading import Thread


class GameEngine:
    def __init__(self):
        self.fruit = None
        self.map = None
        self.player = None

        self.interface = Interface(self)
        self.game_mode = "normal"

        self.screen_state = "home_screen"
        self.current_screen = None

        self.total_fruit_collected = 0

        self.game_end = False

        self.__clear_fruit_thread = None

    def init_game(self, game_mode="normal"):
        self.total_fruit_collected = 0
        self.game_mode = game_mode
        self.fruit = Queue()

        self.map = Map(self)
        self.player = Player(self)

        self.player.init(self.map)
        self.map.init(self.player)

        self.map.generate()

    def start(self):
        while True:
            if not self.screen_state:
                continue

            if self.screen_state == "home_screen":
                self.current_screen = self.screen_state
                self.interface.home_screen()

            if self.screen_state == "tutorial":
                self.current_screen = self.screen_state
                self.interface.tutorial_screen()

            if self.screen_state == "credit_screen":
                self.current_screen = self.screen_state
                self.interface.credit_screen()

            if self.screen_state == "select_mode":
                self.current_screen = self.screen_state
                self.interface.select_mode_screen()

            if self.screen_state == "game_screen":
                self.current_screen = self.screen_state
                self.interface.game_screen()

            if self.screen_state == "pause_screen":
                self.current_screen = self.screen_state
                self.interface.pause_screen()

    def controller(self):
        while True:
            if self.game_end:
                break

            key = msvcrt.getch()

            if key == bytes("w", "utf-8"):
                self.player.move("up")
            elif key == bytes("s", "utf-8"):
                self.player.move("down")
            elif key == bytes("a", "utf-8"):
                self.player.move("left")
            elif key == bytes("d", "utf-8"):
                self.player.move("right")
            elif key == b"\x1b":
                if self.current_screen == "tutorial":
                    self.screen_state = "home_screen"

                if self.current_screen == "game_screen":
                    self.screen_state = "pause_screen"

                break
            else:
                continue

            os.system("cls" if os.name == "nt" else "clear")

            self.map.print()

            self.interface.stats_widget()

    def clear_fruit(self):
        if not self.__clear_fruit_thread:
            self.__clear_fruit_thread = Thread(target=self.__clear_fruit)
            self.__clear_fruit_thread.start()

    def __clear_fruit(self):
        while not self.fruit.is_empty():
            self.fruit.dequeue()
            self.total_fruit_collected += 1
            time.sleep(1)

        self.__clear_fruit_thread = None
