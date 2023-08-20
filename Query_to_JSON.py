import openai
class QueryToJsonConverter:
    def __init__(self):
        self.openai_api_key = openai_api_key
        self.categories = {
            'gender': ['Men', 'Women', 'Boys', 'Girls', 'Unisex'],

            'subCategory': ['Topwear', 'Bottomwear', 'Watches', 'Socks', 'Shoes', 'Belts', 'Flip Flops', 'Bags', 'Innerwear', 'Sandal', 'Shoe Accessories', 'Fragrance', 'Jewellery',
            'Lips', 'Saree', 'Eyewear', 'Scarves', 'Dress', 'Loungewear and Nightwear',
            'Wallets', 'Apparel Set', 'Headwear', 'Mufflers', 'Skin Care', 'Makeup',
            'Free Gifts', 'Ties', 'Accessories', 'Nails', 'Beauty Accessories',
            'Water Bottle', 'Skin', 'Eyes', 'Bath and Body', 'Gloves',
            'Sports Accessories', 'Cufflinks', 'Sports Equipment', 'Stoles', 'Hair',
            'Perfumes', 'Home Furnishing', 'Umbrellas', 'Wristbands', 'Vouchers'],

            'articleType': ['Shirts', 'Jeans', 'Watches', 'Track Pants', 'Tshirts', 'Socks', 'Casual Shoes', 'Belts', 'Flip Flops', 'Handbags', 'Tops', 'Bra', 'Sandals', 'Shoe Accessories',
            'Sweatshirts', 'Deodorant', 'Formal Shoes', 'Bracelet', 'Lipstick', 'Flats',
            'Kurtas', 'Waistcoat', 'Sports Shoes', 'Shorts', 'Briefs', 'Sarees',
            'Perfume and Body Mist', 'Heels', 'Sunglasses', 'Innerwear Vests', 'Pendant',
            'Laptop Bag', 'Scarves', 'Dresses', 'Night suits', 'Skirts', 'Wallets',
            'Blazers', 'Ring', 'Kurta Sets', 'Clutches', 'Shrug', 'Backpacks', 'Caps',
            'Trousers', 'Earrings', 'Camisoles', 'Boxers', 'Jewellery Set', 'Dupatta',
            'Capris', 'Lip Gloss', 'Bath Robe', 'Mufflers', 'Tunics', 'Jackets', 'Trunk',
            'Lounge Pants', 'Face Wash and Cleanser', 'Necklace and Chains',
            'Duffel Bag', 'Sports Sandals', 'Foundation and Primer', 'Sweaters',
            'Free Gifts', 'Trolley Bag', 'Tracksuits', 'Swimwear', 'Shoe Laces',
            'Fragrance Gift Set', 'Bangle', 'Nightdress', 'Ties', 'Baby Dolls', 'Leggings',
            'Highlighter and Blush', 'Travel Accessory', 'Kurtis', 'Mobile Pouch',
            'Messenger Bag', 'Lip Care', 'Nail Polish', 'Eye Cream', 'Accessory Gift Set',
            'Beauty Accessory', 'Jumpsuit', 'Kajal and Eyeliner', 'Water Bottle',
            'Suspenders', 'Face Moisturisers', 'Lip Liner', 'Robe', 'Salwar and Dupatta',
            'Patiala', 'Stockings', 'Eyeshadow', 'Headband', 'Tights', 'Nail Essentials',
            'Churidar', 'Lounge Tshirts', 'Face Scrub and Exfoliator', 'Lounge Shorts',
            'Gloves', 'Wristbands', 'Tablet Sleeve', 'Ties and Cufflinks', 'Footballs',
            'Compact', 'Stoles', 'Shapewear', 'Nehru Jackets', 'Salwar', 'Cufflinks',
            'Jeggings', 'Hair Colour', 'Concealer', 'Rompers', 'Sunscreen', 'Booties',
            'Mask and Peel', 'Waist Pouch', 'Hair Accessory', 'Body Lotion', 'Rucksacks',
            'Basketballs', 'Lehenga Choli', 'Clothing Set', 'Mascara', 'Cushion Covers',
            'Key chain', 'Rain Jacket', 'Toner', 'Lip Plumper', 'Umbrellas',
            'Face Serum and Gel', 'Hat', 'Mens Grooming Kit', 'Makeup Remover',
            'Body Wash and Scrub', 'Suits', 'Ipad'],

            'baseColour': ['Navy Blue', 'Blue', 'Silver', 'Black', 'Grey', 'Green', 'Purple', 'White',
            'Beige', 'Brown', 'Bronze', 'Teal', 'Copper', 'Pink', 'Off White', 'Maroon',
            'Red', 'Khaki', 'Orange', 'Yellow', 'Charcoal', 'Gold', 'Steel', 'Tan', 'Multi',
            'Magenta', 'Lavender', 'Sea Green', 'Cream', 'Peach', 'Olive', 'Skin',
            'Burgundy', 'Coffee Brown', 'Grey Melange', 'Rust', 'Rose', 'Lime Green',
            'Mauve', 'Turquoise Blue', 'Metallic', 'Mustard', 'Taupe', 'Nude',
            'Mushroom Brown', 'Fluorescent Green'],

            'usage': ['Casual', 'Ethnic', 'Formal', 'Sports', 'Smart Casual', 'Travel', 'Party', 'Home']
        }
    
    def convert_query_to_json(self, query):
        # Call OpenAI API to generate a response
        response = self.generate_response(query)

        # Parse the response to extract relevant category information
        parsed_json = self.parse_response(response)
        
        return parsed_json

    def generate_response(self, query):
        openai.api_key = self.openai_api_key
        
        prompt = f"Convert the query '{query}' into JSON representation."
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can experiment with different engines
            prompt=prompt,
            max_tokens=100  # Adjust this based on response length
        )
        
        return response.choices[0].text.strip()
    
    def parse_response(self, response):
        json_dict = {
            'gender': None,
            'subCategory': None,
            'articleType': None,
            'baseColour': None,
            'usage': None
        }

        # Custom logic to parse the response and extract category information
        # You might need to use regular expressions or other methods here
        
        return json_dict

openai_api_key = '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'

# Create an instance of the QueryToJsonConverter
converter = QueryToJsonConverter()

# Example query
query = "Casual Black watch for Men"
result = converter.convert_query_to_json(query)
print(result)