from file_search import FileSweeper

def main():
    f = FileSweeper("/users/samuelzurowski/Desktop", "extensions.json")
    f.search_file_tree()
    total = f.get_tree_size(f.getRoot())

    print("TOTAL: ", total)

if __name__ == "__main__":
    main()