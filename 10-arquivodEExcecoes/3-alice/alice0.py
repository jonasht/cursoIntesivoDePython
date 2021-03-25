# trantando exceções fileNotfoundError

nomeDoArquivo = 'arquivoQueNaoExiste.txt'

with open(nomeDoArquivo) as f_obj:
    conteudo = f_obj.read()
