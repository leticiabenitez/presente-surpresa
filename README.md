# 🎁 Presente Surpresa

Um presente digital desenvolvido especialmente para minha mãe, com o objetivo de criar uma experiência diferente e tornar a revelação do presente ainda mais especial.

O projeto foi pensado como uma pequena jornada interativa, na qual cada etapa prepara a pessoa para descobrir a surpresa.

## ✨ Funcionalidades

- **Página inicial:** apresentação de uma mensagem convidando a descobrir a surpresa.
- **Prévia do presente:** uma etapa intermediária que mantém o mistério.
- **Contagem regressiva:** contador dinâmico que exibe os dias, horas, minutos e segundos até a data programada.
- **Acesso por senha:** formulário para liberar a revelação do presente.
- **Validação de data:** controle de acesso que impede a revelação antes da data definida.
- **Página de revelação:** apresentação dos presentes e de uma mensagem especial.
- **Navegação entre páginas:** transição entre as etapas utilizando rotas do Flask.

## 🛠️ Tecnologias utilizadas

- **Python:** desenvolvimento da lógica e gerenciamento das funcionalidades.
- **Flask:** criação das rotas e gerenciamento das páginas da aplicação.
- **HTML5:** estruturação das páginas.
- **CSS3:** estilização, layout responsivo e efeitos visuais.
- **JavaScript:** implementação da contagem regressiva e atualização dinâmica dos elementos.

## 📁 Estrutura do projeto

```text
presente-surpresa/
│
├── app.py
│
├── requirements.txt
│
├── public/
│   ├── css/
│   │   └── style.css
│   │
│   ├── img/
│   │   ├── presente.png
│   │   ├── presente1.png
│   │   └── presente2.png
│   │
│   └── js/
│       └── script.js
│
└── templates/
    ├── index.html
    ├── presente.html
    ├── contagem.html
    ├── senha.html
    └── revelacao.html
```

## 🚀 Como executar

**1. Clone o repositório:**

```bash
git clone URL_DO_REPOSITORIO
```

**2. Entre na pasta do projeto:**

```bash
cd presente-surpresa
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Execute a aplicação:**

```bash
python app.py
```

**5. Acesse no navegador:**

```text
http://127.0.0.1:5000
```

## 📚 Conceitos praticados

Durante o desenvolvimento, foram explorados conceitos importantes de programação:

- Criação e gerenciamento de rotas com Flask;
- Requisições HTTP GET e POST;
- Manipulação de formulários;
- Validação de informações;
- Controle de sessões com Flask;
- Manipulação de datas com Python;
- Manipulação do DOM com JavaScript;
- Cálculos e atualização de contagem regressiva;
- Organização de arquivos e separação de responsabilidades.
