# 📦 Projeto Python - Guia de Execução

## 🐍 Versão do Python

Este projeto foi desenvolvido utilizando:

```
Python 3.10.2
```

Recomenda-se usar essa versão para evitar incompatibilidades.

---

## 🔧 Instalação de dependências

O arquivo `requirements.txt` já está disponível no projeto.

Execute:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuração da chave do Hugging Face

### 1. Criar conta

https://huggingface.co

---

### 2. Gerar API Key

Acesse: https://huggingface.co/settings/tokens

* Clique em **New token**
* Permissão: **Read**
* Gere e copie o token

---

### 3. Criar `.env`

Na raiz do projeto, crie:

```
.env
```

Conteúdo:

```
HF_TOKEN=seu_token_aqui
```

---

## 📁 Estrutura de Pastas

```
raiz/
│
├── .env
├── .gitignore
├── requirements.txt
├── main.py
├── test.py
├── readme.md
│
├── curadoria/
│   └── __init__.py
│   └── classificar.py
│   └── curar_dados.py
│
├── dados/
│   └── brutos/
│       └── multiplas_escolhas.json
│       └── questoes_abertas.json
│
│   └── curados/
│       └── abertas_curado_teste.json
│       └── abertas_curado.json
│       └── mcq_curado_teste.json
│       └── mcq_curado.json
│
├── inferencia/
│   └── executar_inferencia.py
│
├── metricas/
│   └── avaliar_abertas.py
│   └── avaliar_multiplas.py
│
├── prompts/
│   └── prompt_abertas.txt
│   └── prompt_multiplas.txt
│
└── resultados/
```

### 📌 Explicação

* **main.py** → execução principal
* **test.py** → execução de teste com menor consumo
* **inferencia/** → integração com API do HugginFace
* **prompts/** → prompts para a LLM
* **curadoria/** → realiza curadoria dos dados brutos
* **dados/** → dados brutos e curados
* **resultados/** → arquivos gerados
* **metricas/** → metricas geradas

---

## 🧪 Teste (baixo custo)

Execute:

```bash
python test.py
```

Esse script roda:

* 2 questões **Múltipla escolha**
* 2 questões **Abertas**

👉 Ideal para testar gastando pouco da API.

---

## 🚀 Execução principal

Cuidado! Ao rodar a execução principal os resultados e metricas obtidas anteriormente serão perdidos

```bash
python main.py
```
