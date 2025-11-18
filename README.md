# Análise Completa da Influência no Preço de Imóveis

Esta análise exploratória de dados (EDA) e o dashboard foram desenvolvidos para o desafio técnico da CATI Jr., empresa júnior do curso de Ciência da Computação da UFSCAR (Universidade Federal de São Carlos).

Neste desafio, foram disponibilizados dois datasets (um de treino e um de teste) com informações detalhadas de inúmeras casas. O objetivo principal é analisar os fatores que exercem maior influência sobre o preço dos imóveis. Para isso, a análise foi conduzida em etapas, detalhadas a seguir.

## Etapa 1: Conhecendo o Dataset

O primeiro passo foi identificar as informações contidas no dataset, verificando as colunas e os valores disponíveis. Como não havia familiaridade com todas as regras de negócio e termos específicos, utilizei o Gemini para obter a descrição e o significado de cada coluna.

Para melhor compreensão e tratamento, os dois datasets foram unificados utilizando o código:
Python

```python
df_casas = pd.concat([train, test])
```

Em seguida, analisei a quantidade de registros, o tipo dos valores, a presença de dados nulos e informações estatísticas (como média, moda, mediana, quartis e desvio padrão) das colunas, utilizando:

```python
df_casas.info()
df_casas.describe()
```

## Etapa 2: Tratamento e Visualização de Dados

Primeiramente, para preparar o dataset, excluí algumas colunas com informações muito específicas (como 'Alley', que se refere ao tipo de entrada do beco, ou 'RoofMatl', tipo do telhado) que não agregariam à análise principal. Para isso, utilizei:

```python
df_casas_limpa = df_casas.drop()
```

Após isso, para uma melhor visualização, traduzi os nomes das colunas remanescentes e seus respectivos valores categóricos utilizando:
Python

```python
df_casas_traduzido = df_casas_limpa.rename('colunas')
df_casas_traduzido['coluna'].replace(mapa_substituicao)
```

Também gerei gráficos para identificar outliers no dataset. O histograma e o boxplot iniciais revelaram uma assimetria positiva acentuada na distribuição de preços, indicando a presença de muitos pontos discrepantes.

<div align='center'> <img width="520" height="455" alt="Histograma de preço original" src="https://github.com/user-attachments/assets/55e268ec-f330-4f43-abc6-72fe550fefe6" />  <img width="520" height="455" alt="Boxplot de preço original" src="https://github.com/user-attachments/assets/372fe2bb-36d0-4e46-a66b-09fb3f2bb98e" /> </div>

Para tratar essa questão, utilizei o Intervalo Interquartil (IQR) e removi os valores que estavam fora dos limites estabelecidos, uma vez que representavam uma pequena parcela dos dados:
Python

```python
Q1 = df_casas_com_preco['PrecoVenda'].quantile(0.25)
Q3 = df_casas_com_preco['PrecoVenda'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df_casas_final = df_casas_com_preco[(df_casas_com_preco['PrecoVenda'] >= limite_inferior) & (df_casas_com_preco['PrecoVenda'] <= limite_superior)]
```

Com o tratamento aplicado, a distribuição do preço se tornou mais próxima da normalidade, conforme as imagens a seguir:

<img width="520" height="455" alt="Histograma de preço após IQR" src="https://github.com/user-attachments/assets/43c68551-68d4-4e3a-a237-ebde87a3af95" /> <img width="520" height="455" alt="Boxplot de preço após IQR" src="https://github.com/user-attachments/assets/80b03713-a84f-46aa-b6bb-e670c7d6ee8a" />

## Etapa 3: Gráficos e Dashboard

Nesta etapa, gerei gráficos para visualizar e comprovar relações que influenciam o Preço de Venda dos imóveis e desenvolvi um dashboard para demonstrar essas visualizações, seguindo esta estrutura:

1. Informações Gerais sobre o Preço de Venda

Na parte inicial, inseri as métricas principais do preço das casas, como média, preço mínimo, preço máximo e desvio padrão, além dos gráficos de distribuição (histograma e boxplot) pós-tratamento.

2. Informações sobre a Vizinhança

