


def main():
    d = {'website': 'google'}
    try:
        print(asdf)
        data = d['url']
    except:
        data = 'https://'
        print('Inside except', data)
        return data
    finally:
        print('Very important action')


if __name__ == '__main__':
    result = main()
    print(result)