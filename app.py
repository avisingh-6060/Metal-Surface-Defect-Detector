import streamlit as st
import tensorflow as tf
import json
import pandas as pd
import plotly.express as px

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import navy, darkgreen, red
from reportlab.lib.units import inch
from datetime import datetime
from PIL import Image
import os
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor

def generate_pdf(
    predicted_class,
    confidence,
    reliability,
    description,
    recommendation
):
    filename = "inspection_report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)

    width, height = letter

    logo_path = "hindalco_logo.png"

    if os.path.exists(logo_path):
        logo = ImageReader(logo_path)
        c.drawImage(
            logo,
            60,
            height - 80,
            width=120,
            height=40,
            preserveAspectRatio=True,
            mask='auto'
        )

    y = height - 105

        # Company Name
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(180, height - 55, "HINDALCO INDUSTRIES LIMITED")

    # Subtitle
    c.setFillColor(darkgreen)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(
        180,
        height - 82,
        "AI-Based Metal Surface Defect Inspection Report"
    )

    # Blue Divider
    c.setStrokeColor(navy)
    c.setLineWidth(1.5)
    c.line(180, height - 95, width - 55, height - 95)

    # Report ID
    report_id = f"MSD-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    c.setFillColor(darkgreen)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(180, height - 120, "Report ID")

    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica",11)
    c.drawString(180, height - 138, report_id)

    # Generated On
    c.setFillColor(darkgreen)
    c.setFont("Helvetica-Bold",11)
    c.drawString(390, height - 120, "Generated On")

    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica",11)
    c.drawString(
        390,
        height - 138,
        datetime.now().strftime("%d-%m-%Y %I:%M %p")
    )

    y = height - 185

    # Card Border
    box_x = 55
    box_y = y - 155
    box_width = 500
    box_height = 190

    c.setStrokeColor(navy)
    c.setLineWidth(1.2)
    c.roundRect(box_x, box_y, box_width, box_height, 8)

    # Blue Header
    c.setFillColor(navy)
    c.roundRect(box_x, box_y + box_height - 30, box_width, 30, 8, stroke=0, fill=1)

    c.setFillColorRGB(1,1,1)
    c.setFont("Helvetica-Bold",13)
    c.drawString(box_x + 15, box_y + box_height - 20, "PREDICTION RESULT")

    y = box_y + box_height - 55

    # ---------- Prediction Rows ----------

    rows = [
        ("Predicted Defect", predicted_class.replace("_", " ").title(), red),
        ("Confidence", f"{confidence:.2f} %", darkgreen),
        ("Prediction Reliability", reliability, darkgreen),
        ("Model Used", "EfficientNetB0", None),
        ("Overall Model Accuracy", "99.20 %", None),
    ]

    c.setFont("Helvetica", 12)

    for label, value, color in rows:

        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 12)
        c.drawString(75, y, label)

        c.drawString(235, y, ":")

        if color:
            c.setFillColor(color)
        else:
            c.setFillColorRGB(0, 0, 0)

        c.setFont("Helvetica-Bold", 12)
        c.drawString(255, y, value)

        y -= 28

    y -= 15

    # ---------------- Defect Description ----------------

    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(60, y, "Defect Description")

    y -= 10

    desc_box_x = 55
    desc_box_y = y - 65
    desc_box_width = 500
    desc_box_height = 55

    c.setStrokeColor(navy)
    c.setLineWidth(1)

    c.roundRect(
        desc_box_x,
        desc_box_y,
        desc_box_width,
        desc_box_height,
        6
    )

    text = c.beginText(desc_box_x + 10, desc_box_y + 35)
    text.setFillColorRGB(0,0,0)
    text.setFont("Helvetica",11)
    text.textLines(description)
    c.drawText(text)

    y = desc_box_y - 25

    # ---------------- Recommendation ----------------

    c.setFillColor(darkgreen)
    c.setFont("Helvetica-Bold",15)
    c.drawString(60,y,"Recommendation")

    y -= 10

    rec_box_x = 55
    rec_box_y = y - 70
    rec_box_width = 500
    rec_box_height = 60

    c.setStrokeColor(darkgreen)
    c.setLineWidth(1)

    c.roundRect(
        rec_box_x,
        rec_box_y,
        rec_box_width,
        rec_box_height,
        6
    )

    text = c.beginText(rec_box_x + 10, rec_box_y + 40)
    text.setFillColorRGB(0,0,0)
    text.setFont("Helvetica",11)
    text.textLines(recommendation)
    c.drawText(text)

    y = rec_box_y - 35

        # ---------------- Footer ----------------

    c.setStrokeColor(navy)
    c.line(1*inch, 0.85*inch, 7.5*inch, 0.85*inch)

    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(
        4.25*inch,
        0.62*inch,
        "AI-Based Metal Surface Inspection System"
    )

    c.setFillColor(darkgreen)
    c.setFont("Helvetica", 10)
    c.drawCentredString(
        4.25*inch,
        0.43*inch,
        "Powered by EfficientNetB0 • TensorFlow • Streamlit"
    )

    c.setFillColor(red)
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(
        4.25*inch,
        0.25*inch,
        "Developed as part of Hindalco Summer Internship 2026"
    )
    
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica",9)
    c.drawCentredString(width/2,8,"Page 1")
        
    c.save()

    return filename


