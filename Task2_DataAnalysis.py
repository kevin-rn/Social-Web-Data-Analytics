import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import f_oneway, mannwhitneyu, ttest_ind, wilcoxon


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


def explore_feature(dataframe, feature, type_plot):
    """
    Separates relevant and non-relevant tweets for certain feature and calculates the p-values.
    """
    feature_relevant = dataframe[dataframe['relevanceJudge'] == 1][feature]
    feature_non_relevant = dataframe[dataframe['relevanceJudge'] == 0][feature]

    print(f"\n{feature}: \nFeature relevant: \n{feature_relevant.describe()} \n\n"
          f"Feature non-relevant \n{feature_non_relevant.describe()}")

    _, mwu_p_value = mannwhitneyu(feature_non_relevant, feature_relevant)
    _, anova_p_value = f_oneway(feature_non_relevant, feature_relevant)
    _, tt_p_value = ttest_ind(feature_non_relevant, feature_relevant)

    print(f"\nP-values:\nMann Whitney U test: {mwu_p_value}"
          f"\nOne way Anova test: {anova_p_value}"
          f"\nT-test: {tt_p_value}")

    plot_feature(feature, feature_relevant, feature_non_relevant, type_plot)


if __name__ == "__main__":
    df = pd.read_csv("task2_data.csv")
    explore_feature(df, '#entities', 'hist')
    explore_feature(df, '#entityTypes', 'box')
    explore_feature(df, '#tweetsPosted', 'hist')
    explore_feature(df, 'sentiment', 'hist')
    explore_feature(df, 'nFavorties', 'box')
