
import json
import base64
import openai


class OpenAI:

    def __init__(self):

        # self.get_api_key(api_key_file_path)
        openai.api_key = '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'

        self.model = openai.Model.retrieve("text-davinci-003")

        self.prompt_raw = """

In this conversation, you will act as a query to json converter. Given a query, your task is to reply with a json that only has the following fields

input_dict = {
    'gender': 
    'subCategory': 
    'articleType': 
    'baseColour': 
    'usage':
}

Now you have classess for each of these fields

gender ['Men' 'Women' 'Boys' 'Girls' 'Unisex']



subCategory ['Topwear' 'Bottomwear' 'Watches' 'Socks' 'Shoes' 'Belts' 'Flip Flops'
 'Bags' 'Innerwear' 'Sandal' 'Shoe Accessories' 'Fragrance' 'Jewellery'
 'Lips' 'Saree' 'Eyewear' 'Scarves' 'Dress' 'Loungewear and Nightwear'
 'Wallets' 'Apparel Set' 'Headwear' 'Mufflers' 'Skin Care' 'Makeup'
 'Free Gifts' 'Ties' 'Accessories' 'Nails' 'Beauty Accessories'
 'Water Bottle' 'Skin' 'Eyes' 'Bath and Body' 'Gloves'
 'Sports Accessories' 'Cufflinks' 'Sports Equipment' 'Stoles' 'Hair'
 'Perfumes' 'Home Furnishing' 'Umbrellas' 'Wristbands' 'Vouchers']



articleType ['Shirts' 'Jeans' 'Watches' 'Track Pants' 'Tshirts' 'Socks' 'Casual Shoes'
 'Belts' 'Flip Flops' 'Handbags' 'Tops' 'Bra' 'Sandals' 'Shoe Accessories'
 'Sweatshirts' 'Deodorant' 'Formal Shoes' 'Bracelet' 'Lipstick' 'Flats'
 'Kurtas' 'Waistcoat' 'Sports Shoes' 'Shorts' 'Briefs' 'Sarees'
 'Perfume and Body Mist' 'Heels' 'Sunglasses' 'Innerwear Vests' 'Pendant'
 'Laptop Bag' 'Scarves' 'Dresses' 'Night suits' 'Skirts' 'Wallets'
 'Blazers' 'Ring' 'Kurta Sets' 'Clutches' 'Shrug' 'Backpacks' 'Caps'
 'Trousers' 'Earrings' 'Camisoles' 'Boxers' 'Jewellery Set' 'Dupatta'
 'Capris' 'Lip Gloss' 'Bath Robe' 'Mufflers' 'Tunics' 'Jackets' 'Trunk'
 'Lounge Pants' 'Face Wash and Cleanser' 'Necklace and Chains'
 'Duffel Bag' 'Sports Sandals' 'Foundation and Primer' 'Sweaters'
 'Free Gifts' 'Trolley Bag' 'Tracksuits' 'Swimwear' 'Shoe Laces'
 'Fragrance Gift Set' 'Bangle' 'Nightdress' 'Ties' 'Baby Dolls' 'Leggings'
 'Highlighter and Blush' 'Travel Accessory' 'Kurtis' 'Mobile Pouch'
 'Messenger Bag' 'Lip Care' 'Nail Polish' 'Eye Cream' 'Accessory Gift Set'
 'Beauty Accessory' 'Jumpsuit' 'Kajal and Eyeliner' 'Water Bottle'
 'Suspenders' 'Face Moisturisers' 'Lip Liner' 'Robe' 'Salwar and Dupatta'
 'Patiala' 'Stockings' 'Eyeshadow' 'Headband' 'Tights' 'Nail Essentials'
 'Churidar' 'Lounge Tshirts' 'Face Scrub and Exfoliator' 'Lounge Shorts'
 'Gloves' 'Wristbands' 'Tablet Sleeve' 'Ties and Cufflinks' 'Footballs'
 'Compact' 'Stoles' 'Shapewear' 'Nehru Jackets' 'Salwar' 'Cufflinks'
 'Jeggings' 'Hair Colour' 'Concealer' 'Rompers' 'Sunscreen' 'Booties'
 'Mask and Peel' 'Waist Pouch' 'Hair Accessory' 'Body Lotion' 'Rucksacks'
 'Basketballs' 'Lehenga Choli' 'Clothing Set' 'Mascara' 'Cushion Covers'
 'Key chain' 'Rain Jacket' 'Toner' 'Lip Plumper' 'Umbrellas'
 'Face Serum and Gel' 'Hat' 'Mens Grooming Kit' 'Makeup Remover'
 'Body Wash and Scrub' 'Suits' 'Ipad']



baseColour ['Navy Blue' 'Blue' 'Silver' 'Black' 'Grey' 'Green' 'Purple' 'White'
 'Beige' 'Brown' 'Bronze' 'Teal' 'Copper' 'Pink' 'Off White' 'Maroon'
 'Red' 'Khaki' 'Orange' 'Yellow' 'Charcoal' 'Gold' 'Steel' 'Tan' 'Multi'
 'Magenta' 'Lavender' 'Sea Green' 'Cream' 'Peach' 'Olive' 'Skin'
 'Burgundy' 'Coffee Brown' 'Grey Melange' 'Rust' 'Rose' 'Lime Green'
 'Mauve' 'Turquoise Blue' 'Metallic' 'Mustard' 'Taupe' 'Nude'
 'Mushroom Brown' 'Fluorescent Green']



usage ['Casual' 'Ethnic' 'Formal' 'Sports' 'Smart Casual' 'Travel' 'Party'
 'Home']



And for example a given string is "Casual Blue shirts for Men", you should reply

{
    'gender': 'Men',
    'subCategory': 'Topwear',
    'articleType': 'Shirts',
    'baseColour': 'Blue',
    'usage': 'Casual'
}

For missing or ambiguous values, keep it as None

for example for the query "Shirts"

{
    'gender': None,
    'subCategory': 'Topwear',
    'articleType': 'Shirts',
    'baseColour': None,
    'usage': None
}

This is the query:

%s

"""


    # def get_api_key(self, file_path):
    #     try:
    #         with open(file_path, 'r') as api_key:
    #             openai.api_key = api_key.readline()
    #     except FileNotFoundError:
    #         raise Exception(f"OpenAI API key file doesnt exist at {file_path}")


    def request(self, query):
        full_prompt = self.prompt_raw % query

        num_prompt_tokens = int(len(full_prompt) / 3) # estimate the length of the prompt
        max_tokens = 4000 - num_prompt_tokens # calculate the max available tokens for the response

        # call the OpenAI API
        response = openai.Completion.create(
            model='text-davinci-003', # the best GPT-3 model
            prompt=full_prompt,
            temperature=0,
            max_tokens=max_tokens,
            top_p=0.1,
            stop=['```'],
            echo=True # returns the whole prompt including the completion
        )

        result_raw = response.choices[0].text
        json_str = result_raw.split('```json')[1].strip() # since we used echo=True, we can split on the json marker

        return json.loads(json_str)