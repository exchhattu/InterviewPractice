"""
Thu Feb 20 10:08:37 2020
"""
import numpy as np
import numpy.random as random

class BlackJack:

    def __init__(self, bet):
        self._card_value = {'K': 10, 
                            'Q': 10, 
                            'J': 10,
                            'A': [1,10] }
        self._bet           = bet 
        self.init_game()

    def init_game(self):
        self._deal_cards    = random.randint(1, 13, 2) 
        self._player_cards  = random.randint(1, 13, 2) 

    def restart_game(self, bet):
        self._bet           = bet 
        self.init_game()


    def hit_or_stand(self, who='player'):
        """
        update the value 
        """
        cur_face_value = self._deal_cards.append(random.randint(1, 13, 1)) 
        if cur_face_value in self._card_value.key():
            cur_face_value = self._card_value[cur_face_value]
        if who is 'dealder':
            self._deal_cards.append(random.randint(1, 13, 1)) 
            return sum(self._deal_cards) 
        elif who is  'dealer':
            self._play_cards.append(random.randint(1, 13, 1)) 
            return sum(self._play_cards) 
        else:
            print('Warn: not recoginzed')
            return -1 

    def print_state(self):
        """
        display the content 
        """
        print("dealer sum: ", self._deal_cards[:-1]) 
        print("player sum: ", self._play_cards) 


    def play(self, user_input, who='player'):
        """
        play based on user input
        """

        if user_input == 'hit' and who=='player':
            current_sum = self.hit_or_stand('player') 
            self.print_state()
            if current_sum > 21:
                print("Dealer %d won!!!" %self.bet)
                return True
        if user_input == 'stand' and who=='dealer':
            current_sum = self.hit_or_stand('dealer') 
            self.print_state()
            if current_sum > 17:
                print("You %d won!!!" %self.bet)
                return True
            else:
                player_current_sum = self.hit_or_stand('player') 
                if player_current_sum > current_sum:
                    print("Player won")
                    return True
                elif player_current_sum == current_sum:
                    print("Tied")
                    return True
                else: 
                    print("Dealer won")
                    return True
        return False


if __name__ == '__main__':
    bet = input("Bet amount ")
    black_jack = BlackJack(bet)
    while True: 
        action = ""
        user = input("player or dealder: ")
        if user == "dealer":
            action = input("Hit/stand: ")
        elif  user == "player":
            action = input("Hit/stand: ")
        else:
            continue
    
        if black_jack.play(user, action):
            yes_no = input("Play Again? (yes or no)")
            if yes_no.lower().strip() == "yes":
                bet = input("Bet amount ")
                self.restart_game(bet)

            elif yes_no.lower().strip() == "no":
                break

