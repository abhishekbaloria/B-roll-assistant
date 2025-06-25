import streamlit as st 
import random
#page title and layout to wide 
st.set_config(page_title="B-Roll Assistant", layout="wide") 

# this database stores the URLs of b-roll videos categorized by themes and subcategories.
video_db = {
    "fitness": {
        "arms": [
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
            "https://videos.pexels.com/video-files/6614725/6614725-uhd_2560_1440_25fps.mp4",
            "https://videos.pexels.com/video-files/857152/857152-hd_1920_1080_30fps.mp4",
            "https://videos.pexels.com/video-files/856983/856983-hd_1920_1080_25fps.mp4"
        ],
        "urban": [
            "https://videos.pexels.com/video-files/855015/855015-hd_1920_1080_30fps.mp4",
            "https://videos.pexels.com/video-files/3215764/3215764-hd_1920_1080_30fps.mp4",
            "https://videos.pexels.com/video-files/854962/854962-hd_1920_1080_30fps.mp4"
        ]
    },
    
