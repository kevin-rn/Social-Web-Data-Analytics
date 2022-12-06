import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import mannwhitneyu, ttest_ind


def plot_feature(feature, feature_relevant, feature_non_relevant, plot_type):
    """"
    Creates basic plots for relevant and non-relevant tweets for a certain feature.
    """
    _, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    ax1.set_title(f"{feature}_relevant")
    feature_relevant.plot(kind=plot_type, ax=ax1)
    ax2.set_title(f"{feature}_non_relevant")
    feature_non_relevant.plot(kind=plot_type, ax=ax2)
    plt.show()


def explore_feature(dataframe, feature, type_plot, is_nd):
    """
    Separates relevant and non-relevant tweets for certain feature and calculates the p-values.
    """
    feature_relevant = dataframe[dataframe['relevanceJudge'] == 1][feature]
    feature_non_relevant = dataframe[dataframe['relevanceJudge'] == 0][feature]

    print(f"\n{feature}: \nFeature relevant: \n{feature_relevant.describe()} \n\n"
          f"Feature non-relevant \n{feature_non_relevant.describe()}")

    if is_nd:
        _, tt_p_value = ttest_ind(feature_non_relevant, feature_relevant)
        print(f"\nT-test - p-value: {tt_p_value}")
    else:
        _, mwu_p_value = mannwhitneyu(feature_non_relevant, feature_relevant)
        print(f"\nMann Whitney U test - p-value: {mwu_p_value}")

    plot_feature(feature, feature_relevant, feature_non_relevant, type_plot)


if __name__ == "__main__":
    df = pd.read_csv("task2_data.csv")
    explore_feature(df, '#entities', 'hist', False)
    explore_feature(df, '#entityTypes', 'hist', False)
    explore_feature(df, '#tweetsPosted', 'hist', False)
    explore_feature(df, 'sentiment', 'box', True)
    explore_feature(df, 'nFavorties', 'box', False)
