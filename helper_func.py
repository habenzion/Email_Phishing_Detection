from sklearn.base import BaseEstimator, TransformerMixin
import regex as re
from wordcloud import STOPWORDS
# class to transform text for Pipeline
class TextClean(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self,X,y=None):
        return self
    def transform(self, X, y=None):
        if type(X)!="list":
            X=list(X)
            X_=[]
            for text in X:
                text = text.lower()
                text = re.sub(r'[!@#$(),\.\n"%^*?:;~`0-9]', '', text)
                text = re.sub(r'\[.*?\]', '', text)
                text = ' '.join([word for word in text.split(' ') if word not in STOPWORDS])
                X_.append(text.strip())
            return X_
        elif type(X)=='str':
            text = X.lower()
            text = re.sub(r'[!@#$(),\.\n"%^*?:;~`0-9]', '', text)
            text = re.sub(r'\[.*?\]', '', text)
            text = ' '.join([word for word in text.split(' ') if word not in STOPWORDS])
            return text