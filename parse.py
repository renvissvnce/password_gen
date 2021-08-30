# Here you should write path where python3 is placed (you can find directory by using 'which python3') just copy path and paste here. String should starts with #!.
import string
import random
import argparse

# This function is generating password.
def ppg(name, length):
    letters = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(letters) for i in range(length))
    arr_answer = (
            ('User: {}, get generated password with length: {}. '.format(name, length))
            + "Password is:" + result)
    return arr_answer


#No need to use this values, but we'll save it for a while
#name = str(input("Write username account: "))
#length = int(input("Choose generating password length: "))


# Second function was created with argparse module. We used it for execute from command line.
def main():
    parser = argparse.ArgumentParser(description='Python password generate')
    parser.add_argument('--name', '-n', type=str, help='Line for input username')
    parser.add_argument('--length', '-l', type=int, help='Line for input password length')
    args = parser.parse_args()
    account = ppg(name=args.name, length=args.length)
    print(account)


if __name__ == "__main__":
    main()