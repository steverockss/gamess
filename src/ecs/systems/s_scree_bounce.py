import esper
import pygame

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity


def system_screen_bounce(world:esper.World, screen:pygame.Surface ):
    components = world.get_components(CTransform, CVelocity, CSurface)
    c_t: CTransform
    c_v:CVelocity
    c_s: CSurface
    screen_rect = screen.get_rect()

    for entity, (c_t, c_v, c_s) in components:

        square_rect = c_s.surf.get_rect(topleft=c_t.pos)

        if square_rect.left < 0 or square_rect.right > screen_rect.width:
            c_v.vel.x *= -1
            square_rect.clamp_ip(screen_rect)
            c_t.pos.x = square_rect.x

        if square_rect.top < 0 or square_rect.bottom > screen_rect.height:
            c_v.vel.y *= -1
            square_rect.clamp_ip(screen_rect)
            c_t.pos.y = square_rect.y

