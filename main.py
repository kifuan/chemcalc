import sys
import traceback
import parse


if __name__ == '__main__':
    while True:
        code = input('> ').strip()
        if code in ('exit', 'quit'):
            break
        if code == '':
            continue
        # noinspection PyBroadException
        try:
            print(parse.parse(code))
        except KeyboardInterrupt:
            break
        except Exception:
            # To make console happy.
            traceback.print_exc(file=sys.stdout)
