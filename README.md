# bda-modulo-3-evaluacion-final-FiSaRaff

# Customer Data Analysis

## Overview

This project focuses on analysing a large customer dataset to explore various patterns, behaviours, and relationships. The primary objective is to identify factors influencing customer behaviours, such as the number of flight bookings, education level, and marital status. The dataset consists of 40,000+ rows of customer information, and we apply statistical tests and visualisations to derive meaningful insights.

## Project Structure

The project is structured into the following sections:

1. **Exploratory Data Analysis (EDA)**: Performing initial analyses to understand data distributions and relationships. 
2. **Data Preprocessing**: Cleaning and preparing the data for analysis.
3. **Visualisations**: Creating charts and graphs to visualise key insights from the data.
4. **Statistical Tests**: Applying statistical methods to test hypotheses, such as the Kruskal-Wallis and post-hoc Dunn tests, to analyse differences in flight bookings across different groups.

## Key Features

- **Data Cleaning**: Handling missing values, duplicates, and data formatting issues.
- **Statistical Analysis**: Hypothesis testing using methods like Kruskal-Wallis, Dunn's post-hoc test, and normality tests (Kolmogorov-Smirnov).
- **Visualisation**: Creating bar charts, line graphs, and other visual representations of the data.
- **Customer Insights**: Analysing the relationship between customer characteristics (e.g., education level, marital status) and flight booking patterns.

## Technologies Used

- **Python**: Primary programming language.
- **Libraries**:
  - `pandas` for data manipulation.
  - `numpy` for numerical operations.
  - `scipy` for statistical analysis.
  - `matplotlib` and `seaborn` for data visualisation.
  - `sklearn` for data imputation and additional analysis.
  - `scikit_posthocs` for post-hoc statistical tests.

## Installation

To get started with this project, you'll need to install the required dependencies. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Adalab/bda-modulo-3-evaluacion-final-FiSaRaff.git
   ```
   
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

   If `scikit_posthocs` is not available, you can install it manually:
   ```bash
   pip install scikit-posthocs
   ```

3. After installing the dependencies, you can run the Python scripts from the `analysis/` directory to begin exploring the data.

## Usage

1. **Data Preprocessing**: The first script loads and cleans the data.
2. **Exploratory Data Analysis**: Next, you can run the EDA script to explore the distribution of key variables and relationships between them.
3. **Statistical Testing**: The statistical tests are applied to check for significant differences in the dataset, followed by post-hoc tests if necessary.
4. **Visualisations**: Visualising the results of your statistical tests and customer characteristics.

## Statistical Analysis Methods

- **Shapiro-Wilk & Kolmogorov-Smirnov Tests**: Used to assess if the data follows a normal distribution. If the data is not normally distributed, non-parametric tests like Kruskal-Wallis are used.

- **Leven's test**: Used to assess whether the variances are equal across multiple groups

- **Kruskal-Wallis Test**: Used to determine if there are significant differences between two or more independent groups. It is used when the data is not normally distributed. It is a non-parametric test.
  
- **Post-hoc Dunn’s Test**: Applied after the Kruskal-Wallis test to determine which specific groups differ from each other when there are significant results.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure your contributions are well-documented and tested.

Let me know if you'd like to adjust any sections or add further details!