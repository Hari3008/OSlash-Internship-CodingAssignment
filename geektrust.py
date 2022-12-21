from sys import argv

def add_items(category_inp,quantity_inp,items_added,category,clearance_criteria): # Add items with the quantity into a dictonary to store records
    if (items_added[category_inp] + quantity_inp) <= clearance_criteria[category[category_inp]]: #Check if the clearance criteria is being matched
        items_added[category_inp]+=quantity_inp
        print("ITEM_ADDED") 
        return 1
    else:
        print("ERROR_QUANTITY_EXCEEDED") #Item in excess of quantity as mentioned in criteria
        return 0
        
def price_without_discount(price,category_inp,quantity_inp): #Returning the item amount without discount
    return price[category_inp]*quantity_inp

def calculate_discount(total_amount,discount,items_added,price): #Calculating discount for the items purchased
    if total_amount < 1000: #If amount under 1000 no discount is provided
        return total_amount,0
    else:
        extra_discount = 0
        total_discount = 0
        for item,quantity in items_added.items(): # Discount provided based on the data given
            total_discount+=discount[item]*(0.01)*price_without_discount(price,item,quantity)
        total_discount = total_discount + extra_discount
        total_amount = total_amount - total_discount
        if total_amount>=3000: # 5% discount on 3000 Rs and above purchases
            extra_discount = total_amount*(0.05)
        total_amount-=extra_discount
    
    return total_amount,total_discount

def calculate_tax(total_amount): # Calculate sales tax of 10%
    return total_amount*1.1

def print_bill(total_amount,discount_amount): # Disply the bill to client
    print(f'TOTAL_DISCOUNT  {discount_amount:.2f}')
    print(f'TOTAL_AMOUNT_TO_PAY  {total_amount:.2f}')

def main():


    # Variables initiated which are required for the stationery store
    category = {'TSHIRT': 'Clothing', 'JACKET':'Clothing', 'CAP':'Clothing', 
                'NOTEBOOK': 'Stationery', 'PENS': 'Stationery', 'MARKERS': 'Stationery'}
    clearance_criteria = {'Clothing':2,'Stationery':3} 
    price = {'TSHIRT': 1000, 'JACKET':2000, 'CAP':500, 
                'NOTEBOOK': 200, 'PENS': 300, 'MARKERS': 500}
    discount = {'TSHIRT': 10, 'JACKET':5, 'CAP':20, 
                'NOTEBOOK': 20, 'PENS': 10, 'MARKERS': 5}
    items_added = {'TSHIRT': 0, 'JACKET':0, 'CAP':0, 
                'NOTEBOOK': 0, 'PENS': 0, 'MARKERS': 0}
    discount_amount = 0
    total_amount = 0

    if len(argv) != 2: #To check valid file path
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r') # Open file
    lines = f.readlines()
    for line in lines:

        command = line.split(' ')[0]
        command = command.strip() # Strip the whitespace
        if command == "ADD_ITEM":
            category_inp = line.split(' ')[1] # Item name
            quantity_inp = int(line.split(' ')[2]) # Item quantity
            if quantity_inp <=0:
                print("INVALID_ITEM_QUANTITY") # Quantity purchased can't be 0
                continue
            if category_inp in items_added:
                clearance = add_items(category_inp,quantity_inp,items_added,category,clearance_criteria) # Adding items
                if clearance: # if matches clearance criteria calculate amount
                    input_item_amount = price_without_discount(price,category_inp,quantity_inp)
                    total_amount+=input_item_amount

            
            else: # Item not in the list of items
                print("INVALID_ITEM")
        elif command == "PRINT_BILL": # Print bill
            total_amount,discount_amount = calculate_discount(total_amount,discount,items_added,price)
            total_amount = calculate_tax(total_amount)
            print_bill(total_amount,discount_amount)
        else:
            print("WRONG_INPUT_COMMAND") #Input command is wrong

    f.close() # File closing
if __name__ == "__main__":
    main()