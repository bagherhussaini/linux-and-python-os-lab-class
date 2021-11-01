products = []


def load_data():
    f = open('database.csv', 'r')
    for line in f:
        info = line[:-1].split(',')
        new_dict = {'Code': info[0], 'Name': info[1], 'Price': info[2], 'Stock': info[3]}
        products.append(new_dict)


def show_menu():
    print('Welcome to Shopping Mall\n1.Add Product\n2.Edit In-Stock Product\n3.Delete Product\n4.Show In-Stock Products'
          '\n5.Search Product\n6.Buy\n7.Save and Quit')


def add_product():
    new_product = {'Code': input('Enter Product Code: '), 'Name': input('Enter Product Name: '),
                   'Price': input('Enter Product Price: '), 'Stock': input('Enter Product Stock: ')}
    f = open('database.csv', 'a')
    flag = True
    for keys in new_product:
        if new_product[keys] not in products:
            f.write(str(new_product[keys]))
            f.write(',')
        else:
            flag = False
            print('Product Already Exists!')
    if flag:
        f.write('\n')


def edit_in_stock_product():
    product_name = input('Enter Product\'s Name to Edit: ')
    index = 0
    found = False
    for product in products:
        if product['Name'] == product_name:
            found = True
            break
        else:
            index += 1
    if found:
        f = open('database.csv', 'r')
        lines_of_file = f.readlines()
        info = lines_of_file[index][:-1].split(',')
        while True:
            choice = input('Which Field of the Product You Wish to Change?\n1.Code\n2.Name\n'
                           '3.Price\n4.Stock\n5.Finish Editing')
            if choice == 'Code' or choice == 'code' or int(choice) == 1:
                new_code = input('Enter New Code: ')
                f = open('database.csv', 'w')
                lines_of_file[index] = lines_of_file[index].replace(info[0], new_code)
                f.writelines(lines_of_file)
                print('Successfully Done.')
                f.close()
            elif choice == 'Name' or choice == 'name' or int(choice) == 2:
                new_name = input('Enter New Name: ')
                f = open('database.csv', 'w')
                lines_of_file[index] = lines_of_file[index].replace(info[1], new_name)
                f.writelines(lines_of_file)
                print('Successfully Done.')
                f.close()
            elif choice == 'Price' or choice == 'price' or int(choice) == 3:
                new_price = input('Enter New Price: ')
                f = open('database.csv', 'w')
                lines_of_file[index] = lines_of_file[index].replace(info[2], new_price)
                f.writelines(lines_of_file)
                print('Successfully Done.')
                f.close()
            elif choice == 'Stock' or choice == 'stock' or int(choice) == 4:
                new_stock = input('Enter New Stock: ')
                f = open('database.csv', 'w')
                lines_of_file[index] = lines_of_file[index].replace(info[3], new_stock)
                f.writelines(lines_of_file)
                print('Successfully Done.')
                f.close()
            elif choice == 'Finish Editing' or choice == 'finish editing' or int(choice) == 5:
                break
            else:
                print('Choose Correctly!')
    else:
        print('The Product is Out of Stock!\nCheck out \'Add\' Option to Add New Product.')


def delete_product():
    product_name = input('Enter Product\'s Name to Delete: ')
    f = open('database.csv', 'r')
    lines_of_file = f.readlines()
    f = open('database.csv', 'w')
    for line in lines_of_file:
        if product_name not in line:
            f.write(line)
    print('Successfully Done.')
    f.close()


def show_in_stock_products():
    print('Code\tName\tPrice\tStock')
    for product in products:
        print(product['Code'], '\t', product['Name'], '\t', product['Price'], '\t', product['Stock'])


def search_product():
    product_name = input('Enter Product\'s Name: ')
    index = 0
    found = False
    for product in products:
        if product['Name'] == product_name:
            found = True
            break
        else:
            index += 1
    if found:
        print('The Product You Searched is in Stock.\nHere\'s the Details:\n', 'Code Name: ', products[index]['Code'],
              '\nPrice: ', products[index]['Price'], '\nStock: ', products[index]['Stock'])
    else:
        print('The Product You Searched is Out of Stock!')


def buy():
    index = 0
    found = False
    valid_purchase = True
    product_name = input('Enter Product\'s Name: ')
    for product in products:
        if product['Name'] == product_name:
            found = True
            product_quantity = int(input('Enter the Number of Product: '))
            while product_quantity <= 0:
                product_quantity = int(input('Enter the Number of Product (Positive): '))
            break
        else:
            index += 1
    if found:
        if product_quantity > int(products[index]['Stock']):
            print('Not Enough Exists in Stock!')
            valid_purchase = False
        elif product_quantity == int(products[index]['Stock']):
            f = open('database.csv', 'r')
            lines_of_file = f.readlines()
            f = open('database.csv', 'w')
            for line in lines_of_file:
                if product_name not in line:
                    f.write(line)
            f.close()
        else:
            new_stock = int(products[index]['Stock']) - product_quantity
            f = open('database.csv', 'r')
            lines_of_file = f.readlines()
            info = lines_of_file[index][:-1].split(',')
            f = open('database.csv', 'w')
            lines_of_file[index] = lines_of_file[index].replace(info[3], str(new_stock))
            f.writelines(lines_of_file)
            f.close()
        if valid_purchase:
            print('Details of Shopping:\nProduct Name: ', product_name, '\nQuantity: ', product_quantity,
                  '\nTotal Price: $', product_quantity*int(products[index]['Price']))
    else:
        print('The Product You\'re Looking for is Out of Stock!')


def save_and_quit():
    exit()


def main():
    load_data()
    while True:
        show_menu()
        choice = int(input('Select Operation: '))
        if choice == 1:
            add_product()
        elif choice == 2:
            edit_in_stock_product()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            show_in_stock_products()
        elif choice == 5:
            search_product()
        elif choice == 6:
            buy()
        elif choice == 7:
            save_and_quit()
        else:
            print('Something Went Wrong with Your Choice!')


if __name__ == '__main__':
    main()
