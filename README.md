# 📊 Review Similarities

Aplicação interativa desenvolvida com **Python** e **Gradio** para identificar **reviews mais similares a um tema específico**, utilizando técnicas de **Processamento de Linguagem Natural (NLP)** e **embeddings semânticos**.

O sistema permite que o usuário envie um arquivo CSV contendo avaliações textuais e, a partir de um tema informado, retorna as reviews semanticamente mais próximas, ordenadas por similaridade.

---

## 🚀 Funcionalidades

- Upload de arquivo **CSV** contendo reviews.  
- Pré-processamento textual em português:
  - Normalização.
  - Remoção de stopwords (mantendo negações relevantes).
  - Remoção de acentuação.
- Geração de **embeddings semânticos**.
- Cálculo de **similaridade por cosseno**.
- Exibição das **200 reviews mais similares**.
- Download do CSV ordenado por similaridade.

---

## 🧠 Tecnologias e Bibliotecas

- **Python**
- **Gradio**
- **NLTK**
- **TensorFlow Hub**
- **Universal Sentence Encoder (USE)**
- **Pandas**
- **Scikit-learn**
- **NumPy**
- **Unidecode**

_____________________________________

# 📊 Review Similarities

An interactive application developed with **Python** and **Gradio** to identify **reviews most similar to a specific topic**, using **Natural Language Processing (NLP)** techniques and **semantic embeddings**.

The system allows users to upload a CSV file containing textual reviews and, based on a given topic, returns the semantically closest reviews, ranked by similarity.

---

## 🚀 Features

- Upload of a **CSV** file containing reviews.  
- Text preprocessing in Portuguese:
  - Normalization.  
  - Stopword removal (while preserving relevant negations).  
  - Accent removal.  
- Generation of **semantic embeddings**.  
- **Cosine similarity** computation.  
- Display of the **top 200 most similar reviews**.  
- Download of the CSV file ordered by similarity.  

---

## 🧠 Technologies and Libraries

- **Python**
- **Gradio**
- **NLTK**
- **TensorFlow Hub**
- **Universal Sentence Encoder (USE)**
- **Pandas**
- **Scikit-learn**
- **NumPy**
- **Unidecode**

__________________________

title: Review Similarities
emoji: 📊
colorFrom: gray
colorTo: pink
sdk: gradio
sdk_version: 6.3.0
app_file: app.py
pinned: false

---

Check out the application on Hugging Face: https://huggingface.co/spaces/lunecarvalho/review-similarities/
