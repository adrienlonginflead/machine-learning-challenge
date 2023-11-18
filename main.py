from data_manager import load_image_text_pairs
from vectorizer import vectorize_text
from search_engine import SearchIndex
from display import display_image_text_pairs


def main():
    # Load the image-text pairs
    data_dir = 'data'
    image_text_pairs = load_image_text_pairs(data_dir)

    # Initialize and build the search index
    # Your code here #

    # User input for text query
    keep_going = True
    while keep_going:
        query_text = input("Enter your text query: ")

        # Process query and perform search
        query_vector = vectorize_text(query_text)
        # Your code here #

        # Display the top N results
        query_text = input("Do you want to continue? (y/n)")
        if query_text.lower() == 'n':
            keep_going = False


if __name__ == "__main__":
    main()
