# The player only needs to collect some of the gems.
game.spawnPlayerXY("knight", 39, 23)

# Set goal to collect only 6 gems to win.
game.addCollectGoal(6)

# Spawn some gems and items.
chest = game.spawnXY("chest", 21, 20)
gem = game.spawnXY("gem", 16, 20)
gem = game.spawnXY("gem", 47, 21)
gem = game.spawnXY("gem", 51, 20)
gem = game.spawnXY("gem", 51, 26)
gem = game.spawnXY("gem", 46, 24)
potionMedium = game.spawnXY("potion-medium", 52, 9)
potionSmall = game.spawnXY("potion-small", 32, 22)
potionLarge = game.spawnXY("potion-large", 31, 20)
