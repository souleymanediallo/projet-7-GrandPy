from app import parser


class TestParser:
    def test_sentence_to_lowercase(self):
        ask = parser.Parser("WHERE ARE YOU ?")
        assert ask.sentence_to_lowercase() == "where are you ?"

    def test_remove_special(self):
        ask = parser.Parser(",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²")
        assert ask.remove_special() == "                                "

    def test_change_letter(self):
        ask = parser.Parser("éèêëãàäâåîïìöôòõñûüÿ")
        assert ask.change_letter() == "eeeeaaaaaiiioooonuuy"

    def test_move_space(self):
        ask = parser.Parser("  some problem with sentence  ")
        assert ask.move_space() == "some problem with sentence"



