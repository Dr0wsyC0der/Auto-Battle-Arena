from auto_battle.engine.game_engine import GameEngine
def main():
    engine = GameEngine.create_default_game()
    engine.run()

if __name__ == '__main__':
     main()