# Pass an argument to addSurviveGoal() to specify a time.


# This means the player must survive for 20 seconds.
game.addSurviveGoal(20)

# Spawn a generator with spawnXY
# Use the variable to configure the generator below.
generator = game.spawnXY("generator", 60, 40)
generator.maxHealth = 10
generator.attackDamage = 5
# Set the generator's spawnType to "munchkin"
generator = game.spawnXY("generator", 21, 20)
generator.spawnType = "munchkin"
generator.spawnDelay = 10
generator.spawnAI = "AttacksNearest"
generator.maxHealth = 100 

# Use spawnPlayerXY to spawn a hero for the player.
player = game.spawnPlayerXY("knight", 15, 15)
# Set the player's maxHealth to at least 100
player.maxHealth = 10000

# Set the player's attackDamage to at least 10
player.attackDamage = 10

#Player speed at least 10
player.maxSpeed = 10

# Play the game!
potionLarge = game.spawnXY("potion-large", 45, 23)
potionLarge = game.spawnXY("potion-large", 28, 37)
