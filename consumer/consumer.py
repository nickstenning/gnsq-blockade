import logging
import sys

import gnsq

logging.basicConfig(format='%(asctime)s %(process)d %(name)s [%(levelname)s] '
                           '%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


def handle_message(reader, message=None):
    if message is None:
        return
    sys.stdout.write(message.body)
    sys.stdout.flush()


def main():
    reader = gnsq.Reader('test', 'testchan', nsqd_tcp_addresses=['nsqd:4150'])
    reader.on_message.connect(handle_message)
    reader.start(block=True)


if __name__ == '__main__':
    main()
