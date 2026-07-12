boat_side ='right'
missionaries_on_right =3
missionaries_on_left =0
cannibals_on_right =3
cannibals_on_left =0

print('M=',missionaries_on_left,'C=',cannibals_on_left, '|-----B|', 'M=',missionaries_on_right,'C=',cannibals_on_right)

while True:
   missionaries = int(input('enter no of missionaries: '))
   cannibals = int(input('enter no of cannibals: '))


   if (missionaries+cannibals) != 1 and (missionaries+cannibals) != 2:
    print("invaild move")
    continue

   if (boat_side == 'right'):
      if missionaries_on_right < missionaries or cannibals_on_right < cannibals:    
        print("invaild move")

      missionaries_on_right = missionaries_on_right - missionaries
      cannibals_on_right = cannibals_on_right - cannibals

      missionaries_on_left += missionaries
      cannibals_on_left += cannibals

      print('M=' ,missionaries_on_left, 'C=',cannibals_on_left, '|B-----|', 'M=',missionaries_on_right,'C=',cannibals_on_right)
      boat_side = 'left'

   else:
     if missionaries_on_left < missionaries or cannibals_on_left < cannibals:
       print("invaild move")

     missionaries_on_left = missionaries_on_left - missionaries
     cannibals_on_left = cannibals_on_left - cannibals

     missionaries_on_right += missionaries
     cannibals_on_right += cannibals

     print('M=',missionaries_on_left, 'C=',cannibals_on_left, '|-----B|', 'M=',missionaries_on_right, 'C=',cannibals_on_right)
     boat_side = 'right'

   if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0 ) or ( missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
     print("you loose")
     break

   if((missionaries_on_left == 3 ) and (cannibals_on_left == 3)):
      print("you won")
      break