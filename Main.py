import sys
from pathlib import Path

from Buffer import Buffer


def run():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            usage()
            print('Make sure that whatever tile you wish to be used as the transparency tile is the FIRST tile (top '
                  'left corner) in your tilemap')
            return

    if len(sys.argv) != 4:
        print('Invalid arguments provided')
        usage()
        return

    path = Path(sys.argv[1])
    if not path.is_file():
        print('The provided filepath does not exist')
        return

    palette_num = int(sys.argv[2])

    if palette_num > 15:
        print('Palette ID must be between 0 and 15 (inclusive)')
        return

    with open(sys.argv[1], 'rb') as f:
        data = f.read()
    buffer = Buffer(bytearray(data), write=True)
    buffer.seek_local(36)

    has_read_yet = False

    while buffer.pos != len(buffer.data):
        tile = buffer.read_u16()
        buffer.seek_local(-2)
        if not has_read_yet:
            has_read_yet = True
            transparency_tile = tile & 0x3FF
        if tile & 0x3FF != transparency_tile:
            tile |= (palette_num << 12)
        buffer.write_u16(tile)

    with open(sys.argv[3], 'wb') as f:
        f.write(buffer.data)


def usage():
    print('\t%s [-h] <tilemap file> <palette ID for it to use> <name of file to output>' % sys.argv[0])


if __name__ == '__main__':
    run()
