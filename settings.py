map_layout = [
	'                                              ',
	'             c                                ',
	'             c                                ',
	'             c            cccc                ',
	'          b  e  b        XXXXXX               ',
	'          XXXXXXX                             ',
	'                                              ',
	'                            cc  ccb  e  b     ',
	'                           c   c   XXXXX      ',
	'                   ccccc           XXXXX      ',
	'      O   ccc    XXXXXXXXX         XXXXX      ',
	'   XXXXXXXXXXX   XXXXXXXXX         XXXXX      ',
	'   XXXXXXXXXXX   XXXXXXXXX         XXXXX      ',
]

tile_size = 64

screen_height = len(map_layout) * tile_size
screen_width = int(screen_height * 1.5)