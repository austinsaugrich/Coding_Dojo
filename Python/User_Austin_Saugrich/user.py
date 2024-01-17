class User:
    def __init__(self, first_name, last_name, email, age,):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 2

    def display_info(self):
        for i in self.__dict__:
            print(self.__dict__[i])

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print('User is already a member.')

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print('You dont have enough.')
        else:
            self.gold_card_points = self.gold_card_points - amount


jessica = User('Jessica', 'Simpson', 'jessica@gmail.com', 21)
tj = User('TJ', 'JT', 'TJ@gmail.com', 35)
nolan = User('Nolan', 'Smith', 'nolan@gmail.com', 13)

jessica.spend_points(50)
tj.enroll()
tj.spend_points(80)
jessica.display_info()
tj.display_info()
nolan.display_info()
nolan.spend_points(40)
