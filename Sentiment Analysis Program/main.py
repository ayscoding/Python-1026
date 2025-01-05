""" 
Date: 12 Nov 2023
This file contain the main function to initiate Sentiment Analysis. 
"""

# main file
from sentiment_analysis import read_keywords, read_tweets, make_report, write_report


def main():
    try:
        # Inputs & Outputs
        keywords_file = input("Input keyword filename (.tsv file): ").strip()
        tweets_file = input("Input tweet filename (.csv file): ").strip()
        output_file = input("Input filename to output report in (.txt file): ").strip()

        # Functions
        keywords = read_keywords(firstfile=keywords_file)

        # Check if the keywords file is valid
        if not keywords:
            raise ValueError("Invalid keywords file. Make sure it's not empty.")

        tweets = read_tweets(secondfile=tweets_file)

        # Check if the tweets file is valid
        if not tweets:
            raise ValueError("Invalid tweets file. Make sure it's not empty.")

        report = make_report(tweets, keywords)

        # Check if the output file is valid
        if not output_file.lower().endswith(".txt"):
            raise ValueError("Invalid report file. Please provide a valid '.txt' file.")

        write_report(report, output_file)
        print("Report generated successfully.")
    except FileNotFoundError as e:
        raise (f"Error: {e}")
    except ZeroDivisionError as e:
        raise (f"Error: {e}")
    except ValueError as e:
        raise (f"Error: {e}")
    except Exception as e:
        raise (f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
