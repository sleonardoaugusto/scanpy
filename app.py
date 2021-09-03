import argparse

from scrapper import run


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--password')
    parser.add_argument('--secret_key', help='OTP secret key')

    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    run(args.username, args.password, args.secret_key)
