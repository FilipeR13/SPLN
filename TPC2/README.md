# TPC2 - Comentário de Linhas Duplicadas

## Descrição

Este projeto consiste em um script Python (`comment_lines.py`) que comenta linhas duplicadas de um arquivo de texto. O script lê um arquivo de entrada, processa as linhas para comentar duplicatas e salva o resultado em um novo arquivo.

## Como Utilizar

### Execução

Para executar o script, utilize o seguinte comando no terminal:

```bash
python3 comment_lines.py <nome_do_arquivo.txt>
```

### Exemplo

Se tiver um arquivo chamado `exemplo.txt` com o seguinte conteúdo:

```
linha1
linha2

linha1
linha3

linha2
```

Execute o script:

```bash
python3 comment_lines.py exemplo.txt
```

O script irá gerar um novo arquivo chamado `exemplo_filtered.txt` com o seguinte conteúdo:

```
linha1
linha2
#
linha3
#
```

### Entrada via stdin

Também pode fornecer a entrada via stdin:

```bash
cat exemplo.txt | python3 comment_lines.py
```

### Opções

- `-s`, `--spaces`: Considera espaços na comparação de linhas.
- `-p`, `--comment`: Comenta linhas vazias com `#`.

## Estrutura do Código

- `comment_duplicate_lines(input_lines, spaces=False, comment=False)`: Função que comenta linhas duplicadas de uma lista de linhas.
- `main()`: Função principal que gerencia a leitura do arquivo de entrada, chama a função de comentário de duplicatas e escreve o resultado em um novo arquivo ou imprime no terminal.
