# Spawn a hero and add a goal.
game.spawnPlayerXY("champion", 40, 15)
game.addDefeatGoal()

# Spawn at least 2 "munchkin"s.
munchkin = game.spawnXY("munchkin", 21, 20)
munchkin = game.spawnXY("munchkin", 53, 22)
# Spawn at least 2 "thrower"s.
thrower = game.spawnXY("thrower", 51, 20)
thrower = game.spawnXY("thrower", 24, 20)
# Spawn at least 2 "soldier"s.
soldier = game.spawnXY("soldier", 21, 34)
soldier = game.spawnXY("soldier", 67, 20)
# Spawn at least 2 "archer"s.
archer = game.spawnXY("archer", 21, 48)
archer = game.spawnXY("archer", 60, 50)

