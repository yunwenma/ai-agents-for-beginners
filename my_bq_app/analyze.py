# analyze.py (Azure OpenAI version via GitHub Codespaces)
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from rag_utils import retrieve_relevant_chunks
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

load_dotenv()

# Setup Azure OpenAI client using GitHub-provided token
client = AzureOpenAI(
    api_key=os.environ["GITHUB_TOKEN"],
    api_version="2024-02-15-preview",
    azure_endpoint="https://models.inference.ai.azure.com"
)

def build_prompt(role, question, answer, context_chunks):
    context_text = "\n\n".join(context_chunks)
    return f"""
You are an experienced interviewer preparing candidates for the role of {role}.

The candidate is preparing for the following behavioral interview question:
{question}

Here is their answer:
{answer}

You also have access to the following reference materials from a behavioral interview training course:
{context_text}

Please evaluate the response in the following aspects:
0. Ensure the time to tell the whole story is 3-5 mins
1. Does the answer follow the STAR format (Situation, Task, Action, Result)?
2. Does the response demonstrate senior-level behaviors such as:
   - Leadership and initiative
   - Influence across teams or functions
   - Strategic problem-solving
   - Clear and measurable outcomes
3. Is the language clear, concise, and persuasive?
4. Provide constructive feedback on how the answer could be improved
5. Rewrite an improved version of the answer, maintaining the original facts but enhancing structure, clarity, and leadership tone

Please:
1. Provide a brief summary in Chinese to call out the pros and cons;
2. Respond in English with a clear, structured and more detailed feedback.
"""

def analyze_behavior_text(question, answer, role):
    try:
        context_chunks = retrieve_relevant_chunks(question + "\n" + answer)
        prompt = build_prompt(role, question, answer, context_chunks)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior technical interviewer for L5-L6 roles in top tech companies. \
                        You evaluate behavioral interview answers with high expectations around leadership, \
                        cross-functional collaboration, and strategic thinking."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error during analysis: {str(e)}"