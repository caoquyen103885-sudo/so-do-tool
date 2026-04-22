import streamlit as st
from PIL import Image, ImageDraw
import requests
from io import BytesIO

st.title("📄 Tool che sổ đỏ + map lô đất")

uploaded_file = st.file_uploader("Upload ảnh sổ đỏ", type=["jpg", "png"])

lat = st.text_input("Latitude")
lng = st.text_input("Longitude")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh gốc", use_column_width=True)

    st.write("👉 Chọn vùng cần che (ước lượng)")

    x = st.slider("X", 0, image.width, 0)
    y = st.slider("Y", 0, image.height, 0)
    w = st.slider("Width", 10, 500, 100)
    h = st.slider("Height", 10, 500, 100)

    if st.button("🔒 Che vùng đã chọn"):
        img_draw = image.copy()
        draw = ImageDraw.Draw(img_draw)
        draw.rectangle([x, y, x+w, y+h], fill="black")
        st.image(img_draw, caption="Ảnh đã che")

if lat and lng:
    if st.button("🗺️ Tạo bản đồ"):
        url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=17&size=600x400&markers=color:red%7C{lat},{lng}&key=YOUR_API_KEY"
        response = requests.get(url)
        map_img = Image.open(BytesIO(response.content))
        st.image(map_img, caption="Google Map")
