import os
from dotenv import load_dotenv
import uuid
from datetime import datetime

secreat_key = str(uuid.uuid4())
print(f"{datetime.utcnow()}: Secreat key of quickoo backend: {secreat_key}")

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

constant_dict = {
    "mongo_url": MONGO_URL,
    "secreat_key": secreat_key,
    "background_images": [
    {
        "background_image": "https://backendapp.stylic.ai/download/1.webp",
        "id": "04e52a98-a810-4206-83fb-6555c2bcf174"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/2.webp",
        "id": "b52d4cb9-c777-4486-8411-efb63fe9aedd"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/3.webp",
        "id": "29b78066-c5bd-44e4-83e9-b9d19d5e72ed"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/4.webp",
        "id": "c04a9230-af85-49c8-b193-7faaca5d174b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/5.webp",
        "id": "83437853-76d6-491d-8e30-37fbbe5b9c66"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/6.webp",
        "id": "9adc91db-32e4-4271-824b-73b88fdd4500"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/7.webp",
        "id": "f18a3883-e567-4a37-abf6-dbeeb8a0db0b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/8.webp",
        "id": "9573c0bf-2d94-4b93-bb7a-9ae21ccb0766"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/9.webp",
        "id": "0076fa79-b299-4154-a0d6-d320f753a0f5"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/10.webp",
        "id": "55e468c8-453e-42cf-9b53-144a6e2b2df9"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/11.webp",
        "id": "a38c7ed2-11bb-48da-94d8-f2ec18aff680"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/12.webp",
        "id": "82a1cd71-ad9a-4941-9d8e-223d2e0c41df"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/13.webp",
        "id": "8266984c-5141-43f8-9963-d868e4685a90"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/14.webp",
        "id": "a4391e9d-bb9b-4f04-af6c-2843f19e314e"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/15.webp",
        "id": "0fec9715-910e-4a7f-bd7e-0495d1e0341b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/16.webp",
        "id": "8e92ef81-6513-468a-b3bb-cd19cebec1c5"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/17.webp",
        "id": "055f53de-6a57-49d0-8f67-b62d320eb8af"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/18.webp",
        "id": "3cfa21f5-208b-47bc-a1cb-3a091ed1abe9"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/19.webp",
        "id": "22a4015a-49f3-4b7b-821f-48aaf5e1d02d"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/20.webp",
        "id": "3eeb705e-b067-453c-b5b5-c187233eec37"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/21.webp",
        "id": "67d687ec-18ef-4565-b147-b89962f6d728"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/22.webp",
        "id": "d2b85203-7ace-403b-9f99-15f5f3928b51"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/23.webp",
        "id": "d126bca0-d996-448a-ab57-38133bbeeeef"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/24.webp",
        "id": "1f694b00-34cb-40c2-9d54-5434fd5df62e"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/25.webp",
        "id": "d87e9366-fc78-46c5-9f5d-d427715d2d28"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/26.webp",
        "id": "cca8d951-bf3a-464a-9bab-decd23499534"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/27.webp",
        "id": "f80dc66d-fa7e-4a3d-a8db-23e02f5aed6c"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/28.webp",
        "id": "f3820d78-0844-426f-b481-e95b18e7b881"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/29.webp",
        "id": "fb7a4962-c1c8-4b2a-851e-4ad2084f0289"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/30.webp",
        "id": "a42d1951-1d1a-47d6-a34f-2f64b2984893"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/31.webp",
        "id": "bf1d77f8-d1bc-48d5-a06f-34351e948b49"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/32.webp",
        "id": "6ac34d94-1d01-4529-a924-10fcbdf823fb"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/33.webp",
        "id": "143a4150-d7ef-4f0b-8a54-02dfc59054d8"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/34.webp",
        "id": "6a82d854-451f-4d90-9244-69064c4706cf"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/35.webp",
        "id": "308aa9f6-55a2-4472-a953-b244c89c1e5e"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/36.webp",
        "id": "2b51e97c-e6f5-4aee-80c0-2250fc3fc7ca"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/37.webp",
        "id": "bd45a15f-36e9-491c-9f96-c4917167b777"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/38.webp",
        "id": "2da005d4-bad5-4512-bfa3-dd84d1f1ef7a"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/39.webp",
        "id": "d6c3aa03-69ca-4024-8498-9e553a3b331a"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/40.webp",
        "id": "8e6e4b9c-a208-4c7b-b4ca-358157cfb8cf"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/41.webp",
        "id": "6f771dbe-2d44-4f7c-92ae-bf82760ffb86"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/42.webp",
        "id": "db08adf9-0503-419b-ac8a-ec68a00f364c"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/43.webp",
        "id": "1b245660-c003-4815-8914-4aa1a01b7f58"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/44.webp",
        "id": "41f36d81-49e8-4d3c-86f6-2ebc073d5463"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/45.webp",
        "id": "3fcfd9f1-0934-45b1-a3c9-6f3b2e48ec58"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/46.webp",
        "id": "a4df6115-7f97-42be-bcec-1ad38edd97e4"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/47.webp",
        "id": "8dc55ed1-7f39-40d5-b486-5d814b29cc62"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/48.webp",
        "id": "2409f230-6c30-4c9f-aae1-506bf3140483"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/49.webp",
        "id": "3dc3e8da-de9a-48af-8ea8-f5ca5abba46f"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/50.webp",
        "id": "557140e3-5db4-4bfa-b07a-e403c6057a34"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/51.webp",
        "id": "77b0b04b-c54e-491b-8d33-f87d10ebe039"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/52.webp",
        "id": "6c4c9062-9f0a-4376-be08-97989a887ef6"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/53.webp",
        "id": "14ae2ea6-6a11-4208-a26f-7a1f63e4d865"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/54.webp",
        "id": "0b43fe89-bee8-4bde-8c82-fabcddc9aa94"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/55.webp",
        "id": "5924ac3c-3e44-46ad-a73a-38dac0a177db"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/56.webp",
        "id": "e027758c-3bfb-4983-aaa4-f41f152e8f63"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/57.webp",
        "id": "9114d40c-92c0-457f-9d10-884b7baa506a"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/58.webp",
        "id": "cba27e30-3956-4a3a-84eb-6c7f74083777"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/59.webp",
        "id": "6ef15208-baea-475f-b81e-cb09891be57c"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/60.webp",
        "id": "260a9e0e-5cd5-4d07-bf50-58910245d2cd"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/61.webp",
        "id": "381b8272-3fc4-42e1-b73a-4fc19490cd0b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/62.webp",
        "id": "a96186f2-4600-40ae-a6d1-5c29a2a89b88"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/63.webp",
        "id": "fd839db2-96cd-4de7-8491-39e7ddb31e10"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/64.webp",
        "id": "5db9439b-f127-4013-85e5-4c7b75c95163"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/65.webp",
        "id": "91a484da-cb98-4e4f-8319-6a2cf4140d77"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/66.webp",
        "id": "4876318b-877c-4c28-8354-c075f9c93998"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/67.webp",
        "id": "7742355c-6cc7-4a01-9c06-d37ddc5b7cdf"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/68.webp",
        "id": "2ff74750-affa-4790-a873-d3cc1d63b577"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/69.webp",
        "id": "97d59d12-6ce3-4667-9731-c575057c7dde"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/70.webp",
        "id": "dc83ad5c-a9a7-4384-9593-e6198b5916f7"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/71.webp",
        "id": "3ce558ef-070f-4277-9517-3c3ee2060832"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/72.webp",
        "id": "6f0133a2-506b-447c-86a3-fbf15848807d"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/73.webp",
        "id": "cbde4b06-dcf6-4b67-9e90-d76b3ef5b32c"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/74.webp",
        "id": "39f1f2ba-198c-46e7-915a-42ab9b9c343a"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/75.webp",
        "id": "be2c8782-9136-4f09-9b26-cb314ccf5cb3"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/76.webp",
        "id": "7e015d6f-3498-4ee1-86b5-9cadb1aaad33"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/77.webp",
        "id": "a2b9106d-f0d4-4d3d-8f87-0e0f63d95224"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/78.webp",
        "id": "a24a8a40-3db7-4e60-ae41-2cf13d64bb88"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/79.webp",
        "id": "257a9de0-0114-47b9-a3a8-799dbf6bdf06"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/80.webp",
        "id": "22b8d5ee-4548-43fb-960e-4ddf5af7a3f7"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/81.webp",
        "id": "7dd3b35c-75df-4b2b-b37a-d47e19fd8375"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/82.webp",
        "id": "27980ebf-318c-4cdd-8b08-52994fd64dba"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/83.webp",
        "id": "89050680-5005-4eef-b6a9-ad7b4c096f5b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/84.webp",
        "id": "e09c9985-fe4a-4992-b151-b7e9f03735d0"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/85.webp",
        "id": "07ff94ca-978f-4257-915d-a732dc684a22"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/86.webp",
        "id": "7d9d9a19-ad47-452f-ad07-e1d7e511a864"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/87.webp",
        "id": "ac1f28e9-5673-4beb-9fed-1f5311708023"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/88.webp",
        "id": "8277c246-60b3-4ba7-a922-34bd4158bdc1"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/89.webp",
        "id": "a5403526-3cd9-43c5-918e-c0088cdffa95"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/90.webp",
        "id": "c4085e76-4256-4307-9f36-cef1b1ed5115"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/91.webp",
        "id": "2cdbf47e-a15b-4a57-bfb0-4416f3ab987a"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/92.webp",
        "id": "ad3bdb26-ca05-4424-9701-a9276a9b5d60"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/93.webp",
        "id": "043bfde7-2a0b-406b-a5e6-fdf8b22e1d8f"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/94.webp",
        "id": "4747a2b4-693a-4717-800e-f9cd3b706cee"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/95.webp",
        "id": "374407a9-9652-4a50-9dff-8edceee6108b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/96.webp",
        "id": "91986503-7267-456e-8afe-cdd50aa2a9fa"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/97.webp",
        "id": "f32a7e28-17cf-4610-95a5-aad4f187c529"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/98.webp",
        "id": "1cfac23a-5ef1-4bb7-ad35-be23f00c8df7"
    }
    ]
}