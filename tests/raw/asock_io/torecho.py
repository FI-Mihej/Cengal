import cProfile
import pstats
import os
from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
import socket

# PROFILE_CODE = True
PROFILE_CODE = False


class StreamHandler:
    def __init__(self, stream):
        print('StreamHandler.__init__()')
        self._stream = stream
        stream.set_nodelay(True)
        self._stream.set_close_callback(self._handle_close)
        self._stream.read_until_close(None, self._handle_read)

    def _handle_read(self, data):
        # print('StreamHandler._handle_read()')
        self._stream.write(data)

    def _handle_close(self):
        print('StreamHandler._handle_close()')
        if PROFILE_CODE:
            IOLoop.instance().stop()


class EchoServer(TCPServer):
    def handle_stream(self, stream, address):
        print('EchoServer.handle_stream() from "{}"'.format(address))
        StreamHandler(stream)


def torecho():
    server = EchoServer()
    server.bind(18495, 'localhost', socket.AF_INET)
    # server.bind(18495, '136.243.105.170', socket.AF_INET)
    server.start(1)
    # server.start(10)
    IOLoop.instance().start()
    IOLoop.instance().close()


def profiled__torecho():
    cProfile.run('torecho()',
                 'profiled__torecho.prof')


def print_profiler_result(function_name):
    if function_name.startswith('profiled__'):
        prof_name = function_name + '.prof'
        prof_full_file_name = os.path.join(os.getcwd(), prof_name)
        s = pstats.Stats(prof_full_file_name)
        s = s.strip_dirs()
        s = s.sort_stats('cumtime', 'tottime', 'ncalls')
        # s.print_stats(.4)
        s.print_stats()
        # s.print_callees(['get_set_of_assumed_triangles'])


if __name__ == '__main__':
    if PROFILE_CODE:
        profiled__torecho()
        print_profiler_result(profiled__torecho.__name__)
    else:
        torecho()
