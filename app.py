import gradio as gr
import pandas as pd 
import nltk
import re 
import unidecode
import numpy as np 
from nltk.tokenize import word_tokenize
from functools import partial 
from nltk.corpus import stopwords 
from sklearn.metrics.pairwire import cosine_similarity 
import tensorflow_hub as hub

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

modulo_url ='https://tfhub.dev/google/universal-sentence-encoder/4'
modelo = hub.load(modulo_url)

def tratar_texto(texto): 
  texto = re.sub(r'\W', ' ', texto.lower())

  word_tokenize_pt = partial(word_tokenize, language='portuguese')
  tokens = word_tokenize_pt(texto)
  stop_words = set(stopwords.words('portuguese'))
  stop_words.discard('não')
  tokens = [w for w in tokens if w not in stop_words]

  texto_sem_acentos = unidecode.unidecode(' '.join(tokens))

  texto_normalizado = re.sub(r'(?!rr|ss)(.)\1+', r'\1', texto_sem_acentos)

  return texto_normalizado

def process_csv(arquivo, tema):
  df = pd.read_csv(arquivo.name)

  df['review_tratada'] = df['review'].apply(tratar_texto)
  df = df[df['review_tratada']!='']
  df.drop_duplicates(subset='review_tratada', inplace=True)

  reviews_emb = modelo(df['review_tratada'].tolist())
  tema_emb = modelo([tema])

  similaridades = cosine_similarity(tema_emb, reviews_emb).flatten()
  top_indices = np.argsort(-similaridades)

  similar_reviews = df[['nota_review', 'review']].iloc[top_indices]
  similar_df = similar_reviews.head(200)
  nome_arquivo = f'reviews_similares_{tema}.csv'
  similar_reviews.to_csv(nome_arquivo)

  return similar_df, nome_arquivo

with gr.Blocks() as app:
  with gr.Row():
    gr.Markdown('## Encontrando as reviews mais similares ao tema')
  csv_entrada = gr.File(label='Envie o CVS com as reviews', file_types=['.csv'])
  tema_entrada = gr.Textbox(label='Digite o tema de busca (Ex.: "Entrega")')
  
  botao = gr.Button('Clique para buscas as reviews')

  tabela_saida = gr.Dataframe(label='Top 200 reviews similares', headers=['Nota', 'Reviews'], interactive=False)
  arquivo_saida = gr.File(label='Baixar CSV ordenado com as reviews mais similares ao tema', interactive=False)

  botao.click(process_csv, inputs=[csv_entrada, tema_entrada], outputs=[tabela_saida, arquivo_saida])
app.launch()