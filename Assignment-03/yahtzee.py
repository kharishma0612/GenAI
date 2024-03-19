import random

class YahtzeeGame:
    def __init__(self):
        self.dice = [0] * 5
        self.roll_count = 0
        self.score_card = {}

    def roll_dice(self, keep=[]):
        self.dice = [random.randint(1, 6) if i not in keep else self.dice[i] for i in range(5)]
        self.roll_count += 1

    def display_dice(self):
        print("Dice:", self.dice)

    def display_score_card(self):
        print("Score Card:")
        for category, score in self.score_card.items():
            print(f"{category}: {score}")

    def score_ones(self):
        return sum(die for die in self.dice if die == 1)

    def score_twos(self):
        return sum(die for die in self.dice if die == 2)

    def score_threes(self):
        return sum(die for die in self.dice if die == 3)

    def score_fours(self):
        return sum(die for die in self.dice if die == 4)

    def score_fives(self):
        return sum(die for die in self.dice if die == 5)

    def score_sixes(self):
        return sum(die for die in self.dice if die == 6)

    def score_three_of_a_kind(self):
        for die in set(self.dice):
            if self.dice.count(die) >= 3:
                return sum(self.dice)
        return 0

    def score_four_of_a_kind(self):
        for die in set(self.dice):
            if self.dice.count(die) >= 4:
                return sum(self.dice)
        return 0

    def score_full_house(self):
        counts = [self.dice.count(die) for die in set(self.dice)]
        if 2 in counts and 3 in counts:
            return 25
        return 0

    def score_small_straight(self):
        sorted_dice = sorted(set(self.dice))
        if len(sorted_dice) >= 4 and (sorted_dice[-1] - sorted_dice[0]) >= 3:
            return 30
        return 0

    def score_large_straight(self):
        sorted_dice = sorted(set(self.dice))
        if len(sorted_dice) == 5 and (sorted_dice[-1] - sorted_dice[0]) == 4:
            return 40
        return 0

    def score_chance(self):
        return sum(self.dice)

    def score_yahtzee(self):
        if len(set(self.dice)) == 1:
            return 50
        return 0

    def score(self, category):
        if category not in self.score_card:
            if category == "Ones":
                self.score_card[category] = self.score_ones()
            elif category == "Twos":
                self.score_card[category] = self.score_twos()
            elif category == "Threes":
                self.score_card[category] = self.score_threes()
            elif category == "Fours":
                self.score_card[category] = self.score_fours()
            elif category == "Fives":
                self.score_card[category] = self.score_fives()
            elif category == "Sixes":
                self.score_card[category] = self.score_sixes()
            elif category == "Three of a Kind":
                self.score_card[category] = self.score_three_of_a_kind()
            elif category == "Four of a Kind":
                self.score_card[category] = self.score_four_of_a_kind()
            elif category == "Full House":
                self.score_card[category] = self.score_full_house()
            elif category == "Small Straight":
                self.score_card[category] = self.score_small_straight()
            elif category == "Large Straight":
                self.score_card[category] = self.score_large_straight()
            elif category == "Chance":
                self.score_card[category] = self.score_chance()
            elif category == "Yahtzee":
                self.score_card[category] = self.score_yahtzee()
            else:
                print("Invalid category!")
                return
            print(f"Scored {self.score_card[category]} points for {category}.")
        else:
            print(f"{category} has already been scored.")

    def play_round(self):
        print(f"Round {self.roll_count + 1}:")
        self.roll_dice()
        self.display_dice()
        for i in range(2):
            reroll_indices = input("Enter indices of dice to re-roll (comma-separated, leave blank to keep current dice): ")
            if reroll_indices:
                reroll_indices = [int(index) for index in reroll_indices.split(",")]
                self.roll_dice(keep=reroll_indices)
                self.display_dice()
            else:
                break
        self.display_score_card()
        category = input("Enter category to score: ")
        self.score(category)


def main():
    yahtzee = YahtzeeGame()
    print("Welcome to Yahtzee!")
    while yahtzee.roll_count < 13:
        input("Press Enter to roll the dice...")
        yahtzee.play_round()
    print("Game Over!")
    yahtzee.display_score_card()


if __name__ == "__main__":
    main()