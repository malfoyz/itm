


def main():
    d = {'website': 'google', 'url': 'google.ru'}
    try:
        data = d['url']
    except:
        data = 'https://'
    else:
        data = data.upper()
    print(data)


if __name__ == '__main__':
    main()