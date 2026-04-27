from main import Base, engine, session
from User import User
from Post import Post

#criar tabelas
Base.metadata.create_all(bind=engine)

#função para exibier menu de opoes
def menu():
    print("1. Adicionar usuário")
    print("2. Adicionar post")
    print("3. Exibir usuários")
    print("4. Exibir posts")
    print("5. Sair")

#função para adicionar usuário
def add_user():
    name = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print('Usuário adicionado com sucesso!')

def add_post():
    print('Adicionando novo post')
    title = input('Título: \n')
    content = input('Conteúdo: \n')
    author_id = input('Id do Autor: \n')
    user = session.query(User).filter_by(id = author_id).first()
    if user:
        post = Post(title = title, content = content, author_id= user.id)
        session.add(post)
        session.commit()
        print('Usuário adicionado com sucesso')
    else:
        print('Usuário não encontrado')
# funçao para consultar usuário e post

def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f'User: {user.name}, Email: {user.email}')
        for post in user.posts:
            print(f'Post: {post.title}, Conteúdo: {post.content}')
