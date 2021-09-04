# create a product and price for three items
product1_name,product1_price='lipstick', 400
product2_name,product2_price='nailpaint',50 
product3_name,product3_price='makupfixer',500 
product4_name,product4_price='perfume', 600
product5_name,product5_price='fondation',400 
product6_name,product6_price='maskara', 180
product7_name,product7_price='primer', 150
product8_name,product8_price='consiler',250 
product9_name,product9_price='eyeshadow', 500
product10_name,product10_price='eyeliner',150 
# create a company name and information
company_name = 'beauty store'
company_address = 'suncity'
company_city = 'solapur'

# declare ending message
message = 'Thanks for shopping with us today!'

# create a top border
print('*' * 50)

# print company information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

# print a line between sections
print('=' * 50)

# print out header for section of items
print('\tProduct Name\tProduct Price')

# create a print statement for each item
print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))
print('\t{}\t\t\t${}'.format(product4_name.title(), product4_price))
print('\t{}\t\t${}'.format(product5_name.title(), product5_price))
print('\t{}\t\t\t${}'.format(product6_name.title(), product6_price))
print('\t{}\t\t\t${}'.format(product7_name.title(), product7_price))
print('\t{}\t\t${}'.format(product8_name.title(), product8_price))
print('\t{}\t\t${}'.format(product9_name.title(), product9_price))
print('\t{}\t\t${}'.format(product10_name.title(),product10_price))
# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
total = product1_price + product2_price + product3_price+product4_price+product5_price+product6_price+product6_price+product7_price+product8_price+product9_price+product10_price
print('\t\t\t${}'.format(total))

# print a line between sections
print('=' * 50)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 50)
