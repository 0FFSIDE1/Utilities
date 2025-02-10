import os
import cloudinary
import cloudinary.uploader

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
)

def upload_folder_to_cloudinary(folder_path, cloudinary_folder_name, output_file):
    

    with open(output_file, 'a') as file:
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                name = os.path.splitext(os.path.basename(file_path))[0]
                extension = file_path.split('.')[-1].lower()

                # Define the resource type based on file type
                if extension in ['jpg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp']:
                    resource_type = "image"
                elif extension in ['mp4', 'avi', 'mov', 'mp3', 'wav', 'ogg', 'flac']:
                    resource_type = "video"
                else:
                    resource_type = "raw"

                try:
                    response = cloudinary.uploader.upload(
                        file_path,
                        folder=cloudinary_folder_name,
                        resource_type=resource_type,
                        public_id=name
                    )
                    result = f"Uploaded {file_name} to Cloudinary: {response['url']}\n"
                    print(result.strip())
                    file.write(result)
                except Exception as e:
                    error_message = f"Failed to upload {file_name} to Cloudinary: {str(e)}\n"
                    print(error_message.strip())
                    file.write(error_message)

# Define paths
local_folder = input('Enter path to folder you want to upload:\n')
website_static_files = input('Which folder do you want to add it to?:\n')
cloudinary_folder = f'{website_static_files}/static'
output_file_path = input('Enter output file path:\n')

# Upload folder and save results
upload_folder_to_cloudinary(local_folder, cloudinary_folder, output_file_path)


r'C:\Users\USER\cheexomglobal\app\static\app'
r'C:\Users\USER\cheexomglobal\upload_results.txt'