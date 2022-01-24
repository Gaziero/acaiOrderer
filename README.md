### A simple app made for creating acai and milkshake orders.
Note that this was made for a very specific use.
I work on a small ice cream shop, and for the past years, we've been using paper to mannually write down the orders that needed to go to the kitchen.
I've decided that it would be so much better to write the orders using our computer and print it using our thermal printer.

### How it works
First, a windown pops up, there you can choose between the different sizes of acais and milkshakes
### The options frames change accordingly to the item chosen.
>As you can see [here](https://prnt.sc/26istz1) and [here](https://prnt.sc/26isuh6)
- ### Choosing an acai size:
- You can pick its fillings, wich are avaliable in three different prices;
- Picking more than three of the "Free" list, adds R$1,00 to final price;
- Before finalizing the order, you can chose to cover the acai with a lid.
- ### Choosing a milkshake size :
- You can chose its flavor and topping;
- You can choose one of three alcoholic beverages to add, this sums an extra R$5,00 to the final price
### Finalizing the order:
- Clicking the bottom right button ends the current order, which basically:
  - Reads the initial item chosen;
  - Reads the fillings/flavors/toppings chosen;
  - Writes it down on two different .txt files, toPrintTop.txt and toPrintBot.txt,
  - Prints out both files in a thermal printer.
- #### toPrintTop.txt:
  - This part goes to the kitchen;
  - It contains the item, its size, and all the related information of the order;
  - Also contains the order number.
- #### toPrintBot:
  - This part is given to the custumer;
  - Contains the order number, basic item name, and total cost.
>The printed document will look like [this](https://prnt.sc/26isveu)
The program will generate the orders numbers until it is closed, wich resets the number back to 1.

###### The code is all spaghetti, I know it, I'm starting to learn OOP and plan to revisit this project once I get at least the basics.
#### Thank you for reading
