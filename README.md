# Análise completa de influencias no preço de casas
Essa análise e o dashboard foram feitos para um desafio técnico da CATI jr, 
empresa junior do curso ciência da computação da UFSCAR (Universidade Federal de São Carlos).

Nesse desafio, foram disponibilizados dois datasets, um de treino e outro para teste, 
dedicado para o treinamento de um modelo preditivo, 
contendo as informações de inumeras casas, 
e como objetivo principal é analisar quais fatores que influenciam o preço dos imoveis, 
para isso fiz a análise em algumas etapas, que irei apresentar agora.

## Etapa 1: Conhecendo o dataset
O primeiro passo foi indentificar as informações contidas no dataset, 
ver as colunas e os valores que estão contidos nelas,
como eu não conhecia as regras de negócio nem os termos, 
utilizei o Gemini para me explicar o que cada coluna representava,
para melhor compreenção unifiquei os dois datasets utilizando: 

```python
df_casas = pd.concat([train, test])
```

Depois análisei a quantidade de registros, o tipo dos valores, quantidade de valores vazios
e informações estatísticas como por exemplo média, moda, mediana, quartis e desvio padrão
das colunas, utilizando: 
```python
df_casas.info()
df_casas.describe()
```

## Etapa 2: Tratando os dados e vizualização
Primeiramente, para preparar o dataset, exclui algumas colunas de informações muito específicas 
que não complementaria na análise, como por exemplo: 'Alley' que significa tipo de entrada no beco,
ou 'RoofMatl' que é o tipo do telhado. Para isso utilizei:
```python
df_casas_limpa = df_casas.drop()
```

Após isso para uma melhor vizualização traduzi o nome das colunas que restaram 
e os seus valores utilizando: 
```python
df_casas_traduzido = df_casas_limpa.rename('colunas)
df_casas_traduzido['coluna'].replace(mapa_substituicao)
```

Também gerei alguns gráficos para identificar os outliers do nosso dataset,
utilizei um histograma e um boxplot e identifiquei muitos outliers com uma assimetria positiva
no gráfico:

<div aling='center'>
<img width="520" height="455" alt="image" src="https://github.com/user-attachments/assets/55e268ec-f330-4f43-abc6-72fe550fefe6" /> 
<img width="520" height="455" alt="image" src="https://github.com/user-attachments/assets/372fe2bb-36d0-4e46-a66b-09fb3f2bb98e" />
</div>

Para tratar utilizei o intevalo interquartil e removi todos os valores que estavam fora dos limites,
pois eram poucos os valores:

```python
Q1 = df_casas_com_preco['PrecoVenda'].quantile(0.25)
Q3 = df_casas_com_preco['PrecoVenda'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df_casas_final = df_casas_com_preco[(df_casas_com_preco['PrecoVenda'] >= limite_inferior) & (df_casas_com_preco['PrecoVenda'] <= limite_superior)]
```

<img width="520" height="455" alt="image" src="https://github.com/user-attachments/assets/43c68551-68d4-4e3a-a237-ebde87a3af95" />
<img width="520" height="455" alt="image" src="https://github.com/user-attachments/assets/80b03713-a84f-46aa-b6bb-e670c7d6ee8a" />


## Etapa 3: Alguns Gráficos e Dashboard
Nessa etapa gerei alguns gráficos para vizualizar e comprovar algumas relações que fazem sentido
e influenciam no Preço de venda das casa e fiz um dashboard para demonstrar esses graficos com a segute estrutura:

- <b>Informações gerais sobre o Preço Venda</b>:
Na parte inicial, inseri algumas métricas principais do preço das casa com informaçãos como média, menor preço, maior preço e desvio padrão, além dos gráficos mostrados anteriormente do histograma e boxplot

- <b>Informações gerais sobre vizinhança</b>:
Nessa parte busquei relacionar como o bairro afeta o valor das casas, para isso utilizei tres gráficos:

1. Distribuição de Preços por vizinhança: Histograma comparando os bairros se baseando na média dos preços entre eles.
<img width="624" height="455" alt="Sem título" src="https://github.com/user-attachments/assets/a7f79fa8-cf9c-46e6-b24b-14945cd5c119" />

2. Distribuição de Qualidade por vizinhanca: Histograma comparando os bairros se baseando na média da qualidade entre elas.
<img width="624" height="455" alt="Sem título" src="https://github.com/user-attachments/assets/a626621a-3893-4f09-bbd9-d46dab0c7fa7" />


 


