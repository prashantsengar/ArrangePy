import argparse
import main
import os
import webapp

parser = argparse.ArgumentParser()

exclusive_group = parser.add_mutually_exclusive_group()

exclusive_group.add_argument(
    "-w", "--weak", action="store_true", required=False, help="Weak arrange"
)
exclusive_group.add_argument(
    "-s", "--strong", action="store_true", required=False, help="Strong arrange"
)
exclusive_group.add_argument(
    "-b", "--web", action="store_true", required=False, help="Run web GUI"
)

parser.add_argument(
    "directory",
    nargs="?",
    help="The directory to arrange, default is current working directory",
)

args = parser.parse_args()

print(args)

target = os.getcwd()

if args.directory:
    target = args.directory
if args.web:
    webapp.main()
elif args.weak:
    main.main(target, choice=main.CHOICES.WEAK)
elif args.strong:
    main.main(target, choice=main.CHOICES.STRONG)
else:
    main.main(target)
