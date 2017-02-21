article = ' ... '

men_quoted = article.count(' he said')
women_quoted = article.count('  she said')
if women_quoted == 0 or men_quoted > women_quoted * 2:
	print """No women were quoted,
	or twice as many quotes came from men"""
