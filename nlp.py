import matplotlib.pyplot as plt

def plot_bag_of_words(bag_of_words):
    plt.style.use('ggplot')

    fig, _ = plt.subplots()

    bag_of_words = bag_of_words.most_common(6)

    print(bag_of_words)

    x = [word_freq_pair[1] for word_freq_pair in bag_of_words]
    y = [word_freq_pair[0] for word_freq_pair in bag_of_words]

    # reverse order
    x = x[::-1]
    y = y[::-1]
    
    plt.barh(y, x)

    return fig