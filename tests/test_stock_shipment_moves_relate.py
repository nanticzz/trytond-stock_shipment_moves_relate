# This file is part of the stock_shipment_moves_relate module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockShipmentMovesRelateTestCase(ModuleTestCase):
    'Test Stock Shipment Moves Relate module'
    module = 'stock_shipment_moves_relate'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockShipmentMovesRelateTestCase))
    return suite
