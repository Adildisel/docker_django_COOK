from django.test import TestCase

import logging

from . import models

logger = logging.getLogger(__name__)

class TestModel(TestCase):

    def setUp(self):
        logger.error('setUp: Run once for every test method to setup clean data.')
        pass

    def test_ingredient_in_data(self):
        all_ingredient = models.Ingredient.objects.all()
        list_ingredient = ['яйцо', 'огурец', 'мясо', 'картофель', 'рыба',]
        test_index = None
        print(all_ingredient)
        for i in all_ingredient:
            if list_ingredient is i.name:
                test_index = True
            else:
                test_index = False
                break
        self.assertTrue(test_index)

    