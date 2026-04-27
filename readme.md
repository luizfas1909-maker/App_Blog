📝 Blog com Python + SQLAlchemy (ORM)

Projeto simples de um sistema de blog utilizando Python e SQLAlchemy (ORM), com foco em aprendizado de persistência de dados, relacionamento entre entidades e manipulação via terminal.

📌 Objetivo

Este projeto foi desenvolvido para praticar:

Uso de ORM com SQLAlchemy
Criação de modelos e relacionamentos
Operações CRUD (Create e Read)
Organização de código em múltiplos arquivos
Interação com o usuário via terminal
🧱 Estrutura do Projeto
orm/
│
├── App_blog.py   # Arquivo principal (menu e execução)
├── Blog.py       # Lógica das operações (usuário e post)
├── User.py       # Model de usuário
├── Post.py       # Model de post
├── main.py       # Configuração do banco e sessão
└── blog.db       # Banco SQLite (gerado automaticamente)
🗄️ Modelos
👤 User
id
name
email
relacionamento com posts
📰 Post
id
title
content
author_id (FK)
relacionamento com usuário
🔗 Relacionamento
Um usuário pode ter vários posts
Um post pertence a um usuário
🚀 Como executar o projeto
1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate  # Windows
3. Instale as dependências
pip install sqlalchemy
4. Execute o projeto
python App_blog.py
📋 Funcionalidades
✅ Adicionar usuário
✅ Adicionar post
✅ Listar usuários com seus posts
💡 Exemplo de uso
1. Adicionar usuário
2. Adicionar post
3. Exibir usuários
4. Exibir posts
5. Sair
⚠️ Observações
O banco de dados é criado automaticamente com:
Base.metadata.create_all(bind=engine)
O projeto utiliza SQLite, então não precisa instalar banco externo.
🧠 Aprendizados

Durante o desenvolvimento, foram trabalhados conceitos como:

ORM vs SQL puro
Chaves estrangeiras (Foreign Key)
Relacionamentos com relationship
Sessões com SQLAlchemy
Organização de projeto em camadas simples
🔧 Melhorias futuras
 Atualizar e deletar usuários/posts (CRUD completo)
 Validação de dados (email único, campos obrigatórios)
 Interface gráfica ou API (Flask/FastAPI)
 Testes automatizados
👨‍💻 Autor

Desenvolvido por Luiz Fernando
