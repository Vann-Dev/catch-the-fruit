import msvcrt
import random
import os
import time
from src.lib.constant import screens, colors


class Interface:
    def __init__(self, engine):
        self.engine = engine
        self.widget_text = ""

    # method untuk menampilkan screen home
    def home_screen(self):
        selection_hover = "start game"
        selections = ["start game", "tutorial", "quit"]

        self.engine.screen_state = None

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print(f"""
{random.choices(colors)[0]}
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
{"\n".join(selection_hover == selection and "\t➡️ ‎ \033[34m" + selection.capitalize() + "\033[m" or "\t‎   " + selection.capitalize() for selection in selections)}

\tUse W and S to navigate, press Enter to select
                """)

            # handle input dari user
            key = msvcrt.getch()

            if key == bytes("w", "utf-8"):
                selection_hover = selections[
                    (selections.index(selection_hover) - 1) % len(selections)
                ]

            elif key == bytes("s", "utf-8"):
                selection_hover = selections[
                    (selections.index(selection_hover) + 1) % len(selections)
                ]

            elif key == bytes("\r", "utf-8"):
                # jika user memilih start game, maka akan masuk ke screen select
                if selection_hover == "start game":
                    self.engine.screen_state = screens["select"]
                    break

                # jika user memilih tutorial, maka akan masuk ke screen tutorial
                elif selection_hover == "tutorial":
                    self.engine.screen_state = screens["tutorial"]
                    break

                # jika user memilih quit, maka akan keluar dari game
                elif selection_hover == "quit":
                    os.system("cls" if os.name == "nt" else "clear")
                    exit()

            else:
                continue

    # method untuk menampilkan screen tutorial
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

    # method untuk menampilkan screen select mode
    def select_mode_screen(self):
        self.engine.screen_state = None

        selection_hover = "normal"
        selections = ["normal", "normal_dark", "big", "big_dark", "quit"]

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print(f"""
{random.choices(colors)[0]}
  /$$$$$$            /$$                       /$$           /$$      /$$                 /$$          
 /$$__  $$          | $$                      | $$          | $$$    /$$$                | $$          
| $$  \__/  /$$$$$$ | $$  /$$$$$$   /$$$$$$$ /$$$$$$        | $$$$  /$$$$  /$$$$$$   /$$$$$$$  /$$$$$$ 
|  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$_____/|_  $$_/        | $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$__  $$
 \____  $$| $$$$$$$$| $$| $$$$$$$$| $$        | $$          | $$  $$$| $$| $$  \ $$| $$  | $$| $$$$$$$$
 /$$  \ $$| $$_____/| $$| $$_____/| $$        | $$ /$$      | $$\  $ | $$| $$  | $$| $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$$  |  $$$$/      | $$ \/  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$
 \______/  \_______/|__/ \_______/ \_______/   \___/        |__/     |__/ \______/  \_______/ \_______/
\033[m
            """)

            print(f"""
{"\n".join(selection_hover == selection and "\t➡️ ‎ \033[34m" + " ".join(selection.split("_")).capitalize() + "\033[m" or "\t‎   " + " ".join(selection.split("_")).capitalize() for selection in selections)}

\tUse W and S to navigate, press Enter to select
""")

            key = msvcrt.getch()

            if key == bytes("w", "utf-8"):
                selection_hover = selections[
                    (selections.index(selection_hover) - 1) % len(selections)
                ]

            elif key == bytes("s", "utf-8"):
                selection_hover = selections[
                    (selections.index(selection_hover) + 1) % len(selections)
                ]

            elif key == bytes("\r", "utf-8"):
                if selection_hover == "quit":
                    self.engine.screen_state = screens["home"]
                    break
                else:
                    self.engine.init_game(selection_hover)
                    self.engine.screen_state = screens["game"]
                    break

    # method untuk menampilkan screen pause
    def pause_screen(self):
        selection_hover = "continue"
        selections = ["continue", "restart", "quit"]

        self.engine.screen_state = None

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print(f"""
{random.choices(colors)[0]}
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
{"\n".join(selection_hover == selection and "\t➡️ ‎ \033[34m" + selection.capitalize() + "\033[m" or "\t‎   " + selection.capitalize() for selection in selections)}

\tUse W and S to navigate, press Enter to select
            """)

            key = msvcrt.getch()

            if key == bytes("w", "utf-8"):
                selection_hover = selections[
                    (selections.index(selection_hover) - 1) % len(selections)
                ]

            elif key == bytes("s", "utf-8"):
                selection_hover = selections[
                    (selections.index(selection_hover) + 1) % len(selections)
                ]

            # handle input dari user
            elif key == bytes("\r", "utf-8"):
                # jika user memilih continue, maka akan kembali ke screen game
                if selection_hover == "continue":
                    self.engine.screen_state = screens["game"]
                    break
                # jika user memilih restart, maka akan mereset game
                elif selection_hover == "restart":
                    self.engine.init_game(self.engine.game_mode)
                    self.engine.screen_state = screens["game"]
                    break
                # jika user memilih quit, maka akan kembali ke screen home
                elif selection_hover == "quit":
                    self.engine.screen_state = screens["home"]
                    break

    # method untuk menampilkan screen game
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

        print(f"""
{random.choices(colors)[0]} 
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

        time.sleep(1)

        print(f"""
🍇 Fruit Collected: {self.engine.total_fruit_collected}
        """)

        time.sleep(2)

        input("Press enter to continue...")

        self.engine.screen_state = screens["home"]

    # method untuk menampilkan interface game
    def game_screen_playing(self):
        os.system("cls" if os.name == "nt" else "clear")

        self.engine.map.print()
        self.stats_widget()
