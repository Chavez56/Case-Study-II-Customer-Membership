# Import module
from module_membership import Membership

print("TEST CASE 1")
print("----------------")

user_membership = Membership(username='Shandy')
user_membership.show_benefit()

print()

print("TEST CASE 2")
print("----------------")


user_membership.show_requirements()


print()

print("TEST CASE 3")
print("----------------")

expense_income = [9,12]

user_membership.predict_membership(monthly_expense=expense_income[0], monthly_income=expense_income[1])
print()
user_membership.user_data
print()
user_membership.show_membership(username='Shandy')


print("TEST CASE 4")
print("----------------")

list_harga_barang = [150_000, 200_000, 400_000]

user_membership.calculate_price(membership=user_membership.show_membership(username='Shandy'),
                                list_harga_barang=list_harga_barang)


print()


print("TEST CASE 5")
print("----------------")

list_harga_barang = [150_000, 200_000, 400_000]

user_membership.calculate_price(membership=user_membership.show_membership(username='Ana'),
                                list_harga_barang=list_harga_barang)

print("----------------")
print()

list_harga_barang = [150_000, 200_000, '400_000']

user_membership.calculate_price(membership=user_membership.show_membership(username='Ana'),
                                list_harga_barang=list_harga_barang)

print("----------------")
print()

list_harga_barang = [150_000, 200_000, 400_000]

user_membership.calculate_price(membership=user_membership.show_membership(username='Elsa'),
                                list_harga_barang=list_harga_barang)

print()

print("TEST CASE 6")
print("----------------")

user_bambang = Membership(username='Bambang')
user_bambang.predict_membership(monthly_expense=3, monthly_income=4)
print()
list_harga_barang = [300_000, 150_000, 1_250_000, 15_000]

user_bambang.calculate_price(membership=user_bambang.show_membership(username='Bambang'),
                             list_harga_barang=list_harga_barang)
