# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Page Configuration
st.set_page_config(page_title="Plastic Reusability Analyzer", layout="wide")

# Sidebar Styling
st.markdown("""
    <style>
    .css-1d391kg {background: linear-gradient(to bottom, #a8edea, #fed6e3);}
    .css-1d391kg .css-1v0mbdj {background: transparent;}
    footer {text-align: center; padding-top: 10px; font-size: 12px;}
    </style>
""", unsafe_allow_html=True)

# Sidebar Content
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2329/2329168.png", width=100)
    st.title("♻ Plastic Analyzer")
    st.markdown("---")
    page = st.radio("Navigate", ["Plastic Details", "Usage Statistics", "Global Plastic Pollution", "Recycling Tips", "Plastic Detection"])

    st.markdown("---")
    st.info("Understand plastic types, their recyclability, reusability, and environmental impacts.")

# Plastic data
plastic_data = {
    "PET": {
        "full_name": "Polyethylene Terephthalate",
        "description": "PET is a clear, strong, and lightweight plastic used for packaging foods and beverages.",
        "recyclability": "Highly recyclable (Plastic #1)",
        "reusability": "Safe for one-time use; may degrade if reused",
        "common_uses": ["Water bottles", "Soft drink bottles", "Food containers"],
        "global_usage_percent": 30,
        "environmental_impact": "Takes over 400 years to decompose. Recycling significantly reduces CO2 emissions.",
        "detailed_analysis": "PET is the most recycled plastic worldwide. It's widely used in textiles (rPET)."
    },
    "HDPE": {
        "full_name": "High-Density Polyethylene",
        "description": "HDPE is known for its high strength-to-density ratio.",
        "recyclability": "Highly recyclable (Plastic #2)",
        "reusability": "Safe for reuse",
        "common_uses": ["Milk jugs", "Detergent bottles", "Toys"],
        "global_usage_percent": 18,
        "environmental_impact": "Low toxicity and energy-efficient recycling.",
        "detailed_analysis": "HDPE is easy to recycle and used in industrial applications too."
    },
    "PVC": {
        "full_name": "Polyvinyl Chloride",
        "description": "PVC is tough and used in construction for pipes, doors, and windows.",
        "recyclability": "Difficult to recycle (Plastic #3)",
        "reusability": "Reusable but may release harmful chemicals",
        "common_uses": ["Pipes", "Cables", "Vinyl flooring"],
        "global_usage_percent": 12,
        "environmental_impact": "Can release toxic chemicals like dioxins.",
        "detailed_analysis": "PVC recycling is limited but chemical recycling is promising."
    },
    "LDPE": {
        "full_name": "Low-Density Polyethylene",
        "description": "LDPE is a flexible plastic used in grocery bags, bread bags, and food wraps.",
        "recyclability": "Recyclable with specialized processes (Plastic #4)",
        "reusability": "Reusable but prone to wear and tear",
        "common_uses": ["Plastic bags", "Packaging films"],
        "global_usage_percent": 10,
        "environmental_impact": "Takes hundreds of years to degrade and often ends up in oceans.",
        "detailed_analysis": "Biodegradable LDPE alternatives are being developed."
    },
    "PP": {
        "full_name": "Polypropylene",
        "description": "PP is a tough, lightweight plastic used in food containers and automotive parts.",
        "recyclability": "Recyclable (Plastic #5)",
        "reusability": "Highly reusable and microwave-safe",
        "common_uses": ["Yogurt containers", "Medicine bottles"],
        "global_usage_percent": 16,
        "environmental_impact": "Safer for food contact; recyclable but underutilized.",
        "detailed_analysis": "PP recycling is growing but needs better infrastructure."
    },
    "PS": {
        "full_name": "Polystyrene",
        "description": "Used for disposable coffee cups, food boxes, and packaging materials.",
        "recyclability": "Difficult to recycle (Plastic #6)",
        "reusability": "Single-use only; can leach toxic chemicals",
        "common_uses": ["Foam containers", "Disposable cups"],
        "global_usage_percent": 7,
        "environmental_impact": "Breaks into microplastics easily; environmental hazard.",
        "detailed_analysis": "Efforts are ongoing to dissolve and reuse PS with eco-friendly solvents."
    },
    "Other": {
        "full_name": "Miscellaneous Plastics",
        "description": "Includes polycarbonate, bioplastics, and other plastics.",
        "recyclability": "Rarely recycled (Plastic #7)",
        "reusability": "Varies depending on material",
        "common_uses": ["Baby bottles", "Electronics"],
        "global_usage_percent": 7,
        "environmental_impact": "May leach BPA or other harmful compounds.",
        "detailed_analysis": "Recycling these materials needs advanced sorting."
    }
}

# Online image placeholder
uploaded_image_path = "https://cdn-icons-png.flaticon.com/512/565/565547.png"

