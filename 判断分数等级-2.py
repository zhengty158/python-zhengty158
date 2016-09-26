score = int(input('Please enter your score:'))
if 90 < score <= 100:
	print ('A')
else:
	if 80 < score <= 90:
		print('B')
	else:
		if 60 < score <= 80:
			print ('C')
		else:
			print ('D')
if score > 100 or score < 0:
	print ('enter error, try again')