<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "393eea8000f305b94010dd5b380902d8",
  "translation_date": "2025-05-20T10:02:23+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "pt"
}
-->
# Exemplo de Servidor Github MCP

## Descrição

Esta foi uma demonstração criada para o AI Agents Hackathon realizado pelo Microsoft Reactor.

A ferramenta é usada para recomendar projetos de hackathon com base nos repositórios Github de um usuário.  
Isso é feito por meio de:

1. **Github Agent** - Utiliza o Github MCP Server para recuperar repositórios e informações sobre eles.  
2. **Hackathon Agent** - Recebe os dados do Github Agent e cria ideias criativas de projetos para hackathon com base nos projetos, linguagens usadas pelo usuário e as categorias do AI Agents hackathon.  
3. **Events Agent** - Com base nas sugestões do Hackathon Agent, o Events Agent recomenda eventos relevantes da série AI Agent Hackathon.

## Executando o código

### Variáveis de Ambiente

Esta demonstração usa Azure Open AI Service, Semantic Kernel, o Github MCP Server e Azure AI Search.

Certifique-se de que as variáveis de ambiente corretas estejam configuradas para usar essas ferramentas:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Executando o Chainlit Server

Para se conectar ao MCP server, esta demonstração usa o Chainlit como interface de chat.

Para iniciar o servidor, use o seguinte comando no seu terminal:

```bash
chainlit run app.py -w
```

Isso deve iniciar seu servidor Chainlit em `localhost:8000` as well as populate your Azure AI Search Index with the `event-descriptions.md`.

## Conectando ao MCP Server

Para se conectar ao Github MCP Server, selecione o ícone de "plug" abaixo da caixa de chat "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.dce6ea039fc19641b00370fafc9e68a7ab349ec064fb9170f5555f894376116e.pt.png)

A partir daí, clique em "Connect an MCP" para adicionar o comando que conecta ao Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Substitua "[YOUR PERSONAL ACCESS TOKEN]" pelo seu Token de Acesso Pessoal real.

Após a conexão, você deve ver um (1) ao lado do ícone de plug para confirmar que está conectado. Caso contrário, tente reiniciar o servidor chainlit com `chainlit run app.py -w`.

## Usando a Demonstração

Para iniciar o fluxo do agente que recomenda projetos de hackathon, você pode digitar uma mensagem como:

"Recommend hackathon projects for the Github user koreyspace"

**Atualmente, este fluxo é acionado ao detectar as palavras "reccomend" e "github". Futuramente, isso será feito por um Router Agent.**

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.