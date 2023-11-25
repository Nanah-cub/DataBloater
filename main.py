import argparse
from DataBloater.DataBloater import DataBloater

parser = argparse.ArgumentParser()
parser.add_argument('--file')
args = parser.parse_args()

DataBloater(args.file)

