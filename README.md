# Simulador 2D de Colisões Elásticas
Este simulador de colisões elásticas foi originalmente desenvolvido como uma Atividade Prática Supervisionada (APS) da disciplina de Física 1, ministrada no primeiro período do curso de Engenharia de Computação da Universidade Tecnológica Federal do Paraná (UTFPR). Posteriormente, um menu inicial foi implementado. O código foi escrito em Python, utilizando principalmente as bibliotecas Pygame e NumPy.

## Instalação & Uso

Para executar o simulador, basta realizar o download do arquivo executável (.exe) disponível neste repositório e executá-lo.

Então, preencha os campos solicitados com valores numéricos e pressione Enter.

## Fundamentos Teóricos
Na física, uma colisão elástica é um encontro entre dois corpos caracterizado pela conservação da energia cinética e do momento linear. Ainda, neste simulador as colisões são perfeitamente elásticas, ou seja, não há nenhuma transformação de energia cinética em outros tipos de energia, em outras palavras, o coeficiente de restituição é igual a 1.

Neste caso, após a colisão, a velocidade final das partículas pode ser calculada através da seguinte fórmula, adaptada da Wikipédia:
<p align="center">
  <img src="https://github.com/fallgatter/simulador-de-colisoes/blob/main/Imagens/formula.png" width="386" height="100" />
</p>
Onde v representa a velocidade inicial, v' representa a velocidade final, x é a posição do centro da partícula e os símbolos < e > representam um produto interno de dois vetores. Como neste simulador todas as partículas são iguais, o termo envolvendo as massas pode ser ignorado.

## Capturas de Tela
<p align="center">
  <img src="https://github.com/fallgatter/simulador-de-colisoes/blob/main/Imagens/menu.png" width="546" height="300" />
</p>

<p align="center">
  <img src="https://github.com/fallgatter/simulador-de-colisoes/blob/main/Imagens/running.png" width="546" height="300" />
</p>

## Contato
E-mail: fallgatter@alunos.utfpr.edu.br

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
