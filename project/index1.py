import streamlit as st
import random

#setup of the layout and title of the web app 
st.set_page_config(page_title="B-Roll Assistant", layout="wide")
st.title(" B-Roll Assistant")
st.write("Pick and preview b-roll videos based on the type of video you're creating.")

# this function shows the video as divided to diffrent category and sub category for example in fitness videos subcategory would be the body parts of the specific fitness workout 
def get_video_data():
    return {
        "fitness": {
            "arms": [
                # the video links are direct .mp4 files that can be directly displayed on the web app 
                "https://media.musclewiki.com/media/uploads/videos/branded/male-Cables-cable-push-down-front.mp4#t=0.1",
                "https://media.musclewiki.com/media/uploads/videos/branded/male-bodyweight-chinup-side.mp4#t=0.1",
                "https://media.musclewiki.com/media/uploads/videos/branded/male-Barbell-barbell-curl-side.mp4#t=0.1",
                "https://media.musclewiki.com/media/uploads/videos/branded/male-Kettlebells-kettlebell-goblet-curl-side.mp4#t=0.1"
            ],
            "legs": [
                "https://media.musclewiki.com/media/uploads/videos/branded/male-Kettlebells-kettlebell-single-arm-forward-lunge-side.mp4#t=0.1",
                "https://media.musclewiki.com/media/uploads/videos/branded/male-Kettlebells-kettlebell-calf-raise-side.mp4#t=0.1",
                "https://media.musclewiki.com/media/uploads/videos/branded/male-Kettlebells-kettlebell-staggered-deadlift-single-side.mp4#t=0.1",
                "https://media.musclewiki.com/media/uploads/videos/branded/male-Dumbbells-dumbbell-bulgarian-split-squat-side.mp4#t=0.1"
            ]
        },
        "travel": {
            "nature": [
                "https://videos.pexels.com/video-files/2894891/2894891-uhd_2560_1440_24fps.mp4",
                "https://videos.pexels.com/video-files/3018669/3018669-hd_1920_1080_24fps.mp4"
            ],
            "urban": [
                "https://videos.pexels.com/video-files/5857311/5857311-uhd_1440_2732_25fps.mp4",
                "https://videos.pexels.com/video-files/852352/852352-hd_1920_1080_30fps.mp4",
                "https://videos.pexels.com/video-files/7251030/7251030-uhd_1440_2560_25fps.mp4"
            ]
        },
        "cooking": {
            "healthy": [
                "https://videos.pexels.com/video-files/4360751/4360751-uhd_2560_1440_25fps.mp4",
                "https://videos.pexels.com/video-files/4252335/4252335-uhd_1440_2732_25fps.mp4",
                "https://videos.pexels.com/video-files/3195942/3195942-uhd_2560_1440_25fps.mp4"
            ],
            "fast food": [
                "https://videos.pexels.com/video-files/3196344/3196344-uhd_2560_1440_25fps.mp4",
                "https://videos.pexels.com/video-files/2922562/2922562-hd_1920_1080_25fps.mp4"
            ]
        },
        "tech": {
            "programming": [
                "https://videos.pexels.com/video-files/852421/852421-hd_1920_1080_30fps.mp4",
                "https://videos.pexels.com/video-files/5495845/5495845-hd_1920_1080_30fps.mp4",
                "https://videos.pexels.com/video-files/2887463/2887463-hd_1920_1080_25fps.mp4"
            ],
            "setup": [
                "https://videos.pexels.com/video-files/7914824/7914824-hd_1920_1080_30fps.mp4",
                "https://videos.pexels.com/video-files/30470982/13057074_2560_1440_24fps.mp4",
                "https://videos.pexels.com/video-files/30470981/13057092_2560_1440_24fps.mp4"
            ]
        }
    }

# Load the video list
video_db = get_video_data()

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