from file_search import FileSweeper

def main():
    f = FileSweeper("/users/samuelzurowski/Desktop", "extensions.json")
    f.search_file_tree()

if __name__ == "__main__":
    main()