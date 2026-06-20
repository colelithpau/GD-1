# Move to all the X-marks.
# Those fire-traps hurt!

game.spawnPlayerXY("samurai", 40, 50)
game.addSurviveGoal()
game.addMoveGoalXY(25,40)
game.addMoveGoalXY(55,40)
game.spawnXY("fire-trap", 55, 40)
game.addMoveGoalXY(40,20)
game.addMoveGoalXY(41,40)
game.spawnXY("fire-trap", 41, 40)
game.spawnXY("fire-trap", 40, 20)
game.spawnXY("potion-small", 40, 25)

# Spawn some "potion-small" objects to heal the player!
game.spawnXY("potion-small", 40, 33)
game.spawnXY("potion-small", 43, 26)
game.spawnXY("potion-small", 39, 28)
game.spawnXY("potion-small", 25, 20)
game.spawnXY("potion-small", 56, 23)
