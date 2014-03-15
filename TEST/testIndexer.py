#!/usr/bin/env python

import indexer
import os

refDir = os.getcwd()
testDir = os.path.join(refDir, 'testDir')

testedIndex = indexer.getIndex(testDir, refDir)
indexer.printIndex(testedIndex)
