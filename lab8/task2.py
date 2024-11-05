import random

def dat():
    ticket = random.sample(range(1, 50), 6)
    ticket.sort()
    return ticket
lottery_ticket = dat()
print("Ваш лотерейный билет:", lottery_ticket)
