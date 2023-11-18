class SearchIndex:
    def __init__(self):
        self.image_vectors = []
        self.text_vectors = []
        self.image_text_pairs = []

    def add_to_index(self, image_text_pairs):
        """
        Processes a list of image-text pairs and adds their vector representations to the index.

        :param image_text_pairs: List of tuples containing (image, text).
        """

    def build_index(self):
        """
        Converts lists to numpy arrays for efficient search.
        """

    def search(self, query_vector, similarity_fn, top_n=3):
        """
        Searches for the most similar image-text pairs based on the query vector.

        :param query_vector: The vector representation of the query.
        :param similarity_fn: The function that calculates the similarity between 2 vectors.
        :param top_n: Number of top matches to return.
        :return: Top N matching image-text pairs.
        """
        pass
