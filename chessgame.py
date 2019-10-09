import random
accounts = open("accounts.txt", "r").read().split('\n')
moves = open("gameMoves.txt", "r").read().split('\n')

random.shuffle(accounts)