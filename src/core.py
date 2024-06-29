def main(query):
    print(f"Query: {query}")
    print("core.py finished")

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "")
