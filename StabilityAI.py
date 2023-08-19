
import requests
import json
import base64
from PIL import Image
from io import BytesIO

class StableDiffusion:
    def __init__(self, api_key_file_path):
        self.api_key = None
        self.api_host = 'https://api.stability.ai'

        self.get_api_key(api_key_file_path)

        # self.engine_id = "stable-diffusion-xl-1024-v1-0"
        self.engine_id = "stable-diffusion-512-v2-0"

        self.image_size = (512, 512)

        self.prompt_raw = """Show me a garment with the following properties,
it should be for a %s person who is %s. It should adhere to %s clothing style
It must be fit for wearing in %s season and it should include %s colour
Other than this, adhere to the below prompt to further customize the garment

%s""" #gender, age group, type, season, colour, prompt



    def get_api_key(self, file_path):
        try:
            with open(file_path, 'r') as api_key_file:
                self.api_key = api_key_file.readline()
        except FileNotFoundError:
            raise Exception(f"Stability API key file doesnt exist at {file_path}")


    def request_trend(self, prompt, user_id, user_preferance, image_url, strength=0.3):

        trend_response = requests.get(image_url)
        if not trend_response:
            raise Exception("Trend image url not reachable")


        trend_img = Image.open(BytesIO(trend_response.content))
        trend_img = trend_img.resize(self.image_size)
        trend_img.save(f"./out/{user_id}.png")

        print("response with trend")

        success = self.request(prompt, user_id, user_preferance, strength=strength)

        return success


    def request(self, prompt, user_id, user_preferance, strength=0.45):

        full_prompt = self.prompt_raw % (
            user_preferance['gender'] if user_preferance['gender'] is not None else '',
            'a ' + user_preferance['age'] if user_preferance['age'] is not None else 'any age',
            ' or '.join(user_preferance['type']) if user_preferance['type'] else 'any',
            user_preferance['season'] if user_preferance['season'] is not None else 'any',
            ' and '.join(user_preferance['colour']) if user_preferance['colour'] else 'any',
            prompt

            )

        response = requests.post(
            f"{self.api_host}/v1/generation/{self.engine_id}/image-to-image",
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            },
            files={
                "init_image": open(f"./out/{user_id}.png", "rb")
            },
            data={
                "image_strength": strength,
                "init_image_mode": "IMAGE_STRENGTH",
                "text_prompts[0][text]": full_prompt,
                "cfg_scale": 35,
                "samples": 1,
                "steps": 30,
                "style_preset": "photographic",
            }
        )


        if response.status_code != 200:
            print(response.reason)
            return "FAIL"

        data = response.json()

        print("response!!")

        image = Image.open(BytesIO(base64.b64decode(data['artifacts'][0]["base64"])))
        image = image.resize(self.image_size)
        image.save(f"./out/{user_id}.png")

        return data["artifacts"][0]["finishReason"]

    def request_no_trend(self, prompt, user_id, user_preferance):

        full_prompt = self.prompt_raw % (
            user_preferance['gender'] if user_preferance['gender'] is not None else '',
            'a ' + user_preferance['age'] if user_preferance['age'] is not None else 'any age',
            ' or '.join(user_preferance['type']) if user_preferance['type'] else 'any',
            user_preferance['season'] if user_preferance['season'] is not None else 'any',
            ' and '.join(user_preferance['colour']) if user_preferance['colour'] else 'any',
            prompt

            )

        response = requests.post(
            f"{self.api_host}/v1/generation/{self.engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": full_prompt
                    }
                ],
                "cfg_scale": 35,
                "height": self.image_size[0],
                "width": self.image_size[1],
                "samples": 1,
                "steps": 30,
                "style_preset": "photographic",
            },
        )

        if response.status_code != 200:
            print(response.reason)
            return "FAIL"

        data = response.json()


        # for i, image in enumerate(data["artifacts"]):
        #     with open(f"./out/{user_id}.png", "wb") as f:
        #         f.write(base64.b64decode(image["base64"]))

        print("response without trend")

        image = Image.open(BytesIO(base64.b64decode(data['artifacts'][0]["base64"])))
        image = image.resize(self.image_size)
        image.save(f"./out/{user_id}.png")

        return data["artifacts"][0]["finishReason"]