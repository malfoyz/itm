


def main():
    d = {'website': 'google'}
    try:
        print(asdf)
        data = d['url']
    except KeyError:
        data = 'https://'
    except Exception:      # прерывание (KeyboardInterrupt) здесь уже обарабатываться не будет
        print('ooops')     # в бесконечном цикле прерывание уже не будет перехватываться здесь



if __name__ == '__main__':
    main()