from picraft import *
world = World()
world.say('Hello World')
position = world.player.tile_pos
print position
world.player.tile_pos += Vector( y = 5 )
blockBelow = world.blocks[world.player.tile_pos - Y]
print blockBelow
world.blocks[world.player.tile_pos - Y]=Block(1)
