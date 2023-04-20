def mergeDict(dict1, dict2):
    ##################################################
    # Code your program here
    ##################################################


def printDict(p_dict):

    ##################################################
    # Code your program here
    #########################################
    print('***************')
    for k, v in p_dict.items():
        print(f'{k} : \t {v}')


def main():
    dict1 = {'name': 'KIM', 'ZIP': 94598, 'address': '1234 Grand ave'}
    printDict(dict1)
    dict2 = {'score': [100, 90], 'Grade': 'Senior'}
    printDict(dict2)
    dict3 = mergeDict(dict1, dict2)
    printDict(dict3)


if __name__ == '__main__':
    main()
