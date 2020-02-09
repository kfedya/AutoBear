class CreateJson:

    def bear_json(bear_type, bear_name, bear_age):
        bear_json = {
            "bear_type": bear_type,
            "bear_name": bear_name,
            "bear_age": bear_age

        }
        return bear_json

    def bear_etalon_json(bear_id, bear_type, bear_name, bear_age):
        etalon_bear = {
            "bear_id": bear_id,
            "bear_type": bear_type,
            "bear_name": bear_name,
            "bear_age": bear_age
        }
        return etalon_bear