import pygame
import esper
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.create.prefab_creator import create_enemy

def system_enemy_spawner(world: esper.World, delta_time: float, enemies_data: dict):
    spawner_entities = world.get_components(CEnemySpawner)
    
    for entity, (c_spawner,) in spawner_entities:
        c_spawner.elapsed_time += delta_time
        

        for event in c_spawner.spawn_events[:]:  
            if c_spawner.elapsed_time >= event["time"]:
                enemy_type = event["enemy_type"]
                position = pygame.Vector2(event["position"]["x"], event["position"]["y"])
                

                if enemy_type in enemies_data:
                    enemy_data = enemies_data[enemy_type]
                    create_enemy(world, position, enemy_data)
                
                c_spawner.spawn_events.remove(event)