while True:
    usuario = input('Digite seu nome de usuário (mínimo 5 caracteres): ')
    senha = input('Digite sua senha (mínimo 8 caracteres): ')

    if len(usuario) >= 5 and len(senha) >= 8:
        print('Cadastro realizado com sucesso!')
        break
    if len(usuario) < 5:
        print('ERRO! O nome de usuário deve ter pelo menos 5 caracteres')
    if len(senha) < 8:
        print('ERRO! A senha deve ter pelo menos 8 caracteres')

