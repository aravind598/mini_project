#Joshua Coded this lines 1 to 17
import pickle

menus = {'mc_donalds':[{'Hotcakes':'$4.95', 'Sausage McMuffin with Egg':'$4.20', 'Big Breakfast':'$5.90'}, {'Cheeseburger Meal':'$8.95', 'McChicken':'$2.00', 'Big Mac':'$5.75', 'McSpicy':'$5.25'}],
'kfc_':{'2 pcs Chicken Meal':'$10.15', 'Mac N Cheese':'$10.45', 'Zinger':'$5.30', 'Curry Rice Bowl':'$5.30'},
'subway':{'6-inch':'$5.70', 'Footlong':'$9.50', 'Wrap':'$6.10'},
'pizza_hut':{'Hawaiian':'$10.80', 'Pepperoni':'$10.80', 'Seafood Deluxe':'$11.20'},
'sandwich_guys':{'BBQ Pulled Pork':'$6.00', 'Philly Cheesesteak':'$7.00', 'Mexicana Grilled Chicken':'$6.00', 'Cubano':'$7.00'}}

filename = 'menus'
outfile = open(filename,'w+b')

pickle.dump(menus, outfile)
outfile.close()

# for mcdonalds, [0] -> breakfast menu, [1] -> lunch/dinner menu
