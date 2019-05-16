from file_search import FileSweeper, message
import sys

def main():
    if len(sys.argv) == 3:
        f = FileSweeper(sys.argv[1], sys.argv[2])
        f.search_file_tree()
        total = f.get_tree_size(f.getRoot())

        print("TOTAL: ", total)
    else:
        print(message)

if __name__ == "__main__":
    main()