# Simulador 2D de Colisões Elásticas

Este simulador de colisões elásticas foi originalmente desenvolvido como uma Atividade Prática Supervisionada (APS) da disciplina de Física 1, ministrada no primeiro período do curso de Engenharia de Computação da Universidade Tecnológica Federal do Paraná. Posteriormente, um menu inicial foi implementado. O código foi escrito em Python, utilizando principalmente as bibliotecas Pygame e NumPy.

## Instalação & Uso

Para executar o simulador, basta realizar o download do arquivo executável (.exe) disponível neste repositório e executá-lo.

Então, preencha os campos solicitados com valores numéricos e pressione Enter.

## Fundamentos Teóricos

Na física, uma colisão elástica é um encontro entre dois corpos caracterizado pela conservação da energia cinética e do momento linear. Ainda, neste simulador as colisões são perfeitamente elásticas, ou seja, não há nenhuma transformação de energia cinética em outros tipos de energia, em outras palavras, o coeficiente de restituição é igual a 1.

Neste caso, após a colisão, a velocidade final das partículas pode ser calculada através da seguinte fórmula:
<p align="center">
  <img src="https://github.com/fallgatter/simulador-de-colisoes/blob/main/formula.png" width="938" height="243" />
</p>
(Fonte: Wikipédia)
Onde v representa a velocidade inicial da partícula, v' representa a velocidade final, x é a posição do centro e os símbolos < e > representam um produto interno de dois vetores. Como neste simulador todas as partículas são iguais, o termo envolvendo as massas pode ser ignorado.

## Contato
E-mail: fallgatter@alunos.utfpr.edu.br

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
