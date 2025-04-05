import random
import esper
import pygame

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.tags.c_tag_enemy import CTagEnemy
from src.ecs.tags.c_tag_player import CTagPlayer
def create_enemy(world: esper.World, position: pygame.Vector2, enemy_data: dict):
    entity = world.create_entity()
    
    world.add_component(entity, CTransform(position))
    
    size = pygame.Vector2(enemy_data["size"]["x"], enemy_data["size"]["y"])
    color = pygame.Color(enemy_data["color"]["r"], 
                          enemy_data["color"]["g"], 
                          enemy_data["color"]["b"])
    world.add_component(entity, CSurface(size, color))
    
    velocity_x = random.randint(enemy_data["velocity_min"], enemy_data["velocity_max"])
    velocity_y = random.randint(enemy_data["velocity_min"], enemy_data["velocity_max"])
    world.add_component(entity, CVelocity(pygame.Vector2(velocity_x, velocity_y)))
    world.add_component(entity, CTagEnemy)

def create_player_square(world: esper.World, player_info:dict, player_lvl_info:dict):
    size = pygame.Vector2(player_info["size"]["x"], player_info["size"]["y"])
    
    color = pygame.Color(player_info["color"]["r"], 
                          player_info["color"]["g"], 
                          player_info["color"]["b"])
    position = pygame.Vector2(player_lvl_info["position"]["x"] - (size.x/2), player_lvl_info["position"]["y"] - (size.y/2))

    velocity = pygame.Vector2(0,0 )
    player_entity = create_square(world, size, position, velocity, color)
    world.add_component(player_entity, CTagPlayer)
    return player_entity
    

def create_square(ecs_world:esper.World,
                  size: pygame.Vector2, 
                  pos: pygame.Vector2,
                  vel: pygame.Vector2,
                  color: pygame.Color):
    
    square_entity = ecs_world.create_entity()
    ecs_world.add_component(square_entity, 
                                     CSurface(size,
                                              color))
    ecs_world.add_component(square_entity, 
                                     CTransform(pos))

    ecs_world.add_component(square_entity,
                                     CVelocity(vel))
    
    return square_entity
    

