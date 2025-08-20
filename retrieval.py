import os
import sqlite3
import logging

from tools import claim_guarantee, customer_order_checking, info_product
from prompt import system_prompt

from langchain.schema import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
                    force=True)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Env Set
LOCAL_BASE_URL = os.getenv('LOCAL_BASE_URL')
DOCKER_BASE_URL = os.getenv('DOCKER_BASE_URL')
API_KEY = os.getenv('API_KEY')
MODEL_NAME = os.getenv('MODEL_NAME')
DB_PATH = os.getenv('DB_PATH')

# Main Class
class Retrieval:
    def __init__(self):
        self.model = ChatOpenAI(model=MODEL_NAME, base_url=DOCKER_BASE_URL, api_key=API_KEY, temperature=0.6)
        self.tools = [claim_guarantee, customer_order_checking, info_product]
    
    def tools_execution(self, response_tools):
        tool_messages = []
        for tool_call in response_tools.tool_calls:
            tool_name = tool_call["name"]
            args = tool_call["args"]

            for tool in self.tools:
                if tool.name == tool_name:
                    tool_result = tool.invoke(args)
                    tool_messages.append(f"{tool.name}:\n{tool_result}\n")
        
        return tool_messages

    def prompt_building(self, question, tools_response, history):
        final_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("human", "Question History: {history}\nUser Question : {question}")
        ])
        final_template = final_template.invoke({"knowledge_base": "\n".join(tools_response), "history": history, "question": question})
        return final_template

    def ask(self, question):
        history = self.get_history()
        logger.debug(f"Question History : {history}")

        response_tools = self.model.bind_tools(self.tools).invoke(question)
        logger.debug(f"Tools Calling Response: {response_tools}")

        if not response_tools.tool_calls:
            return "Maaf, saya tidak menemukan jawaban terhadap pertanyaan ini. Harap hubungan kontak yang tertera XXXX-XXXX-XXXX"

        tools_response = self.tools_execution(response_tools)
        logger.debug(f"Tools Execution Response: {tools_response}")
            
        final_prompt = self.prompt_building(question, tools_response, history)
        logger.debug(f"Final Prompt: {final_prompt}")

        final_response = self.model.invoke(final_prompt)
        logger.debug(f"Final Response: {final_response}")

        final_response_content = final_response.content
        self.save_history(question, final_response_content)

        return final_response_content
    
    def get_history(self):
        rows = []
        try:
            conn = sqlite3.connect(DB_PATH)

            with conn:
                query = """
                SELECT user_prompt FROM conversation ORDER BY created_at DESC LIMIT 5;"""
                cursor = conn.cursor()
                cursor.execute(query)
                rows_tuple = cursor.fetchall()
                rows = [row[0] for row in rows_tuple]

            return rows
        except Exception as e:
            logger.exception(f"There is an error while receiving history : {str(e)}")
            return rows

    def save_history(self, question, response):
        try:
            conn = sqlite3.connect(DB_PATH)

            with conn:
                query = "INSERT INTO conversation (user_prompt, system_answer) VALUES (?, ?);"
                cursor = conn.cursor()
                cursor.execute(query, [question, response])
            return "Save Success"
        except Exception as e:
            logger.exception(f"There is an error while saving history : {str(e)}")
            return f"Save Conversation Error with {str(e)} as the error"