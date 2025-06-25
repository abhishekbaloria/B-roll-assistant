import json
import streamlit as st
import random

#setup of the layout and title of the web app 
st.set_page_config(page_title="B-Roll Assistant", layout="wide")
st.title(" B-Roll Assistant")
st.write("Pick and preview b-roll videos based on the type of video you're creating.")

# this will Load video links (organized by category and subcategory) from a JSON file.
# Each category like 'fitness' has subcategories like 'arms', 'legs' etc.
def load_video_data():
    with open("videos.json", "r") as f:
        return json.load(f)
#load the data
video_db = load_video_data()

# Sidebar- this will help people to choose thier categorys and subcategories of the videos they want to make 
st.sidebar.header(" Choose a Category")
main_category = st.sidebar.selectbox("Main Category", list(video_db.keys()))
sub_category = st.sidebar.selectbox("Subcategory", list(video_db[main_category].keys()))

#this part helps to show random videos from the subcategary selected by the user 
if st.sidebar.button(" Show Random Video"):
    selected = random.choice(video_db[main_category][sub_category])
    st.video(selected)
else:
    selected = None  # Nothing selected yet

# Favorites- a person can select the video they like 
st.sidebar.header(" Your Favorites")
favorites = st.session_state.get("fav_list", [])

#  this section helps you to put selected video to saved 
if st.sidebar.button("➕ Add to Favorites") and selected:
    favorites.append(selected)
    st.session_state.fav_list = favorites

# this will show all the videos that are saved as favorite 
for f in favorites:
    st.sidebar.video(f)

#gives output in accordance to the answers given to the suggestion section 
st.markdown("---")
st.header(" Not Sure What to Pick?")
st.write("Answer a few quick questions and we’ll suggest something!")

#this section has questions to personalize recommendations of videos 
topic = st.radio("What is your video about?", ["Fitness", "Travel", "Cooking", "Tech"])
mood = st.selectbox("What kind of mood do you want your video to be?", ["Energetic", "Calm", "Inspiring", "Fun"])
location = st.selectbox("Where are you filming?", ["Indoors", "Outdoors"])

# Show suggestions 
if st.button(" Suggest B-Rolls"):
    if topic == "Fitness":
        suggestions = video_db["fitness"]["arms"] + video_db["fitness"]["legs"]
    elif topic == "Travel":
        suggestions = video_db["travel"]["nature"] + video_db["travel"]["urban"]
    elif topic == "Cooking":
        suggestions = video_db["cooking"]["healthy"] + video_db["cooking"]["fast food"]
    elif topic == "Tech":
        suggestions = video_db["tech"]["programming"] + video_db["tech"]["setup"]

    random.shuffle(suggestions)  # Randomize suggestion order 
    st.subheader(" Suggested Clips:")
    for i, link in enumerate(suggestions[:4], 1):  # Shows up to 4 suggestions at once 
        st.markdown(f"**Option {i}:**")
        st.video(link)

#this section is made to get feeback for future improvemnt of the project 
st.markdown("---")
st.header(" Feedback")
user_feedback = st.text_area("Let us know what you think!")

if st.button(" Submit Feedback"):
    # Save feedback to a file
    with open("feedback.txt", "a") as f:
        f.write(f"\nFeedback: {user_feedback}\n")
    st.success("Thanks for your feedback!")

# project ending 
st.markdown("---")
st.markdown(" Made by Abhishek — The idea of this project came from my intrest in videography and editing  .")