Busquei relacionar a influência do bairro no valor dos imóveis, utilizando três gráficos:

- <b>Distribuição de Preços por Vizinhança</b>: Gráfico de Barras comparando os bairros com base na média dos preços entre eles. 

<img width="624" height="455" alt="Gráfico de Barras: Preço médio por Vizinhança" src="https://github.com/user-attachments/assets/a7f79fa8-cf9c-46e6-b24b-14945cd5c119" />

- <b>Distribuição de Qualidade por Vizinhança</b>: Gráfico de Barras comparando os bairros com base na média de qualidade entre eles.

<img width="624" height="455" alt="Gráfico de Barras: Qualidade média por Vizinhança" src="https://github.com/user-attachments/assets/a626621a-3893-4f09-bbd9-d46dab0c7fa7" />

- <b>Distribuição de Preço por Zoneamento</b>: Gráfico de Barras comparando o Zoneamento pela média dos preços entre eles.

<img width="757" height="455" alt="Gráfico de Barras: Preço médio por Zoneamento" src="https://github.com/user-attachments/assets/0287d41e-47d5-42f1-b572-6ba394d85bbb" />

Esses dados confirmam que o bairro e o zoneamento influenciam o Preço de Venda das casas. No entanto, o bairro com o maior preço médio não é, necessariamente, o que apresenta a melhor média de qualidade, como visto no gráfico de qualidade.

3. Relação entre Idade e Preço

Busquei relacionar o preço com a idade da casa, focando nos anos de construção e reforma. Para isso utilizei dois gráficos de dispersão:

- <b>Distribuição de Ano de Construção e Preço</b>: Gráfico de Dispersão que correlaciona o ano de construção das casas e o preço.

<img width="597" height="455" alt="Gráfico de Dispersão: Ano de Construção vs Preço" src="https://github.com/user-attachments/assets/c3258503-7d5f-4af0-bb7f-853c85fccfdc" />

- <b>Distribuição de Ano de Reforma e Preço</b>: Gráfico de Dispersão que correlaciona o ano de reforma das casas e o preço.

<img width="597" height="455" alt="Gráfico de Dispersão: Ano de Reforma vs Preço" src="https://github.com/user-attachments/assets/d91e6054-c06d-408e-9122-256ae7865f83" />

# Conclusão

Esta análise exploratória, desenvolvida para o desafio da CATI Jr., alcançou seu objetivo principal ao identificar os fatores que exercem maior influência sobre o Preço de Venda dos imóveis. A análise confirmou que o preço é um resultado da interação de múltiplos fatores, com destaque para a localização e o estado de conservação/idade da propriedade.

Os principais drivers de preço identificados, e que mais chamaram a atenção neste estudo, são:

- <b>Localização e Zoneamento</b>: O impacto da Vizinhança e do Zoneamento no valor de venda foi claramente evidenciado. No entanto, observou-se que a vizinhança com o maior preço médio nem sempre corresponde àquela com a melhor média de qualidade geral. Isso sugere que a valorização do bairro pode ser impulsionada tanto pela qualidade das construções quanto por fatores macroeconômicos e de infraestrutura local.

- <b>A Idade da Construção e a Reforma</b>: A comparação entre o ano de construção e o ano de reforma revelou um insight importante: casas recém-reformadas tendem a apresentar um Preço de Venda maior do que aquelas simplesmente mais novas. Isso demonstra que os compradores estão dispostos a pagar um prêmio pela modernização e pela redução de manutenções futuras.

É importante ressaltar que diversos outros fatores presentes no dataset como a Área Habitável, o número de Cômodos e a Área Total do Porão também desempenham papéis cruciais na determinação do preço final. No entanto, as relações envolvendo Vizinhança/Qualidade e Ano de Construção/Reforma foram as que mais se destacaram nesta análise exploratória, fornecendo bases sólidas para a próxima etapa, que é a construção do modelo preditivo.

Este dashboard serve, portanto, como uma fonte de inteligência de mercado inicial, validando as regras de negócio implícitas nos dados e preparando o caminho para uma modelagem de Machine Learning mais precisa e informada.
