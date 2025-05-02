import streamlit as st
from PIL import Image, ImageEnhance
import io

def enhance_image(image, brightness, contrast, sharpness):
    """
    Enhances the uploaded image using PIL's ImageEnhance functions.

    Args:
        image (PIL.Image.Image): The image to enhance.
        brightness (float): The brightness enhancement factor.
        contrast (float): The contrast enhancement factor.
        sharpness (float): The sharpness enhancement factor.

    Returns:
        PIL.Image.Image: The enhanced image.  Returns the original image if no enhancements are applied.
    """
    enhanced_image = image

    if brightness != 1.0:
        enhancer = ImageEnhance.Brightness(enhanced_image)
        enhanced_image = enhancer.enhance(brightness)
    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(enhanced_image)
        enhanced_image = enhancer.enhance(contrast)
    if sharpness != 1.0:
        enhancer = ImageEnhance.Sharpness(enhanced_image)
        enhanced_image = enhancer.enhance(sharpness)
    return enhanced_image

def main():
    """
    Main function to run the Streamlit application.
    """
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
        brightness = st.sidebar.slider("Brightness", 0.0, 2.0, 1.0, 0.1)  # Default: 1.0 (no change)
        contrast = st.sidebar.slider("Contrast", 0.0, 2.0, 1.0, 0.1)    # Default: 1.0 (no change)
        sharpness = st.sidebar.slider("Sharpness", 0.0, 2.0, 1.0, 0.1)  # Default: 1.0 (no change)

        # Enhance the image
        enhanced_image = enhance_image(image, brightness, contrast, sharpness)

        # Display the enhanced image
        st.subheader("Enhanced Image")
        st.image(enhanced_image, use_column_width=True)

        # Add a download button for the enhanced image
        # Convert the enhanced image to bytes
        img_bytes = io.BytesIO()

        # Save the image in a format that the browser can download (e.g., PNG)
        enhanced_image.save(img_bytes, format="PNG")  # You can change the format if needed
        img_bytes = img_bytes.getvalue()

        st.download_button(
            label="Download Enhanced Image",
            data=img_bytes,
            file_name="enhanced_image.png",  # Provide a filename
            mime="image/png",  # Set the correct MIME type
        )

if __name__ == "__main__":
    main()
