# test_cryptoshield.py
"""
Tests for CryptoShield module.
"""

import unittest
from cryptoshield import CryptoShield

class TestCryptoShield(unittest.TestCase):
    """Test cases for CryptoShield class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoShield()
        self.assertIsInstance(instance, CryptoShield)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoShield()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
