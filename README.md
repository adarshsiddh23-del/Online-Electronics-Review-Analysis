# Online Electronics Product Reviews and Rating Sentiment-Category Analysis System 

## Project Overview

This project analyzes customer reviews and ratings of electronics products using Python. It studies product ratings, review sentiment, review categories, product performance, verified purchases, and price information.

The project uses Pandas for data processing, NumPy for numerical and statistical analysis, and Matplotlib for data visualization.


## Objectives

- Analyze customer ratings of electronics products.
- Classify reviews into Positive, Neutral, and Negative sentiment using ratings.
- Categorize reviews based on important keywords.
- Analyze product-wise and category-wise ratings.
- Analyze sentiment distribution across products and categories.
- Study verified purchase information.
- Analyze product price information.
- Identify frequently reviewed products and positive/negative reviews.


## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Git & GitHub


## Dataset

The project uses a dataset containing approximately 10,000 electronics product reviews.

Important dataset attributes include:

- Review_ID
- Product
- Category
- Rating
- Review
- Sentiment
- Price_INR
- Verified_Purchase
- Review_Date


## Methodology

### 1. Data Loading

The dataset is loaded using Pandas.

### 2. Data Cleaning

The project checks for missing values and duplicate records. Review text is also cleaned by removing unnecessary spaces and converting text to lowercase for keyword analysis.

### 3. Rating Analysis

NumPy is used to calculate statistical values such as:

- Mean
- Median
- Minimum
- Maximum
- Standard deviation

### 4. Sentiment Analysis

Sentiment is calculated from the product rating:

| Rating | Sentiment |
|---|---|
| 4–5 | Positive |
| 3 | Neutral |
| 1–2 | Negative |

### 5. Review Category Analysis

Reviews are categorized using keyword matching.

Categories include:

- Battery
- Performance
- Camera
- Display
- Sound
- Quality
- Price
- Comfort
- General 


### 6. Product Analysis

The project analyzes:

- Number of reviews per product
- Average product rating
- Product-wise sentiment distribution

### 7. Category Analysis

The project calculates average ratings and sentiment distribution for different electronics categories.

### 8. Verified Purchase Analysis

Verified and non-verified purchases are analyzed to compare their review counts and average ratings.

### 9. Price Analysis

The project calculates basic price statistics such as average, minimum, and maximum product price.

### 10. Visualization

Matplotlib is used to visualize the analysis results using charts and graphs.


## Project Features

- Customer rating analysis
- Rule-based sentiment classification
- Keyword-based review categorization
- Product-wise analysis
- Category-wise analysis
- Verified purchase analysis
- Price analysis
- Positive and negative review identification
- Data visualization
- Processed dataset export


## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install Required Libraries

```bash
pip install pandas numpy matplotlib

### 3. Run the Python Program

Open CMD or a terminal inside the project folder and run:

```bash
python project_code.py     

## Future Scope

The project can be further improved by:

- Using Natural Language Processing (NLP)
- Implementing machine learning-based sentiment analysis
- Using advanced text preprocessing
- Creating an interactive dashboard
- Adding more visualization techniques
- Developing a web-based interface
- Supporting real-time review analysis  

## Conclusion

This project provides a Python-based system for analyzing electronics product reviews and ratings. It combines data processing, statistical analysis, rule-based sentiment classification, keyword-based review categorization, and visualization to extract useful information from customer review data.