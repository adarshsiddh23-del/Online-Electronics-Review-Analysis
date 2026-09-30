# ============================================================
# ONLINE ELECTRONICS PRODUCT REVIEWS AND
# RATING SENTIMENT-CATEGORY ANALYSIS SYSTEM
# ============================================================

# -------------------------------
# 1. IMPORT LIBRARIES
# -------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------
# 2. LOAD DATASET
# -------------------------------

file_name = "electronics_product_reviews_10000.csv"

df = pd.read_csv(file_name)

print("\n================================================")
print("       ELECTRONICS REVIEW ANALYSIS SYSTEM")
print("================================================")

print("\nDataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())


# -------------------------------
# 3. BASIC DATA INFORMATION
# -------------------------------

print("\n\nDataset Information:")
print(df.info())

print("\n\nStatistical Summary:")
print(df.describe())


# -------------------------------
# 4. CHECK MISSING VALUES
# -------------------------------

print("\n\nMissing Values:")
print(df.isnull().sum())


# -------------------------------
# 5. REMOVE DUPLICATES
# -------------------------------

duplicate_count = df.duplicated().sum()

print("\nDuplicate Records:", duplicate_count)

df = df.drop_duplicates()

print("Records after removing duplicates:", len(df))


# -------------------------------
# 6. DATA CLEANING
# -------------------------------

# Convert review to string
df["Review"] = df["Review"].astype(str)

# Remove extra spaces
df["Review"] = df["Review"].str.strip()

# Convert review to lowercase
df["Clean_Review"] = df["Review"].str.lower()

# Remove missing reviews
df = df.dropna(subset=["Review"])

print("\nData cleaning completed.")


# ============================================================
# 7. RATING ANALYSIS
# ============================================================

print("\n================================================")
print("                 RATING ANALYSIS")
print("================================================")

ratings = np.array(df["Rating"])

print("\nAverage Rating:",
      round(np.mean(ratings), 2))

print("Maximum Rating:",
      np.max(ratings))

print("Minimum Rating:",
      np.min(ratings))

print("Median Rating:",
      np.median(ratings))

print("Standard Deviation:",
      round(np.std(ratings), 2))


# Rating counts

rating_count = df["Rating"].value_counts().sort_index()

print("\nRating Distribution:")
print(rating_count)


# ============================================================
# 8. SENTIMENT ANALYSIS
# ============================================================

print("\n================================================")
print("              SENTIMENT ANALYSIS")
print("================================================")


def sentiment_from_rating(rating):

    if rating >= 4:
        return "Positive"

    elif rating == 3:
        return "Neutral"

    else:
        return "Negative"


df["Calculated_Sentiment"] = df["Rating"].apply(
    sentiment_from_rating
)


sentiment_count = df["Calculated_Sentiment"].value_counts()

print("\nSentiment Distribution:")
print(sentiment_count)


# Calculate sentiment percentage

sentiment_percentage = (
    df["Calculated_Sentiment"]
    .value_counts(normalize=True)
    * 100
)

print("\nSentiment Percentage:")
print(sentiment_percentage.round(2))


# ============================================================
# 9. KEYWORD ANALYSIS
# ============================================================

print("\n================================================")
print("                KEYWORD ANALYSIS")
print("================================================")


keywords = {

    "Battery": [
        "battery",
        "charging"
    ],

    "Performance": [
        "performance",
        "fast",
        "slow"
    ],

    "Camera": [
        "camera",
        "photo",
        "picture"
    ],

    "Display": [
        "display",
        "screen"
    ],

    "Sound": [
        "sound",
        "audio",
        "bass"
    ],

    "Quality": [
        "quality",
        "build"
    ],

    "Price": [
        "price",
        "worth"
    ],

    "Comfort": [
        "comfortable",
        "comfort"
    ]
}


def find_category(review):

    review = review.lower()

    for category, words in keywords.items():

        for word in words:

            if word in review:
                return category

    return "General"


df["Review_Category"] = df["Clean_Review"].apply(
    find_category
)


category_count = df["Review_Category"].value_counts()

print("\nReview Category Distribution:")
print(category_count)


# ============================================================
# 10. PRODUCT ANALYSIS
# ============================================================

print("\n================================================")
print("                PRODUCT ANALYSIS")
print("================================================")


product_count = df["Product"].value_counts()

print("\nNumber of Reviews per Product:")
print(product_count)


# Average rating by product

product_rating = (
    df.groupby("Product")["Rating"]
    .mean()
    .sort_values(ascending=False)
)


print("\nAverage Rating by Product:")
print(product_rating.round(2))


# ============================================================
# 11. CATEGORY-WISE RATING
# ============================================================

category_rating = (
    df.groupby("Category")["Rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Rating by Product Category:")
print(category_rating.round(2))


# ============================================================
# 12. PRODUCT-WISE SENTIMENT
# ============================================================

product_sentiment = pd.crosstab(
    df["Product"],
    df["Calculated_Sentiment"]
)

print("\nProduct-wise Sentiment:")
print(product_sentiment)


# ============================================================
# 13. CATEGORY-WISE SENTIMENT
# ============================================================

category_sentiment = pd.crosstab(
    df["Category"],
    df["Calculated_Sentiment"]
)

print("\nCategory-wise Sentiment:")
print(category_sentiment)


# ============================================================
# 14. VERIFIED PURCHASE ANALYSIS
# ============================================================

print("\n================================================")
print("           VERIFIED PURCHASE ANALYSIS")
print("================================================")

verified_count = df["Verified_Purchase"].value_counts()

print("\nVerified Purchase Distribution:")
print(verified_count)


verified_rating = (
    df.groupby("Verified_Purchase")["Rating"]
    .mean()
)

print("\nAverage Rating:")
print(verified_rating.round(2))


# ============================================================
# 15. PRICE ANALYSIS
# ============================================================

print("\n================================================")
print("                 PRICE ANALYSIS")
print("================================================")

price = np.array(df["Price_INR"])

print("\nAverage Product Price: ₹",
      round(np.mean(price), 2))

print("Minimum Product Price: ₹",
      round(np.min(price), 2))

print("Maximum Product Price: ₹",
      round(np.max(price), 2))


# ============================================================
# 16. TOP POSITIVE REVIEWS
# ============================================================

print("\n================================================")
print("             TOP POSITIVE REVIEWS")
print("================================================")

positive_reviews = df[
    df["Calculated_Sentiment"] == "Positive"
]

print(
    positive_reviews[
        ["Product", "Rating", "Review"]
    ].head(10)
)


# ============================================================
# 17. NEGATIVE REVIEWS
# ============================================================

print("\n================================================")
print("             NEGATIVE REVIEWS")
print("================================================")

negative_reviews = df[
    df["Calculated_Sentiment"] == "Negative"
]

print(
    negative_reviews[
        ["Product", "Rating", "Review"]
    ].head(10)
)


# ============================================================
# 18. MOST REVIEWED PRODUCTS
# ============================================================

print("\n================================================")
print("            MOST REVIEWED PRODUCTS")
print("================================================")

print(product_count.head(10))


# ============================================================
# 19. SAVE ANALYZED DATA
# ============================================================

output_file = "electronics_review_analysis_result.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nAnalysis data saved to:",
      output_file)


# ============================================================
# 20. VISUALIZATION 1
#     RATING DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    rating_count.index,
    rating_count.values
)

