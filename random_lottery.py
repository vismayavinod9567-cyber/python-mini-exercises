#Generate 100 random lottery tickets and pick two lucky tickets from it as a winner
import random
def generate_tickets():
    tickets=[]
    for i in range(100):
        ticket=random.randint(100000,999999)
        tickets.append(ticket)
    return tickets
def winner(tickets):
    return random.sample(tickets,2)
x=generate_tickets()
print(x)
print("two lucky winners are",winner(x))