# Page Logic
if page == "Plastic Details":
    st.title("🔍 Plastic Reusability & Environmental Impact Analyzer")
    st.markdown("---")

    plastic_type = st.selectbox("Select the type of plastic:", list(plastic_data.keys()))
    data = plastic_data[plastic_type]

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(uploaded_image_path, caption=f"{plastic_type} - {data['full_name']}", use_container_width=True)

    with col2:
        st.header(f"{plastic_type} - {data['full_name']}")
        st.subheader("🧴 Description")
        st.write(data['description'])

        st.subheader("♻ Reusability & Recyclability")
        st.write(f"*Reusability:* {data['reusability']}")
        st.write(f"*Recyclability:* {data['recyclability']}")

        st.subheader("🔧 Common Uses")
        st.write(", ".join(data['common_uses']))

        st.subheader("📊 Usage Stats")
        st.write(f"*Global Usage Share:* {data['global_usage_percent']}%")

        st.subheader("🌍 Environmental Impact")
        st.write(data['environmental_impact'])

        st.subheader("📘 In-Depth Analysis")
        st.write(data['detailed_analysis'])

elif page == "Usage Statistics":
    st.title("📈 Global Plastic Usage Statistics")
    st.markdown("---")

    usage_df = pd.DataFrame({
        'Plastic Type': list(plastic_data.keys()),
        'Usage (%)': [plastic_data[key]['global_usage_percent'] for key in plastic_data]
    })

    fig1, ax1 = plt.subplots(figsize=(8, 8))
    ax1.pie(usage_df['Usage (%)'], labels=usage_df['Plastic Type'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", n_colors=len(usage_df)))
    plt.title("Global Plastic Usage by Type")
    plt.axis('equal')
    st.pyplot(fig1)

    st.subheader("♻ Recyclability vs Reusability")
    recyclability = [1 if 'recyclable' in plastic_data[key]['recyclability'].lower() else 0 for key in plastic_data]
    reusability = [1 if 'reuse' in plastic_data[key]['reusability'].lower() else 0 for key in plastic_data]

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    ax2.scatter(recyclability, reusability, color=sns.color_palette("coolwarm", n_colors=len(plastic_data)))
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(['Non-Recyclable', 'Recyclable'])
    ax2.set_yticks([0, 1])
    ax2.set_yticklabels(['Non-Reusable', 'Reusable'])
    plt.title("Recyclability vs Reusability")
    plt.xlabel("Recyclability")
    plt.ylabel("Reusability")
    st.pyplot(fig2)

elif page == "Global Plastic Pollution":
    st.title("🌍 Global Plastic Pollution Trends")
    st.markdown("---")

    # Plastic production data
    production_years = [1950, 1970, 1990, 2010, 2020]
    production_tonnes = [2, 35, 150, 270, 400]  # Millions of tonnes

    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3.plot(production_years, production_tonnes, marker='o', color='green')
    plt.title("Global Plastic Production Over Time")
    plt.xlabel("Year")
    plt.ylabel("Plastic Production (Million Tonnes)")
    plt.grid(True)
    st.pyplot(fig3)

    st.markdown("**Plastic production increased from 2 million tonnes in 1950 to over 400 million tonnes by 2020.**")

    # Plastic waste management data
    waste_types = ['Recycled', 'Incinerated', 'Landfilled', 'Mismanaged']
    waste_percentages = [9, 19, 50, 22]

    fig4, ax4 = plt.subplots(figsize=(8, 8))
    ax4.pie(waste_percentages, labels=waste_types, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title("Global Plastic Waste Management")
    plt.axis('equal')
    st.pyplot(fig4)

    st.markdown("**Only 9% of plastic waste is recycled globally. 22% is mismanaged, contributing to ocean pollution.**")

elif page == "Recycling Tips":
    st.title("♻ Helpful Tips for Recycling Plastics")
    st.markdown("---")

    st.subheader("✅ General Tips:")
    st.markdown("""
    - Rinse containers before recycling to avoid contamination.
    - Check local guidelines for accepted plastic numbers.
    - Remove caps unless stated otherwise (they may be made from different plastics).
    - Avoid recycling plastic bags with curbside pickup — drop them off at collection points.
    """)

    st.subheader("🚫 Avoid:")
    st.markdown("""
    - Black plastic trays (often not detected by recycling machines).
    - Food-contaminated containers (like greasy pizza boxes).
    - Mixing non-recyclable plastics with recyclables.
    """)

    st.success("Every small action counts toward reducing plastic pollution! 🌱")

elif page == "Plastic Detection":
    st.title("🖼️ Plastic Type Detection from Image")
    st.markdown("---")
    
    st.subheader("Upload an image to analyze the type of plastic:")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        st.markdown("### 🔎 Detection Result")
        st.success("**Detected Plastic Type:** PET (Polyethylene Terephthalate)")
        st.info("**Prediction Confidence:** 80%")
        
        st.markdown("""
        ---
        **Note:** This is a demo prediction. Future updates will support real model-based classification! 🚀
        """)
    else:
        st.warning("Please upload an image to proceed.")



# Footer
st.markdown("""
    <footer>
    <p>Data sourced from <a href="https://ourworldindata.org/plastic-pollution" target="_blank">Our World in Data</a> and environmental studies.</p>
    </footer>
""", unsafe_allow_html=True)
