import streamlit as st

# Set the title and introduction text
st.title("Home Ideas App")
st.write("Welcome to the Home Ideas app! Here, you'll find inspiring ideas for improving your home decor and layout.")

# Sidebar for selecting categories
st.sidebar.title("Choose a Category")
category = st.sidebar.selectbox(
    "Select a category",
    ("Living Room", "Bedroom", "Kitchen", "Outdoor", "Workspace")
)

# Dictionary of ideas with example descriptions and images
ideas = {
    "Living Room": {
        "description": "Brighten up your living room with modern decor, comfy seating, and plants.",
        "image_url": "https://via.placeholder.com/150"  # Replace with actual URLs of home decor images
    },
    "Bedroom": {
        "description": "Transform your bedroom into a cozy retreat with soft colors and minimalist furniture.",
        "image_url": "https://via.placeholder.com/150"
    },
    "Kitchen": {
        "description": "Make your kitchen functional and stylish with open shelving and sleek cabinetry.",
        "image_url": "https://via.placeholder.com/150"
    },
    "Outdoor": {
        "description": "Create an inviting outdoor space with lounge furniture and ambient lighting.",
        "image_url": "https://via.placeholder.com/150"
    },
    "Workspace": {
        "description": "Boost productivity with an organized workspace that includes ergonomic furniture and plenty of light.",
        "image_url": "https://via.placeholder.com/150"
    },
}

# Display selected category's content
st.subheader(f"{category} Ideas")
st.write(ideas[category]["description"])
st.image(ideas[category]["image_url"], caption=f"{category} Decor")

# Option to display more ideas
if st.button("Show More Ideas"):
    st.write("More ideas coming soon!")
