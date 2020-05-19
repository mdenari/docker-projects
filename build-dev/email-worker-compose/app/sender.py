from bottle import route, run, request

@route('/', method='POST')
def send():
    assunto = request.forms.get('assunto')
    messagem = request.forms.get('mensagem') 
    return 'Mnesagem enfileira ! Assunto: {}  Mensagem: {}'.format(
        assunto,mensagem
    )

if __name__ == '__main__':
    run(host='0.0.0.0', port-8080, debug=True)
    