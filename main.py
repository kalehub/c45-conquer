# contekan pemabahasan https://www.ilmuskripsi.com/2016/07/algoritma-c45.html

from c45Class import *
from c45Tree import *

''' for my macOS '''
DATASET_DIR = '/Users/teguhsatya/Dev/c45Go/c45-Dataset.csv'

''' for my linux '''
# DATASET_DIR = '/home/kale/Dev/c45-forsure/c45-Dataset.csv'


def main():
    c45 = C45(DATASET_DIR)
    root = c45.get_root()
    # build root
    c45Root = Tree(root)
    c45Root.print_tree(c45Root.root)


if __name__ == '__main__':
    main()
