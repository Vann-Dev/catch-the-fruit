from src.lib.constant import road, fruits, door


class Player:
    def __init__(self, engine):
        self.pos_x = 0
        self.pos_y = 0
        self.map = None
        self.engine = engine

    def init(self, map):
        self.map = map

    def print(self):
        return "🤓"

    def move(self, direction):
        current_pos_x = self.pos_x
        current_pos_y = self.pos_y

        def check_path(x, y, fruit_only=False, door_only=False):
            if fruit_only:
                return self.map.map.stack[y].stack[x] in fruits
            if door_only:
                return self.map.map.stack[y].stack[x] == door
            return (
                self.map.map.stack[y].stack[x] == road
                or self.map.map.stack[y].stack[x] in fruits
                or self.map.map.stack[y].stack[x] == door
            )

        match direction:
            case "up":
                if check_path(current_pos_x, current_pos_y + 1):
                    current_pos_y += 1

            case "down":
                if check_path(current_pos_x, current_pos_y - 1):
                    current_pos_y -= 1

            case "left":
                if check_path(current_pos_x + 1, current_pos_y):
                    current_pos_x += 1

            case "right":
                if check_path(current_pos_x - 1, current_pos_y):
                    current_pos_x -= 1

            case _:
                return

        touching_door = False
        if check_path(current_pos_x, current_pos_y, door_only=True):
            touching_door = True

        if check_path(current_pos_x, current_pos_y, fruit_only=True):
            self.engine.fruit.enqueue(
                self.map.map.stack[current_pos_y].stack[current_pos_x]
            )
            self.map.fruit_size -= 1

        if self.pos_x == self.map.door["x"] and self.pos_y == self.map.door["y"]:
            self.map.map.stack[self.pos_y].stack[self.pos_x] = door
        else:
            self.map.map.stack[self.pos_y].stack[self.pos_x] = road

        self.map.map.stack[current_pos_y].stack[current_pos_x] = self.print()

        self.pos_x = current_pos_x
        self.pos_y = current_pos_y

        if touching_door:
            if self.map.fruit_size < 2 and self.engine.fruit.is_empty():
                self.engine.screen_state = "credit_screen"
                self.engine.game_end = True
            else:
                self.engine.clear_fruit()
