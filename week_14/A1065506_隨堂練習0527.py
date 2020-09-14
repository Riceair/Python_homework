import jieba
from wordcloud import WordCloud

line = '國立高雄大學資訊工程學系A1065506'
txt = ' '.join(jieba.cut(line))
txt=txt+" 韓定紘"

wc = WordCloud(font_path=r"C:\Windows\Fonts\mingliu",\
               background_color="white").generate(txt)

img = wc.to_image()
img.show()
