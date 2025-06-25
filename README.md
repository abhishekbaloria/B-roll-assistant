 #  B-Roll Assistant

A simple and beginner-friendly video helper app built using Streamlit.  
The idea? Help content creators (like me) quickly find high-quality b-rolls based on the mood, theme, and style of their video.

This project was created as part of my first-semester coursework — combining basic Python skills with real-world creativity.

---

##  What It Does

- Lets you pick from 4 main video types:
  - **Fitness** (e.g., gym clips)
  - **Travel** (nature & city shots)
  - **Cooking** (healthy & fast food)
  - **Tech** (programming or setup)
  
- Each category includes multiple subtopics
- Click a button to preview a **random video**
- Save your favorite clips
- Get **custom suggestions** by answering a few simple questions (like your video's purpose, vibe, or setting)
- Submit feedback — it gets stored in a local file called `feedback.txt`

---

##  How to Run It

1. Make sure Python is installed  
2. Install Streamlit (just once):

```bash
  pip install streamlit
  ```

2.  **Save the Code:** Save all the files on a same folder for you to run  .

3.  **Run the Game:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run:
    ```bash
    streamlit run index1.py
    ```

    This will automatically open the game in your web browser.

    ---

##  How the App Works

1. **Pick a Category:** Use the sidebar to choose what type of video you want to  work on — like Fitness, Travel, Cooking, or Tech — and then pick a subcategory (like arms, nature, fast food, etc.).
2. **Preview Clips:** Click “Show Random Video” to get a quick view of a related b-roll. The video will play right inside the app.
3. **Save What You Like:** If a clip feels right, hit “Add to Favorites” — you can watch your saved ones anytime from the sidebar.
4. **Get Suggestions:** Not sure what to use? answer some  quick questions about your video’s mood, setting, and purpose — the app will suggest good b-rolls automatically.
5. **Leave Feedback:** At the end of the page, there’s a simple box where you can drop feedback or ideas. It saves to a file for future improvements.

---

##  What’s Happening in the Background

- The whole app runs on **Streamlit** (makes it look like a clean website)
- I used **Python dictionaries** to organize all the video categories and links
- It picks clips randomly using the `random` module
- Favorites are stored using **Streamlit’s session memory** so they don’t vanish when you switch categories
- Feedback is saved in a text file called `feedback.txt` using basic Python file handling

---

## Future Improvements (Stuff I’ll Add Later)

This is just the start. Here are a few things I plan to add next:

- **Camera Position Guide:** Along with each b-roll suggestion, I want to show where to place the camera, what angle to shoot from, and how to stand — so it’s easier for creators to recreate the shots.

- **Upload Your Own B-Rolls:** A feature to upload and organize your own clips, so you can build a personal library over time.

- **Mood & Lighting Filters:** Add filters like "low light", "sunlight", or "calm vibe" to get even better suggestions.

- **Save Project Boards:** Let users save b-roll sets under project names (like “Gym Video” or “Street Vlog”) and come back to them anytime.

These are small ideas I’ll build on as I keep learning.

##  How to Run on Windows

1. Install Python from https://python.org  
2. Open Command Prompt and run:  
   pip install streamlit  
3. Download or clone this project from GitHub  
4. Navigate to the folder where index1.py is located  
5. Run the app with:  
   streamlit run index1.py  
