# NSCR-Palette-Restorer
> Developed by Turtleisaac

Inserts palette data into a tilemap (NSCR) output by TilemapStudio that has lost its palette data



## Requirements

* Python3
  * ndspy 

## Usage

```
python3 Main.py [-h] <tilemap file> <palette ID for it to use> <name of file to output>
```

## Details
Given an `NSCR` file as input, sets all tiles in the tilemap except for instances of the transparency tile (first tile in NCGR) (tile in top left corner of the base image) (tile with the lowest tile ID) to use the user-specified palette ID
