**1 Introdução**

1\.1 Descrição do Projeto

O projeto consiste no desenvolvimento de um chatbot do Regulamento da

UFPB, utilizando técnicas de processamento de linguagem natural e aprendizado

de máquina. O objetivo é facilitar a busca e fornecer informações sobre o

regulamento da Universidade Federal da Paraíba, de forma mais acessível e

intuitiva para os usuários.

O chatbot foi desenvolvido utilizando a linguagem de programação Python,

fazendo uso de diversas bibliotecas e ferramentas. Além do NLTK (Natural

Language Toolkit) para o pré-processamento de dados, o chatbot também emprega

a biblioteca sklearn (scikit-learn) para implementar a abordagem de aprendizado de

máquina utilizada na seleção das respostas mais relevantes.

O processo de interação do chatbot inicia-se com o pré-processamento da

entrada do usuário, no qual são removidas pontuações, acentos e palavras

irrelevantes, utilizando o NLTK. Em seguida, a biblioteca sklearn é utilizada para

aplicar uma abordagem baseada em TF-IDF (Term Frequency-Inverse Document

Frequency) e calcular a similaridade entre as perguntas dos usuários e as

sentenças do Regulamento. Com base nessa similaridade, o chatbot seleciona as

sentenças mais relevantes e as apresenta como resposta ao usuário.

O principal objetivo do chatbot é simplificar o processo de busca de informações,

superando as dificuldades encontradas no arquivo oficial do regulamento. Ele

proporciona aos usuários um meio mais eficiente e conveniente para obter

informações específicas sobre o regulamento da UFPB.

1\.2 Fonte de dados utilizada

A fonte de dados utilizada neste projeto é um arquivo disponibilizado pela

Universidade Federal da Paraíba (UFPB) em seu site oficial. O arquivo em questão

é um documento em formato PDF contendo o regulamento da UFPB, conforme

estabelecido pela UFPB Resolução Nº 29/2020 (UNIVERSIDADE FEDERAL DA

PARAÍBA [UFPB], 2020).

Para facilitar a geração de respostas e tornar o conteúdo mais acessível, foi

realizada a extração dos dados desse arquivo. O texto foi reescrito de forma a

destacar o tema de cada sentença, colocando-o no início da mesma. Essa

abordagem teve como objetivo proporcionar um formato mais adequado para a

geração de respostas e facilitar o entendimento das informações contidas nas

normas e regulamentos da universidade.

É importante ressaltar que os dados utilizados neste projeto são derivados do

Regulamento Oficial UFPB Resolução Nº 29/2020. A utilização deste regulamento

como fonte de dados permite ao chatbot oferecer informações atualizadas e em

conformidade com as diretrizes estabelecidas pela UFPB.

**1**



<a name="br5"></a> 


**3 Pré-processamento de Dados**

Nesta etapa do projeto, foi utilizado o NLTK (Natural Language Toolkit), uma

biblioteca amplamente utilizada para processamento de linguagem natural em

Python, para realizar

o

pré-processamento dos dados.

O

objetivo do

pré-processamento é preparar os dados de entrada de forma adequada para as

etapas subsequentes de processamento e análise.

Foram aplicadas as seguintes técnicas de pré-processamento de dados:

**Remoção de pontuação**: e caracteres especiais: Foi realizada a remoção de

pontuação, como vírgulas, pontos e sinais de exclamação, assim como caracteres

especiais, visando limpar o texto e remover elementos que não agregam

informações relevantes para o processamento posterior.

**Normalização de palavras**: Com o objetivo de reduzir a dimensionalidade e

tratar diferentes formas de uma mesma palavra, foram aplicadas técnicas de

normalização. Isso incluiu a remoção de acentos das palavras, de forma a tratar

palavras acentuadas e não acentuadas como iguais.

**Lematização**: A lematização é uma técnica que visa reduzir palavras

flexionadas ou conjugadas ao seu lema, ou seja, sua forma base. Foi utilizada a

lematização para transformar palavras em sua forma canônica, o que permite

agrupar diferentes formas de uma mesma palavra.

Essas técnicas de pré-processamento têm como objetivo reduzir

a

dimensionalidade dos dados, tratar variações morfológicas e facilitar a identificação

de padrões e similaridades nas perguntas dos usuários em relação às sentenças do

regulamento da UFPB.

**3**



<a name="br7"></a> 

**4 Geração de Respostas**

Nesta etapa do projeto, é utilizada a técnica TF-IDF (Term Frequency-Inverse

Document Frequency) em conjunto com o algoritmo de similaridade do cosseno

para calcular a similaridade entre as perguntas do usuário e as sentenças do

regulamento. Isso permite que o chatbot encontre a sentença mais relevante do

regulamento que corresponda à pergunta do usuário.

Imagem 1ª ( Trecho codigo função de geração de Resposta)

4\.1 Cálculo do TF-IDF

O cálculo do TF-IDF é realizado utilizando o vetorizador TfidfVectorizer da

biblioteca sklearn.feature\_extraction.text. No trecho de código TfidfVec =

