#development file

file = open('./data/traindev/en-de/dev.ende.df.short.tsv')
data = file.readlines()[1:]
file.close()

de = open('./data/traindev/en-de/wmt20_dev.de', 'w')
en = open('./data/traindev/en-de/wmt20_dev.en', 'w')
hter = open('./data/traindev/en-de/wmt20_dev.hter_avg', 'w')
for d in data:
	d = d.split('\t')
	print(d)
	de.write(d[1] + "\n")
	en.write(d[2] + "\n")
	hter.write(d[4] + "\n")
de.close()
en.close()
hter.close()