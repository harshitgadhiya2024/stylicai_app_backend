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
        "background_image": "https://backendapp.stylic.ai/download/0.webp",
        "id": "545ad8f4-5fc8-4074-9ee8-088635dbf7cd"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/1.webp",
        "id": "97ce1db2-9bb9-4b1d-9458-a61217c06929"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/2.webp",
        "id": "9b7b01c7-e439-4bbb-9053-f287fcf3f5d5"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/3.webp",
        "id": "2774662b-216d-4540-b34f-479943a2e5bb"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/4.webp",
        "id": "eb7fe0ab-0db8-4f6b-80cb-d5f7a507d038"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/5.webp",
        "id": "6f3cac72-ec0c-4e10-babb-9200d7e8b697"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/6.webp",
        "id": "f96c4b01-7bc7-4081-99bf-8a90ef61b6e2"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/7.webp",
        "id": "530b4eec-f6ee-4ec0-80dc-d27486ab71ea"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/8.webp",
        "id": "03bb5d23-798e-4426-8473-a1afe5fb2618"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/9.webp",
        "id": "f22604cc-4e4d-4817-8abe-33c6383568a5"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/10.webp",
        "id": "38231500-bfdf-44da-8f3e-88ccc979e6a6"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/11.webp",
        "id": "544e6e82-9606-4961-8c8d-3ecf061f0140"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/12.webp",
        "id": "bb138d22-d971-4118-8f9b-a23d46d9ae78"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/13.webp",
        "id": "2fb9937e-b886-440a-9fbe-7754c8b854bf"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/14.webp",
        "id": "f9c7e885-4ea7-43bd-8b09-556f0f454773"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/15.webp",
        "id": "1749d41f-a80f-4bee-a2e7-a4b869fb35e2"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/16.webp",
        "id": "0ea43edc-01f4-4369-ab9d-08a7a968428d"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/17.webp",
        "id": "4966ee0a-3593-49d7-a6b9-054cac68b055"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/18.webp",
        "id": "5ed81038-eaba-4421-9398-f9b118c28715"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/19.webp",
        "id": "9d088613-493d-4952-a6c5-16c241f7d677"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/20.webp",
        "id": "bb46b265-11e4-498c-be6c-965d6c21a326"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/21.webp",
        "id": "b8d87933-cb35-4677-a631-dfa35e983702"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/22.webp",
        "id": "2fd1564e-7896-4ead-89b5-96e3d89f1296"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/23.webp",
        "id": "c1b184d8-b0c5-4e38-a04c-e16481461ea5"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/24.webp",
        "id": "01c1a14f-f0fb-452e-bba0-59854e5859ac"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/25.webp",
        "id": "3a3128a6-7ff7-49b8-a140-cf292348e273"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/26.webp",
        "id": "1f0240fa-ecad-4b4d-8dec-440d366670a3"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/27.webp",
        "id": "dd5656eb-a4ab-49c0-8483-43422858af01"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/28.webp",
        "id": "097edf24-8e4d-4dc0-be94-1c06eb7069e5"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/29.webp",
        "id": "3d7f6f00-3b1b-41e2-a212-88f95f895669"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/30.webp",
        "id": "bc1e9f3a-53fb-4726-9096-f9891da46a79"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/31.webp",
        "id": "4cb83a63-f7db-4fbc-a255-d2f75560c8af"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/32.webp",
        "id": "0f73ec41-e99e-4e56-a2fd-fa9b3d832dad"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/33.webp",
        "id": "0922d95a-5462-47fb-b96b-7e3fdee5de56"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/34.webp",
        "id": "ac90b765-6b9b-4f87-b109-c7cfb04e02b1"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/35.webp",
        "id": "e67fe253-1de2-4218-bd2f-d68b6c031fde"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/36.webp",
        "id": "adbba849-5f41-4f32-95a0-30a0b2b5522b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/37.webp",
        "id": "2e77cf53-471d-437e-9d18-705462bbc494"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/38.webp",
        "id": "509cbc99-e273-4406-bdfd-b10acf0da980"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/39.webp",
        "id": "5997ac85-3c1d-4480-b97c-88554e3a09a8"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/40.webp",
        "id": "7cdd9a9a-0ada-4c77-9512-26263c59f6d9"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/41.webp",
        "id": "e3772133-2d9b-4d07-b7e9-a7e1fd4acb79"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/42.webp",
        "id": "9e782194-91b6-4bd2-8f01-710af30297a3"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/43.webp",
        "id": "17f275aa-b5de-4427-9bb2-5807412dd5fa"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/44.webp",
        "id": "fc731809-a3cc-4607-969e-d15cb0f46348"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/45.webp",
        "id": "b748a748-3a2a-4441-95c5-c5f3e79ea72e"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/46.webp",
        "id": "21021ad8-df9f-4c9b-a383-9971038b173b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/47.webp",
        "id": "0d7d00a7-9fc2-429a-b49f-355fd5869f62"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/48.webp",
        "id": "91772414-8f5e-4f62-a095-fa0cf37f7370"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/49.webp",
        "id": "771868ab-ce7b-419d-af9e-9034f49ccd97"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/50.webp",
        "id": "b1fef18e-e732-44cc-af00-87b0a55ad893"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/51.webp",
        "id": "696bb0a9-e38b-4b87-9c05-c48095391232"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/52.webp",
        "id": "b3c4cdf3-136a-40ec-8e98-268cb34df806"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/53.webp",
        "id": "be94a6df-8e08-449b-bc25-72525039faef"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/54.webp",
        "id": "b5b0d91b-883c-41dd-9cc2-0abab8323d80"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/55.webp",
        "id": "ef30f43e-7057-45ec-90d9-2e30be9745d2"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/56.webp",
        "id": "e81b8dd8-1132-4ccf-a477-fd6cec6c1fde"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/57.webp",
        "id": "15e0523c-3396-4941-a61a-e7ca808d9ef3"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/58.webp",
        "id": "9632e094-6ad7-4a9a-a603-18b6f17aa763"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/59.webp",
        "id": "78b2f92a-cbd9-45f3-9229-5c91e995c937"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/60.webp",
        "id": "b9f4fa6a-639f-4bef-983b-120fa5fa43d2"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/61.webp",
        "id": "ef03b519-30c9-4648-a09e-569953035345"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/62.webp",
        "id": "9e363681-2dee-4f23-87f2-ad6460ab95e2"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/63.webp",
        "id": "b59a412c-c8ab-47de-ab9e-1baffced5936"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/64.webp",
        "id": "dbec0e2b-c992-41cc-9432-13e5f59d4112"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/65.webp",
        "id": "ee11d7e9-576f-476d-b267-ddf2c106b65b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/66.webp",
        "id": "8cdfef93-e892-4a24-a11d-62e63e119656"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/67.webp",
        "id": "215f4c1d-c71f-4a09-a7c9-d2a201b86e2e"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/68.webp",
        "id": "f2411692-decc-418f-8c2e-7aead2cb07b7"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/69.webp",
        "id": "15d7c757-ab14-4810-a46a-63bfc9768134"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/70.webp",
        "id": "01f94797-a154-4362-95b9-4b2626e3a252"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/71.webp",
        "id": "9f628aab-c113-4697-a791-ca0ac1278a4e"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/72.webp",
        "id": "493dcd62-2e95-44ac-8e82-408e05d8dc3b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/73.webp",
        "id": "0e1d5cf9-a2c1-48b0-95e5-4d08872fdc45"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/74.webp",
        "id": "3368c137-75dd-413e-b9ec-106d0103f804"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/75.webp",
        "id": "7b6ee8a6-58a5-4403-860e-5b8ecd5537d3"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/76.webp",
        "id": "f9be17c0-2edc-474c-97d5-f8afb3e6eeb6"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/77.webp",
        "id": "c750cc28-c48d-4c2e-81e2-7fcf5c0419d7"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/78.webp",
        "id": "22de8490-7fe9-4140-bbeb-c9c29a6fc1d8"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/79.webp",
        "id": "17387bba-8613-43ca-bf3e-bcc3635de80e"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/80.webp",
        "id": "a6f7b032-3369-4c82-8fc0-bd410df5794e"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/81.webp",
        "id": "7a3677cf-34e0-41e4-b64c-5c56799d88ef"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/82.webp",
        "id": "6398a62c-d4e4-44fc-86dd-d4f06afa7123"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/83.webp",
        "id": "f581672e-5a2c-4fff-8c15-a776442a8a51"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/84.webp",
        "id": "9291bf52-fc02-4687-8943-8d6b20c64db1"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/85.webp",
        "id": "34b3f94a-61b9-4e65-a6bf-cf3faaef1cf5"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/86.webp",
        "id": "b0b320e9-e0c2-4582-80f8-6ed15919d8a6"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/87.webp",
        "id": "f2f8d17a-7828-4f7b-8207-8abaa0974e98"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/88.webp",
        "id": "2091eafd-f128-4c16-82f0-e319d455325b"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/89.webp",
        "id": "61c92d23-462a-4896-9553-fe5716b81959"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/90.webp",
        "id": "a82dbbec-7ae2-4c4f-b4d3-ed7047408a14"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/91.webp",
        "id": "18384727-b26c-4406-a874-1207538786e8"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/92.webp",
        "id": "c648df32-f8ce-4787-acba-47adb3641263"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/93.webp",
        "id": "c261f827-9fd2-4e2c-aafe-12e270fab987"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/94.webp",
        "id": "f13bfe66-589e-4344-9a89-ddebe0cde7a7"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/95.webp",
        "id": "3de0bc9a-a582-4e67-bdda-52a0b5dd7f85"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/96.webp",
        "id": "c21e87c4-9ae4-4a3d-81dc-2509ccfdc897"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/97.webp",
        "id": "cbbbb5ef-c532-4330-899c-52c579441964"
    },
    {
        "background_image": "https://backendapp.stylic.ai/download/98.webp",
        "id": "d14cf9d7-db0e-4353-8873-aa3b9cd04b76"
    }
    ]
}