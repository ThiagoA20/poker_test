# About
---
This is a project to create a poker game, making the comparison between the hands to check
which one is the highest.

---
# Getting started
---
First, clone the repository for your machine: `git pull https://github.com/ThiagoA20/poker_test.git`<br />
then, remove the comments in the last lines and start the program with the following command: `python poker_game.py`<br /><br />

to run the tests, type the command: `python tests.py`

---
# Project Structure
---

All the modules used are built in, so it's not necessary to setup the virtual environment and install another modules.

There are 4 main functions in the program, one to check if all the cards have the same suit, one to check the groups of cards by value,
one to check the highest card and one to check if a sequence exists.

When a pokerHand is initialized all those functions are called to set the properties of the current hand, the pokerHand class have two methods,
one is the classification, that will return a number after checking the parameters of the current hand, and the other method is to compare two
hands, it will receive a pokerHand instance, call the classification function of the two hands and compare the value to return which one is the
winner.