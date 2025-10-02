# test_transactionpool.py
"""
Tests for TransactionPool module.
"""

import unittest
from transactionpool import TransactionPool

class TestTransactionPool(unittest.TestCase):
    """Test cases for TransactionPool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TransactionPool()
        self.assertIsInstance(instance, TransactionPool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TransactionPool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
