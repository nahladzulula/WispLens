# test_wisplens.py
"""
Tests for WispLens module.
"""

import unittest
from wisplens import WispLens

class TestWispLens(unittest.TestCase):
    """Test cases for WispLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WispLens()
        self.assertIsInstance(instance, WispLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WispLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
