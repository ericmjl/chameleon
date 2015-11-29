# chameleon
A simulation of a card game my wife taught me.

# Todo List

- [ ] check for bugs in the game.
- [ ] write tests for the game progression. 

# Rules

## Game initialize

1. Any number of players can play, but should at least be 2.
1. Shuffle the deck, which includes all 52 cards + 2 jokers, and then deal 5 cards to each player.
1. Randomly nominate one player to pick a card value to act as the "chameleon" cards.
    1. The chameleon card allows the player dealing it to nominate any other suite to continue the game.
1. Play the game!

## Rules of the game

1. Starting with the nominated player, deal cards from your hand that either: 
    1. match the deck, or 
    1. match the value of the current deck on top.
1. If you do not have a card that matches that, then either:
    1. Place one card face down in your penalty pile, or
    1. Place a chameleon card to change the card suite. 
1. After that, draw a card from the rest of the deck.
1. At the end of each round, sum up the card values in the penalty pile. The player with the smallest penalty pile value wins.
