i=0
while i < 3:
	password = input('請輸入密碼：')
	if password == 'a123456':
		print('登入成功')
		log_in = True
	else:
		i = i + 1
		print('還有',3 - i,'次機會' )
		log_in = False

	if log_in == True:
		break

