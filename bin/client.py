from lib.fileparser import file_parser_func
from lib.preprocess import preprocess_func
from utils.augment import argu_func
from utils.logger import logg_func

if __name__ == "__main__":
    file_parser_func()
    preprocess_func()
    argu_func()
    logg_func()