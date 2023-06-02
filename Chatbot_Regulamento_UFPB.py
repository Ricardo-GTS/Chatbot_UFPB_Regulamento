# Chatbot do Regulamento da UFPB
import io
import random
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import warnings
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Baixar recursos do NLTK
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('rslp', quiet=True)
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages
warnings.filterwarnings('ignore')

# Mapeamento de acentos, com o objetivo de remover os acentos das palavras
mapa_acentos = {
    'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
    'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
    'ú': 'u', 'ù': 'u', 'ũ': 'u', 'û': 'u', 'ü': 'u'
}

# Pré-processamento
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Geração de resposta
def response(user_response):
    robo_response=''
    sentencas.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(sentencas)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"NULL"
        return robo_response
    else:
        robo_response = robo_response+sentencas[idx]
        sentencas.remove(user_response)
        return robo_response


# Correspondência de palavras-chave
CUMPRIMENTO_INPUTS = ("olá", "saudações", "e aí", "como vai", "oi", "bom dia", "boa tarde", "boa noite")
CUMPRIMENTO_RESPONSES = [
    "Oi",
    "Olá",
    "Tudo bem?",
    "Olá, como posso ajudar?",
    "Olá, é um prazer falar com você!",
    "Olá! Como posso ser útil?",
    "Oi, tudo bem por aí?",
    "Olá, como está o seu dia?",
    "Oi, como posso auxiliar você hoje?"
]

# Função para gerar uma resposta de cumprimento ao usuário
def cumprimento(frase):
    """Se a entrada do usuário for um cumprimento, retorna uma resposta de cumprimento"""
    frase = frase.lower()
    if frase in CUMPRIMENTO_INPUTS:
        return random.choice(CUMPRIMENTO_RESPONSES)
    return None



# Pré-processamento da entrada do usuário
def processar_entrada_usuario(entrada):
    entrada = entrada.lower().translate(remove_punct_dict)
    entrada = pattern.sub(lambda m: mapa_acentos[m.group(0)], entrada)

    stop_words = set(stopwords.words('portuguese'))
    palavras_sem_stopwords = [palavra for palavra in word_tokenize(entrada, language='portuguese') if palavra.lower() not in stop_words]
    
    texto_sem_stopwords = ' '.join(palavras_sem_stopwords)
    return texto_sem_stopwords


# Leitura do arquivo que contém o texto do Regulamento da UFPB
with open("Regulamento_extrated.txt", encoding="utf8") as file:
    texto = file.read()
    texto = texto.lower()
    texto = re.sub(r'\n\s*\n', '\n', texto)
    texto = re.sub(''.join(mapa_acentos.keys()), lambda m: mapa_acentos[m.group(0)], texto)
    pattern = re.compile("|".join(mapa_acentos.keys()))
    texto = pattern.sub(lambda m: mapa_acentos[m.group(0)], texto)


# tokenizar as sentenças
sentencas = sent_tokenize(texto, language='portuguese')

resposta = ''
entradaPosProcessada = ''
Acumulador = []


# Início do diálogo, Loop principal.
flag=True
print("\nOlá! Sou o Chatbot da UFPB. Posso responder perguntas sobre o Regulamento da UFPB. Se quiser sair, digite tchau!")
while(flag==True):
    print("\nUSUARIO: ",end="")
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='tchau'):
        if(user_response=='obrigado' or user_response=='valeu' ):            
            print("De nada!")
            continue
        else:
            if(cumprimento(user_response)!=None):
                print("ROBO: "+cumprimento(user_response))
            else:
                print("ROBO: ",end="")
                count = 0
                resposta = ''
                for i in range(6):
                    entradaPosProcessada = processar_entrada_usuario(user_response)
                    resposta = response(entradaPosProcessada)
                    if(resposta != 'NULL'):
                        sentencas.remove(resposta)
                        print(resposta)
                        Acumulador.append(resposta)
                        count = count + 1
                    else:
                        break    
                if(count == 0):
                    print("ROBO: Desculpe Não Entendi!")
                for i in Acumulador:
                    sentencas.append(i)
                Acumulador.clear() 
    else:
        flag=False
        print("ROBO:tchau! cuide-se...")    
        