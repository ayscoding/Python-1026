# Sentiment Analysis Program

This Python program performs sentiment analysis on Twitter data, analyzing tweets based on keywords to generate insights into public opinion about a business, product, or security. It uses text processing, statistical analysis, and data visualization techniques to produce a sentiment report.

## Overview
The program reads two input files:
1. **Keywords File (.tsv)**: Contains keywords with assigned sentiment values.
2. **Tweets File (.csv)**: Contains tweets with metadata.

The analysis generates a detailed report including:
- Average sentiment of all tweets.
- Number of positive, negative, and neutral tweets.
- Sentiment analysis of favorited and retweeted tweets.
- Top 5 countries by average sentiment.

## Features

### 1. **Reading Data**
- Reads and processes the **keywords file** to create a dictionary of keywords and their sentiment values.
- Reads and processes the **tweets file**, cleaning the text and extracting relevant metadata.

### 2. **Cleaning and Processing Tweets**
- Cleans tweet text by removing punctuation, numbers, and special characters.
- Converts the text to lowercase for consistent keyword matching.

### 3. **Calculating Sentiment**
- Uses a sentiment scoring system where the score of a tweet is calculated based on the presence of keywords in its text.
- Sentiment scores are classified as:
  - Positive: Score > 0
  - Negative: Score < 0
  - Neutral: Score = 0

### 4. **Analyzing Sentiment**
- Computes:
  - Average sentiment of all tweets.
  - Average sentiment of favorited and retweeted tweets.
  - Number of positive, negative, and neutral tweets.
- Identifies the top 5 countries with the highest average sentiment.

### 5. **Generating the Report**
- Outputs a comprehensive sentiment report to a user-specified `.txt` file.

## Input and Output

### Inputs
1. **Keywords File (.tsv)**:
   - Format: Each line contains a keyword and its sentiment value, separated by a tab (`\t`).
   - Example:
     ```
     happy   2
     sad     -1
     excited 3
     ```

2. **Tweets File (.csv)**:
   - Format: Each row contains metadata about a tweet (e.g., text, user, location, retweets, favorites).
   - Example Columns:
     ```
     date,text,user,retweet,favorite,lang,country,state,city,lat,lon
     ```

3. **Output File (.txt)**:
   - The file to which the generated report is saved.
