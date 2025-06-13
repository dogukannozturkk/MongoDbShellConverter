import re

class MongoJsonConverter:
    @staticmethod
    def convert_robo3t_to_compass(json_text: str) -> str:
        # ObjectId("...") → {"$oid": "..."}
        json_text = re.sub(r'ObjectId\("([a-fA-F0-9]{24})"\)', r'{"$oid": "\1"}', json_text)

        # NumberInt(...) → {"$numberInt": "..."}
        json_text = re.sub(r'NumberInt\("?(\d+)"?\)', r'{"$numberInt": "\1"}', json_text)

        # ISODate("...") → {"$date": "..."}
        json_text = re.sub(r'ISODate\("([^"]+)"\)', r'{"$date": "\1"}', json_text)

        return json_text

    @staticmethod
    def convert_compass_to_robo3t(json_text: str) -> str:
        # $oid → ObjectId("...")
        json_text = re.sub(r'{\s*"\$oid"\s*:\s*"([a-fA-F0-9]{24})"\s*}', r'ObjectId("\1")', json_text)

        # $numberInt → NumberInt(...)
        json_text = re.sub(r'{\s*"\$numberInt"\s*:\s*"(\d+)"\s*}', r'NumberInt(\1)', json_text)

        # $date → ISODate("...")
        json_text = re.sub(r'{\s*"\$date"\s*:\s*"([^"]+)"\s*}', r'ISODate("\1")', json_text)

        # Boolean ve null düzeltmeleri
        json_text = json_text.replace('true', 'true')  # opsiyonel
        json_text = json_text.replace('false', 'false')
        json_text = json_text.replace('null', 'null')

        return json_text