import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
from collections import Counter


st.set_page_config(
    page_title="Parasight AI",
    page_icon="🦠",
    layout="centered"
)


st.title("🦠 Parasight AI")

st.markdown("""
AI-powered parasite egg detection using YOLOv8 model.
Upload a microscopic image to analyze and detect parasite eggs automatically.
""")

model = YOLO("parasite.pt")


with st.expander(" View Model Information"):

    st.markdown("""
    ### Model Details

    - **Model:** YOLOv8
    - **Dataset Classes:** 8
    - **Validation Images:** 168
    

    ### Performance Metrics

    - **Precision:** 81.1%
    - **Recall:** 71.1%
    - **mAP50:** 80.4%
    - **mAP50-95:** 64.5%

    ### Supported Parasites Performance

    - Ancylostoma Spp → Precision: 83.5% | mAP50: 85.3%
    - Ascaris Lumbricoides → Precision: 85.4% | mAP50: 91.4%
    - Enterobius Vermicularis → Precision: 71.0% | mAP50: 76.7%
    - Fasciola Hepatica → Precision: 78.7% | mAP50: 53.4%
    - Hymenolepis → Precision: 77.3% | mAP50: 84.0%
    - Schistosoma → Precision: 86.9% | mAP50: 71.6%
    - Taenia Sp → Precision: 78.8% | mAP50: 85.1%
    - Trichuris Trichiura → Precision: 87.4% | mAP50: 96.1%
    """)


confidence = st.slider(
    "Confidence Threshold",
    min_value=0.1,
    max_value=1.0,
    value=0.25
)


uploaded_file = st.file_uploader(
    "Upload Microscopic Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    # BEFORE IMAGE
    st.subheader("Before Prediction")
    st.image(
        image,
        caption="Original Microscopic Image",
        use_container_width=True
    )

    # SAVE TEMP IMAGE
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:

        image.save(temp_file.name)

        # MODEL PREDICTION
        results = model.predict(
            temp_file.name,
            conf=confidence
        )

    # DRAW RESULTS
    annotated_image = results[0].plot()

    # CONVERT BGR TO RGB
    annotated_image = annotated_image[:, :, ::-1]

    # AFTER IMAGE
    st.subheader("After Prediction")
    st.image(
        annotated_image,
        caption="Detected Parasite Eggs",
        use_container_width=True
    )

    st.subheader("Detection Results")

    boxes = results[0].boxes

    if len(boxes) > 0:

        names = model.names
        detected_classes = []

        for box in boxes:

            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            parasite_name = names[cls_id]

            detected_classes.append(parasite_name)

            st.success(
                f"{parasite_name} detected "
                f"with confidence: {conf:.2f}"
            )

      
        st.subheader("Parasite Count")

        counts = Counter(detected_classes)

        for parasite, count in counts.items():

            st.info(f"{parasite}: {count}")

    else:

        st.warning("No parasite eggs detected.")
    
st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 14px;'>
        🦠 Parasight AI <br>
         Application Developed by Sarah © 2026 <br><br>
         ⚠️ This AI system is intended for research and diagnostic assistance only.  
    </div>
    """,
    unsafe_allow_html=True
)