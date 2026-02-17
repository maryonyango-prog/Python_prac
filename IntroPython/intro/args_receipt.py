#def sum_receipt(a, b, c):
 #   sum = a + b + c
 #   print("The sum of the receipt is:", sum)
 #   return sum

def new_receipt(*args):
    print("The items in the receipt are:", args)
    sum = 0
    for item in args:
        print("item is", item)
        sum=sum+item
    print("The sum of the receipt is:", sum)
#new_receipt(10, 20, 30) 
#new_receipt()


def main():
   prices_list = []

   while True:
         user_input = input("Enter the price of an item or 'done' to finish: ").lower()
            if user_input == 'done':
                break
            try:
                price = float(user_input)
                prices_list.append(price)
            except Exception as e:
                print("Invalid input. Please enter a valid price")
            print(prices_list)
main()
    