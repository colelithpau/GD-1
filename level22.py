# Make your own game by changing the code below!

# Spawn a maze. Change the number for a different maze!
game.spawnMaze("forest", 7)

# Spawn a player with spawnPlayerXY()
player = game.spawnPlayerXY("champion", 36, 30)
player.attackDamage = 1000
player.maxHealth = 10000
player.maxSpeed = 90
# Add at least one goal!
game.addSurviveGoal(20)
game.addDefeatGoal(5)

# Spawn some things to collect!
game.spawnXY("gem", 28, 27)
# You need a key to collect a locked chest.
game.spawnXY("locked-chest", 44, 28)
game.spawnXY("silver-key", 43, 60)
game.spawnXY("potion-medium", 60, 12)

# Spawn some enemies!
s1 = game.spawnXY("skeleton", 43, 50)
s1.behavior = "Defends"
s2 = game.spawnXY("skeleton", 49, 59)
s2.behavior = "Defends"
s3 = game.spawnXY("munchkin", 36, 30)
s3.behavior = "Defends"
game.spawnXY("lightstone", 60, 44)

gen = game.spawnXY("generator", 26, 44)
gen.spawnType = "munchkin"
gen.spawnDelay = 4

game.spawnXY("munchkin", 28, 19)
# Ogre Spear Throwers have a ranged attack!
game.spawnXY("thrower", 48, 28)
# This gargoyle shoots fire!
spewer = game.spawnXY("fire-spewer", 37, 12)
spewer.direction = "horizontal"

# Track plays and ogres defeated in the database.
db.add("plays", 1)
ui.track(db, "plays")
ui.track(db, "defeated")

def onVictory(event):
    db.add("defeated", game.defeated)

game.on("victory", onVictory)
