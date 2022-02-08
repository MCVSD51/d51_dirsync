from ._base import D51_DirSyncTestCase
from . import trees

from d51_dirsync import sync


class ErrorsTests(D51_DirSyncTestCase):

    init_trees = (('src', trees.simple), ('dst', trees.simple))

    def test_nonexistent_src(self):
        with self.assertRaises(ValueError):
            sync('srcc', 'dst', 'sync', create=True)

    def test_nonexistent_dest(self):
        with self.assertRaises(ValueError):
            sync('src', 'dstt', 'sync', create=False)
