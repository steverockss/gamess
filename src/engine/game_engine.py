

import json
import pygame
import esper

from src.create.prefab_creator import create_player_square
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_input_command import CInputCommand
from src.ecs.components.c_velocity import CVelocity
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_scree_bounce import system_screen_bounce
from src.ecs.systems.s_system_enemy_spawner import system_enemy_spawner

class GameEngine:
    def __init__(self, level_json_path: str, enemies_json_path: str, windows_json_path: str, player_json_path: str) -> None:
        pygame.init()


        with open(level_json_path, 'r') as f:
            self.level_data = json.load(f)
        with open(enemies_json_path, 'r') as f:
            self.enemies_data = json.load(f)
        with open(windows_json_path, 'r') as f:
            self.windows_data = json.load(f)
        with open(player_json_path, 'r') as f:
            self.player_data = json.load(f)    

        pygame.display.set_caption(self.windows_data["title"])
        self.screen = pygame.display.set_mode((self.windows_data["size"]["w"], self.windows_data["size"]["h"]), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.framerate = self.windows_data["framerate"]
        self.delta_time = 0
        self.ecs_world = esper.World()



    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        self._player_entity = create_player_square( self.ecs_world ,self.player_data, self.level_data["player_spawn"])
        self._player_c_vel = self.ecs_world.component_for_entity(self._player_entity, CVelocity)
        
        
        spawner_entity = self.ecs_world.create_entity()
        self.ecs_world.add_component(spawner_entity, CEnemySpawner(self.level_data, self.enemies_data))

        
    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.is_running = False

    def _update(self):
        system_enemy_spawner(self.ecs_world, self.delta_time, self.enemies_data)
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)

    def _draw(self):
        self.screen.fill((self.windows_data["bg_color"]["r"], 
                  self.windows_data["bg_color"]["g"], 
                  self.windows_data["bg_color"]["b"]))
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()

    def _clean(self):
        pygame.quit()

    def _do_action(self, c_input:CInputCommand):
            pass
