# PORT-SCANNER

Projeto que faz um scanner de portas utilizando Python.


## Funcionalidades

O programa possui a seguinte funcionalidade:

- `run_scanner(threads, mode)`: Executa um scanner de portas no alvo especificado com um número de threads definido pelo usuário e de acordo com o modo escolhido. O usuário pode escolher entre os modos 1, 2, 3 ou 4. Os modos 1 e 2 verificam as portas de 1 a 1023 e de 1 a 49152, respectivamente. O modo 3 verifica apenas as portas 20, 21, 22, 23, 25, 53, 80, 110 e 443. O modo 4 permite que o usuário insira as portas manualmente.

Exemplo de uso:

run_scanner(100, 1) # verifica as portas de 1 a 1023 no alvo 127.0.0.1 com 100 threads.


## Instalação

Para utilizar o programa, é necessário ter Python instalado na sua máquina. Além disso, é preciso instalar as bibliotecas socket e threading. Para instalar as bibliotecas, basta executar o seguinte comando:

pip install socket threading


## Contribuição

Sinta-se à vontade para contribuir com o projeto. Para isso, basta fazer um fork do repositório, implementar suas alterações e enviar um pull request.