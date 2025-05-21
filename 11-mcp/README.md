# Lesson 11: Model Context Protocol (MCP) Integration

## Learning Objectives
- Understand what MCP is and its role in AI agent development
- Set up and configure an MCP server for GitHub integration
- Build a multi-agent system using MCP tools
- Implement RAG (Retrieval Augmented Generation) with Azure Cognitive Search

## Prerequisites
- Python 3.8+
- Node.js 14+
- Azure subscription
- GitHub account
- Basic understanding of Semantic Kernel

## Setup Instructions

1. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Azure Services**
   - Create an Azure Cognitive Search resource
   - Set up Azure OpenAI service
   - Configure environment variables in `.env`

3. **MCP Server Setup**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Project Structure

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## Core Components

### 1. Multi-Agent System
- GitHub Agent: Repository analysis
- Hackathon Agent: Project recommendations
- Events Agent: Tech event suggestions

### 2. Azure Integration
- Cognitive Search for event indexing
- Azure OpenAI for agent intelligence
- RAG pattern implementation

### 3. MCP Tools
- GitHub repository analysis
- Code inspection
- Metadata extraction

## Code Walkthrough

The sample demonstrates:
1. MCP server integration
2. Multi-agent orchestration
3. Azure Cognitive Search integration
4. RAG pattern implementation

Key features:
- Real-time GitHub repository analysis
- Intelligent project recommendations
- Event matching using Azure Search
- Streaming responses with Chainlit

## Running the Sample

1. Start the MCP server:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Launch the application:
   ```bash
   chainlit run app.py -w
   ```

3. Test the integration:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Troubleshooting

Common issues and solutions:
1. MCP Connection Issues
   - Verify server is running
   - Check port availability
   - Confirm GitHub tokens

2. Azure Search Issues
   - Validate connection strings
   - Check index existence
   - Verify document upload

## Next Steps
- Explore additional MCP tools
- Implement custom agents
- Enhance RAG capabilities
- Add more event sources

## Resources
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)