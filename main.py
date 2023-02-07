import glob
import streamlit
import datetime
import nltk
import plotly.express as express
import nltk.sentiment as sentiment

diary_entries = sorted(glob.glob("files/diary/*.txt"))

analyzed_dict = {}
positive_dict = {}
negative_dict = {}
dates = []
analyzer = sentiment.SentimentIntensityAnalyzer()
for diary in diary_entries:
    with open(diary, "r") as file:
        date = datetime.datetime.strptime(diary.strip(".txt")[-8:], "%y-%m-%d").strftime("%B %d %Y")
        analyzed_dict[date] = analyzer.polarity_scores(file.read())
        positive_dict[date] = analyzed_dict[date]["pos"]
        negative_dict[date] = analyzed_dict[date]["neg"]

for key, value in analyzed_dict.items():
    print(f"{key}: {value}")
    print(positive_dict[key])
    print(negative_dict[key])
    print("\n")

streamlit.title("Diary Tone Analyzer")

streamlit.subheader("Positivity")

plotly_figure = express.line(x=positive_dict.keys(), y=positive_dict.values(), labels={"x": "Date", "y": "Positivity"})
streamlit.plotly_chart(plotly_figure)

streamlit.subheader("Negativity")

plotly_figure = express.line(x=negative_dict.keys(), y=negative_dict.values(), labels={"x": "Date", "y": "Negativity"})
streamlit.plotly_chart(plotly_figure)

