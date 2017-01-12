import difflib

list1 = """https://mondotees.com/products/death-star-ii-duel-poster
https://mondotees.com/products/cloud-city-duel-poster
https://mondotees.com/products/the-aviator-poster
https://mondotees.com/products/the-aviator-variant-poster"""
product_list1 = list1.splitlines()

list2 = """https://mondotees.com/products/death-star-ii-duel-poster
https://mondotees.com/products/cloud-city-duel-poster
https://mondotees.com/products/drive-poster-3
https://mondotees.com/products/the-aviator-poster
https://mondotees.com/products/the-aviator-variant-poster"""
product_list2 = list2.splitlines()

d = difflib.Differ()
diff = d.compare(product_list1, product_list2)

change_delta = '\n'.join(i for i in diff if i.startswith('+ '))
product_added = change_delta.replace('+ ', "")

print(product_added)
