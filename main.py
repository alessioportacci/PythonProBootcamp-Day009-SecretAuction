from replit import clear
import logo


def winner(bidders):
  winner = ""
  top_bid = 0
  for key in bidders:
    if bidders[key] > top_bid:
      winner = key
  return winner


another_bidders = True
bidders = {}

print(logo.logo)
print("Welcome to the secret auction program.")

while another_bidders:
  name = input("What is your name? " )
  bid = int(input("What's your bid? $"))
  bidders[name] = bid

  if(input("Are there any other bidders? Type 'yes' or 'no' ") == "no"):
    another_bidders = False
  clear()

winner_bidder = winner(bidders)

print(f"The winner is {winner_bidder} with a bid of ${bidders[winner_bidder]}")