TfidfVectorizer(tokenizer=LemNormalize), o vetorizador é configurado para utilizar a

função LemNormalize como tokenizador. Essa função realiza a lematização das

palavras e remove as pontuações e caracteres especiais. Em seguida, o método

fit\_transform().

O método fit\_transform() é utilizado para calcular o TF-IDF para todas as

sentenças do regulamento, incluindo a pergunta do usuário. Esse método executa

duas etapas principais: ajuste (fitting) e transformação (transforming).

●

●

Ajuste (fitting): Durante o ajuste, o vetorizador analisa as sentenças do

regulamento e constrói um vocabulário, que consiste em todas as

palavras únicas presentes nas sentenças. Além disso, ele calcula as

frequências dos termos (TF) e as frequências inversas de documento

(IDF) para cada termo no vocabulário.

Transformação (transforming): Após o ajuste, o vetorizador utiliza o

vocabulário e as informações de frequência para transformar as

sentenças em vetores numéricos, onde cada valor representa a

importância relativa de um termo na sentença (de acordo com o

TF-IDF). Esses vetores são chamados de vetores TF-IDF e são usados

para calcular a similaridade entre as perguntas e as sentenças.

**4**



<a name="br8"></a> 

4\.2 Similaridade do cosseno

Após o cálculo do TF-IDF, a similaridade do cosseno é calculada entre a

pergunta do usuário (representada como um vetor TF-IDF) e todos os vetores

TF-IDF das sentenças utilizando o método cosine\_similarity(). Esse método mede o

ângulo entre dois vetores e retorna o valor do cosseno desse ângulo. Quanto mais

próximo o valor estiver de 1, maior é a similaridade entre os vetores.

A similaridade do cosseno é uma medida comum utilizada para comparar a

similaridade entre dois vetores em espaços vetoriais. Ela considera a direção e

magnitude dos vetores, mas não a sua dimensão absoluta. Portanto, é uma métrica

eficaz para calcular a similaridade entre as perguntas do usuário e as sentenças do

regulamento.

Ao aplicar o cosine\_similarity() passando o vetor TF-IDF da pergunta do usuário

(tfidf[-1]) e todos os vetores TF-IDF das sentenças (tfidf), obtemos uma matriz de

similaridade. Essa matriz tem dimensões (número de sentenças + 1) x (número de

sentenças), onde cada elemento da matriz representa a similaridade entre a

pergunta do usuário e uma sentença específica.

4\.3 Extração da sentença mais similar

A matriz de similaridade é utilizada para identificar a sentença mais relevante

que corresponde

à

pergunta do usuário. No trecho de código

idx=vals.argsort()[0][-2], os índices das sentenças são ordenados com base nos

valores de similaridade e o índice da segunda maior similaridade é selecionado.

Isso é feito assumindo que a maior similaridade é a própria pergunta do usuário. A

sentença correspondente é obtida através de sentencas[idx] e é apresentada como

resposta ao usuário.

**5**



<a name="br9"></a> 

**5 Demonstração do Projeto Funcionando**

Nesta demonstração foi perguntado como funciona a Reopção, logo abaixo está a

resposta dada pelo Chatbot, podemos observar que a resposta é a junção de várias

sentenças que têm similaridade com a pergunta do Usuário.

Outro exemplo de funcionamento.

**6 Conclusão**

O projeto teve como objetivo desenvolver um chatbot capaz de fornecer respostas

relevantes às perguntas dos usuários relacionadas ao Regulamento da Universidade

Federal da Paraíba (UFPB). Através da aplicação de técnicas de processamento de

linguagem natural e aprendizado de máquina, o chatbot conseguiu compreender as

perguntas dos usuários e encontrar as respostas mais adequadas no regulamento.

Em conclusão, o chatbot do Regulamento da UFPB demonstrou ser uma ferramenta

eficiente para auxiliar os usuários na obtenção de respostas precisas e relevantes sobre

o regulamento da universidade. No entanto, sempre há espaço para melhorias e futuras

expansões do projeto. Algumas possíveis melhorias e expansões podem incluir:

**6**



<a name="br10"></a> 

●

●

Aumento da base de dados: A inclusão de mais perguntas e respostas

no conjunto de dados pode melhorar a capacidade do chatbot de lidar

com uma variedade maior de consultas dos usuários.

Refinamento do modelo de aprendizado de máquina: A exploração de

diferentes algoritmos de aprendizado de máquina e técnicas de

pré-processamento de dados pode ajudar a aprimorar a precisão e a

capacidade do chatbot de lidar com perguntas complexas.

●

Integração com outras fontes de informação: Além do regulamento, o

chatbot pode ser expandido para integrar outras fontes de informação

relevantes.

**7 Referências**

Universidade Federal da Paraíba (UFPB). Resolução nº 29/2020 [PDF].

Disponível em: https://www.ufpb.br/dgeoc/contents/documentos/RESOLUCAO\_29\_2020.pdf.

Acesso em: 15 de Abril 2023.

**7**

