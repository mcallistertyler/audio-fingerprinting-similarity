import argparse
import acoustid
import chromaprint
from fuzzywuzzy import fuzz

def calculate_fingerprints(filename):
   print('calculate fingerprints of audio file') 
   duration, fp_encoded = acoustid.fingerprint_file(filename)
   fingerprint, version = chromaprint.decode_fingerprint(fp_encoded)
   return fingerprint

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source")
    parser.add_argument("-t", "--target")
    args = parser.parse_args()

    source_file = args.source if args.source else None
    target_file = args.target if args.target else None

    if not source_file or not target_file:
        raise Exception("Source or target files not provided.")

    return source_file, target_file

if __name__ == "__main__":
    source_file, target_file = main()
    print('Calculating fingerprint of source file')
    source_fingerprint = calculate_fingerprints(source_file)
    print('Calculating fingerprint of target file')
    target_fingerprint = calculate_fingerprints(target_file)
    similarity = fuzz.ratio(source_fingerprint, target_fingerprint)
    print('Similarity', similarity)
