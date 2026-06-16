# Control the simulation by adjusting these values:

### Ogres
# Number of ogres at the start.
game.startingOgres = 5
# Ogre movement speed.
game.ogreSpeed = 1
# Peasants an ogre needs to catch to spawn a new ogre.
game.ogreSplit = 1
# Ogre must be this close to see a peasant.
game.ogreSight = 12
# Seconds an ogre survives without catching a peasant.
game.ogreLifespan = 5


### Humans
# Number of ogres at the start.
game.startingHumans = 50
# Ogre movement speed.
game.humansSpeed = 10
# Peasants an ogre needs to catch to spawn a new ogre.
game.humansSplit = 3
# Ogre must be this close to see a peasant.
game.humansSight = 12
# Seconds an ogre survives without catching a peasant.
game.humansLifespan = 10


### Peasants
# Number of peasants at the start.
game.startingPeasants = 50
# Peasant movement speed.
game.peasantSpeed = 50
# Coins a peasant must collect to spawn a new peasant.
game.peasantSplit = 3
# Peasant must be this close to see a coin.
game.peasantSight = 10
# Seconds a peasant survives without collecting a coin.
game.peasantLifespan = 10000

### Coins
# Seconds between new coins spawning.
game.coinSpawnTime = 1
# Amount of coins that spawn at a time.
game.coinSpawnAmount = 10

# Don't change code below here!
ui.track(game, "time")
ui.track(game, "humans")
ui.track(game, "ogres")
