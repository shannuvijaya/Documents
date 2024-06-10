import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob Storage Python quickstart sample")
    account_url = "https://<storageaccountname>.blob.core.windows.net"
    storageaccount_key = "<accountkey>"
    default_credential = DefaultAzureCredential()
# Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=storageaccount_key)

    # Create a unique name for the container
    container_name = str(uuid.uuid4())
# Create the container
    container_client = blob_service_client.create_container(container_name)

    # Create a local directory to hold blob data
    local_path = "./data"
    #os.mkdir(local_path)

# Create a file in the local data directory to upload and download
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)

# Write text to the file
    file = open(file=upload_file_path, mode='w')
    file.write("Hello, World!")
    file.close()

# Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(file=upload_file_path, mode="rb") as data:
        blob_client.upload_blob(data)

    blobname = str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt')

    download_file_path = os.path.join(local_path, blobname)
    container_client = blob_service_client.get_container_client(container= container_name) 
    
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(file=download_file_path, mode="wb") as download_file:
        download_file.write(container_client.download_blob(local_file_name).readall())

    print("Download Completed !!!")
    
except Exception as ex:
    print('Exception:')
    print(ex)