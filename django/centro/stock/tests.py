from django.test import TestCase
from items.models import Item
from companies.models import Terminal
from stock.models import Stock, StockLog


class StockTest (TestCase):
    """
    All tests of the Stock model.
    """
    def _sum_stock_log_equals_current_quantity (self, stocked_item, item, store):
        """
        The stock log per item and per bussiness unit should equal the
        current quantity of stocked items in that bussiness unit.
        """
        quantity = 0
        store_terminals = Terminal.objects.filter (store=store)
        all_events = StockLog.objects.filter (item=item).\
                                      filter (terminal__in = store_terminals).\
                                      order_by('date_time')
        for event in all_events:
            quantity += event.quantity

        self.assertTrue (stocked_item.quantity == quantity,
                         "Stocked quantity of item %s should be %s, but %s is annotated." %
                         (item.__unicode__ ( ), quantity, stocked_item.quantity))


    def _log_existance_implies_stock_existance (self, item):
        """
        If the stock log contains entries for an item, the stock
        for this empty should exist.
        """
        if (StockLog.objects.filter (item=item).count ( ) > 0):
            self.assertTrue (Stock.objects.filter (item=item).count ( ) > 0,
                             "There is no stock entry for item %s" %
                             (item.__unicode__ ( )))


    def test_stock_and_log_should_not_be_empty (self):
        """
        If the stock log contains entries, the stock
        should not be empty at all. This should hold for all items.
        """
        all_logged_items = Item.objects.raw ('SELECT item_id AS id \
                                                FROM stock_stocklog \
                                            GROUP BY item_id')
        for item in all_logged_items:
            self._log_existance_implies_stock_existance (item)


    def test_stock_againts_log (self):
        """
        The current quantity of a stocked item must match the
        quantity sum of all events logged for this item.
        """
        for stocked_item in Stock.objects.all ( ):
            self._sum_stock_log_equals_current_quantity (stocked_item,
                                                         stocked_item.item,
                                                         stocked_item.store)


