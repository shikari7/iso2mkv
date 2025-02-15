#!/bin/python

# convert any ISO or iso in "src" to MKV in "dest"

# Eric D. Hendrickson
# ericdavidhendrickson@gmail.com
# Sat Jan  4 21:27:53 CST 2025

# To Do:

import os
import sys
import subprocess

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) >= 2:
        input_root = sys.argv[1]
        output_root = sys.argv[2]
    makemkvcon = "/usr/local/bin/makemkvcon"
    process_isos(input_root, output_root, makemkvcon)

def process_isos(input_root, output_root, makemkvcon="makemkvcon"):
    """
    Process ISO files in a directory tree with makemkvcon.
    
    Args:
        input_root (str): Root directory containing ISO files.
        output_root (str): Directory where output should be stored.
        makemkvcon_path (str): Path to makemkvcon executable.
    """
    # Ensure the output root exists
    os.makedirs(output_root, exist_ok=True)

    # Traverse the input directory tree
    for root, _, files in os.walk(input_root):
        for file in files:
            if file.lower().endswith(".iso"):
                iso_path = os.path.join(root, file)
                # Create an output directory named after the ISO file (without extension)
                iso_name = os.path.splitext(file)[0]
                output_dir = os.path.join(output_root, iso_name)
                # Skip processing if the output directory already exists
                if os.path.exists(output_dir):
#                   print(f"Skipping {iso_path} - output directory already exists.")
                    continue
                os.makedirs(output_dir, exist_ok=True)

                print(f"Processing {iso_path} into {output_dir}...")

                # Run makemkvcon command
                try:
                    subprocess.run(
                        [
                            makemkvcon,
                            "mkv",
                            "iso:" + iso_path,
                            output_dir
                        ],
                        check=True
                    )
                    print(f"Successfully processed {iso_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Error processing {iso_path}: {e}")

def process_iso_files(dir):
    for root, _, files in walk(dir):
        for file in files:
            if file.endswith(".iso"):   # Blu Ray
                file_path = os.path.join(root, file)
                print("Blu Ray == ", file_path)
                check_iso_type(file_path)
            if file.endswith(".ISO"):   # DVD
                file_path = os.path.join(root, file)
                print("DVD == ", file_path)
                check_iso_type(file_path)

def check_iso_type(iso_path):
    try:
       with open(iso_path, 'rb') as iso_file:
           # Read the first 4MB of the ISO
           header = iso_file.read(4 * 1024 * 1024) 

           if b"VIDEO_TS" in header:
               return "DVD ISO"
           elif b"BDMV" in header:
               return "Blu-ray ISO"
           else:
               return "Unknown ISO type"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def usage():
    print("Usage: script.py [options] [arguments]")
    print("Options:")
    print("  -h, --help            show this help message and exit")
    print("  -o, --output <file>   specify output file")
    print("  -v, --verbose         enable verbose mode")
