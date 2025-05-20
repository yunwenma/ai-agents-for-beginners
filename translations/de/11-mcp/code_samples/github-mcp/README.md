<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "393eea8000f305b94010dd5b380902d8",
  "translation_date": "2025-05-20T10:02:45+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "de"
}
-->
# Github MCP Server Beispiel

## Beschreibung

Dies ist eine Demo, die für den AI Agents Hackathon erstellt wurde, der im Microsoft Reactor stattfand.

Das Tool wird verwendet, um Hackathon-Projekte basierend auf den Github-Repositories eines Nutzers zu empfehlen.  
Dies geschieht durch:

1. **Github Agent** – Verwendet den Github MCP Server, um Repositories und Informationen über diese Repositories abzurufen.  
2. **Hackathon Agent** – Nutzt die Daten vom Github Agent und entwickelt kreative Hackathon-Projektideen basierend auf den Projekten, den vom Nutzer verwendeten Programmiersprachen und den Projektkategorien des AI Agents Hackathons.  
3. **Events Agent** – Basierend auf den Vorschlägen des Hackathon Agents empfiehlt der Events Agent relevante Veranstaltungen aus der AI Agent Hackathon Reihe.

## Ausführen des Codes

### Umgebungsvariablen

Diese Demo nutzt Azure Open AI Service, Semantic Kernel, den Github MCP Server und Azure AI Search.

Stelle sicher, dass die entsprechenden Umgebungsvariablen korrekt gesetzt sind, um diese Tools zu verwenden:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Starten des Chainlit Servers

Um eine Verbindung zum MCP Server herzustellen, verwendet diese Demo Chainlit als Chat-Oberfläche.

Um den Server zu starten, nutze folgenden Befehl im Terminal:

```bash
chainlit run app.py -w
```

Dadurch sollte dein Chainlit Server unter `localhost:8000` as well as populate your Azure AI Search Index with the `event-descriptions.md` gestartet werden.

## Verbindung zum MCP Server herstellen

Um eine Verbindung zum Github MCP Server herzustellen, klicke auf das „Stecker“-Symbol unterhalb des Chat-Feldes „Type your message here..“:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.dce6ea039fc19641b00370fafc9e68a7ab349ec064fb9170f5555f894376116e.de.png)

Dort kannst du auf „Connect an MCP“ klicken, um den Befehl zum Verbinden mit dem Github MCP Server hinzuzufügen:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Ersetze „[YOUR PERSONAL ACCESS TOKEN]“ durch deinen tatsächlichen Personal Access Token.

Nach der Verbindung sollte neben dem Stecker-Symbol eine (1) erscheinen, die bestätigt, dass die Verbindung steht. Falls nicht, versuche den Chainlit Server mit `chainlit run app.py -w` neu zu starten.

## Nutzung der Demo

Um den Agenten-Workflow zum Empfehlen von Hackathon-Projekten zu starten, kannst du eine Nachricht wie diese eingeben:

„Recommend hackathon projects for the Github user koreyspace“

**Derzeit ist der Workflow so programmiert, dass er die Wörter „reccomend“ und „github“ erkennt, um zu starten. Später wird dies von einem Router Agent übernommen.**

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.