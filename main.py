from cardinal import guess_cardinal_num
import argparse


def main(min=0, max=100):
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-c", "--cardinals", action='store_true', help="Exercise cardinal numbers")
    argParser.add_argument("-cs", "--minimal", action='store_true', help="Lowest value")
    argParser.add_argument("-ce", "--maximal", action='store_true', help="Highest value")

    args = argParser.parse_args()

    if args.cardinals is True:
        if args.minimal is True and args.maximal is True:
            guess_cardinal_num(min=args.minimal, max=args.maximal)
        else:
            guess_cardinal_num()
    else:
        print("dupa")


if __name__ == '__main__':
    main()
