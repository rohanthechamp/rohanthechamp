import art
game_over=True
Auction_data = {
  "data": {
   "bidders_name":[],
    "bids":[]
   }
   }
print(art.logo)
while game_over:

    names=str(input("Enter your Name Gentleman:\n "))
    Auction_data["data"]["bidders_name"].append(names)
    bid=int(input("Enter the Bid amount Gentleman: \n $"))
    Auction_data["data"]["bids"].append(bid)

    restart=input("are there any bidders? type yes or no:  ")
    if restart == "no":
      game_over = False
      if  isinstance(bid,int):
       max_bid=max(Auction_data["data"]["bids"])

       max_bid_amount_index=Auction_data["data"]["bids"].index(max_bid)
       max_bidder=Auction_data["data"]["bidders_name"][max_bid_amount_index]
       print(f"***\n \t The Winner of the bid is  Mr.{max_bidder} with a bid of amount ${max_bid}  ")

      else: 
       print("The Winner with a bid of $0")
    elif restart =="yes":
      print("\n" * 50)

#bidders_name and  invalid input handling