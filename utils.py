from llama import LlamaModel
from config import hf_api_url, hf_headers
from fuzzywuzzy import process


class QueryToJson:
    def __init__(self):
        self.llama_model = LlamaModel(hf_api_url, hf_headers)
        self.categories = {
            'gender': ['Men', 'Women', 'Boys', 'Girls', 'Unisex'],

            'subCategory': ['Topwear', 'Bottomwear', 'Watches', 'Socks', 'Shoes', 'Belts', 'Flip Flops', 'Bags', 'Innerwear', 'Sandal', 'Shoe Accessories', 'Fragrance', 'Jewellery', 'Lips', 'Saree', 'Eyewear', 'Scarves', 'Dress', 'Loungewear and Nightwear', 'Wallets', 'Apparel Set', 'Headwear', 'Mufflers', 'Skin Care', 'Makeup',
            'Free Gifts', 'Ties', 'Accessories', 'Nails', 'Beauty Accessories',
            'Water Bottle', 'Skin', 'Eyes', 'Bath and Body', 'Gloves',
            'Sports Accessories', 'Cufflinks', 'Sports Equipment', 'Stoles', 'Hair',
            'Perfumes', 'Home Furnishing', 'Umbrellas', 'Wristbands', 'Vouchers'],

            'articleType': ['Shirts', 'Jeans', 'Watches', 'Track Pants', 'Tshirts', 'Socks', 'Shoes', 'Belts', 'Flip Flops', 'Handbags', 'Tops', 'Bra', 'Sandals', 'Shoe Accessories', 'Sweatshirts', 'Deodorant', 'Formal Shoes', 'Bracelet', 'Lipstick', 'Flats', 'Kurtas', 'Waistcoat', 'Sports Shoes', 'Shorts', 'Briefs', 'Sarees',
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

            'baseColour': ['Navy Blue', 'Blue', 'Silver', 'Black', 'Grey', 'Green', 'Purple', 'White', 'Beige', 'Brown', 'Bronze', 'Teal', 'Copper', 'Pink', 'Off White', 'Maroon', 'Red', 'Khaki', 'Orange', 'Yellow', 'Charcoal', 'Gold', 'Steel', 'Tan', 'Multi', 'Magenta', 'Lavender', 'Sea Green', 'Cream', 'Peach', 'Olive', 'Skin',
            'Burgundy', 'Coffee Brown', 'Grey Melange', 'Rust', 'Rose', 'Lime Green',
            'Mauve', 'Turquoise Blue', 'Metallic', 'Mustard', 'Taupe', 'Nude',
            'Mushroom Brown', 'Fluorescent Green'],

            'usage': ['Casual', 'Ethnic', 'Formal', 'Sports', 'Smart Casual', 'Travel', 'Party', 'Home']
        }
        self.prompt = '''
Given a query, your task is to just reply with a json that only has the following fields

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

The query string is: "%s"

        '''
    def compare(prev_value, curr_value, prev_score, curr_score):
        if curr_score > prev_score:
            return curr_value, curr_score
        else:
            return prev_value, prev_score
    
    def get_json_by_llama(self, query_str):
        # generate request with query_str in self.prompt

        request_str = self.prompt % query_str
        response = self.llama_model.query(request_str)
        return response
    
    def get_json_by_fuzzy_wuzzy(self, query):
        json_dict = {
            'gender': None,
            'subCategory': None,
            'articleType': None,
            'baseColour': None,
            'usage': None
        }
        
        best_match_gender, gender_score = process.extractOne(query, self.categories['gender'])

        best_match_sub_category, sub_category_score = process.extractOne(query, self.categories['subCategory'])
        
        best_match_article_type, article_type_score = process.extractOne(query, self.categories['articleType'])
        
        best_match_base_colour, base_colour_score = process.extractOne(query, self.categories['baseColour'])
        
        best_match_usage, usage_score = process.extractOne(query, self.categories['usage'])

        if gender_score > 45:
            json_dict['gender'] = best_match_gender
        if sub_category_score > 45:
            json_dict['subCategory'] = best_match_sub_category
        if article_type_score > 45:
            json_dict['articleType'] = best_match_article_type
        if base_colour_score > 45:
            json_dict['baseColour'] = best_match_base_colour
        if usage_score > 45:
            json_dict['usage'] = best_match_usage

        return json_dict

    def merge_json(self, json1, json2):
        # take all 4 fields from json2 and put into json1 if its None
        # return json1
        
        new_json = json1

        for key in json2.keys():
            if json1[key] is None:
                new_json[key] = json2[key]
        
        return new_json