import matplotlib.pyplot as plt


def display_image_text_pairs(pairs, n):
    """
    Display a specified number of image-text pairs.

    :param pairs: List of tuples containing (image, text).
    :param n: Number of pairs to display.
    """
    if n > len(pairs):
        n = len(pairs)

    fig, axs = plt.subplots(n, 2, figsize=(10, n * 5))

    for i in range(n):
        img, text = pairs[i]
        axs[i, 0].imshow(img)
        axs[i, 0].axis('off')
        axs[i, 1].text(0.5, 0.5, text, ha='center', va='center')
        axs[i, 1].axis('off')

    plt.show()
