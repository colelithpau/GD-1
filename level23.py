#spawn a player with spawnPlayerXY(type, x, y)
player = game.spawnPlayerXY("champion", 36, 30)
player.maxHealth = 10000
player.maxSpeed = 30
player.attackDamage = 100
game.addSurviveGoal(20)


# Add at least one goal!
game.addSurviveGoal(30)
game.addDefeatGoal(20)
game.addCollectGoal(5)



# Spawn objects into the game with spawnXY(type, x, y)
generator = game.spawnXY("generator", 28, 28)
generator.spawnType = "skeleton"
generator.spawnAI = "AttacksNearest"
generator.attackDamage = 20
generator.spawnDelay = 1
generator.maxHealth = 5

generator = game.spawnXY("generator", 28,51)
generator.spawnType = "munchkin"
generator.spawnAI = "AttacksNearest"
generator.attackDamage = 50
generator.spawnDelay = 5
generator.maxHealth = 10

generator = game.spawnXY("generator", 52, 56)
generator.spawnType = "munchkin"
generator.spawnAI = "AttacksNearest"
generator.attackDamage = 50
generator.spawnDelay = 1
generator.maxHealth = 10

#spawn a fence to protect the generator being destroyed
game.spawnXY("fence", 25, 39)
game.spawnXY("fence", 29, 39)
game.spawnXY("fence", 43, 39)
game.spawnXY("fence", 43, 36)
game.spawnXY("fence", 43, 33)
game.spawnXY("fence", 43, 30)

generator = game.spawnXY("generator", 52, 38)
generator.spawnType = "munchkin"
generator.spawnAI = "AttacksNearest"
generator.attackDamage = 50
generator.spawnDelay = 1
generator.maxHealth = 10

generator = game.spawnXY("generator", 53, 13)
generator.spawnType = "munchkin"
generator.spawnAI = "AttacksNearest"
generator.attackDamage = 50
generator.spawnDelay = 1
generator.maxHealth = 10


# Persistent data stays the same between plays of your game!

generator = game.spawnXY("generator", 28, 28)
generator.spawnType = "skeleton"
generator.spawnAI = "AttacksNearest"
generator.attackDamage = 50
generator.spawnDelay = 1
generator.maxHealth = 1

generator = game.spawnXY("generator", 11, 13)
generator.spawnType = "munchkin"
generator.spawnAI = "AttacksNearest"
generator.attackDamage = 50
generator.spawnDelay = 1
generator.maxHealth = 100

generator = game.spawnXY("generator", 14, 59)
generator.spawnType = "munchkin"
generator.spawnDelay = 1
generator.spawnAI = "AttacksNearest"
generator.attackDamage = 1000

# db stands for database
# db.add(key, value) increments a value stored in the database.
# This adds 1 to the "plays" key in the database.
db.add("plays", 1)

# Show the value of the "plays" and other keys in the db
ui.track(db, "plays")
ui.track(db, "wins")
ui.track(game, "defeated")
ui.track(game, "time")
# Show the value of the "defeated" property of the game object
ui.track(db,"total defeated")

def onVictory(event):
    db.add("wins", 1)
    db.set("total defeated", game.defeated) 

game.on("victory", onVictory)

#Acquire potion to add for Player's Health
potionLarge = game.spawnXY("potion-large", 44, 36)
potionLarge = game.spawnXY("potion-large", 60, 14)
potionLarge = game.spawnXY("potion-large", 21, 20)

#The Lightstone is used to defend the skeleton
lightstone = game.spawnXY("lightstone", 60, 44)

#Spawn a collectible chest and gems 
chest = game.spawnXY("chest", 44, 13)
chest.value = 100
gem = game.spawnXY("gem", 44, 45)
gem.value = 10
gem = game.spawnXY("gem", 12, 30)
gem = game.spawnXY("gem", 63, 31)
gem = game.spawnXY("gem", 24, 60)




