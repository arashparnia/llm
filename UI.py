from io import BytesIO

import requests
import streamlit as st
import os
import tempfile
from PIL import Image
from service.ChatGPTService import ChatGPTService
from service.ExerciseGenerator import ExerciseGenerator

# Initialize ExerciseGenerator and ChatGPTService
exercise_generator = ExerciseGenerator()
chat_gpt_service = ChatGPTService()

st.title("Exercise Generator")

# User input for age, difficulty, scenario, and character
age = st.slider("Select the age of the child:", min_value=4, max_value=12, value=6)
difficulty = st.slider("Select the difficulty level:", min_value=1, max_value=5, value=3)
scenario = st.text_input("Enter the scenario:")
character = st.text_input("Enter the main character:")

# Define audio_file_path outside of the block
audio_file_path = None

if st.button("Generate Exercise"):
    # Generate the exercise using ExerciseGenerator
    exercise = exercise_generator.generate_exercise(age, difficulty, scenario, character)

    # Display exercise text, answer, and image
    st.subheader("Exercise Text:")
    st.write(exercise["exercise"])

    st.subheader("Answer:")
    st.write(exercise["answer"])

    audio_bytes = exercise["audio"]

    # Save the MP3 audio data to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_mp3:
        temp_mp3.write(audio_bytes)
        audio_file_path = temp_mp3.name

    # Display the generated image
    # Download and display the generated image from the URL
    st.subheader("Generated Image:")
    image_url = exercise["image"]
    image_data = requests.get(image_url)
    image = Image.open(BytesIO(image_data))
    st.image(image, caption="Generated Image", use_column_width=True)

    # Play the saved audio file with the correct format
    st.subheader("Generated Audio:")
    st.audio(audio_file_path, format="audio/mpeg")

# Reset button to clear user inputs
if st.button("Reset"):
    st.experimental_rerun()

# Clean up temporary audio file if it exists
if audio_file_path is not None:
    os.remove(audio_file_path)
