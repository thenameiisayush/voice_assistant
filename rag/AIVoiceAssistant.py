from qdrant_client import QdrantClient
from llama_index.llms.ollama import Ollama
from llama_index.core import SimpleDirectoryReader
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import ServiceContext, VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.storage.storage_context import StorageContext

import warnings
warnings.filterwarnings("ignore")

class AIVoiceAssistant:
    def __init__(self):
        self._qdrant_url = "http://localhost:6333"
        self._client = QdrantClient(url=self._qdrant_url, prefer_grpc=False)
        self._llm = Ollama(model="mistral", request_timeout=120.0)
        self._service_context = ServiceContext.from_defaults(llm=self._llm, embed_model="local")
        self._index = None
        self._create_kb()
        self._create_chat_engine()

    def _create_chat_engine(self):
        memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
        self._chat_engine = self._index.as_chat_engine(
            chat_mode="context",
            memory=memory,
            system_prompt=self._prompt,
        )

    def _create_kb(self):
        try:
            reader = SimpleDirectoryReader(
                input_files=[r"D:\voice_assistant_llm-main\voice_assistant_llm-main\rag\restaurant_file.txt"]
            )
            documents = reader.load_data()
            vector_store = QdrantVectorStore(client=self._client, collection_name="kitchen_db")
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            self._index = VectorStoreIndex.from_documents(
                documents, service_context=self._service_context, storage_context=storage_context
            )
            print("Knowledgebase created successfully!")
        except Exception as e:
            print(f"Error while creating knowledgebase: {e}")

    def interact_with_llm(self, customer_query):
        AgentChatResponse = self._chat_engine.chat(customer_query)
        answer = AgentChatResponse.response
        return answer

    @property
    def _prompt(self):
        return """
            You are a professional AI Assistant receptionist working in a top restaurant called Bangalore Kitchen.
            Engage customers with questions such as their name, contact number, and their order. End the conversation with greetings!
            Don't ask all questions at once; keep the conversation engaging by asking one question at a time.
            If you don't know the answer, say you don't know, and keep responses concise, no more than 2 sentences.
            """
