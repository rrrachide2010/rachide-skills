---
name: espiao-de-concorrente
description: Mapeia o funil de um concorrente a partir do link-in-bio, site, landing page ou perfil: escada de ofertas (grátis, low ticket, principal, serviço), mecânica de captura, promessa, posicionamento, e devolve o que copiar e onde ele perde dinheiro. Use sempre que o usuário colar o link de um concorrente, perguntar "como esse cara vende", "analisa esse perfil", "o que esse concorrente faz", pedir benchmark, análise de concorrência ou engenharia reversa de funil.
---

# Espião de Concorrente

Engenharia reversa de funil. Você recebe uma porta de entrada (link-in-bio, site, perfil) e devolve o mapa completo do que a pessoa vende, em que ordem, e por onde o dinheiro entra e escapa.

Fale no idioma do usuário. A saída deve ser acionável: "copie isso, evite aquilo, sua vantagem é essa".

## Passo 1: Coletar

1. Busque a URL recebida. Se a URL tiver parâmetros longos (`utm_`, `fbclid`), remova tudo depois do `?` antes de buscar.
2. Se a página for um link-in-bio, extraia todos os links e visite os que forem do próprio concorrente (página de produto, lista de espera, formulário, PDF, checkout). Páginas de checkout externas (Hotmart, Kiwify, Eduzz) às vezes mostram o preço.
3. Se a busca direta falhar, use o script `scripts/fetch_page.py <url>` que limpa parâmetros, segue redirecionamentos e extrai texto e links. Se ainda assim falhar (página em JavaScript), peça prints ao usuário.
4. Anote também o que é PDF ou repositório público: baixe e leia. Iscas gratuitas revelam a qualidade real do trabalho.

Nunca invente o que não conseguiu ver. Diga "não consegui acessar X" e siga com o que tem.

## Passo 2: Mapear a escada de ofertas

Classifique cada coisa encontrada em um degrau:

| Degrau | O que é | O que observar |
|---|---|---|
| Isca | Grátis (PDF, skill, aula, ferramenta) | Exige captura de contato? Se o link é aberto, ele perde o lead. |
| Low ticket | R$ 27 a 197 | É produto ou é "guia de instalação" de algo gratuito? Tem preço visível? |
| Principal | Curso, mentoria, software | Está pronto ou é lista de espera? Tem prova? |
| Serviço | Consultoria, implementação, agência | Qual a porta de entrada (formulário, diagnóstico, call)? Qualifica orçamento? |
| Comunidade / recorrência | Assinatura, grupo | Existe? |

Degraus vazios são tão informativos quanto os cheios.

## Passo 3: Diagnosticar

Responda, com evidência:

- **Posicionamento:** em uma frase, o que ele promete e contra o que se posiciona.
- **Público real vs público declarado:** a isca atrai quem? Esse alguém compra o produto principal? (Uma isca para desempregados não alimenta uma consultoria B2B.)
- **Barreira de entrada:** o que o público precisa ter ou saber para consumir o produto (ferramenta paga, conhecimento técnico).
- **Captura:** onde ele coleta contato e onde deixa de coletar.
- **Prioridade da página:** o que está no topo é o que fatura ou o que ainda não existe?
- **Prova:** números, depoimentos, demonstração. Ou ausência.
- **Sinais de amadorismo:** domínios inconsistentes, links quebrados, PDF gerado por script sem design, promessas incoerentes.
- **Fosso:** o que dele é difícil de copiar (audiência, marca, tecnologia) e o que é trivial (um prompt, um guia).

## Passo 4: Entregar

```
# Espião: [nome / marca]

## Em uma frase
O que ele vende, para quem, com que promessa.

## Escada de ofertas
Isca: ...
Low ticket: ...
Principal: ...
Serviço: ...
(degraus vazios marcados)

## O que ele faz bem (copiar)
3 itens, com o porquê.

## Onde ele perde dinheiro
3 a 5 itens, com evidência.

## Sua vantagem
O que o usuário tem ou pode fazer que o concorrente não consegue. Se o usuário não deu contexto sobre o próprio negócio, pergunte antes desta seção.

## Próximo passo
Uma ação concreta para esta semana.
```

## Ética

Só analise o que é público. Não tente acessar áreas logadas, não simule compra, não colete dados pessoais de clientes do concorrente. O objetivo é aprender com o funil, não prejudicar a pessoa.
