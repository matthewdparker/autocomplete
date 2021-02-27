def lv_dist(str_1, str_2):
  '''
  A simple, non-optimized version of the Levenshtein
  Distance algorithm. If performance suffers, I imagine
  it will be because of the potential 3^n function calls,
  where n is the number of digits in the smaller string.

  :param string str_1: 1 string to measure distance
  :param string str_2: 2nd string to measure distance
  :return: An int giving the distance between the two strings
  '''
  
  if str_1 and str_2:
    if str_1[0] == str_2[0]:
      return lv_dist(str_1[1:], str_2[1:])
    else:
      del_1 = lv_dist(str_1[1:], str_2)
      del_2 = lv_dist(str_1, str_2[1:])
      del_12 = lv_dist(str_1[1:], str_2[1:])
      return 1 + min(del_1, del_2, del_12)
  elif str_1:
    return len(str_1)
  else:
    return len(str_2)