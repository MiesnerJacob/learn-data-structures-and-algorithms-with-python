def linear_search_single_match(search_list, target_value):
  for idx in range(len(search_list)):
    print(search_list[idx])
    if search_list[idx] == target_value:
      return idx
  raise ValueError(f"{target_value} not in list")

def linear_search_multi_match(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches != []:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

def linear_search_max_value(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    print(search_list[idx])
    if (maximum_score_index == None) or (search_list[idx] > search_list[maximum_score_index]):
      maximum_score_index = idx
  return maximum_score_index

# Test linear search singe match
number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33
try:
  result_1 = linear_search_single_match(number_list, target_number)
  print(result_1)
  result_2 = linear_search_single_match(number_list, 100)
  print(result_2)
except ValueError as error_message:
  print("{0}".format(error_message))

# Test linear search multi match
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"
tour_stops = linear_search_multi_match(tour_locations, target_city)
print(tour_stops)

# Test linear search max value
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]
highest_score = linear_search_max_value(test_scores)
print(highest_score)