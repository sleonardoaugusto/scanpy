import argparse

from scrapper import run


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--password')
    parser.add_argument('--secret_key', help='OTP secret key')
    parser.add_argument('--secret_answer')

    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    run(
        username=args.username,
        password=args.password,
        secret_key=args.secret_key,
        secret_answer=args.secret_answer,
    )
