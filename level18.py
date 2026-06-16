# Players like seeing score, so use ui.track()!
# It will create a user-interface element for them to see.
player = game.spawnPlayerXY("samurai", 20, 20)
player.maxHealth = 2000
game.addSurviveGoal(20)
game.addDefeatGoal(6)

spawner = game.spawnXY("generator", 50, 50)
spawner.maxHealth = 100
spawner.spawnType = "munchkin"
# Add more spawners for more enemies on the field:
spawner = game.spawnXY("generator", 20, 18)
spawner.maxHealth = 100
spawner.spawnType = "skeleton"

# ui.track() displays an object's property for players to see!
ui.track(game, "time")
# Use ui.track to track game's "defeated" property:
ui.track(game, "defeated property")
player.attackDamage = 100
# Increase the hero's maxSpeed:
player.maxSpeed = 200
# ui.track() displays an object's property for players to see!
ui.track(game, "time")
# Track the game's "defeated" property:
ui.track(game, "defeated")
