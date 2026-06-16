# Generators spawn enemies over time.
# Skeletons are afraid of lightstones.

player = game.spawnPlayerXY("champion", 15, 35)
player.attackDamage = 100
player.maxSpeed = 100

game.addSurviveGoal(20)
game.addDefeatGoal(10)
game.spawnXY("x-mark-stone", 60, 35)
# Spawn a "generator"
generator = game.spawnXY("generator", 20, 20)
generator.spawnType = "skeleton"
generator.spawnDelay = 5
# Spawn a "lightstone"
# Now beat your game!
lightstone = game.spawnXY("lightstone", 30, 46)
lightstone = game.spawnXY("lightstone", 29, 21)
lightstone = game.spawnXY("lightstone", 53, 31)
lightstone = game.spawnXY("lightstone", 54, 21)
lightstone = game.spawnXY("lightstone", 41, 35)
lightstone = game.spawnXY("lightstone", 19, 36)
potionLarge = game.spawnXY("potion-large", 21, 20)
potionLarge = game.spawnXY("potion-large", 46, 40)
potionLarge = game.spawnXY("potion-large", 48, 20)
potionLarge = game.spawnXY("potion-large", 56, 20)
potionLarge = game.spawnXY("potion-large", 21, 20)
potionLarge = game.spawnXY("potion-large", 42, 20)
potionLarge = game.spawnXY("potion-large", 35, 25)
potionLarge = game.spawnXY("potion-large", 42, 20)
potionLarge = game.spawnXY("potion-large", 34, 20)


