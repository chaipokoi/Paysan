import urllib2
import random
import re

random.seed()

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letter = letters[random.randint(0,25)]

page = urllib2.urlopen("http://www.cocoledico.com/dictionnaire-verbe/lettre-"+letter+".xhtml?nbr="+str(random.randint(0, 1001)));
verbs_page = page.read();

tverbs = re.findall("\<a href=\"\/dictionnaire\/[a-z]*\.xhtml\" title=\"definition de [a-z]*\"\>([a-z]*)\<\/a\>", verbs_page)

verbs = []

for v in tverbs:
	if v not in verbs:
		verbs.append(v)
		

letter = letters[random.randint(0,25)]		

page = urllib2.urlopen("http://www.cocoledico.com/dictionnaire-nom-commun/lettre-"+letter+".xhtml?nbr="+str(random.randint(0, 1001)));
words_page = page.read();

twords = re.findall("\<a href=\"\/dictionnaire\/[a-z]*\.xhtml\" title=\"definition de [a-z]*\"\>([a-z]*)\<\/a\>", words_page)

words = []

for v in twords:
	if v not in words:
		words.append(v)

phra = ""
		
typ = random.randint(0, 2)

if typ == 0:
	phra = "C'est "
	if random.randint(0,1) == 0:
		phra = phra + "pas "
	phra = phra + "en " + verbs[random.randint(0,len(verbs)-1)].replace("er", "ant")
	phra  = phra + " qu'on " + verbs[random.randint(0,len(verbs)-1)].replace("er", "e")
	phra = phra + " eul " + words[random.randint(0,len(words)-1)]
elif typ == 1:
	phra = "Qui " + verbs[random.randint(0,len(verbs)-1)].replace("er", "e")
	gn = ""
	if random.randint(0,1) == 0:
		gn = words[random.randint(0,len(words)-1)]
		phra = phra + " eul " + gn
	phra = phra + ", " + verbs[random.randint(0,len(verbs)-1)].replace("er", "e")
	if gn != "":
		phra = phra + " eul " + gn
elif typ == 2:
	ft = "au pieds"
	u = random.randint(0,2)
	if u == 0:
		ft = "au"
	elif u == 1:
		ft ="a la gueule"
	phra = "C'est "+ft+" d'eul " + words[random.randint(0,len(words)-1)] +" qu'on voit eul " + words[random.randint(0,len(words)-1)]
	
		
print phra



