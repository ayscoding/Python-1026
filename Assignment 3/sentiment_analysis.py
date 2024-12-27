""" 
Date: 12 Nov 2023
This file contain the functions used to determine the Sentiment Analysis. 
"""


import csv


# This function calls the Keywords file, cleans it, assigns keys:values to my_dict
def read_keywords(firstfile="keywords.tsv"):
    my_dict = {}
    try:
        read_f = open(firstfile, "r")
        for line in read_f.readlines():
            # Split takes of Tab values, replaces with "," and makes a list.
            devide_t = line.split("\t")
            if len(devide_t) == 2:
                first_value, second_value = map(
                    str.strip, devide_t
                )  # Assigning values respectively
                my_dict[first_value] = int(second_value)
            else:
                print(f"Issue with line in {firstfile}: {line.strip()}")
        return my_dict
    except IOError:
        print(f"Could not open file {firstfile}!")
        return my_dict


# This function cleans text from unwanted characters
def clean_tweet_text(text: str):
    PUNC = "'!@#$%^&*()_-+=}[]{|\:;~<>,.?/1234567890"
    new_text = ""

    for ch in text:
        if ch in PUNC:
            pass
        else:
            new_text += ch.lower()

    return new_text


# This function calculate the sentiment score
def calc_sentiment(tweet_text, keyword_dict):
    sentiment_score = 0
    tweet_words = tweet_text.split()

    for word in tweet_words:
        if word in keyword_dict:
            sentiment_score += keyword_dict[word]

    return sentiment_score


# This function classifies the sentiment score
def classify(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"


# This function reads through the tweets file, and returns list of dictionaries
def read_tweets(secondfile="adidas.csv"):
    # Indexes of data inside the tweets file
    date = 0
    text = 1
    user = 2
    retweet = 3
    favorite = 4
    lang = 5
    country = 6
    state = 7
    city = 8
    lat = 9
    lon = 10

    listof_dict = []  # The returned dictionary
    try:
        with open(secondfile, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)  # Reads CSV file
            for row in reader:
                dict_a = {}
                if len(row) > text:
                    dict_a["date"] = row[date]
                    cleaned_text = clean_tweet_text(
                        row[text]
                    )  # Cleans the text from unwanted Characters
                    dict_a["text"] = cleaned_text
                    dict_a["user"] = row[user]
                    dict_a["favorite"] = int(row[favorite])
                    dict_a["retweet"] = int(row[retweet])
                    dict_a["lang"] = row[lang]
                    dict_a["country"] = row[country]
                    dict_a["state"] = row[state]
                    dict_a["city"] = row[city]
                    try:
                        dict_a["lat"] = float(row[lat])
                    except ValueError:
                        dict_a["lat"] = row[lat]
                    try:
                        dict_a["lon"] = float(row[lon])
                    except ValueError:
                        dict_a["lon"] = row[lon]

                    listof_dict.append(dict_a)
    except IOError:
        print(f"Could not open file {secondfile}")
    return listof_dict


# Fun is used to create the report for the Sentiment Analysis
def make_report(tweet_list, keyword_dict):
    # Some initial values at the beginning
    count = 0
    positive = 0
    negative = 0
    neutral = 0
    favorite = 0
    summation_score = 0
    favorite_count = 0
    favorite_sum = 0
    retweets = 0
    sum_retweet = 0
    count_ret = 0
    sum_count = 0
    count_count = 0

    # This dictionary where all values will be stored
    report_make = {}

    # Number of tweets
    report_make["num_tweets"] = len(tweet_list)

    # For loop to find the average sentiment value
    for i in tweet_list:
        summation_score += calc_sentiment(i["text"], keyword_dict)
        count += 1

    average = summation_score / count if count > 0 else 0
    report_make["avg_sentiment"] = float("{:.2f}".format(average))

    # For loop to find the Negative, Positive, Neutral occurrence.
    for j in tweet_list:
        sentiment = classify(calc_sentiment(j["text"], keyword_dict))
        if sentiment == "Positive":
            positive += 1
        elif sentiment == "Negative":
            negative += 1
        else:
            neutral += 1

    report_make["num_negative"] = negative
    report_make["num_neutral"] = neutral
    report_make["num_positive"] = positive

    # For loop to find the times a tweet was favorited or liked.
    for k in tweet_list:
        if k["favorite"] == 0:
            continue
        if k["favorite"] != "Null":
            favorite += 1

    report_make["num_favorite"] = favorite

    # For loop to find the average of favorited or liked tweets.
    for k in tweet_list:
        if k["favorite"] == 0:
            continue
        if k["favorite"] != "Null":
            favorite_sum += calc_sentiment(k["text"], keyword_dict)
            favorite_count += 1
    avg_fav = favorite_sum / favorite_count if favorite_count > 0 else 0
    report_make["avg_favorite"] = float("{:.2f}".format(avg_fav))

    # For loop to find the number of retweets.
    for i in tweet_list:
        if i["retweet"] == 0:
            continue
        if i["retweet"] != "Null":
            retweets += 1
    report_make["num_retweet"] = retweets

    # For loop to find Average sentiment of favorited tweets.
    for i in tweet_list:
        if i["retweet"] == 0:
            continue
        if i["retweet"] != "Null":
            sum_retweet += calc_sentiment(i["text"], keyword_dict)
            count_ret += 1
    retweetsent_Avg = sum_retweet / count_ret if count_ret > 0 else 0
    report_make["avg_retweet"] = float("{:.2f}".format(retweetsent_Avg))

    # For loop for Top five countries by average sentiment
    country_sent = {}
    country_count = {}
    for i in tweet_list:
        if i["country"] != "Null":
            if i["country"] not in country_count.keys():
                country_count[i["country"]] = 1
            else:
                country_count[i["country"]] += 1

            sum_count += calc_sentiment(i["text"], keyword_dict)
            count_count += 1

    avgSentRetw = sum_count / count_count if count_count > 0 else 0

    # Ranking sentiments for individual contries
    for i in tweet_list:
        if i["country"] == "NULL":
            continue

        if i["country"] != "Null":
            if i["country"] in country_sent.keys():
                country_sent[i["country"]] += calc_sentiment(i["text"], keyword_dict)
            else:
                country_sent[i["country"]] = calc_sentiment(i["text"], keyword_dict)

    for country in country_sent.keys():
        country_sent[country] = country_sent[country] / country_count[country]

    # Sort the countries in descending order
    top_5_keys = sorted(country_sent, key=country_sent.get, reverse=True)[:5]

    result_string = ", ".join(top_5_keys)

    report_make["top_five"] = result_string

    return report_make


# Creating the report file
def write_report(report, output_file):
    with open(output_file, "w", encoding="utf-8") as output:
        output.write(
            f"Average sentiment of all tweets: {report['avg_sentiment']:.2f}\n"
        )
        output.write(f"Total number of tweets: {report['num_tweets']}\n")
        output.write(f"Number of positive tweets: {report['num_positive']}\n")
        output.write(f"Number of negative tweets: {report['num_negative']}\n")
        output.write(f"Number of neutral tweets: {report['num_neutral']}\n")
        output.write(f"Number of favorited tweets: {report['num_favorite']}\n")
        output.write(
            f"Average sentiment of favorited tweets: {report['avg_favorite']:.2f}\n"
        )
        output.write(f"Number of retweeted tweets: {report['num_retweet']}\n")
        output.write(
            f"Average sentiment of retweeted tweets: {report['avg_retweet']:.2f}\n"
        )
        output.write(f"Top five countries by average sentiment: {report['top_five']}\n")
