if __name__ == '__main__':
    s = input()
    print(f'{any(char.isalnum() for char in s)}')
    print(f'{any(char.isalpha() for char in s)}')
    print(f'{any(char.isdigit() for char in s)}')
    print(f'{any(char.islower() for char in s)}')
    print(f'{any(char.isupper() for char in s)}')
