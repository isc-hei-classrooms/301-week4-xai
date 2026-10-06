import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 4: Interpretable Machine Learning for Data Science

    **Problem**: You have been mandated by a large wine-making company in Valais to discover the key chemical factors that determine the quality of wine and build an interpretable model that will help their cellar masters make decisions daily.

    ## Settings things up

    This week will require quite a lot of autonomy on your part, but we will guide you with this high-level notebook. First, take the following steps:

    - Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
    - Then use `uv` to manage your environment. For instance, you can add a new package using:

      ```sh
      uv add polars
      ```

    - Launch this notebook within your `uv` environment with `uv run marimo edit week4-assignment.py` (add `--sandbox` to let marimo manage the dependencies of the notebook itself).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then, let's talk about code formatting. Using [black](https://github.com/psf/black) is a highly encouraged best-practice for all your Python projects: you never have to worry and debate about code formatting anymore. marimo has black built in, so just enable it in the editor settings or format a cell with the formatting shortcut. For your other projects, run it with `uvx black .`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here are the libraries you will most likely need and use during this week:

    - `numpy` for basic scientific computing and `scipy` for statistical testing.
    - `pandas` or `polars` for dataset manipulation. Polars is highly recommended, because it is [awesome](https://github.com/ddotta/awesome-polars). Instructions below will refer to the Polars API.
    - `seaborn` for statistical data visualization, but `matplotlib` is always needed anyway. Use both!
    - `shap` will be used for [interpretability](https://shap.readthedocs.io/en/stable/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html).
    - `sklearn` and `xgboost` will be used for training models. You may import them later when you need them.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fetch the data

    Here we have a very nice package that can do everything for us (aka `ucimlrepo`). Let's use it!

    Take a look at [the website](https://archive.ics.uci.edu/dataset/186/wine+quality) for details.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's check that the data have the correct shape to ensure they have been loaded as expected.

    Calculate how many samples and features we have in total, how many are red or white wines, how many are good or bad wines, etc.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Exploration

    We now will inspect the features one-by-one, and try to understand their dynamics, especially between white and red wines.

    - Use `Dataframe.describe` to display statistics on each feature. Do the same for red wines only, and white wines only. Do you notice any clear difference?
    - Compute the effect size by computing the [strictly standardized mean difference](https://en.wikipedia.org/wiki/Strictly_standardized_mean_difference) (SSMD) between the red and white wines for each feature.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's go a bit deeper into the same analysis, using more visual tools:

    - For every feature, plot boxplots, violinplots or histograms for red and white wines. What can you infer? **If you feel a bit more adventurous**, plot the Cumulative Distribution Function (CDF) of the feature for white and red wines, and compute the [Kullback-Leibler divergence](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html) (or entropy) between them. Explain why this might be useful.
    - Plot the correlation matrix of all features as heatmaps, one for red and one for white wines. How do they differ? What can you infer?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Exploration using Unsupervised Learning

    We first explore the data in an unsupervised fashion. Start by creating a heatmap of the average feature value for red and white wines. Can you spot an easy way to differentiate between reds and whites?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Using PCA to reduce the dimensionality

    Use PCA to reduce the dimensionality of data. Do not forget that it requires data normalization (centering on the mean and scaling to unit variance). Plot the whole dataset onto the two principal components and color it by wine color. What does it tell you?

    Project the unit vectors that correspond to each vector onto the principal components, using the same transformation. What does it tell you about the relative feature importance? Does it match the observations you made previously?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Cluster the data in 2-dimensional space

    Use k-means to cluster the data into 2 clusters and plot the same view as before, but with a coloring that corresponds to the cluster memberships.

    Assuming that the cluster assignments are predictions of a model, what is the performance you can achieve in terms of mutual information score, accuracy, and f1 score?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, we are going to train a **supervised** linear classification model using `sklearn`, and compare the results with the approach using clustering.

    - Set up a train/test dataset using `sklearn.model_selection.train_test_split`.
    - Use `GridSearchCV` to perform a cross-validation of the model's regularization `C`.
    - Compare the test and train performance at the end. Does the model suffer from any overfitting?
    - Analyze the test performance specifically. What can you conclude about this general problem of recognizing white vs red wines?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Basic model interpretability: inspecting the model

    As a first step towards intepretability of the model predictions, let's take a look at the coefficients of the model. What is the most important feature from this perspective? How do you interpret positive or negative coefficients?

    Is it compatible with what you have seen so far? Do you have an explanation why that might be?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Removing features to test their importance

    - What happens if you re-train a model, but remove the most important feature in the list?
    - What happens if you re-train the model with a `l1` penalty and you use more regularization?
    - Interpret the results you obtained above from the perspective of the business problem. What does it tell you about the key differences between a red and white wine?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Using Shapley values

    Now, use SHAP to explore how the model perceives a 'red' and 'white' wine.

    - Use a `beeswarm` plot to analyze the influence of each feature on the model's output.
    - What does the plot tell us about what makes a white wine 'white' and a red wine 'red'?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Now use Partial Dependence Plots to see how the expected model output varies with the variation of each feature.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Now use a waterfall diagram on a specific red and white wine and see how the model has made this specific prediction.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Now, let's take an example where the model has made an incorrect prediction, and see how it made this prediction.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Good vs Bad classification

    We are going to work on a binary classification problem, where all wines with a quality higher than 6 are considered as "good" and other are considered as "bad".

    - Prepare a dataset with a new column `binary_quality` that corresponds to the above definition.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One question that we might ask right away is:

    - Is there any correlation of the quality and the color of the wine?

    Ideally, there should be almost none. Why could it be a problem otherwise?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If it turns out that there are significantly more bad red wines than bad white wines or vice versa, what are the implications for your analysis?

    - Plot a heatmap of the mean feature value for bad and good wines, like we did before for red and white wines.
    - Plot two heatmaps, one for red and white wines. How do they differ? What kind of issue can it cause?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It is a lot more difficult now to tell apart good from bad wines. Let's turn to a more complex model, which is a [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting) [Trees](https://xgboost.readthedocs.io/en/stable/tutorials/model.html). For the sake of interpretability, design your notebook so that you can easily filter on only white and red wines and perform again the entire procedure.

    Let's first train a XGBClassifier model to distinguish between good and bad wines. Make sure to use the same best-practices (train/test split, cross-validation) as we did before. Note that the regularization of the GBTs is a lot more complex than for Logistic Regression. Test the following parameters:

      ```py
      param_grid = {
        "max_depth": [3, 4, 5],  # Focus on shallow trees to reduce complexity
        "learning_rate": [0.01, 0.05, 0.1],  # Slower learning rates
        "n_estimators": [50, 100],  # More trees but keep it reasonable
        "min_child_weight": [1, 3],  # Regularization to control split thresholds
        "subsample": [0.7, 0.9],  # Sampling rate for boosting
        "colsample_bytree": [0.7, 1.0],  # Sampling rate for columns
        "gamma": [0, 0.1],  # Regularization to penalize complex trees
      }
      ```
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Analyze the results (test and train), validate whether there is overfitting.
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interpretability with SHAP

    - Plot the feature importance (gain and cover) from the XGBoost model. What can you conclude?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Use SHAP's `TreeExplainer` to compute feature importance (Shapley values). Do you see any difference with XGBoost's feature importances?
    - Produce different plots to analyze Shapley values:
      - A bar plot that summarizes the mean absolute value of each feature.
      - A beeswarm plot that shows the shapley value for every sample and every feature.
      - A [heatmap plot](https://shap.readthedocs.io/en/stable/example_notebooks/api_examples/plots/heatmap.html#heatmap-plot) that indicates how different feature patterns influence the model's output.
    - Based on the above results, what makes a wine 'good' or 'bad'?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Now use Partial Dependence Plots to see how the expected model output varies with the variation of each feature.
    - How does that modify your perspective on what makes a good or bad wine?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Search for literature or resources that provide indications of the chemical structure of good or poor wines. Do your findings match these resources?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Analyze a few bad wines, and try to see how to make them better

    Pick some of the worst wines, and try to see what make them so bad. Check out [`shap.plots.heatmap`](https://shap.readthedocs.io/en/stable/example_notebooks/api_examples/plots/heatmap.html#heatmap-plot) for some visual tool to do this.

    How would you go about improving them?
    """)
    return


@app.cell
def _():
    # Complete this cell with your code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Wrap-up and conclusion

    As wrap-up, explain what are your key findings, and make 3 recommendations to the wine maker on how to improve the wines for next year. How confident are you that making these changes will lead to better wines? Explain in simple terms to the winemaker the limitations of your approach in terms of capturing causality.
    """)
    return


if __name__ == "__main__":
    app.run()
