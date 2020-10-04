<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Google Play Store Apps - Android market


*Anna Vilardell*

*Data Analytics-Part Time Course | Barcelona October 2020*


## Content
- [Project Description and Workflow](#project-description)
- [Organization](#organization)
- [Links](#links)


## Project Description and Workflow


### Description

This project is to practice statistical analysis using the iterative data analysis process on a dataset.

The dataset chosen is data of 10k Play Store apps - Direct link to the dataset [here](https://www.kaggle.com/lava18/google-play-store-apps)



### Goal

**If I would launch an App, what king of App should I go for if it's important to have positives(+) reviews?**

Sub questions to respond to get to our conclusion:
    - Which is the Category & Genre with +intalls, +reviews and +rating?
    - What is the target of most popular apps?
    - Is there a positive correlation between ratings and reviews?
    - Is there any statistical significance between reviews of Paid and Free Apps?
    - Is there any statistical significance between ratings of Paid and Free Apps?
    - Is there any statistical significance between the different ratings(1,2,3,4,5) given from reviews of Paid and Free Apps?



### Workflow

1. Import Libraries
2. Import Data
3. Exploratory Data Analysis (EDA))
    - Data wrangling
       - Explore data
       - Clean data
4. Statistical analysis
    - Data visualization
    - Check correlation of all numeric varibales
    - Explor correlation of interesting variables
    - Hypothesis Testing
        - **Paid | Free <> reviews: 2samples t test** 
     *¿Is there any statistical significance between reviews of Paid and Free Apps?* 
        - **Paid | Free <> ratings: 2samples t test** 
     *¿Is there any statistical significance between ratings of Paid and Free Apps?*
        - **Paid | Free; Rating <> Reviews: Anova** 
     *¿Is there any statistical significance between the different ratings given from reviews of Paid and Free Apps?*

5. Final Conclusion




## Organization

**Main Organization of the project thought Trello board:**

1. Organize a Trello board with main tasks and timings
2. Create a repository including a .gitignore file and a Readme.md
3. Data cleaning & manipulation
4. Statistical analysis on the data
6. Write conclusions
7. Complete Readme.md




**Inside this repository you can find:**

Folder with GoogleData
    - googleplaystore.csv (used in the project)
    - googleplaystore_user_reviews.csv (willing to use it later to go further with this project)

CSVs clean data:

    - playstore_Clean.csv

Jupyter notebook of the data wrangling:

    - statistical-analysis.ipynb

Other:

    - Gitignore.txt
    - README.md


## Links 

[Repository](https://github.com/AnnaVilardell/PR04-project-statistical-analysis) 
