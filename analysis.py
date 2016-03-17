#coding: utf-8
import re
from wordcloud import WordCloud, STOPWORDS

depoimento = open('depoimento_lula.txt', 'r')

falas = []
for linha in depoimento.readlines():
   sentenca = linha.split(":")
   
   pessoa = sentenca[0] 
   frase = "".join(sentenca[1:])
   
   falas.append(dict(pessoa=pessoa, frase=frase))


declarante = [
   fala['frase'].decode('utf-8') 
   for fala in falas 
   if fala['pessoa'] == 'Declarante'
]

declarante = "".join(declarante).lower()
declarante = declarante.replace(u"não sei", u"nãosei")

swords = ['que', 'eu', u'não', 'da', 'de', 'por', 'ele', u'você', u'está',
          'tem', 'um', 'uma', 'se', 'foi', u'lá', 'pra', 'para', 'vai', 
          u'já', 'na', 'era', 'em', u'aí', 'minha', u'nós', 'os', 'as', 
          'ou', 'essa', 'isso', 'como', 'aqui', 'pois', u'só', 'quando', 
          u'então', 'muito', 'porque', 'acho', 'nem', 'mais', 'meu',
          'ser', 'estou', 'vou', 'coisa', 'tenho', 'tinha', 'ter', u'quem'
          'fui', 'mas', u'são', 'muita', 'mim', 'tudo', 'toda', 'todo', 
          'deve', 'falar', 'eles', 'das']

STOPWORDS = STOPWORDS.union(swords)

wordcloud = WordCloud(width=800, height=400,
                      stopwords=STOPWORDS).generate(declarante)

wordcloud.to_file("wordcloud.png")
