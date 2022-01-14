README

This small script takes any decklist from an MTGO list and pulls all card images as jpg or png files into your directory.

If you like this project or have comments, feel free to reach out on twitter @izzitmichaela!
https://twitter.com/izzitmichaela

INSTRUCTIONS FOR USE

CREATING THE PYTHON ENVIRONMENT:

First, you need python. For this, I installed anaconda, which is a python package that gives you all the tools you need to run programs. You can download the environment here:

https://www.anaconda.com/products/individual

Within the Anaconda package is a program called Spyder. This is what I used to write and run the program. Open it up, and ensure it is working (you can either go in anaconda and launch spyder from there or simply press your windows or program key and start typing Spyder and it'll show up).

Now you are ready to begin! Don't worry, the rest is much less involved!

RUNNING THE PROGRAM
0-Download files included in the project. There should be 3 - a deck txt file and two python runner files

1-Go to https://scryfall.com/docs/api/bulk-data
2-Download the 'All Cards' File from the list.
3-Ensure that the name of the file is "all-cards.json".
4-Place file in the SAME folder as the other files.
5-Update the Deck txt file to include whatever cards you would wish.
	NOTE: Be sure they are in MTGO format, and be sure that only cards with single digit quantities are present
	This means you cannot have '15 Abrade' but you can have '9 Abrade'
6-Open the python file of choice in Spyder and click the 'run' arrow in the top (ir looks like a normal 'play' button to run the python file. If you want the little white corners cropped off, select the Runner_croppedBorders program instead. This stores them as png files rather than jpgs and are larger - but they look cleaner.

The jpg files should appear in your directory after a moment or two!

Enjoy!

Note, if you are experiencing an error involving it not recognizing the 'requests' module, you may need to install the library using the tutorial below. If you installed anaconda and spyder correctly however, you shouldn't need to worry.

https://www.agiratech.com/install-requests-library-in-python


