"""
Agentic AI Starter - Multi-Agent System with RAG Integration
Built by Marcus Pollard - U.S. Navy Veteran
"""

import os
from typing import List, Dict
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class ResearchAgent:
    """Agent that conducts research using RAG"""
    
    def __init__(self, documents: List[str] = None):
        self.llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
        self.vectorstore = None
        
        if documents:
            self.setup_vectorstore(documents)
    
    def setup_vectorstore(self, documents: List[str]):
        """Initialize vector store with documents"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.create_documents(documents)
        
        embeddings = OpenAIEmbeddings()
        self.vectorstore = FAISS.from_documents(texts, embeddings)
    
    def search(self, query: str) -> str:
        """Search documents for relevant information"""
        if not self.vectorstore:
            return "No documents loaded. Please provide documents first."
        
        docs = self.vectorstore.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        
        prompt = f"""Based on the following context, answer the question.
        
Context: {context}

Question: {query}

Answer:"""
        
        response = self.llm.invoke(prompt)
        return response.content


class WritingAgent:
    """Agent that formats and writes output"""
    
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    
    def write_report(self, research_data: str, topic: str) -> str:
        """Format research into professional report"""
        prompt = f"""You are a professional technical writer.
        
Take this research data and write a concise, professional summary about: {topic}

Research Data:
{research_data}

Write a clear, structured summary (200-300 words):"""
        
        response = self.llm.invoke(prompt)
        return response.content


class AgenticSystem:
    """Main orchestrator for multi-agent system"""
    
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.writing_agent = WritingAgent()
    
    def run_workflow(self, topic: str, documents: List[str] = None) -> Dict[str, str]:
        """Execute full agentic workflow"""
        
        print(f"\n🔍 Starting research on: {topic}\n")
        
        # Step 1: Setup knowledge base if documents provided
        if documents:
            print("📚 Loading documents into vector store...")
            self.research_agent.setup_vectorstore(documents)
        
        # Step 2: Research
        print("🤖 Research agent gathering information...")
        research_results = self.research_agent.search(topic)
        
        # Step 3: Write formatted output
        print("✍️  Writing agent formatting report...")
        final_report = self.writing_agent.write_report(research_results, topic)
        
        print("\n✅ Workflow complete!\n")
        
        return {
            "topic": topic,
            "research": research_results,
            "report": final_report
        }


def demo():
    """Demo of the agentic system"""
    
    # Sample documents for RAG
    sample_docs = [
        """Agentic AI systems are autonomous agents that can plan, reason, and execute 
        tasks with minimal human intervention. They use techniques like ReAct 
        (Reasoning and Acting) to break down complex problems.""",
        
        """RAG (Retrieval Augmented Generation) combines the power of large language 
        models with external knowledge retrieval. This allows AI to access up-to-date 
        information and cite sources.""",
        
        """Multi-agent systems coordinate multiple specialized agents, each with 
        specific capabilities. This modular approach allows for more sophisticated 
        problem-solving than single-agent systems."""
    ]
    
    # Initialize system
    system = AgenticSystem()
    
    # Run workflow
    results = system.run_workflow(
        topic="What are the key components of modern AI agent systems?",
        documents=sample_docs
    )
    
    # Display results
    print("=" * 60)
    print("FINAL REPORT")
    print("=" * 60)
    print(f"\nTopic: {results['topic']}\n")
    print(results['report'])
    print("\n" + "=" * 60)


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found in environment")
        print("Create a .env file with: OPENAI_API_KEY=your_key_here")
        print("\nRunning in demo mode with placeholder responses...\n")
    
    demo()
