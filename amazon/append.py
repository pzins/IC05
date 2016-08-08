######################################################
#    This script in used to append the results       #
#    of the amazon_categories script stored in       #
#    tmp_res.txt to the current res file named       #
#    amazon_data if they are not duplicates              #
######################################################

# each res entry must follow the format:
# src_ref;dst_ref;src_label;dst_label


# open temporary and final result file in read mode
tmp_res = open("tmp_res.txt", "r")
res = open("amazon_data", "r")

# store each line in lists
items = res.readlines()
tmp_items = tmp_res.readlines()

tmp_res.close()
res.close()

# open final result file in append mode
res = open("amazon_data", "a")


for i in range(len(tmp_items)):
    # read a temporary item
    tmp_item = tmp_items[i]
    tmp_src_ref = tmp_item.split(";")[0]
    tmp_dst_ref = tmp_item.split(";")[1]

    duplicate = False

    for j in range(len(items)):
        # read a final item
        item = items[j]
        src_ref = item.split(";")[0]
        dst_ref = item.split(";")[1]

        # if both the src and dst are the same,
        # the items are duplicates
        if tmp_src_ref == src_ref:
            if tmp_dst_ref == dst_ref:
                duplicate = True
                break

    if not duplicate:
        res.write(tmp_item)
res.close()