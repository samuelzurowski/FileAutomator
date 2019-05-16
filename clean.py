from file_search import FileSweeper, message
import sys
import os

def main():
    if len(sys.argv) == 3:
        f = FileSweeper(sys.argv[1], sys.argv[2])
        f.search_file_tree()
        total = f.get_tree_size(f.getRoot())

        print("TOTAL: ", total)
    elif len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            while 1:
                choice = input("Are you sure you want to do this? [y/n]: ")
                choice = choice.lower()
                if choice == 'y': break
                elif choice == 'n': 
                    print("Aborting process.")
                    exit(0) 
        try:
            for file in os.listdir(sys.argv[1]):
                os.remove(sys.argv[1] + '/' + file)
                print(file)
        except PermissionError:
            print("You do not have permissions to do this file modify permissions to be able to.")
            exit(0)
        else:
            print("{} is not a directory".format(sys.argv[1]))

    else:
        print(message)

if __name__ == "__main__":
    main()