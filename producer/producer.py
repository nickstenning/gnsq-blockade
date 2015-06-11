import sys

import gnsq


def main():
    client = gnsq.Nsqd('nsqd', http_port='4151')
    while 1:
        try:
            client.publish('test', '.')
            sys.stdout.write('.')
            sys.stdout.flush()
        except KeyboardInterrupt:
            print ""
            break


if __name__ == '__main__':
    main()
