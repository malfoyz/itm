


def main():
    d = {'website': 'google'}
    try:
        print(asdf)
        data = d['url']
    except KeyError:
        data = 'https://'
    except:                   # обрабатывает вообще все исключения, в т.ч. прерывание с помощью CTRL + C, CTRL + V (KeyboardInterrupt)
        print('ooops')        # к примеру, в бесконечном цикле прерывание будет перехватываться этим except



if __name__ == '__main__':
    main()