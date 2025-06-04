import os

# Define the paths
images_folder = 'CXR_png/images'
masks_folder = 'CXR_png/masks'

# Get the list of image filenames and mask filenames
image_filenames = set(os.listdir(images_folder))
mask_filenames = set(os.listdir(masks_folder))

# Remove masks that do not have corresponding images
for mask in mask_filenames:
    # Remove the file extension to compare
    mask_name = os.path.splitext(mask)[0]
    
    # Check if the corresponding image exists
    if f"{mask_name}.png" not in image_filenames:  # Change '.png' if the mask file has a different extension
        # Construct the full path of the mask to be deleted
        mask_path = os.path.join(masks_folder, mask)
        # Remove the mask
        os.remove(mask_path)
        print(f"Removed mask: {mask}")

print("Cleanup of masks complete.")
