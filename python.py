def solution(n) :
  answer = ''
  
  sum = 0
  sum_1 = 0
  num = 1
  list =  []
  
  
  while True:
    sum = sum + 3**(num)
    
    if n <= sum :
      break
    else :
      num += 1
    sum_1 = sum

  gap = n - sum_1 -1
      
  while gap :
    list.append(gap % 3)
    gap = gap //3
    
  start = ['1']*num
  print(list)
 
  for i in range(len(list)):
    if list[i] == 1 :
      start[i] = '2'
    elif list[i] == 2:
      start[i] = '4'

  
  start = ''.join(start)[::-1]
  print(start)
  return start