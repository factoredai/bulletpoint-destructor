import streamlit as st

from src.modeling.bullet_extractor import BulletExtractor

bullet_extractor = BulletExtractor()

st.header("Bullet point destructor")

bullet_point = st.text_input(label="Provide a raw bullet point", value="")

bullet_point_descriptors = bullet_extractor.extract_entities(bullet_point=bullet_point)

st.subheader("What was the project about?")

st.write(bullet_point_descriptors["what"])

st.subheader("How was the project developed?")

st.write(bullet_point_descriptors["how"])

st.subheader("What were the client's needs? Why it was developed?")

st.write(bullet_point_descriptors["why"])

st.subheader("For whom was the project developed ?")

st.write(bullet_point_descriptors["whom"])

st.subheader("Which skills and tools were used for it?")

st.write(bullet_point_descriptors["skills"])
