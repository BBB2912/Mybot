from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import (
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

class ChatBot:
    def __init__(self):
        # Initialize LLM (Llama-3.3-70B Versatile)
        self.llm = ChatGroq(
            model_name="deepseek-r1-distill-llama-70b",
            groq_api_key=os.getenv("GROQ_API_KEY"),
            temperature=0,
        )
        
        # Load System Prompt from File
        self.system_prompt = self.get_system_prompt("system_prompt.txt")

        # Initialize Memory
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Define Chat Prompt Template with System Message, Memory & User Input
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(self.system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{text}")
        ])

        # Create the Chain (Ensures Context is Maintained)
        self.chain = self.prompt | self.llm | RunnablePassthrough()

    def get_system_prompt(self, file_path):
        """Loads the system prompt from a text file."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read().strip()
        except Exception as e:
            return f"Error loading system prompt: {e}"
    def extract_after_think(self,content):
        """Extracts text after the </think> tag."""
        match = re.search(r"</think>\s*\n*(.*)", content, re.DOTALL)
        return match.group(1).strip() if match else content  # Return extracted text or full content if not found

    def get_response(self, user_input):
        """Gets chatbot response while maintaining conversation context."""
        if user_input:
            response=self.chain.invoke({"text": user_input, "chat_history": self.memory.load_memory_variables({})["chat_history"]})
            response=self.extract_after_think(response.content)
            return response
        return "Enter user input"

if __name__ == "__main__":
    chatbot = ChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "bye"):
            print("Goodbye!")
            break
        else:
            response = chatbot.get_response(user_input)
            print("Mahi:", response)