@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("steel_defect_model.keras")
    return model

@st.cache_resource
def load_class_names():
    with open("class_names.json", "r") as file:
        class_names = json.load(file)
    return class_names


st.set_page_config(
    page_title="Metal Surface Defect Detector",
    page_icon="🔍",
    layout="wide"
)

st.markdown("""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Main App */
html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Background */
.stApp{
    background:
    radial-gradient(circle at top left,#1b2a49 0%,transparent 35%),
    radial-gradient(circle at bottom right,#16213e 0%,transparent 35%),
    linear-gradient(135deg,#0b1120,#111827,#0f172a);

    color:white;
}

/* Main Container */
.main .block-container{

    padding-top:2rem;
    padding-bottom:2rem;

    max-width:1350px;
}

/* Scrollbar */

::-webkit-scrollbar{

width:10px;

}

::-webkit-scrollbar-track{

background:#111827;

}

::-webkit-scrollbar-thumb{

background:#3b82f6;
border-radius:10px;

}

::-webkit-scrollbar-thumb:hover{

background:#60a5fa;

}

/* Upload Box */

section[data-testid="stFileUploader"]{

background:rgba(255,255,255,0.05);

border:1px solid rgba(255,255,255,0.12);

border-radius:18px;

padding:18px;

backdrop-filter:blur(12px);

}

/* Divider */

hr{

border-color:rgba(255,255,255,.12);

}

/* Headers */

h1{

font-size:52px !important;

font-weight:700 !important;

}

h2{

font-size:36px !important;

}

h3{

font-size:30px !important;

}

/* ---------- Premium Result Cards ---------- */

.result-card{

background:rgba(255,255,255,.04);

border:1px solid rgba(255,255,255,.08);

border-left:4px solid #3b82f6;

border-radius:16px;

padding:18px 22px;

margin-bottom:14px;

backdrop-filter:blur(18px);

transition:.25s ease;

box-shadow:0 8px 30px rgba(0,0,0,.25);

}

.result-card:hover{

transform:translateY(-3px);

border-left:4px solid #60a5fa;

box-shadow:0 15px 35px rgba(59,130,246,.18);

}

.result-title{

font-size:15px;

font-weight:600;

color:#94a3b8;

margin-bottom:8px;

letter-spacing:.3px;

}

.result-value{

font-size:22px;

font-weight:700;

color:white;

line-height:1.4;

}

.result-text{

font-size:15px;

font-weight:400;

color:#d1d5db;

line-height:1.7;

}

.result-highlight{

color:#38bdf8;

font-weight:600;

}  

.card-green{
border-left:4px solid #22c55e;
}

.card-orange{
border-left:4px solid #f59e0b;
}

.card-blue{
border-left:4px solid #3b82f6;
}

.card-purple{
border-left:4px solid #a855f7;
}

.card-emerald{
border-left:4px solid #10b981;
}

/* Premium Progress Bar */

.stProgress > div > div > div > div{
background:linear-gradient(90deg,#38bdf8,#3b82f6);
border-radius:20px;
}

.stProgress > div > div{
background:#2a3245;
border-radius:20px;
height:10px;
}

.glass-section{
    background:rgba(22,27,45,.55);
    border:1px solid rgba(255,255,255,.06);
    border-radius:18px;
    padding:22px;
    margin-top:22px;
    backdrop-filter:blur(10px);
    box-shadow:0 10px 30px rgba(0,0,0,.25);
}
            
/* Premium File Uploader */

section[data-testid="stFileUploader"]{
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.08);
    border-radius:18px;
    padding:20px;
    transition:.3s;
}

section[data-testid="stFileUploader"]:hover{
    border:1px solid #38bdf8;
    box-shadow:0 0 25px rgba(56,189,248,.20);
}

section[data-testid="stFileUploader"] button{
    border-radius:12px;
    font-weight:600;
}

section[data-testid="stFileUploader"] small{
    color:#94a3b8 !important;
}

</style>        

""", unsafe_allow_html=True)

