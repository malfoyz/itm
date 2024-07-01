


def main():
    d = {'website': 'google'}
    try:
        data = d['url']
    except:
        data = 'https://'
    print(data)



if __name__ == '__main__':
    main()