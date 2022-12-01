import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import mannwhitneyu


def plot_feature(feature_r, feature_nr, ax1_title, ax2_title, plot_type):
    _, (ax1, ax2) = plt.subplots(2)
    ax1.set_title(ax1_title)
    feature_r.plot(kind=plot_type, ax=ax1)
    ax2.set_title(ax2_title)
    feature_nr.plot(kind=plot_type, ax=ax2)
    plt.show()


def explore_feature(dataframe, feature):
    feature_relevant = df[df['relevanceJudge'] == 1][feature]
    feature_non_relevant = df[df['relevanceJudge'] == 0][feature]
    feature_relevant.describe()
    feature_non_relevant.describe()
    u, p_value = mannwhitneyu(feature_non_relevant, feature_relevant)
    plot_feature(feature_relevant, feature_non_relevant, "", "", "box")


if __name__ == "__main__":
    df = pd.read_csv("task2_data.csv")
    explore_feature(df, 'entities')
    explore_feature(df, '#entityTypes')
    explore_feature(df, '#tweetsPosted')
    explore_feature(df, 'sentiment')
    # explore_feature(df, )


