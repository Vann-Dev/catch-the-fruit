import msvcrt
import os
import time


class Interface:
    def __init__(self, engine):
        self.engine = engine
        self.widget_text = ""

    def home_screen(self):
        selection_hover = "start_game"
        self.engine.screen_state = None

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("""
\033[35m
 /$$$$$$              /$$               /$$             /$$$$$$$$ /$$                       /$$$$$$$$                  /$$   /$$    
/$$__  $$            | $$              | $$            |__  $$__/| $$                      | $$_____/                 |__/  | $$    
| $$  \__/  /$$$$$$  /$$$$$$    /$$$$$$$| $$$$$$$          | $$   | $$$$$$$   /$$$$$$       | $$     /$$$$$$  /$$   /$$ /$$ /$$$$$$  
| $$       |____  $$|_  $$_/   /$$_____/| $$__  $$         | $$   | $$__  $$ /$$__  $$      | $$$$$ /$$__  $$| $$  | $$| $$|_  $$_/  
| $$        /$$$$$$$  | $$    | $$      | $$  \ $$         | $$   | $$  \ $$| $$$$$$$$      | $$__/| $$  \__/| $$  | $$| $$  | $$    
| $$    $$ /$$__  $$  | $$ /$$| $$      | $$  | $$         | $$   | $$  | $$| $$_____/      | $$   | $$      | $$  | $$| $$  | $$ /$$
|  $$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$         | $$   | $$  | $$|  $$$$$$$      | $$   | $$      |  $$$$$$/| $$  |  $$$$/
\______/  \_______/   \___/   \_______/|__/  |__/         |__/   |__/  |__/ \_______/      |__/   |__/       \______/ |__/   \___/  
\033[m
            """)

            print(f"""
            {selection_hover == "start_game" and "➡️ \033[34m" or "‎"}\tStart Game\033[m
            {selection_hover == "tutorial" and "➡️ \033[34m" or "‎"}\tTutorial\033[m
            {selection_hover == "quit" and "➡️ \033[34m" or "‎"}\tQuit\033[m

            Use W and S to navigate, press Enter to select
            """)

            key = msvcrt.getch()

            if key == bytes("w", "utf-8"):
                if selection_hover == "start_game":
                    selection_hover = "quit"
                elif selection_hover == "tutorial":
                    selection_hover = "start_game"
                elif selection_hover == "quit":
                    selection_hover = "tutorial"

            elif key == bytes("s", "utf-8"):
                if selection_hover == "start_game":
                    selection_hover = "tutorial"
                elif selection_hover == "tutorial":
                    selection_hover = "quit"
                elif selection_hover == "quit":
                    selection_hover = "start_game"

            elif key == bytes("\r", "utf-8"):
                if selection_hover == "start_game":
                    self.engine.screen_state = "select_mode"
                    break
                elif selection_hover == "tutorial":
                    self.engine.screen_state = "tutorial"
                    break
                elif selection_hover == "quit":
                    os.system("cls" if os.name == "nt" else "clear")
                    exit()

    def tutorial_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

        self.engine.screen_state = None
        self.engine.init_game("tutorial")
        self.engine.map.print()

        print("""
        Use W, A, S, D to move, ESC to quit.
        """)

        self.widget_text = (
            "\033[32mCollect all the fruits and go to the 🚪 to win.\033[m"
        )

        self.engine.controller()

    def stats_widget(self):
        print(f"""
Fruit Collected: {", ".join(self.engine.fruit.items)}
Fruit Remaining: {self.engine.map.fruit_size}

{self.widget_text}
        """)

    def select_mode_screen(self):
        self.engine.screen_state = None
        selection_hover = "normal"

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("""
\033[35m
  /$$$$$$            /$$                       /$$           /$$                                     /$$
 /$$__  $$          | $$                      | $$          | $$                                    | $$
| $$  \__/  /$$$$$$ | $$  /$$$$$$   /$$$$$$$ /$$$$$$        | $$        /$$$$$$  /$$    /$$ /$$$$$$ | $$
|  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$_____/|_  $$_/        | $$       /$$__  $$|  $$  /$$//$$__  $$| $$
 \____  $$| $$$$$$$$| $$| $$$$$$$$| $$        | $$          | $$      | $$$$$$$$ \  $$/$$/| $$$$$$$$| $$
 /$$  \ $$| $$_____/| $$| $$_____/| $$        | $$ /$$      | $$      | $$_____/  \  $$$/ | $$_____/| $$
|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$$  |  $$$$/      | $$$$$$$$|  $$$$$$$   \  $/  |  $$$$$$$| $$
 \______/  \_______/|__/ \_______/ \_______/   \___/        |________/ \_______/    \_/    \_______/|__/
\033[m
            """)

            print(f"""
            {selection_hover == "normal" and "➡️ \033[34m" or "‎"}\tNormal\033[m
            {selection_hover == "normal_dark" and "➡️ \033[34m" or "‎"}\tNormal Dark\033[m
            {selection_hover == "big" and "➡️ \033[34m" or "‎"}\tBig\033[m
            {selection_hover == "big_dark" and "➡️ \033[34m" or "‎"}\tBig Dark\033[m
            {selection_hover == "quit" and "➡️ \033[34m" or "‎"}\tBack\033[m

            Use W and S to navigate, press Enter to select
            """)

            key = msvcrt.getch()

            if key == bytes("w", "utf-8"):
                if selection_hover == "normal":
                    selection_hover = "quit"
                elif selection_hover == "normal_dark":
                    selection_hover = "normal"
                elif selection_hover == "big":
                    selection_hover = "normal_dark"
                elif selection_hover == "big_dark":
                    selection_hover = "big"
                elif selection_hover == "quit":
                    selection_hover = "big_dark"

            elif key == bytes("s", "utf-8"):
                if selection_hover == "normal":
                    selection_hover = "normal_dark"
                elif selection_hover == "normal_dark":
                    selection_hover = "big"
                elif selection_hover == "big":
                    selection_hover = "big_dark"
                elif selection_hover == "big_dark":
                    selection_hover = "quit"
                elif selection_hover == "quit":
                    selection_hover = "normal"

            elif key == bytes("\r", "utf-8"):
                if selection_hover == "quit":
                    self.engine.screen_state = "home_screen"
                    break
                else:
                    self.engine.init_game(selection_hover)
                    self.engine.screen_state = "game_screen"
                    break

    def pause_screen(self):
        selection_hover = "continue"
        self.engine.screen_state = None

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("""
\033[35m
 /$$$$$$$                                        
| $$__  $$                                       
| $$  \ $$ /$$$$$$  /$$   /$$  /$$$$$$$  /$$$$$$ 
| $$$$$$$/|____  $$| $$  | $$ /$$_____/ /$$__  $$
| $$____/  /$$$$$$$| $$  | $$|  $$$$$$ | $$$$$$$$
| $$      /$$__  $$| $$  | $$ \____  $$| $$_____/
| $$     |  $$$$$$$|  $$$$$$/ /$$$$$$$/|  $$$$$$$
|__/      \_______/ \______/ |_______/  \_______/
\033[m
            """)

            print(f"""
            {selection_hover == "continue" and "➡️ \033[34m" or "‎"}\tContinue\033[m
            {selection_hover == "restart" and "➡️ \033[34m" or "‎"}\tRestart\033[m
            {selection_hover == "quit" and "➡️ \033[34m" or "‎"}\tQuit\033[m

            Use W and S to navigate, press Enter to select
            """)

            key = msvcrt.getch()

            if key == bytes("w", "utf-8"):
                if selection_hover == "continue":
                    selection_hover = "quit"
                elif selection_hover == "restart":
                    selection_hover = "continue"
                elif selection_hover == "quit":
                    selection_hover = "restart"

            elif key == bytes("s", "utf-8"):
                if selection_hover == "continue":
                    selection_hover = "restart"
                elif selection_hover == "restart":
                    selection_hover = "quit"
                elif selection_hover == "quit":
                    selection_hover = "continue"

            elif key == bytes("\r", "utf-8"):
                if selection_hover == "continue":
                    self.engine.screen_state = "game_screen"
                    break
                elif selection_hover == "restart":
                    self.engine.init_game(self.engine.game_mode)
                    self.engine.screen_state = "game_screen"
                    break
                elif selection_hover == "quit":
                    self.engine.screen_state = "home_screen"
                    break

    def game_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

        self.engine.screen_state = None
        self.engine.map.print()

        self.widget_text = (
            "\033[32mCollect all the fruits and go to the 🚪 to win.\033[m"
        )

        self.engine.controller()

    def credit_screen(self):
        self.engine.game_end = False
        os.system("cls" if os.name == "nt" else "clear")

        print("""
\033[36m  
  /$$$$$$                            /$$ /$$   /$$    
 /$$__  $$                          | $$|__/  | $$    
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$ /$$ /$$$$$$  
| $$       /$$__  $$ /$$__  $$ /$$__  $$| $$|_  $$_/  
| $$      | $$  \__/| $$$$$$$$| $$  | $$| $$  | $$    
| $$    $$| $$      | $$_____/| $$  | $$| $$  | $$ /$$
|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$| $$  |  $$$$/
 \______/ |__/       \_______/ \_______/|__/   \___/  

Game made by: Stevan Vincent (31230016) [https://www.vann.my.id]
\033[m
        """)

        time.sleep(3)

        print(f"""
🍇 Fruit Collected: {self.engine.total_fruit_collected}
        """)

        time.sleep(2)

        input("Press enter to continue...")

        self.engine.screen_state = "home_screen"
