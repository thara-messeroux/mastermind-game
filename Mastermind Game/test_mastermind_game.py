'''
CS5001
Spring 2021
Final Project : Mastermind Game Test
Thara Messeroux

Purpose: This file test the Mastermind game functions.
         It does not test turtle/view.
         
'''
from mastermind_game import *
import unittest
import turtle

class test_mastermind_game(unittest.TestCase):

    def test_count_bulls_and_cows_1(self):

        # testing if there are the right number of bulls and cows.

        secret_code = ["green",  "yellow", "purple", "black"]
        guess = ["red", "blue", "green",  "yellow"]
        result = count_bulls_and_cows(secret_code, guess)

        self.assertEqual(result,(0, 2))
    
    def test_count_bulls_and_cows_2(self):
        
        # testing if there are the right number of bulls and cows.
        
        secret_code = ["purple",  "yellow", "purple", "black"]
        guess = ["purple", "purple", "purple",  "yellow"]
        result = count_bulls_and_cows(secret_code, guess)
        
        self.assertEqual(result,(2, 1))

    def test_count_bulls_and_cows_3(self):
        
        # testing if there are the right number of bulls and cows.
        
        secret_code = ["green",  "yellow", "purple", "yellow"]
        guess = ["red", "blue", "yellow",  "purple"]
        result = count_bulls_and_cows(secret_code, guess)
        
        self.assertEqual(result,(0, 2))

    
    def test_generate_code_length(self):
        
        # testing if the secret code has 4 colors.
        
        colors = ["r", "blue", "g", "y", "p", "b"]
        result = generate_code(colors)
        
        self.assertEqual(len(result),  4)
        
    def test_generate_code_color(self):

        # testing if the secret code is from the set of permitted colors.

        colors = ["r", "blue", "g", "y", "p", "b"]
        result = generate_code(colors)
        
        for color in result:
            self.assertTrue(color in colors)
                 
    def test_won_game(self):
        
        # test that the file actually contains the content that you want it to.

        result = draw_leaderboard(turtle.Screen())
        leaders = []
        try:
            f = open("leaderboard.txt", "r")
            for line in f:
                if(len(line.strip())> 0):
                    leaders.append(line) 
            f.close()
        except:
            pass
        self.assertEqual(len(leaders), len(result))        
  
def main():
    
    unittest.main(verbosity = 3)
    
if __name__ == "__main__":
    main()




