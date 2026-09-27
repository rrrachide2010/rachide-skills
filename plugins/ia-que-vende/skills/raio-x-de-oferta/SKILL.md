---
name: raio-x-de-oferta
description: Audita uma página de vendas, landing page, oferta ou link-in-bio e devolve nota de 0 a 10 em seis critérios (clareza, dor, prova, oferta, objeções e CTA), os três maiores vazamentos de conversão e a headline reescrita. Use sempre que o usuário colar uma URL ou o texto de uma página e perguntar "o que acha", "por que não converte", "revisa minha página", "avalia minha oferta", ou pedir feedback de landing page, VSL, página de captura ou anúncio.
---

# Raio-X de Oferta

Diagnóstico de página de vendas em formato de nota, com correções concretas. O objetivo não é elogiar nem destruir: é dizer exatamente onde a página perde a venda e o que colocar no lugar.

Fale no idioma do usuário. Seja direto. Nota alta sem justificativa e nota baixa sem correção são igualmente inúteis.

## Passo 1: Obter a página

- Se veio URL, busque o conteúdo (WebFetch ou ferramenta equivalente). Se a página for renderizada em JavaScript e voltar vazia, peça ao usuário para colar o texto ou enviar prints.
- Se veio texto, use o texto.
- Se for link-in-bio, avalie a página como funil (ordem dos links, oferta principal, captura), não como página de vendas.

Identifique antes de avaliar: qual é o produto, o preço (se aparece), para quem é e qual ação a página pede. Se não conseguir responder essas quatro coisas em 20 segundos de leitura, a nota de clareza já está definida.

## Passo 2: Avaliar nos 6 critérios

Leia `references/criterios.md` para as réguas de nota. Resumo:

| Critério | Pergunta que decide |
|---|---|
| Clareza | Em 5 segundos, um estranho entende o que é, para quem é e o que ganha? |
| Dor | A página fala do problema nas palavras do cliente ou em jargão do vendedor? |
| Prova | Existe prova concreta (números, depoimentos com nome, demonstração) e ela aparece antes do preço? |
| Oferta | O que está incluso é específico? Há garantia, bônus com valor e uma razão para agir agora que seja verdadeira? |
| Objeções | A página responde "é pra mim?", "vai dar certo?", "e se eu não conseguir?", "por que esse preço?" |
| CTA | O botão diz o que acontece depois do clique? Aparece mais de uma vez? Está visível no mobile? |

Dê a nota de 0 a 10 por critério com uma frase de justificativa citando o trecho da página. Nota geral é a média, mas destaque qual critério puxa para baixo.

## Passo 3: Os 3 vazamentos

Escolha os três pontos onde mais dinheiro escapa, em ordem de impacto. Para cada um:
- **Onde:** o trecho ou a seção
- **Por que perde:** o que o visitante pensa ali
- **Correção:** o texto ou a mudança específica, pronta para colar

Não liste 15 problemas. Três bem resolvidos mudam a conversão; quinze paralisam o usuário.

## Passo 4: Headline reescrita

Entregue 3 opções de headline, cada uma com uma abordagem (resultado concreto, dor + mecanismo, prova). Sem travessão, sem "revolucionário", sem promessa que a página não sustenta. Marque a sua favorita e diga por quê em uma linha.

## Formato de saída

```
# Raio-X: [nome do produto]

Produto: ... | Preço: ... | Para quem: ... | Ação pedida: ...

## Notas
Clareza 6/10: "..."
Dor 4/10: "..."
Prova 8/10: "..."
Oferta 5/10: "..."
Objeções 3/10: "..."
CTA 7/10: "..."
Geral: 5,5. O que mais derruba: objeções.

## Os 3 vazamentos
1. ...
2. ...
3. ...

## Headline
A) ...
B) ... (favorita: ...)
C) ...

## Próximo passo
Uma ação para fazer hoje.
```

## Cuidados

- Se a página promete cura, resultado financeiro garantido ou usa antes e depois de saúde, avise que isso reprova em anúncio e pode ter implicação legal, independentemente da nota.
- Se o usuário é dono da página e a nota é baixa, o tom é de mecânico, não de crítico: "isso aqui está vazando, troca por isso".