def preprocess_image(image):
    image = tf.keras.utils.load_img(image, target_size=(224, 224))
    image = tf.keras.utils.img_to_array(image)
    image = tf.expand_dims(image, axis=0)
    return image

model = load_model()
class_names = load_class_names()

defect_info = {
    "crazing": "Fine cracks appear on the metal surface due to thermal or mechanical stress.",

    "inclusion": "Foreign particles become trapped inside the metal during manufacturing.",

    "patches": "Uneven surface regions caused by inconsistent rolling or coating.",

    "pitted_surface": "Small pits or holes are formed because of corrosion or manufacturing defects.",

    "rolled-in_scale": "Oxide scale gets rolled into the steel surface during hot rolling, reducing surface quality.",

    "scratches": "Linear marks created by friction, handling, or contact with hard objects."
}

recommendation_info = {

    "crazing": "Inspect the surface for thermal cracks. Avoid using the sheet in high stress applications.",

    "inclusion": "Check the manufacturing process and inspect raw material quality before production.",

    "patches": "Inspect the coating process and verify rolling consistency before further processing.",

    "pitted_surface": "Inspect the surface for corrosion. Repair or replace the damaged metal if required.",

    "rolled-in_scale": "Remove oxide scale before rolling and review the hot rolling process.",

    "scratches": "Re-polish the surface if required and avoid rough handling during transportation."

}

st.markdown("""
<div style="
background: linear-gradient(135deg,#14213d,#1d3557,#274c77);
padding:35px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.08);
box-shadow:0px 0px 25px rgba(0,140,255,0.18);
margin-bottom:25px;
">

<h1 style="
color:white;
font-size:48px;
margin-bottom:5px;
">
🔍 Metal Surface Defect Detector
</h1>

<p style="
font-size:22px;
color:#cfd8dc;
margin-top:0px;
">
AI-Powered Metal Surface Inspection using EfficientNetB0
</p>

<hr style="border:1px solid rgba(255,255,255,0.15);">

<div style="
display:flex;
justify-content:space-between;
font-size:18px;
color:white;
">

<div>
✅ Accuracy<br>
<span style="font-size:26px;color:#00E676;">
99.2%
</span>
</div>

<div>
🧠 Model<br>
<span style="font-size:26px;color:#29B6F6;">
EfficientNetB0
</span>
</div>

<div>
📂 Classes<br>
<span style="font-size:26px;color:#FFD54F;">
6
</span>
</div>

<div>
⚡ Prediction<br>
<span style="font-size:26px;color:#81C784;">
Real Time
</span>
</div>

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
</div>
""", unsafe_allow_html=True)

