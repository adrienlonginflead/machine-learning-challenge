# Vector Search Challenge

The code in the project is to complete and represents the minimum development for vector search.
You are free to create your own structure and organize the code as you wish or simply fill in the different 
files in the project. Remember that readability and clarity are key in the code you write.

## data directory

The data directory contains two subdirectories:
- descriptions that contains all the text files
- images that contains all the image files

## data_manager.py

The data manager loads the text and the image from their filepath.

## display.py

A quick script that enable the user to display a specified number of image-text pairs.


## vectorizer.py

The file aiming to embed the images and the text to a vector representation.

## search_engine.py

A file containing a class with an index based on the embeddings of the text and the images
able to compare vectors, and retrieve the most similar ones.

## main.py

The main file that launch the algorithm. It
- reads the images and the descriptions from the data directory
- transforms the pairs of data into embeddings
- catches the user query and transforms it into a vector
- Compare similarity with the pair data
- Returns the N best matches (with the highest similarity)
