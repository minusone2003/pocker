def flesh(list: list):
	'''Просто флеш'''
	end = 0
	list.sort(key=lambda i: i[1], reverse=True)
	pre = []
	count = 0
	for i in range(1, len(list)):
		if count == 4:
			list.append(list[i])
			break
		elif list[i - 1][1] == list[i][1]:
			count += 1
			pre.append(list[i - 1])
		else:

			pre.clear()
			count = 0
	if count == 4:
		end = 600 + pre[0][0]
	return end


a = [[8, 3], [2, 3], [0, 3], [2, 3], [6, 3], [6, 3]]
print(flesh(a))
