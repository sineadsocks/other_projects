from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyse_sentiment(sentence):
    analyser = SentimentIntensityAnalyzer()
    sentiment_score = analyser.polarity_scores(sentence)
    
    # Classify sentiment based on compound score
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    print("Enter a sentence to analyse its sentiment (type 'exit' to quit)")

    while True:
        user_input = input("Enter a sentence: ")

        if user_input.lower() == 'exit':
            print("Exiting")
            break
        
        sentiment = analyse_sentiment(user_input)
        print("Sentiment:", sentiment)

if __name__ == "__main__":
    main()