# 👇 YAHAN PASTE KARO
tab1, tab2, tab3, tab4 = st.tabs([
    "🏠 Home",
    "🧠 Model Information",
    "📚 Defect Guide",
    "ℹ️ About Project"
])

with tab1:

    st.markdown("""
    <div style="
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.08);
    padding:22px;
    border-radius:18px;
    margin-bottom:18px;
    backdrop-filter:blur(12px);
    ">

    <h2 style="
    margin:0;
    font-size:28px;
    font-weight:600;
    color:white;">
    📤 Upload Metal Surface Image
    </h2>

    <p style="
    margin-top:8px;
    margin-bottom:0;
    color:#94a3b8;
    font-size:15px;
    ">

    Upload a metal surface image for AI-powered defect detection using
    <b>EfficientNetB0 Deep Learning Model</b>.

    </p>

    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a metal surface image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        left, right = st.columns([1, 1.2])

        with left:
            st.image(
                uploaded_file,
                caption="Uploaded Metal Surface",
                use_container_width=True
            )

            img = Image.open(uploaded_file)

            file_size = uploaded_file.size / 1024
            width, height = img.size

            st.markdown(f"""
            <div class="glass-section">

            <h4 style="margin-top:0;color:white;">
            📄 Image Details
            </h4>

            <table style="width:100%;color:#cbd5e1;font-size:15px;">

            <tr>
            <td><b>Filename</b></td>
            <td>{uploaded_file.name}</td>
            </tr>

            <tr>
            <td><b>Format</b></td>
            <td>{img.format}</td>
            </tr>

            <tr>
            <td><b>Resolution</b></td>
            <td>{width} × {height} px</td>
            </tr>

            <tr>
            <td><b>File Size</b></td>
            <td>{file_size:.1f} KB</td>
            </tr>

            </table>

            </div>
            """, unsafe_allow_html=True)

        image = preprocess_image(uploaded_file)

        prediction = model.predict(image)

        predicted_index = tf.argmax(prediction[0]).numpy()

        predicted_class = class_names[predicted_index]

        description = defect_info[predicted_class]

        recommendation = recommendation_info[predicted_class]

        confidence = float(tf.reduce_max(prediction[0])) * 100

        if confidence >= 95:
            reliability = "🟢 Very High"
        elif confidence >= 80:
            reliability = "🟡 Moderate"
        else:
            reliability = "🔴 Low"

        with right:
            st.markdown(f"""
            <div class="result-card card-green">

            <div class="result-title">
            Inspection Result
            </div>

            <div class="result-value">
             {predicted_class.replace("_"," ").title()}
            </div>

            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="result-card card-orange">

            <div class="result-title">
            Defect Description
            </div>

            <div class="result-text">
            {description}
            </div>

            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="result-card card-blue">

            <div class="result-title">
            Confidence Score
            </div>

            <div class="result-value">
            <span class="result-highlight">{confidence:.2f}%</span>
            </div>

            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="result-card card-emerald">

            <div class="result-title">
            Recommendation
            </div>

            <div class="result-text">
            {recommendation}
            </div>

            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="result-card card-purple">

            <div class="result-title">
            Reliability
            </div>

            <div class="result-value">
            {reliability}
            </div>

            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-top:18px;
            margin-bottom:8px;
            font-size:15px;
            color:#94a3b8;
            font-weight:500;
            ">

            <span>Overall Confidence</span>

            <span style="
            color:#38bdf8;
            font-size:18px;
            font-weight:700;">
            {confidence:.2f}%
            </span>

            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div style="
            margin-top:8px;
            margin-bottom:22px;
            width:100%;
            height:10px;
            background:#2a3245;
            border-radius:999px;
            overflow:hidden;
            ">

            <div style="
            width:{confidence:.2f}%;
            height:100%;
            background:linear-gradient(90deg,#38bdf8,#3b82f6);
            border-radius:999px;
            transition:0.5s;">
            </div>

            </div>
            """, unsafe_allow_html=True)


        st.markdown("""
        <div style="margin-top:12px;margin-bottom:12px;">

        <h3 style="
        font-size:28px;
        font-weight:700;
        color:white;
        margin-bottom:2px;">
        📋 Prediction Summary
        </h3>

        <p style="
        color:#94a3b8;
        font-size:15px;
        margin-top:0;">
        Model confidence ranked from highest to lowest prediction probability.
        </p>

        </div>
        """, unsafe_allow_html=True)


        summary_df = pd.DataFrame({
            "Defect Type": [
                name.replace("_", " ").title()
                for name in class_names
            ],
            "Probability (%)": prediction[0] * 100
        })


        summary_df = summary_df.sort_values(
            by="Probability (%)",
            ascending=False
        ).reset_index(drop=True)


        summary_df.insert(
            0,
            "Rank",
            ["🥇","🥈","🥉","4","5","6"]
        )


        summary_df["Probability (%)"] = summary_df[
            "Probability (%)"
        ].map(lambda x: f"{x:.2f}%")


        st.dataframe(
            summary_df,
            use_container_width=True,
            hide_index=True
        )

        

        st.markdown("""
        <div style="margin-top:25px; margin-bottom:15px;">

        <h3 style="
        font-size:28px;
        font-weight:700;
        color:#ffffff;
        margin-bottom:6px;">
        📊 Prediction Probability Analysis
        </h3>

        <p style="
        color:#94a3b8;
        font-size:15px;
        margin-top:0;">
        Confidence distribution across all six steel surface defect classes.
        </p>

        </div>
        """, unsafe_allow_html=True)

        probability_df = pd.DataFrame({
            "Defect Type": class_names,
            "Probability (%)": prediction[0] * 100
        })

        # Sort by confidence (highest first)
        probability_df = probability_df.sort_values(
            "Probability (%)",
            ascending=True
        )

        # Premium colors
        colors = [
            "#2b3448" if i != len(probability_df)-1 else "#38bdf8"
            for i in range(len(probability_df))
        ]

        fig = px.bar(
            probability_df,
            x="Probability (%)",
            y="Defect Type",
            orientation="h",
            text="Probability (%)"
        )

        fig.update_traces(
            marker_color=colors,
            texttemplate="%{text:.2f}%",
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>%{x:.2f}%<extra></extra>"
        )

        fig.update_layout(

            height=430,

            plot_bgcolor="#111827",
            paper_bgcolor="#111827",

            font=dict(
                color="white",
                size=14
            ),

            margin=dict(
                l=20,
                r=40,
                t=20,
                b=20
            ),

            xaxis=dict(
                title="Confidence (%)",
                showgrid=True,
                gridcolor="#263449",
                zeroline=False
            ),

            yaxis=dict(
                title="",
                tickfont=dict(size=14),
                categoryorder="total ascending"
            ),

            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displaylogo": False,
                "modeBarButtonsToRemove": [
                    "select2d",
                    "lasso2d",
                    "zoomIn2d",
                    "zoomOut2d",
                    "autoScale2d"
                ]
            }
        )

        pdf_file = generate_pdf(
        predicted_class,
        confidence,
        reliability,
        description,
        recommendation
        )

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="📄 Download Inspection Report (PDF)",
                data=pdf,
                file_name="Metal_Surface_Defect_Report.pdf",
                mime="application/pdf"
            )


with tab2:

    st.header("🧠 Model Information")

    st.markdown("""
### Model Overview

This application uses **EfficientNetB0**, a lightweight and highly efficient Convolutional Neural Network (CNN) architecture for steel surface defect classification.

### Training Details

- Model : EfficientNetB0
- Framework : TensorFlow / Keras
- Input Size : 224 × 224
- Number of Classes : 6
- Accuracy : 99.2%

### Detectable Defects

- Crazing
- Inclusion
- Patches
- Pitted Surface
- Rolled-in Scale
- Scratches

### Prediction Workflow

1. Upload image
2. Image preprocessing
3. Deep learning prediction
4. Confidence calculation
5. Final defect classification
""")
        
with tab3:

    st.header("📚 Defect Guide")

    for defect, info in defect_info.items():

        st.markdown(f"""
### {defect.replace("_"," ").title()}

**Description**

{info}

**Recommendation**

{recommendation_info[defect]}

---
""")
        
with tab4:

    st.header("ℹ️ About Project")

    st.markdown("""
## 🎯 Project Objective

This application automatically detects surface defects on steel sheets using a Deep Learning model.

The goal is to help manufacturers identify defects quickly, improve quality control, and reduce manual inspection time.
""")

    st.markdown("""
## 🧠 Deep Learning Model

- EfficientNetB0
- TensorFlow / Keras
- Transfer Learning
- Input Size : 224 × 224
- Multi-Class Image Classification
""")
    
    st.markdown("""
## 📂 Dataset

The model is trained on the NEU Metal Surface Defect Dataset containing six categories of steel surface defects used for multi-class classification.

""")

    st.markdown("""
## ⚙️ Technologies & ML Pipeline

### 🐍 Programming Language
- Python

### 🧠 Deep Learning
- TensorFlow
- Keras
- EfficientNetB0 (Transfer Learning)
- Convolutional Neural Network (CNN)

### 🖼 Image Processing
- Image Preprocessing
- Image Resizing (224 × 224)
- Image Normalization

### 📊 Data Handling
- Pandas
- NumPy

### 📈 Model Evaluation
- Accuracy: **99.2%**
- Multi-Class Image Classification
- Confidence Score Analysis

### 🌐 Web Application
- Streamlit
- Plotly (Interactive Visualizations)

### 💾 Model Deployment
- Saved Keras Model (.keras)
- Real-Time Image Prediction
- End-to-End Deep Learning Pipeline
""")
    
    
    st.markdown("""
## 🔄 Machine Learning Workflow

1️⃣ **Dataset Collection**
- NEU Metal Surface Defect Dataset

⬇️

2️⃣ **Image Preprocessing**
- Image Loading
- Resize to **224 × 224**
- Pixel Normalization

⬇️

3️⃣ **Deep Learning Model**
- EfficientNetB0
- Transfer Learning
- CNN Architecture

⬇️

4️⃣ **Model Training**
- TensorFlow / Keras
- Multi-Class Classification
- Accuracy Achieved: **99.2%**

⬇️

5️⃣ **Model Saving**
- Saved as **steel_defect_model.keras**

⬇️

6️⃣ **Deployment**
- Streamlit Web Application

⬇️

7️⃣ **Real-Time Prediction**
- Upload Image
- Defect Detection
- Confidence Score
- Recommendation Generation
""")
    

    st.markdown("""
## ⭐ Project Highlights

- 🎯 99.2% Classification Accuracy
- 🧠 CNN-Based Deep Learning Model
- 🚀 EfficientNetB0 Transfer Learning
- 🔍 Multi-Class Steel Surface Defect Classification
- ⚡ Confidence Score Analysis
- 📊 Interactive Prediction Probability Visualization
- 💡 Intelligent Defect Recommendation System
- 🌐 Real-Time Streamlit Deployment
""")
    
    st.markdown("""
## 🚀 Key Features

- ✅ AI-powered Metal Surface Defect Detection
- ✅ EfficientNetB0 Deep Learning Model
- ✅ Real-time Image Classification
- ✅ Confidence Score
- ✅ Prediction Reliability Indicator
- ✅ Defect Description
- ✅ Maintenance Recommendation
- ✅ Interactive Probability Graph
- ✅ Raw Prediction Table
- ✅ Modern Responsive UI
""")

  
    st.markdown("""
## 👨‍💻 Developer

Developed by **Avi Singh**

BCA Student | AI & Machine Learning/ Deep Learning Enthusiast

Built using Python, Streamlit, TensorFlow and EfficientNetB0.
""")