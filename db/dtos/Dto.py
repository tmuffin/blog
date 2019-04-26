#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    Dto 基类
    @author Philip
'''
from django.core.paginator import Paginator

class Dto:
    def __init__(self, dao):
       self.dao = dao

    # 查询
    def query(self, filters, paging):
        try:
            data = self.dao.objects.all().filter(filters)
            pager = Paginator(data, paging.pageSize)

        except Exception as e:
            return False

        return {
            list: pager.page(paging.pageIndex),
            total: pager.count
        }

    # 查询一条数据
    def queryOne(self, filters):
        try:
            data = self.dao.get(filters)
        except Exception as e:
            return False

        return data

    # 创建
    def create(self, data):
        try:
            instance = self.dao.objects.create(data)
        except Exception as e:
            return False

        return True

    # 删除
    def delete(self, ids):
        try:
            for _id in ids:
                self.dao.objects.filter(id = _id).delete()
        except Exception as e:
            return False

        return True

    # 删除一条数据
    def deleteOne(self, _id):
        try:
            self.dao.objects.filter(id = _id).delete()
        except Exception as e:
            return False

        return True

    # 更新一条数据
    def update(self, _id, data):
        try: 
            self.dao.objects.filter(id = _id).update(data)
        except Exception as e:
            return False

        return True