plt.title("Electronics Product Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")

plt.xticks([1, 2, 3, 4, 5])

plt.tight_layout()

plt.show()


# ============================================================
# 21. VISUALIZATION 2
#     SENTIMENT DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

sentiment_count.plot(
    kind="bar"
)

plt.title("Customer Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# ============================================================
# 22. VISUALIZATION 3
#     PRODUCT AVERAGE RATINGS
# ============================================================

plt.figure(figsize=(12, 6))

product_rating.plot(
    kind="bar"
)

plt.title("Average Rating by Product")
plt.xlabel("Product")
plt.ylabel("Average Rating")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ============================================================
# 23. VISUALIZATION 4
#     REVIEW CATEGORIES
# ============================================================

plt.figure(figsize=(10, 6))

category_count.plot(
    kind="bar"
)

plt.title("Review Category Analysis")
plt.xlabel("Review Category")
plt.ylabel("Number of Reviews")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ============================================================
# 24. VISUALIZATION 5
#     PRODUCT-WISE SENTIMENT
# ============================================================

product_sentiment.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Product-wise Sentiment Analysis")

plt.xlabel("Product")

plt.ylabel("Number of Reviews")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ============================================================
# 25. VISUALIZATION 6
#     CATEGORY-WISE RATING
# ============================================================

plt.figure(figsize=(10, 6))

category_rating.plot(
    kind="bar"
)

plt.title("Average Rating by Electronics Category")

plt.xlabel("Category")

plt.ylabel("Average Rating")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ============================================================
# 26. VISUALIZATION 7
#     VERIFIED VS NON-VERIFIED
# ============================================================

plt.figure(figsize=(7, 5))

verified_count.plot(
    kind="bar"
)

plt.title("Verified vs Non-Verified Purchases")

plt.xlabel("Purchase Type")

plt.ylabel("Number of Reviews")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# ============================================================
# 27. FINAL SUMMARY
# ============================================================

print("\n================================================")
print("                 FINAL SUMMARY")
print("================================================")

print("\nTotal Reviews:",
      len(df))

print(
    "Average Rating:",
    round(df["Rating"].mean(), 2)
)

print(
    "Positive Reviews:",
    len(df[df["Calculated_Sentiment"] == "Positive"])
)

print(
    "Neutral Reviews:",
    len(df[df["Calculated_Sentiment"] == "Neutral"])
)

print(
    "Negative Reviews:",
    len(df[df["Calculated_Sentiment"] == "Negative"])
)

print(
    "\nMost Reviewed Product:",
    product_count.idxmax()
)

print(
    "Highest Average Rated Product:",
    product_rating.idxmax()
)

print(
    "Most Common Review Category:",
    category_count.idxmax()
)

print("\n================================================")
print("             ANALYSIS COMPLETED")
print("================================================")