from django.shortcuts import render

from django.views.generic import View

from .models import Component, Ingredient, Recipe

from django.shortcuts import HttpResponse
from django.http import JsonResponse
import json

from collections import Counter

import logging

logger = logging.getLogger(__name__)


class Home(View):
    def get(self, request):
        all_ingredient = Ingredient.objects.all()
        context = {
            'all_ingredient': all_ingredient,
        }
        return render(request, 'app/index.html', context=context)

def search(request):
    all_ingredient = Ingredient.objects.all()
    all_recipe = Recipe.objects.all()
    all_component = Component.objects.all()

    data = {'recipes':[]}
    for recipe in all_recipe:
        data['recipes'].append(
                {
                    'name':recipe.name,
                    'components': [{'item': i.ingredient.name, 'q': i.dosage,} for i in recipe.component.all()]
                }
            )
    logger.error(data)

    data_string = request.GET.get('selected')
    data_json = json.loads(data_string)

    helper = Helper(list_keys=data_json['name'], list_values=data_json['value'], data=data)

    return JsonResponse(helper.list_recipes)

class Helper:
    def __init__(self, list_keys=[], list_values=[], data = {}):
        self.list_recipes = Counter()
        self.list_keys = list_keys
        self.list_values = list_values
        self.data = data

        self.dict_ = {i:j for i, j in zip(self.list_keys, self.list_values)}

        self.search_ric(ing = self.dict_)

    def search_ric(self, ing = {}):
        for i in self.data['recipes']:
            list_item = {}
            for j in i['components']:
                list_item[j['item']] = j['q']
            if set(ing.keys())>=set(list_item.keys()):
                self.list_values = [ing[key]-list_item.get(key, 0) for key in ing.keys()]
                if min(self.list_values) >= 0:
                    self.list_recipes[i['name']] += 1
                    ing = {i:j for i, j in zip(self.list_keys, self.list_values)}
                else:
                    continue
        if min(self.list_values) < 0 or len(self.list_recipes) < 1:
            return 0
        else:
            dict_ = {i:j for i, j in zip(self.list_keys, self.list_values)}
            return self.search_ric(ing = dict_)


