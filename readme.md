# `png2jpg.py`

A simple script to convert PNG <-> JPEG.

## Setup

Python setup:

```
pip install pillow
```

## Install

Add something like this to `PATH`:

```
# png2jpg and jpg2png
export PATH="$PATH:$HOME/path/to/this/directory"
```

## Usage

```
png2jpg image.png  # -> image.jpg
```

or, in reverse:

```
png2jpg image.jpg  # -> image.png
```

or with a specified output file:

```
png2jpg image.png output  # -> output.jpg
```

```
png2jpg image.png output.jpg  # -> output.jpg
```

## Notes

`png2jpg` and `jpg2png` are synonyms.