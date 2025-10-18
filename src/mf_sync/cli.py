import argparse
from .sync import run_sync

def make_parser():
    p = argparse.ArgumentParser("mmfarm-ai-sync")
    p.add_argument("--collections", nargs="+", default=["seed-of-hope"])
    p.add_argument("--push", action="store_true", help="commit build/manifests/proofs")
    return p

def main():
    args = make_parser().parse_args()
    run_sync(collections=args.collections, push=args.push)

if __name__ == "__main__":
    main()
