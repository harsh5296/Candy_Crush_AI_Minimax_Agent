# Candy_Crush_AI_Minimax_Agent

The Candy Crush Fruit Rage is a two player game in which each player tries to maximize 
his/her share from a batch of fruits randomly placed in a box. 

Players play in turn and can pick a cell of the box in their own turn 
and claim all fruit of the same type, in all cells that are connected to the 
selected cell through horizontal and vertical paths.

For each selection or move the agent is rewarded a numeric value which is the square of the number of fruits claimed in that move.
Once an agent picks the fruits from the cells, their empty place will be filled with other fruits on top of them (which fall down due to gravity), 
if any. In this game, no fruit is added during game play. Hence, players play until all fruits have been claimed.

You can have a look on Homework_2.pdf for more detailed explanation and examples.
