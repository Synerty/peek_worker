import logging
import shutil
import unittest

import os

import peek_platform

peek_platform.PeekPlatformConfig.componentName = "unit_test"

from peek_worker.PeekWorkerConfig import PeekWorkerConfig

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)



class PeekWorkerConfigTest(unittest.TestCase):
    COMPONENT_NAME = "unit_test"
    HOME_DIR = os.path.expanduser('~/%s.home' % COMPONENT_NAME)
    CONFIG_FILE_PATH = os.path.join(HOME_DIR, 'config.json')

    def _rmHome(self):
        if os.path.exists(self.HOME_DIR):
            shutil.rmtree(self.HOME_DIR)

    def setUp(self):
        PeekWorkerConfig._PeekFileConfigBase__instance = None
        self._rmHome()
        os.makedirs(self.HOME_DIR, PeekWorkerConfig.DEFAULT_DIR_CHMOD)

        with open(self.CONFIG_FILE_PATH, 'w') as fobj:
            fobj.write('{"nothing":{"is_true":true}}')

    def tearDown(self):
        self._rmHome()

    def testPlatformDetails(self):
        bas = PeekWorkerConfig()

        # Defaults
        logger.info('platformVersion = %s', bas.platformVersion)
        bas.platformVersion = '4.4.4'

        PeekWorkerConfig._PeekFileConfigBase__instance = None

        logger.info('platformVersion = %s', bas.platformVersion)
        self.assertEqual(bas.platformVersion, '4.4.4')
