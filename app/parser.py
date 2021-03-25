import json


class Parser:
    def __init__(self, sentence):
        self.sentence = sentence

    def __str__(self):
        return self.sentence

    def clean(self):
        self.sentence_to_lowercase()
        self.remove_special()
        self.change_letter()
        self.move_space()
        return self.sentence

    def sentence_to_lowercase(self):
        str = "WHERE ARE YOU ?"
        return str.lower()

    def remove_special(self):
        caract_in = ",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²"
        caract_out = "                                "
        result_caract = str.maketrans(caract_in, caract_out)
        return (",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²".translate(result_caract))

    def change_letter(self):
        caract_in = "éèêëãàäâåîïìöôòõñûüÿ"
        caract_out = "eeeeaaaaaiiioooonuuy"
        result_caract = str.maketrans(caract_in, caract_out)
        return ("éèêëãàäâåîïìöôòõñûüÿ".translate(result_caract))

    def move_space(self):
        move_space = "  some problem with sentence  "
        return move_space.strip().replace("  ", " ")

    def remove_stop_words(self):
        """Open file json and filter the words in a list"""
        with open('stop_words.json', 'r') as f:
            stop_words = json.load(f)

        cleaned_words = []

        for word in self.sentence.split():
            if word not in stop_words:
                cleaned_words.append(word)
        self.sentence = " ".join(cleaned_words)
