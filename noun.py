import nltk
from nltk.corpus import stopwords

from flask import Flask
app = Flask(__name__)

   
# return '<h3>' + str(ctr) + '</h3>'
text = "an elephant and an apple"
# return text

sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()
grammar = r"""
	NBAR:
		{<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
		
	NP:
		{<NBAR>}
		{<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)
toks = nltk.regexp_tokenize(text, sentence_re)
postoks = nltk.tag.pos_tag(toks)
print(postoks)
tree = chunker.parse(postoks)
stopwords = stopwords.words('english')
@app.route('/')


def counter(): 
	global stopwords
	def leaves(tree):
		"""Finds NP (nounphrase) leaf nodes of a chunk tree."""
		for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
			yield subtree.leaves()

	def normalise(word):
		"""Normalises words to lowercase and stems and lemmatizes it."""
		word = word.lower()
		# word = stemmer.stem_word(word) #if we consider stemmer then results comes with stemmed word, but in this case word will not match with comment
		word = lemmatizer.lemmatize(word)
		return word

	def acceptable_word(word):
		"""Checks conditions for acceptable word: length, stopword. We can increase the length if we want to consider large phrase"""
		accepted = bool(2 <= len(word) <= 40
			and word.lower() not in stopwords)
		return accepted


	def get_terms(tree):
		for leaf in leaves(tree):
			term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
			yield term

	terms = get_terms(tree)
	nounlist = ""

	i = 0
	for term in terms:
		for word in term:
			nounlist + 
			i + 1
	
	return nounlist


if __name__ == '__main__':  
	print('starting Flask app', app.name)  
	app.run(debug=True)







# f = open('helloworld.html','w')

# message = """
# <html>
#     <head></head>
#     <body>
#         <p>%s</p>
#         <svg width="100" height="100">
#           <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
#         </svg>
#     </body>
# </html>"""%(text)

# f.write(message)
# f.close()