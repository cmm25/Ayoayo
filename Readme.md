# Initial Thoughts

As I read the Ayoayo for the first time, I was interested but confused. I had never seen the game played before, so I read the rules over and over again so I knew how to play it correctly. I was fascinated by the fact that the pieces move round to the left, how to capture a piece, and that one must "take another turn," but it might be difficult to learn.

First I considered how to represent the game board. I decided a straightforward list where a number represented a pit or a shop was easiest - player 1's pits were represented by numbers 0-5, their shop represented by number 6, player 2's pits represented by numbers 7-12, and player 2's shop was represented by number 13. I mapped it out on a piece of paper to examine how seeds would be placed on the board.

Initially, I had a few ideas that I incorporated into my design:
1. I assumed players were not allowed to pick empty pits for their move (this was not stated clearly within the rules).
2. I assumed the game would need to track whose turn it was, though later realized the assignment didn't require this
3. I initially assumed the capture rule would be more complex than it actually was

For the Player class, I kept it straightforward since it only required a name. I put much thought trying to organize the playGame method, particularly how to manage special cases if a player is given a bonus turn or scoops seeds from the opposite pit.

# Final Thoughts


I kept referring to the rules document as I was coding simply to check that I was doing it correctly. It is strange how something easy to read is made more difficult once you begin to code!

The most difficult thing was implementing the seed capturing rule. I had to observe where the last seed was placed to determine whether it was according to the capture rules. I took a significant amount of time rectifying this area so it was accurate every single time.

It was not easy to declare all the data members private. It is Python convention but not a Python rule, so I prefixed the variable names with a special underscore symbol. However, I kept forgetting to use the prefixes when calling these variable names within the methods as well! This introduced some irritating bugs that were troublesome to debug.

I had to alter a few of my original ideas during programming.
I needed to introduce explicit rules for a player picking up from a vacant hole.
I realized that the assignment did not require maintaining turns in game logic since the test cases indicated that invoking playGame with any pit/player pair was sufficient.
I discovered that the rules allow a player to make a few turns consecutively without alternating to the second player, which is not typical for standard turn-taking games.

I'm glad I was able to remove the check_game_end method from the playGame method. I initially had all of the code for it within playGame, and it cluttered up the program. But by moving it to a separate method, the program was much cleaner and easier to read.

It was helpful for me to attempt the example assignments. If I made a mistake, then I knew where I needed to improve. I think I could have saved valuable time if I had attempted these tests before.

There were a few odd scenarios that I did not consider initially: - What if a player attempts to make a move after the end of the game?

- How to handle invalid pit numbers (less than 1 or greater than 6)

- What do you do if there are not enough players created ahead of the game?

Working on this project was beneficial to learn how games are created. You can see how the rules work as a player, but entering them as code forces you to examine them more intensely. 
I also learned that good tests are crucially important - without test cases, it would've been much more difficult for me to verify whether my code was correct. 
