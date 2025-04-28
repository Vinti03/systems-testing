import unittest
from tree import Tree
from node import Node

class TestTree(unittest.TestCase):
    
    def setUp(self):
        self.tree = Tree()
        # Create a simple tree structure
        #        5
        #       / \
        #      3   7
        #     / \   \
        #    2   4   8
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(2)
        self.tree.add(4)
        self.tree.add(8)
    
    def test_find_existing_node(self):
        """Test finding an existing node in the tree"""
        node = self.tree._find(3, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 3)
        
        node = self.tree._find(8, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 8)
    
    def test_find_nonexistent_node(self):
        """Test finding a non-existent node in the tree"""
        node = self.tree._find(6, self.tree.getRoot())
        self.assertIsNone(node)
        
        node = self.tree._find(9, self.tree.getRoot())
        self.assertIsNone(node)
    
    def test_find_in_empty_tree(self):
        """Test finding a node in an empty tree"""
        empty_tree = Tree()
        # Can't directly call _find on an empty tree since it expects a node
        # This would normally be handled by the public find method
        # This test is to show we understand the behavior
        self.assertIsNone(empty_tree.find(5))

if __name__ == '__main__':
    unittest.main()