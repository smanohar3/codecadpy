#Write your function here
def combine_sort(lst1, lst2):
  comb_list = lst1 + lst2
  comb_sort = sorted(comb_list)
  return comb_sort

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))