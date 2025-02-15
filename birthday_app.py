import streamlit as st
import requests
import os

def main_page():
    st.markdown("""
    <style>
        .title { font-family: 'Times New Roman', serif; font-size: 36px; color: #B22222; font-style: italic; text-align: center; }
        .heart { color: #FFFFFF; }
        .birthday-message { font-family: 'Arial', sans-serif; font-size: 24px; color: #B8860B; text-align: center; margin-top: 20px; }
    </style>
    <div class="title">
        Happieeee Birthdayyyy Babieeee<span class="heart">🤍</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    
    with col1:
        gif_url = "https://i.pinimg.com/originals/b5/c1/f1/b5c1f10192ce092412534f0af8ea72e4.gif"
        st.image(gif_url, width=200)
        second_image_url = "https://i.pinimg.com/736x/26/33/96/263396076e0c23e658255898692555bb.jpg"
        st.image(second_image_url, width=200)
    
    with col2:
        gift_image_url = "https://img.freepik.com/free-photo/wood-surprise-copyspace-wooden-box_1150-1625.jpg"
        st.image(gift_image_url, width=600)
        st.markdown('<div class="birthday-message">இனிய பிறந்தநாள் வாழ்த்துக்கள்🤍</div>', unsafe_allow_html=True)
    
    if st.button("Click to open your gift"):
        st.session_state.page = "gift_page"

def gift_page():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        image_url = "https://img.freepik.com/premium-vector/vector-kawai-cat-is-listening-music_995281-2173.jpg"
        st.image(image_url, width=150)
    
    with col2:
        st.markdown("""
        <style>
            .audio-title { font-family: 'Times New Roman', serif; font-size: 36px; color: #B22222; font-style: italic; text-align: center; }
        </style>
        <div class="audio-title">
            Your Birthday Gift is hereeeee pls use your headphones! 🎧
        </div>
        """, unsafe_allow_html=True)
    
    
    local_audio_path = "C:\\Chutamale.m4a"
    
    try:
        response = requests.get(google_drive_url)
        if response.status_code == 200:
            st.audio(response.content, format="audio/m4a")
        else:
            raise Exception("Google Drive failed")
    except:
        if os.path.exists(local_audio_path):
            with open(local_audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/m4a")
        else:
            st.error("⚠️ Audio file not found! Please check the file location.")
    
    col5, col6 = st.columns([1, 1])
    
    with col5:
        image_below_url = "https://media1.tenor.com/m/YdX_1WLlaC4AAAAd/alverda-verdansa.gif"
        st.image(image_below_url, width=150)
    
    with col6:
        new_left_image_url = "https://media.tenor.com/0RDUsEAznV8AAAAj/girl-cute.gif"
        st.image(new_left_image_url, width=160)
        st.markdown("""
        <style>
            .right-align { position: absolute; right: 0; top: 10px; font-size: 20px; }
        </style>
        <div class="right-align">Finished listening? Ok, now call me!</div>
        """, unsafe_allow_html=True)

def app():
    if "page" not in st.session_state:
        st.session_state.page = "main"
    if st.session_state.page == "main":
        main_page()
    elif st.session_state.page == "gift_page":
        gift_page()

if __name__ == "__main__":
    app()
