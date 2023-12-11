import pickle
import os


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
  
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def find(self, key):
        return self._find_recursive(self.root, key)

    def _find_recursive(self, node, key):
        if node is None or node.key == key:
            return node.key if node else None
        if key < node.key:
            return self._find_recursive(node.left, key)
        else:
            return self._find_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_minimum(node.right)
            node.key = min_node.key
            node.right = self._delete_recursive(node.right, min_node.key)
        return node

    def _find_minimum(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def print_tree(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node:
            self._print_inorder(node.left)
            print(node.key, end=' ')
            self._print_inorder(node.right)

    def clear_tree(self):
        self.root = None

    def dump_tree(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.root, file)

    def load_tree(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'rb') as file:
                try:
                    self.root = pickle.load(file)
                except (pickle.UnpicklingError, EOFError):
                    print(f"Invalid backup file: {filename}")
        else:
            print(f"Backup file not found: {filename}")


def main():
    backup_filename = 'tree_backup.pickle'
    tree = BinarySearchTree()
    tree.load_tree(backup_filename)

    while True:
        command = input('Enter a command (add X, find X, delete X, print, clear, dump, exit): ')
        if command.startswith('add'):
            value = int(command.split()[1])
            tree.insert(value)
        elif command.startswith('find'):
            value = int(command.split()[1])
            result = tree.find(value)
            if result:
                print(f"Value {value} found in the tree.")
            else:
                print(f"Value {value} not found in the tree.")
        elif command.startswith('delete'):
            value = int(command.split()[1])
            tree.delete(value)
        elif command == 'print':
            tree.print_tree()
            print()
        elif command == 'clear':
            tree.clear_tree()
        elif command == 'dump':
            tree.dump_tree(backup_filename)
        elif command == 'exit':
            break
        else:
            print("Invalid command.")

    tree.dump_tree(backup_filename)


if __name__ == '__main__':
    main()
