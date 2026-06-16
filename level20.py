# You can use a database to store persistent data.
# Persistent data stays the same between plays of your game!

generator = game.spawnXY("generator", 60, 40)
generator.spawnType = "munchkin"
generator.spawnDelay = 1
generator = game.spawnXY("generator", 16, 40)
generator.spawnType = "munchkin"
generator.spawnDelay = 2
player = game.spawnPlayerXY("champion", 36, 30)
player.maxHealth = 100000
player.attackDamage = 10000
game.addSurviveGoal(20)

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
ui.track(db,"defeated property", 2)

potionMedium = game.spawnXY("potion-medium", 21, 20)
# The code below will run when the player wins the game.
def onVictory(event):
    db.add("wins", 1)
    # Use db.add(key, value) to add the value of
    # game.defeated to the database with the key "total defeated"
    ui.track(game, "total defeated")
    ui.track(game, "defeated")
    ui.track(db, "defeated property")
    ui.track(db, "total defeated")
    ui.track = "generator"
    # Example: Move hero towards gem at (xx, yy)
    
 

# Properly show the defeated property
ui.track(game, "defeated property")


game.on("victory", onVictory)
# Correct way to set the 'defeated' property in the database
db.set("defeated", game.defeated)
db.set("defeated property", game.defeatedProperty)
game.addDefeatGoal()

# The code below will run when the player wins the game.
def onVictory(event):
    db.add("wins", 1)
    # Save the defeated count or property in the database
    db.set("defeated", game.defeated)  # Use db.set to store the value when winning.

game.on("victory", onVictory)
