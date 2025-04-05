#!/usr/bin/python3
"""Función Main"""

from src.engine.game_engine import GameEngine

if __name__ == "__main__":
    engine = GameEngine("resources/config/level_01.json", "resources/config/enemies.json", "resources/config/window.json", "resources/config/player.json")
    engine.run()
