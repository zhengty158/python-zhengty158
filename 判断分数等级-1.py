score = int(input('Please enter your score:'))
if 100 >= score > 90:
	print ('A')
if 90 >= score > 80:
	print ('B')
if 80 >= score > 60:
	print ('C')
if 60 >= score:
	print ('D')
if score > 100 or score < 0:
	print ('input error, try again')