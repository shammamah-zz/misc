import os

sel = -1; 

print("ayyy lmao you're lazy so you automated this holla \nWhat type of reference?")
path = os.getcwd()

while(sel!=0):

	sel = int(input('0 - exit\n1 - book\n2 - article\n3 - unpublished\n4 - Open .bib file\n5 - Print file\n'))

	if(sel==1):
		refType = '@book'
		keyword = input('Keyword\n')
		author = input('Author\n')
		year = input('Year\n')
		title = input('Title\n')
		publisher = input('Publisher\n')

		with open(path+"/refs.bib","a") as bibliography:
			bibliography.write(refType+'{'+keyword
				+',\nauthor={'+author
				+'},\nyear={'+year
				+'},\ntitle={'+title
				+'},\npublisher={'+publisher
				+'}\n}\n\n')
		bibliography.close()

	elif(sel==2):
		refType = '@article'
		keyword = input('Keyword\n')
		author = input('Author\n')
		year = input('Year\n')
		title = input('Title\n')
		journal = input('Journal\n')

		with open(path+"/refs.bib","a") as bibliography:
			bibliography.write(refType+'{'+keyword
				+',\nauthor={'+author
				+'},\nyear={'+year
				+'},\ntitle={'+title
				+'},\njournal={'+journal
				+'}\n}\n\n')
		bibliography.close()

	elif(sel==3):
		refType = '@unpublished'
		keyword = input('Keyword\n')
		author = input('Author\n')
		note = input('Note\n')
		title = input('Title\n')

		with open(path+"/refs.bib","a") as bibliography:
			bibliography.write(refType+'{'+keyword
				+',\nauthor={'+author
				+'},\ntitle={'+title
				+'},\nnote={'+note
				+'}\n}\n\n')
		bibliography.close()

	elif(sel==4):
		os.system("open "+path+"/refs.bib")

	elif(sel==5):
		print('--------------------------------------------\n')
		b = open(path+"/refs.bib")
		for line in b:
			print(line[:-1])
		b.close()
		print('--------------------------------------------')





