from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test store').save_to_db()
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            StoreModel('test store').save_to_db()
            ItemModel('test', 19.99, 1).save_to_db()

            self.assertEqual(ItemModel.query.filter_by(name='test').first().store.name, "test store")

