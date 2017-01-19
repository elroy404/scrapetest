import difflib

# compare og_list to new_list
def compareList(og, new):
    og_file = open(og, "r")
    new_file = open(new, "r")
    count = 0
    prod = []

    list_og = og_file.read()
    og_list = list_og.splitlines()

    list_new = new_file.read()
    new_list = list_new.splitlines()

    d = difflib.Differ()
    diff = d.compare(og_list, new_list)

    change_delta = '\n'.join(i for i in diff if i.startswith('+ '))
    new_product = change_delta.replace('+ ', "")

    if not change_delta:
        print "no change"
        print change_delta
        time.sleep(2)
        collectLinks(file_new)
        compare = compareList(og, new)
        openLoc(compare)
    else:
        new_product_list = new_product.split()
        for i in range(len(new_product_list)):
            prod.insert(0,new_product_list[i])
    return prod
    og_file.close()
    new_file.close()
