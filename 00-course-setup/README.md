# Course Setup

## Introduction

This lesson will cover how to run the code samples of this course.

## Requirements

- A GitHub Account
- Python 3.12+
- Azure Subscription
- Azure AI Foundry Account

## Clone or Fork this Repo

To begin, please clone or fork the GitHub Repository. This will make your own version of the course material so that you can run, test, and tweak the code!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

You should now have your own forked version of this course in the following link:

![Forked Repo](./images/forked-repo.png)

## Retrieve Your GitHub Personal Access Token (PAT)

Currently, this course uses the Github Models Marketplace to offer free access to Large Language Models (LLMs) that will be used to create AI Agents.

To access this service, you will need to create a GitHub Personal Access Token.

This can be done by going to your <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> in your GitHub Account.

Select the `Fine-grained tokens` option on the left side of your screen.

Then select `Generate new token`.

![Generate Token](./images/generate-token.png)

Copy your new token that you have just created. You will now add this to your `.env` file included in this course. 

## Setting Up Your `.env` File for Azure AI Foundry

To create your `.env` file run the following command in your terminal:

```bash
cp .env.example .env
```

This will copy the example file and create a `.env` in your directory, fill in the values for the environment variables.

Here's where you can find each value in Azure AI Foundry, the portal, or other relevant locations.

### GitHub
- `GITHUB_TOKEN` - Create a personal access token in GitHub, then paste it into the `GITHUB_TOKEN=` field in your `.env` file.

### Overview Page (Project)
- `AZURE_SUBSCRIPTION_ID` - Check **Project details** on the **Overview** page of your project.
- `AZURE_AI_PROJECT_NAME` - Look at the top of the **Overview** page for your project.
- `AZURE_OPENAI_SERVICE` - Find this in the **Included capabilities** tab for **Azure OpenAI Service** on the **Overview** page.
- `PROJECT_CONNECTION_STRING` - On the **Overview** page, go to **Project details** connection and copy the **Project connection string**. Please assert that the string starts with **https://** and has four parts separated with **;** (semicolon). Currently in Azure AI Foundry the string is missing the leading **https://**  

### Management Center
- `AZURE_OPENAI_RESOURCE_GROUP` - Go to **Project properties** on the **Overview** page of the **Management Center**.
- `GLOBAL_LLM_SERVICE` - Under **Connected resources**, find the **Azure AI Services** connection name. If not listed, check the **Azure portal** under your resource group for the AI Services resource name.

### Models + Endpoints Page
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Select your embedding model (e.g., `text-embedding-ada-002`) and note the **Deployment name** from the model details.
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Select your chat model (e.g., `gpt-4o-mini`) and note the **Deployment name** from the model details.

### Azure Portal
- `AZURE_OPENAI_ENDPOINT` - Look for **Azure AI services**, click on it, then go to **Resource Management**, **Keys and Endpoint**, scroll down to the "Azure OpenAI endpoints", and copy the one that says "Language APIs".
- `AZURE_OPENAI_API_KEY` - From the same screen, copy KEY 1 or KEY 2.
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Find your **Azure AI Search** resource, click it, and see **Overview**.
- `AZURE_SEARCH_API_KEY` - Then go to **Settings** and then **Keys** to copy the primary or secondary admin key.


### External Webpage
- `AZURE_OPENAI_API_VERSION` - Visit the [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) page under **Latest GA API release**.

## Install Required Packages

To ensure you have all the required Python packages to run the code, run the following command in your terminal.

We recommend creating a Python virtual environment to avoid any conflicts and issues.

```bash
pip install -r requirements.txt
```

This should install the required Python packages.

# Sign in to Azure

As a security best practice, we'll use [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) to authenticate to Azure OpenAI with Microsoft Entra ID. Before you can do so, you'll first need to install the **Azure CLI** per the [installation instructions](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) for your operating system.

Next, open a terminal and run `az login` to sign in to your Azure account.

## Sign in to Azure

Login with your Azure AI account used to provision the Azure resources.

Open a new terminal and enter the following command and follow the instructions in the terminal:

`az login --use-device-code`

Once you've logged in, select your subscription in the terminal.

## Access the environment variables.

We'll import `os` and `load_dotenv` so that you can access the environment variables.

```python
import os
from dotenv import load_dotenv

load_dotenv()
```

## Setup keyless authentication

Rather than hardcode your credentials, we'll use a keyless connection with Azure OpenAI. To do so, we'll import `DefaultAzureCredential` and later call the `DefaultAzureCredential` function to get the credential.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

You are now ready to run the code of this course, happy learning more about the world of AI Agents!

If you have any issues running this setup, hop into our <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> or <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">create an issue</a>.

## Next Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)
