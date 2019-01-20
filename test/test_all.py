import unittest
import logging

# Suppress logging during testing
logging.getLogger().setLevel(logging.CRITICAL)

def load_tests(loader, tests, pattern):
    test_loader = unittest.defaultTestLoader.discover('.', pattern='*ing.py')
    tests.addTests(test_loader)
    return tests

if __name__ == '__main__':
    unittest.main()
