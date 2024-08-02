import seutil as su
from jsonargparse import CLI


class SimpleParser:
    def tokenize(self, input: su.arg.RPath): ...

    def extract_methods(self, input: su.arg.RPath): ...


if __name__ == "__main__":
    CLI(SimpleParser, as_positional=False)
