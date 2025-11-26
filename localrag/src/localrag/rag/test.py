from rag import invoke_agent

def main():
    print(invoke_agent("What is the purpose of this project?", "rag/milvus/milvus_rag.db", "rag/database/database.db"))

if __name__ == "__main__":
    main()
