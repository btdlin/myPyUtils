import os
import random
import string
import time
import logging

import bt_rts.thrift.gen.recs as recs_thrift

from thriftpy.thrift import TClient
from thriftpy.transport import TCyFramedTransportFactory, TSocket
from thriftpy.protocol import TCyBinaryProtocolFactory
from thriftpy.thrift import TException

from .response import Recommendation

LOG = logging.getLogger(__name__)

class RecommendationsClient(object):

    def __init__(self, host='127.0.0.1', port=7070, timeout=3000, calling_app=None, **kwargs):
        self.__host = host
        self.__port = port
        LOG.info('Starting connection to RTS Recommendations on {0}:{1}'.format(host, port))

        self.__timeout = timeout
        if not calling_app:
            raise ValueError('Must supply a calling app string')
        self.__calling_app = calling_app

        self.__create_client()

        self.__open = False
        self.__initialized = True


    def __create_client(self):
        socket = TSocket(self.__host, self.__port, socket_timeout=self.__timeout)
        self.__transport = TCyFramedTransportFactory().get_transport(socket)
        protocol = TCyBinaryProtocolFactory().get_protocol(self.__transport)
        self.__client = TClient(recs_thrift.RecommendationsService, protocol)

    def open(self):
        if self.__transport.is_open():
            return

        self.__transport.open()
        self.__open = True

    def close(self):
        if not self.__transport.is_open():
            return

        self.__transport.close()
        self.__open = False

    def __del__(self):
        try:
            self.__initialized
        except AttributeError:
            return
        else:
            self.close()

    def client(self):
        return self.__client

    def is_open(self):
        return self.__open

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def get_recommendations(self, request):
        request_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        context = recs_thrift.TRequestContext(self.__calling_app, request_id)
        result =  [ Recommendation.from_thrift(rec) for rec in
                    self.__client.get_recommendations(context, request.to_thrift())]

        return result
