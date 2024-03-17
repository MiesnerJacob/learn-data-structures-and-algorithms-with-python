import random

def bubble_sort(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if comparison_function(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr

def quicksort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer - 1, comparison_function)
  quicksort(list, less_than_pointer + 1, end, comparison_function)

def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  else:
    return False

def by_author_ascending(book_a, book_b):
  if book_a['author_lower'] > book_b['author_lower']:
    return True
  else:
    return False
  
def by_total_length(book_a, book_b):
  print((len(book_a['title']) + len(book_a['author'])))
  if (len(book_a['title']) + len(book_a['author'])) > (len(book_b['title']) + len(book_b['author'])):
    return True
  else:
    return False

bookshelf_v1 = [{'title_lower': 'adventures of huckleberry finn', 'author_lower': 'mark twain', 'author': 'Mark Twain', 'title': 'Adventures of Huckleberry Finn'}, {'title_lower': 'best served cold', 'author_lower': 'joe abercrombie', 'author': 'Joe Abercrombie', 'title': 'Best Served Cold'}, {'title_lower': 'dear emily', 'author_lower': 'fern michaels', 'author': 'Fern Michaels', 'title': 'Dear Emily'}, {'title_lower': 'collected poems', 'author_lower': 'robert hayden', 'author': 'Robert Hayden', 'title': 'Collected Poems'}, {'title_lower': 'end zone', 'author_lower': 'don delillo', 'author': 'Don DeLillo', 'title': 'End Zone'}, {'title_lower': 'forrest gump', 'author_lower': 'winston groom', 'author': 'Winston Groom', 'title': 'Forrest Gump'}, {'title_lower': 'gravity', 'author_lower': 'tess gerritsen', 'author': 'Tess Gerritsen', 'title': 'Gravity'}, {'title_lower': "hiromi's hands", 'author_lower': 'lynne barasch', 'author': 'Lynne Barasch', 'title': "Hiromi's Hands"}, {'title_lower': 'norwegian wood', 'author_lower': 'haruki murakami', 'author': 'Haruki Murakami', 'title': 'Norwegian Wood'}, {'title_lower': "middlesex: a novel (oprah's book club)", 'author_lower': 'jeffrey eugenides', 'author': 'Jeffrey Eugenides', 'title': "Middlesex: A Novel (Oprah's Book Club)"}]  
sort_1 = bubble_sort(bookshelf_v1, by_title_ascending)
print(sort_1)

bookshelf_v2 = bookshelf_v1.copy()
sort_2 = bubble_sort(bookshelf_v2, by_author_ascending)
print(sort_2)

bookshelf_v3 = bookshelf_v1.copy()
sort_3 = quicksort(bookshelf_v3, 0, len(bookshelf_v3) -1, by_author_ascending)
print(sort_3)

bookshelf_v4 = bookshelf_v1.copy()
sort_4 = bubble_sort(bookshelf_v4, by_total_length)
print(sort_4)

bookshelf_v5 = bookshelf_v1.copy()
sort_5 = quicksort(bookshelf_v5, 0, len(bookshelf_v5) -1, by_total_length)
print(sort_5)