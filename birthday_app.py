import streamlit as st

# Function to display the first page with the gift box
def main_page():
    # Apply custom title styling using Markdown and HTML
    st.markdown("""
    <style>
        .title {
            font-family: 'Times New Roman', serif;
            font-size: 36px;
            color: #B22222; /* Brick red */
            font-style: italic;
            text-align: center;
        }
        .heart {
            color: #FFFFFF; /* White heart */
        }
        .birthday-message {
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            color: #B8860B;  /* Dark yellow color */
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <div class="title">
        Happieeee Birthdayyyy Babieeee! <span class="heart">❤️</span>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns for the layout
    col1, col2 = st.columns([1, 3])  # The first column is narrower for the GIF and second image

    # Display the GIF and second image in the first column (left side)
    with col1:
        gif_url = "https://i.pinimg.com/originals/b5/c1/f1/b5c1f10192ce092412534f0af8ea72e4.gif"  # Replace with your GIF URL
        st.image(gif_url, width=200)  # Adjust width to your preference

        # Display another image below the GIF
        second_image_url = "https://i.pinimg.com/736x/26/33/96/263396076e0c23e658255898692555bb.jpg"  # Replace with the URL of your second image
        st.image(second_image_url, width=200)  # Adjust width to your preference

        # Use columns to align third image and new image side by side
        col3, col4 = st.columns([1, 1])  # Creating two columns in the first column for side-by-side images

        with col3:
            # Display the third (small logo-like) image
            third_image_url = "https://i.pinimg.com/736x/a8/42/ba/a842ba1c055522fbf1cff787f40b253f.jpg"  # Replace with your logo URL
            st.image(third_image_url, width=350)  # Set the width to a small size (logo size)

        with col4:
            # Display the new image closer to the right side of the third image
            new_image_url = "https://i.pinimg.com/736x/b4/a9/f9/b4a9f931fd06e54bc2a526632755d6a6.jpg"  # Replace with the URL of the new image
            st.image(new_image_url, width=150)  # Display the new image with a small width like the third image

    # Display the huge gift box image in the second column (right side)
    with col2:
        gift_image_url = "https://img.freepik.com/free-photo/wood-surprise-copyspace-wooden-box_1150-1625.jpg?t=st=1739361462~exp=1739365062~hmac=abc1400873a40d083efd7f67a2e34a4ab0e503998abd9c03d2842658e3e29949&w=826"
        st.image(gift_image_url, width=600)

        # Display the "இனிய பிறந்தநாள் வாழ்த்துக்கள்" message with a heart in dark yellow
        st.markdown('<div class="birthday-message">இனிய பிறந்தநாள் வாழ்த்துக்கள் ❤️</div>', unsafe_allow_html=True)
    
    # When the image is clicked, show the "Open your gift" message
    if st.button("Click to open your gift"):
        st.session_state.page = "gift_page"  # Redirect to the next page

# Function to display the second page with the audio file
def gift_page():
    # Create two columns for the layout
    col1, col2 = st.columns([1, 3])  # Adjust column ratio as needed
    
    with col1:
        # Display an image on the left side of the title
        image_url = "https://img.freepik.com/premium-vector/vector-kawai-cat-is-listening-music_995281-2173.jpg?w=740"  # Replace with your image URL
        st.image(image_url, width=150)  # Adjust width as needed

    with col2:
        # Title for the audio page with styling
        st.markdown("""
        <style>
            .audio-title {
                font-family: 'Times New Roman', serif;
                font-size: 36px;
                color: #B22222; /* Brick red */
                font-style: italic;
                text-align: center;
            }
        </style>
        <div class="audio-title">
            Your Birthday Gift is hereeeee pls use your headphones! 🎧
        </div>
        """, unsafe_allow_html=True)
    
    # Replace with the actual audio file path or URL
    audio_file = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"  # Example path, update as needed
    st.audio(audio_file, format="audio/mp3")
    
    st.write("Did you like it??")
    
    # Display an image below the "Did you like it??"
    image_below_url = "https://i.pinimg.com/736x/f3/55/d4/f355d4c73ff8d3739dd4c6f08818faa0.jpg"  # Replace with the URL of the image you want to show
    st.image(image_below_url, width=250)  # Adjust width as needed

# Streamlit layout logic
def app():
    if "page" not in st.session_state:
        st.session_state.page = "main"  # Initialize the session state to the main page

    # Show the correct page based on the session state
    if st.session_state.page == "main":
        main_page()
    elif st.session_state.page == "gift_page":
        gift_page()

# Run the app
if __name__ == "__main__":
    app()
