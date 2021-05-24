import hmtai
import random

nsfwlist=['ass','bdsm','cum','manga','femdom','hentai','masturbation','ero','orgy','yuri','pantsu','glasses','cuckold','blowjob','foot','thighs','vagina','ahegao','uniform','gangbang','tentacles','gif','nsfwNeko','nsfwMobileWallpaper','zettaiRyouiki']
sfwlist=['wallpaper','mobileWallpaper','neko','jahy']

def hentai(category,number,nsfw):
	if category.lower()=='show':
		if(nsfw):
			li=', '.join(nsfwlist)
		else:
			li=', '.join(sfwlist)
		li='Categories: '+li
		return li
	else:
		if category=='':
			if(nsfw):
				category=random.choice(nsfwlist)
			else:
				category=random.choice(sfwlist)
			number=1
		elif number=='':
			if category.isnumeric():
				number=int(category)
				if(nsfw):
					category=random.choice(nsfwlist)
				else:
					category=random.choice(sfwlist)
			else:
				if(nsfw):
					if not category.lower() in nsfwlist:
						return 'Wrong Category. Use `!nsfw show` to list categories'
				else:
					if not category.lower() in sfwlist:
						return 'Wrong Category. Use `!sfw show` to list categories'
				number=1
		else:
			if not number.isnumeric():
				return 'Wrong number'
			else:
				number=int(number)
				if(nsfw):
					if not category.lower() in nsfwlist:
						return 'Wrong Category. Use `!nsfw show` to list categories'
				else:
					if not category.lower() in sfwlist:
						return 'Wrong Category. Use `!sfw show` to list categories'
		if number>5:
			return "No Horny!!"
		li=[]
		category=category.lower()
		for i in range(number):
			li.append(f"{hmtai.useHM('v2',category)}")
			
		if 'nothing' in li:
			return 'Category currently not available'

		return li