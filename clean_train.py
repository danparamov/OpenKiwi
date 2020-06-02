#train file

file = open('./OpenKiwi/data/traindev/train.ende.df.short.tsv')
data = file.readlines()[1:]
file.close()


de = open('./OpenKiwi/data/traindev/wmt20_train.de', 'w')
en = open('./OpenKiwi/data/traindev/wmt20_train.en', 'w')
hter = open('./OpenKiwi/data/traindev/wmt20_train.hter_avg', 'w')
for d in data:
	d = d.split('\t')
	print(d)
	de.write(d[1] + "\n")
	en.write(d[2] + "\n")
	hter.write(d[4] + "\n")
de.close()
en.close()
hter.close()