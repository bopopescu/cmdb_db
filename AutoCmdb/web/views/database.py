#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Author :Yangky
# @TIME : 2019-07-24 20:55

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from web.service import database


class DatabaseListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'database_list.html')


class DatabaseJsonView(View):
    def get(self, request):
        obj = database.Database()
        response = obj.fetch_database(request)
        return JsonResponse(response.__dict__)

    def delete(self, request):
        response = database.Database.delete_database(request)
        return JsonResponse(response.__dict__)

    def put(self, request):
        response = database.Database.put_database(request)
        return JsonResponse(response.__dict__)


class DatabaseDetailView(View):
    def get(self, request, db_name, db_id):
        response = database.Database.database_detail(db_name, db_id)
        return render(request, 'database_detail.html', {'response': response, 'db_name': db_name})


class AddAssetView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_asset.html')