from src.lib.queue import Queue
from src.map import Map
from src.player import Player
from src.interface import Interface
from src.lib.constant import screens
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

        self.screen_state = screens["home"]
        self.current_screen = None

        self.total_fruit_collected = 0

        self.game_end = False

        self.__clear_fruit_thread = None

    # method untuk menginisiasi game baru
    def init_game(self, game_mode="normal"):
        self.total_fruit_collected = 0
        self.game_mode = game_mode
        self.fruit = Queue()

        self.map = Map(self)
        self.player = Player(self)

        self.player.init(self.map)
        self.map.init(self.player)

        self.map.generate()

    # method untuk menghandle setiap screen saat berubah
    def start(self):
        while True:
            if not self.screen_state:
                continue

            if self.screen_state == screens["home"]:
                self.current_screen = self.screen_state
                self.interface.home_screen()

            if self.screen_state == screens["tutorial"]:
                self.current_screen = self.screen_state
                self.interface.tutorial_screen()

            if self.screen_state == screens["credit"]:
                self.current_screen = self.screen_state
                self.interface.credit_screen()

            if self.screen_state == screens["select"]:
                self.current_screen = self.screen_state
                self.interface.select_mode_screen()

            if self.screen_state == screens["game"]:
                self.current_screen = self.screen_state
                self.interface.game_screen()

            if self.screen_state == screens["pause"]:
                self.current_screen = self.screen_state
                self.interface.pause_screen()

    # method untuk menghandle setiap tombol yang ditekan
    def controller(self):
        while True:
            # jika game sudah selesai, maka akan keluar dari loop
            if self.game_end:
                break

            # menggunakan msvcrt untuk menghandle input keyboard
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
                if self.current_screen == screens["tutorial"]:
                    self.screen_state = screens["home"]

                if self.current_screen == screens["game"]:
                    self.screen_state = screens["pause"]

                break
            else:
                continue

            # ini berguna untuk membersihkan layar, sehingga kosong
            os.system("cls" if os.name == "nt" else "clear")

            # method yang berfungsi untuk menampilkan interface game
            self.interface.game_screen_playing()

    # method ini untuk menghapus buah-buahan yang sudah diambil
    def clear_fruit(self):
        if not self.__clear_fruit_thread:
            # menggunakan thread untuk menghandle proses menghapus buah-buahan, sehingga game tetap berjalan
            self.__clear_fruit_thread = Thread(target=self.__clear_fruit)
            self.__clear_fruit_thread.start()

    # method ini untuk menghapus buah-buahan yang sudah diambil dan pengecekan apakah sudah selesai
    def __clear_fruit(self):
        while not self.fruit.is_empty():
            self.fruit.dequeue()
            self.total_fruit_collected += 1
            self.interface.game_screen_playing()
            # jika sudah selesai, maka akan menampilkan credit screen
            if self.player.touching_door:
                if self.map.fruit_size < 2 and self.fruit.is_empty():
                    self.screen_state = screens["credit"]
                    self.game_end = True
                    break
                else:
                    self.clear_fruit()
            time.sleep(1)

        # pengosongan thread
        self.__clear_fruit_thread = None
