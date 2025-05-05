import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io
import time  # For progress bar

def enhance_image(image, brightness, contrast, sharpness, saturation, blur_level, rotate_angle):
    """
    Enhances the uploaded image using PIL's ImageEnhance and ImageFilter functions.

    Args:
        image (PIL.Image.Image): The image to enhance.
        brightness (float): The brightness enhancement factor.
        contrast (float): The contrast enhancement factor.
        sharpness (float): The sharpness enhancement factor.
        saturation (float): The saturation enhancement factor.
        blur_level (float): The blur level (for Gaussian blur).
        rotate_angle (float): The rotation angle in degrees.

    Returns:
        PIL.Image.Image: The enhanced image.  Returns the original image if no enhancements are applied.
    """
    enhanced_image = image.copy()

    if rotate_angle != 0.0:
        enhanced_image = enhanced_image.rotate(rotate_angle, expand=True)  # rotate first

    if brightness != 1.0:
        enhancer = ImageEnhance.Brightness(enhanced_image)
        enhanced_image = enhancer.enhance(brightness)
    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(enhanced_image)
        enhanced_image = enhancer.enhance(contrast)
    if saturation != 1.0:
        enhancer = ImageEnhance.Color(enhanced_image)
        enhanced_image = enhancer.enhance(saturation)
    if sharpness != 1.0:
        enhancer = ImageEnhance.Sharpness(enhanced_image)
        enhanced_image = enhancer.enhance(sharpness)
    if blur_level > 0.0:
        enhanced_image = enhanced_image.filter(ImageFilter.GaussianBlur(radius=blur_level))

    return enhanced_image


def main():
    """
    Main function to run the Streamlit application.
    """
    # --- Page Configuration ---
    st.set_page_config(
        page_title="Image Enhancement App",
        page_icon="✨",  # You can use an emoji or a path to a small image
        layout="wide",  # Use the full width of the screen
        initial_sidebar_state="expanded",  # Keep the sidebar open by default
    )

    # --- Custom CSS for Background and Layout ---
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0;  /* Light gray background */
            color: #333;  /* Darker text */
            font-family: sans-serif;
        }
        .main-content {
            padding: 20px;
            border-radius: 10px;
            background-color: #ffffff; /* white background for the main content area */
            box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* subtle shadow */
            margin-bottom: 20px;
        }
        .sidebar .sidebar-content {
            background-color: #e0e0e0; /* Light gray for sidebar */
            border-radius: 10px;
            padding: 20px;
            margin-right: 20px;
        }
        h1 {
            color: #4CAF50; /* Greenish title */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Main Content Area ---
    st.markdown('<div class="main-content">', unsafe_allow_html=True)  # Start main content div
    st.title("Image Enhancement App")

    uploaded_file = st.file_uploader("Upload an image...", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Read the image from the uploaded file
        image = Image.open(uploaded_file)

        # Display the original image
        st.subheader("Original Image")
        st.image(image, use_column_width=True)

        # Create sliders for adjusting enhancement parameters
        st.sidebar.header("Enhancement Parameters")
        brightness = st.sidebar.slider("Brightness", 0.0, 2.0, 1.0, 0.1)
        contrast = st.sidebar.slider("Contrast", 0.0, 2.0, 1.0, 0.1)
        sharpness = st.sidebar.slider("Sharpness", 0.0, 2.0, 1.0, 0.1)
        saturation = st.sidebar.slider("Saturation", 0.0, 2.0, 1.0, 0.1)
        blur_level = st.sidebar.slider("Blur", 0.0, 10.0, 0.0, 0.1)
        rotate_angle = st.sidebar.slider("Rotation Angle (degrees)", -180.0, 180.0, 0.0, 1.0)

        # Enhance the image
        with st.spinner("Enhancing Image..."):
            enhanced_image = enhance_image(
                image, brightness, contrast, sharpness, saturation, blur_level, rotate_angle
            )

        # Display the enhanced image
        st.subheader("Enhanced Image")
        st.image(enhanced_image, use_column_width=True)

        # Add a download button for the enhanced image
        img_bytes = io.BytesIO()
        enhanced_image.save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()

        st.download_button(
            label="Download Enhanced Image",
            data=img_bytes,
            file_name="enhanced_image.png",
            mime="image/png",
        )
    st.markdown("---")  # Added a separator
    st.markdown("## About this App")
    st.markdown(
        "This app allows you to enhance images by adjusting various parameters such as brightness, contrast, sharpness, and more.  Upload an image and use the sliders in the sidebar to modify the image to your liking."
    )
    st.markdown('</div>', unsafe_allow_html=True) # Close main content div


if __name__ == "__main__":
    main()
