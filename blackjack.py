# Two players, the player and the dealer
# Import random to allow shuffling of cards
# Once shuffled, the dealer will 'deal' two cards each
# The dealers cards are hidden while the player's are visible
# The player has the ability to 'hit', or receive another card
# The player can 'hit' as many times as they want as long as their number does not go over 21, or 'bust'
# If the player's cards equal 21 on the first deal it's called a blackjack.
# Blackjack can only occur on the first deal
# The player cannot see the dealer's cards until the player decides to 'stand'.
# Whoever's cards are closer to 21 without going over wins the game.
import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Dealer():
    CARDS = list(range(1, 14))*4

    def __init__(self):
        random.shuffle(Dealer.CARDS)
        self.cards = Dealer.CARDS
        self.player = []
        self.dealer = []

    def p_cards(self):
        self.player.append(self.cards[0])
        self.cards.remove(self.cards[0])
        self.player.append(self.cards[0])
        self.cards.remove(self.cards[0])

    def d_cards(self):
        self.dealer.append(self.cards[0])
        self.cards.remove(self.cards[0])
        self.dealer.append(self.cards[0])
        self.cards.remove(self.cards[0])

    def hit(self):
        clear_screen()
        self.player.append(self.cards[0])
        self.cards.remove(self.cards[0])
        print("These are your cards: ")
        print(self.player)

    def stand(self):
        clear_screen()
        print(self.player)
        print(self.dealer)
    
    def black_jack(self):
        clear_screen()
        print(self.player)
        print(self.dealer)

    def player_wins(self):
        print("Congrats! You win!")

    def dealer_wins(self):
        print("Oh no! You lose!")

class UI():
    deal = Dealer()

    @classmethod
    def play_game(cls):
        clear_screen()
        print(
        """""""""
        =============================
        WELCOME TO MY BLACKJACK GAME!
        =============================
        """""""""
        )
        input("Press Enter to play!")
        print("These are your cards: ")
        cls.deal.p_cards()
        cls.deal.d_cards()
        print(cls.deal.player)

        sum_player = 0
        sum_dealer = 0

        while True:
            response = input("Would you like to hit or stand? ").lower().strip()

            if response == 'hit':
                cls.deal.hit()
            elif response == 'stand':
                break
            
        for i in cls.deal.player:
            sum_player += i
        for i in cls.deal.dealer:
            sum_dealer += i

        if sum_player == sum_dealer:
            cls.deal.stand()
            print("It's a tie!")
        elif sum_player > 21 and sum_dealer > 21:
            cls.deal.stand()
            print("You both lose!")
        elif sum_player > 21 or sum_dealer > 21:
            if sum_player > sum_dealer:
                cls.deal.stand()
                cls.deal.dealer_wins()

            elif sum_player < sum_dealer:
                cls.deal.stand()
                cls.deal.player_wins()
        elif sum_player <= 21 or sum_dealer <= 21:
            if sum_player > sum_dealer:
                cls.deal.stand()
                cls.deal.player_wins()
            else:
                cls.deal.stand()
                cls.deal.dealer_wins()

UI.play_game()