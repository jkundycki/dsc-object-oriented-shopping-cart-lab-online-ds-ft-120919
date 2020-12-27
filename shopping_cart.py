class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, item_name, item_price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({'item_name': item_name, 'item_price': item_price})
            self.total += item_price
        return self.total
    
    def mean_item_price(self):
        mean = self.total/len(self.items)
        return round(mean,2)

    def median_item_price(self):
        #Need to work on this, does not account for list lengths
        price = []
        for i in range(len(self.items)):
            price.append(self.items[i]['item_price'])
        price.sort()
        median = price[round(len(price)/2)]
        return median

    def apply_discount(self):
        if self.employee_discount:
            discount_total = self.total*(1-(self.employee_discount/100))
            return(discount_total)
        else:
            return("Sorry, there is no discount to apply to your cart :(")

    def void_last_item(self):
        if len(self.items)>0:
            self.total = self.total-(self.items[-1]['item_price'])
            self.items.pop(-1)
            return(self.total)
        else:
            return("There are no items in your cart!")
        