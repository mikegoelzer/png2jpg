#!/usr/bin/env /usr/bin/python3

import os
import sys
import argparse
from PIL import Image

def convert(input_file_path, output_file_path):
    if input_file_path.lower().endswith(".jpg"):
        return convert_jpg_to_png(input_file_path, output_file_path)
    elif input_file_path.lower().endswith(".png"):
        return convert_png_to_jpg(input_file_path, output_file_path)
    else:
        raise ValueError(f"unsupported format: {input_file_path}")

def convert_jpg_to_png(input_file_path, output_file_path):
    image = Image.open(input_file_path)
    image.save(output_file_path, "PNG")
    print(f"saved to {output_file_path}")

def convert_png_to_jpg(input_file_path, output_file_path):
    image = Image.open(input_file_path)
    out_image = Image.new("RGB", image.size, (255, 255, 255))
    out_image.paste(image, (0, 0), image)
    out_image.save(output_file_path, "JPEG")
    print(f"saved to {output_file_path}")

def print_image_info(input_file_path):
    image = Image.open(input_file_path)
    print(f"{image.format} ({image.mode}): {image.size[0]} x {image.size[1]}")

def main():
    parser = argparse.ArgumentParser(description="convert PNG <-> JPG")
    parser.add_argument("INPUT_FILE", type=str, help="input image file")
    parser.add_argument("OUTPUT_FILE", type=str, nargs='?', help="optional output image file (default is just to swap extension on input)", default=None)
    parser.add_argument("-i", "--info", action="store_true", help="just prints information about the input image")
    args = parser.parse_args()

    # validate args
    if not os.path.exists(args.INPUT_FILE):
        raise FileNotFoundError(f"file not found: {args.INPUT_FILE}")

    # default output is input pdf but with extension replaced with jpg/png
    input_dir = os.path.dirname(args.INPUT_FILE)
    input_basename, input_ext = os.path.splitext(os.path.basename(args.INPUT_FILE))
    default_output_ext = ".jpg" if input_ext == ".png" else ".png"
    if args.OUTPUT_FILE is None:
        output_image_path = os.path.join(input_dir, f"{input_basename}{default_output_ext}")
    elif not os.path.splitext(args.OUTPUT_FILE)[1]:
        # output file basename w/o extension specified by user
        output_image_path = f"{args.OUTPUT_FILE}{default_output_ext}"
    else:
        # output file path is specified by user
        _, requested_output_ext = os.path.splitext(args.OUTPUT_FILE)
        if requested_output_ext.lower() not in [".jpg", ".jpeg", ".png"] or (input_ext.lower() in [".jpg", ".jpeg"] and requested_output_ext.lower() in [".jpg", ".jpeg"]) or (input_ext.lower() == ".png" and requested_output_ext.lower() == ".png"):
            raise ValueError(f"incorrect output format: {requested_output_ext}")
        output_image_path = args.OUTPUT_FILE

    # mkdir -p the output directory
    output_dir = os.path.dirname(output_image_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # print info and bail for -i/--info
    if args.info:
        print_image_info(args.INPUT_FILE)
        return 0

    # convert
    convert(args.INPUT_FILE, output_image_path)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)