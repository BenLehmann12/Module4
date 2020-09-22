
def calculate_price(price,cash_coupon,percent_coupon):
    new_cash = price - cash_coupon
    after_percent = new_cash - (new_cash*percent_coupon/100)
    after_tax = after_percent + (after_percent*6)/100
    if after_tax <= 10:
        new_price = after_tax + 5.95
    if after_tax > 10 and after_tax < 30:
        new_price = after_tax + 7.95
    if after_tax > 30 and after_tax < 50:
        new_price = after_tax + 11.95
    if after_tax > 50:
        new_price = after_tax
    print("Price is " + str(price) + " Coupon is " + str(cash_coupon) + " New Price is " + str(new_price) )


if __name__ == '__main__':
    price = calculate_price(8,10,20)




