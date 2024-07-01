


def main():
    d = {'website': 'google'}
    try:
        data = d['url']
    except KeyError:
        data = 'https://'
    print(data)



if __name__ == '__main__':
    main()