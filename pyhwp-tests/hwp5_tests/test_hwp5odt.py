# -*- coding: utf-8 -*-
from unittest import TestCase


class ResourcesTest(TestCase):

    def test_pkg_resources_filename_fallback(self):
        from hwp5.importhelper import pkg_resources_filename_fallback
        fname = pkg_resources_filename_fallback('hwp5', 'xsl/odt/styles.xsl')
        import os.path
        self.assertTrue(os.path.exists(fname))

    def test_hwp5_resources_filename(self):
        from hwp5.utils import hwp5_resources_path
        with hwp5_resources_path('xsl/odt/styles.xsl') as styles_xsl:
            import os.path
            self.assertTrue(os.path.exists(styles_xsl))
