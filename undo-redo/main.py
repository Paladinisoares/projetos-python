print('Digite 1 para adicionar uma tarefa\n'
          'Digite 2 para listar suas tarefas\n'
          'Digite 3 para desfazer sua última ação\n'
          'Digite 4 para refazer sua última ação\n'
          'Digite 5 para encerrar.')

redo_list = []
tarefas = []

def list(tarefas):
    print('Tarefas:')
    print(tarefas)

def undo(tarefas, redo):
    if not tarefas:
        print('Não tem o que desfazer')
    ultimo_item = tarefas.pop()
    redo.append(ultimo_item)

def redo(tarefas, redo):
    if not redo:
        print('Não tem o que refazer')
    tarefas.append(redo)

while True:
    acao = input('Qual opção você deseja: ')

    if acao == '1':
        tarefa = input('Qual tarefa deseja adicionar: ')
        tarefas.append(tarefa)
    elif acao == '2':
        list(tarefas)
    elif acao == '3':
        undo(tarefas, redo_list)
    elif acao == '4':
        redo(tarefas, redo_list)
    else:
        break
