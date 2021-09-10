'''

Spring 2021
Thara Messeroux
Purpose: Programs a Mastermind Game, a coding-breaking board game for two players, 
the mastermind and the codebreaker.

'''

Short Description of the Game:

To start, one player is the Mastermind and one player is the Codebreaker. 
The Mastermind creates the secret code. The Codebreaker tries to guess the secret 
code. The secret code is created using any 4 colored marbles out of the 6 available. 
After each round of guess the Mastermind provides feedback to the Codebreaker 
on their guesses, using 4 pegs. In our case we use bulls and cows for the pegs. 
Bulls are black, they represent the correct color in the right position. 
Cows are red, they represent the correct color in the wrong position. 
We can also have clear pegs, for the wrong colors. We should keep in mind 
the order of the pegs does not match the order of the marbles on the board.
The game allows the Mastermind to repeat colors in their secret code, which
makes it more challenging.
The Mastermind game is played on a board. The board has 10 rows on it.  
On each row there are 4 slots for the code breaker to place their guesses. 
Next to each set of four slots, there are four smaller slots for the Mastermind 
to place their feedback for each guess.

Technology Used: Python Turtle Graphics


![MastermindGame](https://media.github.ccs.neu.edu/user/8933/files/db321000-1269-11ec-91b1-ba84fecf050e)

![image](https://media.github.ccs.neu.edu/user/8933/files/fbaf9980-126c-11ec-8415-8af4370489d8)

The mastermind game was programmed in this order:

1. First, I imported:
	
	a. random: to randomize the secret code
	
	b. Marble starter file: to help me draw the marbles and pegs
	
	c. Point starter file: to create the marbles
	
	d. turtle: to draw the turtle objects
	
	e. time: to sleep some displayed messages and show them temporarily

2. I programmed a function called count_bulls_and_cows to count the number 
   of bulls and cows.

3. A function called generate_code to generate the secret code that the Mastermind, 
  in this case, the computer, will use to play the game. I made the game more 
  challenging by allowing the Mastermind to repeat colors in their code. (Extra Credit)

4. Then, programmed a pop up to capture the player name at the start of the game

5. Drew the turtle screen/board with the left, right, and bottom box, draw_screen.

6. Drew the text of the leaderboard which draws the text of the leaderboard and displays 
  the list of winners with their points/scores. 

7. Drew the cute pink arrow, draw_arrow. 

8. Drew the check button, a green checkmark for the “check” button, draw_check_button.

9. Drew the x button, a red “X” for the “cancel” button, draw_x_button.

10. Drew the quit button, a red square for the “quit” button, draw_quit_button.

11. Programmed a function for each of these 3 buttons, to make sure they reacted 
    properly when clicked. These functions are:

12. click_check_button
	
	a. if the player presses the "check" button:
	
	b. it raises an error message if we enter less than 4 marble colors.
	
	c. it confirms and checks/enters a guess 
	
	d. it draws the appropriate pegs of the round
	
	e. it calls the won_game() function if you win. The player wins if 
	   they guess the code in 10 tries or less. 
	
	f. it calls the lost_game() function if you lose. The player loses 
           if they don’t guess the code in 10 tries.

13. click_x_button
	
	a. if the player presses the "X" button:
	
	b. the program removes a guess that has not yet been checked/entered
	
	c. then, it resets the clickable, colored guess buttons 

14. click_quit_button
 	
	a. if the player presses the Quit button:
 	
	b. the program displays a visual message popup for a few seconds, then
 	
	c. the program closes

15. Drew the marbles, draw_marbles.

16. Drew the pegs, draw_pegs.

17. Programmed 2 functions called marbles_game and click_marbles for the marbles.
	
	a. The function marbles_game calls the function click_marbles(color), 
	   if the user clicks a colored marble.
	
	b. The function click_marbles sets the color of the current marble 
           and redraws the marble.

18. Programmed a function called won_game if the user wins.
	
	a. the program displays a visual message popup saying that you won.
	
	b. displays the list of winners with their scores (the score is the number of guesses 
	  it takes the player to guess the code.)
	
	c.The list of winners gets sorted by score and gets reset after 15 lines to fit the board. 
	
	d. closes the program 

19. Programmed a function called lost_game if the user loses.
	
	a. the program displays a visual popup message saying that you lost.
	
	b. your name won’t show in the list of players
	
	c. closes the program 

Although it was challenging to code my first game, it was a real pleasure to complete it. 

