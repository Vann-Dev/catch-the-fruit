import random
from src.lib.stack import Stack
from src.lib.constant import road, tree, building, fruit, door, border, modes


class Map:
    def __init__(self, engine):
        self.map = Stack()
        self.fruit_size = 0
        self.building_size = 0
        self.fruits = Stack()
        self.player = None
        self.engine = engine
        self.door = {"x": 0, "y": 0}

        self.map_height = 0
        self.map_width = 0
        self.max_fruit_size = 0
        self.max_building_size = 0
        self.fogg = False

    def init(self, player):
        # player sudah diinisasi di engine, jadi bisa diambil dari engine
        self.player = player

        # penginisiasian map, di ambil dari modes yang ada di constant.py
        self.map_height = modes[self.engine.game_mode]["height"]
        self.map_width = modes[self.engine.game_mode]["width"]
        self.max_fruit_size = modes[self.engine.game_mode]["fruit"]
        self.max_building_size = self.map_width * self.map_height - 400
        self.fogg = modes[self.engine.game_mode]["fogg"]

    # method untuk mengecek apakah posisi saat ini berada di border
    def __is_border(self, row, col):
        return (
            col == 0
            or row == 0
            or col == self.map_height - 1
            or row == self.map_width - 1
        )

    # method untuk mengecek apakah objek yang akan di generate tidak terlalu dekat dengan objek lain
    def __is_object_not_close(self, col, row, stack):
        return (
            random.randint(0, 100) < 10
            and self.building_size < self.max_building_size
            and stack.peek() == road
            or stack.peek() == border()
            and self.map.peek().stack[col] == road
            or self.map.peek().stack[col] == border()
        )

    # method untuk generate map
    def generate(self):
        for row in range(self.map_height):
            map_column = Stack()

            for col in range(self.map_width):
                # jika posisi saat ini berada di border, maka akan di push border
                if self.__is_border(col, row):
                    map_column.push(border())
                else:
                    # jika objek yang akan di generate tidak terlalu dekat dengan objek lain, maka akan di push objek tersebut
                    if self.__is_object_not_close(col, row, map_column):
                        map_column.push(building())
                        self.building_size += 1
                    else:
                        # jika tidak, maka akan di push road
                        if self.__is_object_not_close(col, row, map_column):
                            map_column.push(tree())
                            self.building_size += 1
                        else:
                            map_column.push(road)

            self.map.push(map_column)

        self.__place_player()
        self.__place_door()
        self.__place_fruit()

    # method untuk menempatkan buah
    def __place_fruit(self):
        while True:
            row = random.randint(1, self.map_height - 1)
            col = random.randint(1, self.map_width - 1)

            # jika posisi saat ini adalah road dan jumlah buah yang ada belum mencapai maksimal, maka akan di push buah
            if (
                self.map.stack[row].stack[col] == road
                and self.fruit_size != self.max_fruit_size
            ):
                # buah yang di push adalah buah yang sudah di inisiasi di fruit()
                selected_fruit = fruit()
                self.map.stack[row].stack[col] = selected_fruit
                self.fruits.push(selected_fruit)
                self.fruit_size += 1

            # jika jumlah buah yang ada sudah mencapai maksimal, maka akan di break
            if self.fruit_size == self.max_fruit_size:
                break

    # method untuk menempatkan player
    def __place_player(self):
        while True:
            row = random.randint(1, self.map_height - 1)
            col = random.randint(1, self.map_width - 1)

            # jika posisi saat ini adalah road, maka akan di push player
            if self.map.stack[row].stack[col] == road:
                self.player.pos_y = row
                self.player.pos_x = col
                self.map.stack[row].stack[col] = self.player.print()
                break

    # method untuk menempatkan pintu
    def __place_door(self):
        while True:
            row = random.randint(1, self.map_height - 1)
            col = random.randint(1, self.map_width - 1)

            # jika posisi saat ini adalah road, maka akan di push pintu
            if self.map.stack[row].stack[col] == road:
                self.map.stack[row].stack[col] = door
                self.door["x"] = col
                self.door["y"] = row
                break

    # method ini adalah method dimana saat mode fogg di aktifkan, maka akan menampilkan area yang bisa di lihat oleh player
    def __light_up(self, x, y):
        # jika player berada di area yang bisa di lihat, maka akan menampilkan area tersebut
        return (
            self.map_width - x - 1 == self.player.pos_x
            and self.map_height - y == self.player.pos_y
            or self.map_width - x - 2 == self.player.pos_x
            and self.map_height - y == self.player.pos_y
            or self.map_width - x - 2 == self.player.pos_x
            and self.map_height - y - 1 == self.player.pos_y
            or self.map_width - x - 2 == self.player.pos_x
            and self.map_height - y - 2 == self.player.pos_y
            or self.map_width - x - 1 == self.player.pos_x
            and self.map_height - y - 2 == self.player.pos_y
            or self.map_width - x == self.player.pos_x
            and self.map_height - y - 2 == self.player.pos_y
            or self.map_width - x == self.player.pos_x
            and self.map_height - y - 1 == self.player.pos_y
            or self.map_width - x == self.player.pos_x
            and self.map_height - y == self.player.pos_y
        )

    # method untuk menampilkan map
    def print(self):
        map_data = self.map.stack.copy()
        map_for_print = Stack()

        # menampilkan map yang sudah di generate, ini untuk bagian baris
        for row in map_data:
            map_row_data = Stack()

            # menampilkan map yang sudah di generate, ini untuk bagian kolom
            for col in row.stack:
                map_row_data.push(col)

            map_for_print.push(map_row_data)

        # menampilkan map yang sudah di generate, ini untuk bagian kolom
        for y in range(self.map_height):
            map_column = map_for_print.pop()

            # menampilkan map yang sudah di generate, ini untuk bagian baris
            for x in range(self.map_width):
                obj = map_column.pop()

                # jika mode fogg di aktifkan, maka akan menampilkan area yang bisa di lihat oleh player
                if self.fogg:
                    if obj == self.player.print():
                        print(obj, end="")
                    elif self.__light_up(x, y):
                        print(obj, end="")
                    else:
                        print(" ", end="")
                else:
                    print(obj, end="")

            print()
