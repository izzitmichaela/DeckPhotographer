README

This small script takes any decklist from an MTGO list and pulls all card images as jpg files into your directory.

INSTRUCTIONS FOR USE

0-Download files included in the project. There should be two - a deck txt file and a python runner file

1-Go to https://scryfall.com/docs/api/bulk-data
2-Download the 'All Cards' File from the list.
3-Ensure that the name of the file is "all-cards.json".
4-Place file in the SAME folder as the other files.
5-Update the Deck txt file to include whatever cards you would wish.
	NOTE: Be sure they are in MTGO format, and be sure that only cards with single digit quantities are present
	This means you cannot have '15 Abrade' but you can have '9 Abrade'
6-Run the python file. If you want the little white corners cropped off, select the Runner_croppedBorders program. This stores them as png files rather than jpgs and are larger, but they look cleaner and dont have those silly white parts on the four corners.

The jpg files should appear in your directory after a moment or two!

Enjoy!


