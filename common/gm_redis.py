# -*- coding: utf-8 -*-
import redis
import json


class RedisDBConfig:
    HOST = '127.0.0.1'
    PORT = 6379
    DBID = 0


class RedisCache(object):
    def __init__(self):
        if not hasattr(RedisCache, 'pool'):
            RedisCache.create_pool()
        self._connection = redis.Redis(connection_pool=RedisCache.pool)

    @staticmethod
    def create_pool():
        RedisCache.pool = redis.ConnectionPool(
            host=RedisDBConfig.HOST,
            port=RedisDBConfig.PORT,
            db=RedisDBConfig.DBID)


MyRedis = RedisCache()


class BackUpDao(object):
    GAMEIDKEY = 'gameId'
    BACKUPKEY = 'backup:{}:{}'
    r = MyRedis

    @classmethod
    def getBackUpKey(cls, typeId, fz=True):
        value = 'fz' if fz else 'online'
        return cls.BACKUPKEY.format(value, typeId)

    @classmethod
    def saveData(cls, gameId, value, typeId, fz=True):
        key = cls.getBackUpKey(typeId, fz)
        return cls.r._connection.hset(key, gameId, json.dumps(value))

    @classmethod
    def getData(cls, gameId, typeId, fz=True):
        key = cls.getBackUpKey(typeId, fz)
        datas = cls.r._connection.hget(key, gameId)
        if datas:
            return eval(datas)
        else:
            return []

    @classmethod
    def getAllDatas(cls, typeId, fz=True):
        key = cls.getBackUpKey(typeId, fz)
        datas = cls.r._connection.hgetall(key)
        print datas
        if datas:
            return datas
        else:
            return {}

    @classmethod
    def saveGameId(cls, gameId, gameName):
        return cls.r._connection.hset(cls.GAMEIDKEY, gameId, gameName)

    @classmethod
    def getGameId(cls, gameId):
        return cls.r._connection.hget(cls.GAMEIDKEY, gameId)

