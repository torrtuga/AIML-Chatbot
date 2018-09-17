import os
import aiml
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

BRAIN_FILE="brain.dump"
SENTIMENT_ANALYSIS = 0
SENTIMENT_ANALYSIS_FLAG = 0
MAX_NEG = "xxx"
NEG = "xxy"
NEUTRAL = "xyx"
POSITIVE = "xyy"
MAX_POSITIVE = "yxx"

analyser = SentimentIntensityAnalyzer()
k = aiml.Kernel()

def get_sentiment_map(score):
	sentiment_score = None
	if score <= -0.5:
		sentiment_score = MAX_NEG
	elif score > -0.5 and score < 0:
		sentiment_score = NEG
	elif score == 0:
		sentiment_score = NEUTRAL
	elif score > 0 and score < 0.5:
		sentiment_score = POSITIVE
	else:
		sentiment_score = MAX_POSITIVE
	return sentiment_score


def get_sentiment_scores(sentence):
    sentiment_compound_value = analyser.polarity_scores(sentence)['compound']
    return get_sentiment_map(sentiment_compound_value)

def sentiment_operation_check(sentence):
	sentiment_operation_check_flag = 0
	substring_1 = "Good to meet you"
	substring_2 = "How are you?"
	substring_3 = "do you want to learn a new language today?"
	substring_4 = "how about learning a new language today?"

	if substring_1 in sentence and substring_2 in sentence or substring_3 in sentence or substring_4 in sentence:
		sentiment_operation_check_flag = 1

	return sentiment_operation_check_flag


if __name__ == "__main__":
	# if os.path.exists(BRAIN_FILE):
	#     print("Loading from brain file: " + BRAIN_FILE)
	#     k.loadBrain(BRAIN_FILE)
	# else:
	#     print("Parsing aiml files")
	#     k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
	#     print("Saving brain file: " + BRAIN_FILE)
	#     k.saveBrain(BRAIN_FILE)
	print("Parsing aiml files")
	k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")

	print("Hi, I am Athena, a Language Tutor Chatbot.\nWhat's your name?")
	while True:
	    input_text = input("> ")

	    if SENTIMENT_ANALYSIS_FLAG == 1:
	    	user_sentiment = get_sentiment_scores(input_text)
	    	input_text = input_text + " " + user_sentiment
	    	input_text = input_text.replace(".", " ")
	    	
	    	
	    response = k.respond(str(input_text))
	    print(response)
	    if sentiment_operation_check(response)==1:
	    	SENTIMENT_ANALYSIS_FLAG = 1
	    else:
	    	SENTIMENT_ANALYSIS_FLAG = 0