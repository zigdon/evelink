import os
import tempfile
import unittest2 as unittest

from evelink.cache.sqlite import SqliteCache

class SqliteCacheTestCase(unittest.TestCase):

    def setUp(self):
        self.cache_dir = tempfile.mkdtemp()
        self.cache_path = os.path.join(self.cache_dir, 'sqlite')
        self.cache = SqliteCache(self.cache_path)

    def tearDown(self):
        self.cache.connection.close()
        os.remove(self.cache_path)
        os.rmdir(self.cache_dir)

    def test_cache(self):
        self.cache.put('foo', 'bar', 3600)
        self.assertEqual(self.cache.get('foo'), 'bar')

    def test_expire(self):
        self.cache.put('baz', 'qux', -1)
        self.assertEqual(self.cache.get('baz'), None)
