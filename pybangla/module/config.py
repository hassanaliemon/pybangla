
import re
class Config:
    data = {
        "en":{
            "number"   : ["0","1","2","3","4","5", "6", "7","8", "9", "10", "11", "12"],
            "weekdays" : ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
            "months"   : ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november",  "december"],
            "seasons" : ["summer", "wet season", "autumn","dry season", "winter", "spring"],
            "number_mapping": {'0': 'জিরো', '1': 'ওয়ান', '2': 'টু', '3': 'থ্রি', '4': 'ফোর', '5': 'ফাইভ', '6': 'সিক্স', '7': 'সেভেন', '8': 'এইট', '9': 'নাইন'}
            
            },
        "bn":{
            "number"   : ["০","১","২","৩","৪", "৫", "৬", "৭", "৮", "৯", "১০", "১১", "১২"],
            "weekdays" : ["সোমবার", "মঙ্গলবার", "বুধবার","বৃহস্পতিবার", "শুক্রবার", "শনিবার", "রবিবার"],
            "months"   : ["জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন", "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর",  "ডিসেম্বর"],
            "option_name" :  ["বৈশাখ", "জ্যৈষ্ঠ","আষাঢ়", "শ্রাবণ", "ভাদ্র", "আশ্বিন", "কার্তিক", "অগ্রহায়ণ", "পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র"],
            "seasons"  : ["গ্রীষ্ম","বর্ষা", "শরৎ", "হেমন্ত", "শীত", "বসন্ত"],
            "number_mapping": {'০':'শূন্য', '১':'এক', '২':'দুই', '৩':'তিন', '৪':'চার', '৫':'পাঁচ', '৬':'ছয়', '৭':'সাত', '৮':'আট', '৯':'নয়'}

            }
    }
    bn_number_word_mapping = {'০':'শূন্য', '১':'এক', '২':'দুই', '৩':'তিন', '৪':'চার', '৫':'পাঁচ', '৬':'ছয়', '৭':'সাত', '৮':'আট', '৯':'নয়'}

    bn_regex = r'[০-৯]+'
    en_regex = r'[0-9]+'
    samples = ["-", ",", "/", " "]
    _currency = {"৳" : "টাকা", "$" : "ডলার", "£" : "পাউন্ড", "€" : "ইউরো", "¥" : "ইয়েন", "₹" : "রুপি", "₽" : "রুবেল", "₺" : "লিরা"}
    en_to_bn_digits_mapping = {e : b for e, b in zip(data["en"]["number"], data["bn"]["number"])}
    bn_to_en_digits_mapping = {v : k for k, v in en_to_bn_digits_mapping.items()}
    en_month_shortname = [i[:3] for i in data["en"]["months"]]

    data["bn"]["digits_mapping"] = en_to_bn_digits_mapping
    data["en"]["digits_mapping"] = bn_to_en_digits_mapping
    data["en"]["option_name"] = en_month_shortname
    
    _bangla2english_digits_mapping = {'১':'1', '২':'2', '৩':'3', '৪':'4', '৫':'5', '৬':'6', '৭':'7', '৮':'8', '৯':'9', '০':'0'}

    _english2bangla2_digits_mapping = {j:i for i, j in _bangla2english_digits_mapping.items()}
 
    
    
    
    bn_word_map = {
    'শূন্য': '0', 'এক': '1', 'দুই': '2', 'তিন': '3', 'চার': '4', 'পাঁচ': '5', 'ছয়': '6', 'সাত': '7', 'আট': '8', 'নয়': '9', 'দশ': '10', 
    'এগারো': '11', 'বারো': '12', 'তেরো': '13', 'চৌদ্দ': '14', 'পনেরো': '15', 'ষোল': '16', 'সতেরো': '17', 'আঠারো': '18', 'উনিশ': '19', 'বিশ': '20',
    'একুশ': '21', 'বাইশ': '22', 'তেইশ': '23', 'চব্বিশ': '24', 'পঁচিশ': '25', 'ছাব্বিশ': '26', 'সাতাশ': '27', 'আঠাশ': '28', 'ঊনত্রিশ': '29', 'ত্রিশ': '30',
    'একত্রিশ': '31', 'বত্রিশ': '32', 'তেত্রিশ': '33', 'চৌত্রিশ': '34', 'পঁয়ত্রিশ': '35', 'ছত্রিশ': '36', 'সাঁইত্রিশ': '37', 'আটত্রিশ': '38', 'ঊনচল্লিশ': '39', 'চল্লিশ': '40', 
    'একচল্লিশ': '41', 'বিয়াল্লিশ': '42', 'তেতাল্লিশ': '43', 'চুয়াল্লিশ': '44', 'পঁয়তাল্লিশ': '45', 'ছেচল্লিশ': '46', 'সাতচল্লিশ': '47', 'আটচল্লিশ': '48', 'ঊনপঞ্চাশ': '49', 'পঞ্চাশ': '50', 
    'একান্ন': '51', 'বাহান্ন': '52', 'তিপ্পান্ন': '53', 'চুয়ান্ন': '54', 'পঞ্চান্ন': '55', 'ছাপ্পান্ন': '56', 'সাতান্ন': '57', 'আটান্ন': '58', 'ঊনষাট': '59', 'ষাট': '60', 
    'একষট্টি': '61', 'বাষট্টি': '62', 'তেষট্টি': '63', 'চৌষট্টি': '64', 'পঁয়ষট্টি': '65', 'ছেষট্টি': '66', 'সাতষট্টি': '67', 'আটষট্টি': '68', 'ঊনসত্তর': '69', 'সত্তর': '70', 
    'একাত্তর': '71', 'বাহাত্তর': '72', 'তিয়াত্তর': '73', 'চুয়াত্তর': '74', 'পঁচাত্তর': '75', 'ছিয়াত্তর': '76', 'সাতাত্তর': '77', 'আটাত্তর': '78', 'ঊনআশি': '79', 'আশি': '80', 
    'একাশি': '81', 'বিরাশি': '82', 'তিরাশি': '83', 'চুরাশি': '84', 'পঁচাশি': '85', 'ছিয়াশি': '86', 'সাতাশি': '87', 'আটাশি': '88', 'ঊননব্বই': '89', 'নব্বই': '90', 
    'একানব্বই': '91', 'বিরানব্বই': '92', 'তিরানব্বই': '93', 'চুরানব্বই': '94', 'পঁচানব্বই': '95', 'ছিয়ানব্বই': '96', 'সাতানব্বই': '97', 'আটানব্বই': '98', 'নিরানব্বই': '99'
}

    bn_hundreds_1={'একশ': "100",'দুইশ': "200", 'তিনশ':"300",'চারশ': "400",'পাঁচশ':"500",'ছয়শ':"600",'সাতশ': "700",'আটশ':"800",'নয়শ':"900"}

    target_chars = ["শো", "শত", "শ"]

    checking_hunderds = ['একশ', 'দুইশ', 'তিনশ', 'চারশ', 'পাঁচশ', 'ছয়শ', 'সাতশ', 'আটশ', 'নয়শ', 'লক্ষ', 'হাজার', 'কোটি', 'লাখ', "একশত"]

    decimale_chunks = {"কোটি" : "10000000",'লক্ষ': "100000", "লাখ": "100000", 'হাজার': "1000"}

    adjust_number = {"সাড়ে":0.5, "সারে":0.5, "আড়াই": 2.5, "আরাই":2.5, "দেড়":0.5, "দের":0.5}
    conjugative_number = {"ডবল": "2", "ডাবল": "2", "ট্রিপল": "3"}
    en_number_mapping = {"জিরো": "0" ,"ওয়ান": "1", "টু": "2", "থ্রি":"3", "ফোর":"4", "ফাইভ":"5", "সিক্স":"6", "সেভেন":"7", "এইট":"8", "নাইন":"9", "টেন": "10"}

    en_doshok_map = {
        'ইলেভেন':"11", 'টুয়েলভ':"12", 'থার্টিন':"13", 'ফোরটিন':"14", 'ফিফটিন':"15", 'সিক্সটিন':"16", 'সেভেনটিন':"17", 'এইটিন':"18", 
        'নাইনটিন':"19","টুয়েন্টি": "20", "থার্টি": "30", "ফর্টি":"40", "ফিফ্টি": "50", "সিক্সটি": "60", "সেভেন্টি":"70", "এটি": "80", "নাইনটি":"90"
        }

    fraction_int = {"ডেরশ": "150", "দেড়শো":"150", "দেড়শত":"150", "দেরশ": "150", "আরাইশ": "250", "আড়াইশ": "250", "আরাইশো" : "250", "আড়াইশত": "250" }

    


    function_mapping = {
                    "সাড়ে" : "equation_of_sare_and_der", "সারে": "equation_of_sare_and_der", "আড়াই": "equation_of_arai", 
                    "আরাই": "equation_of_arai", "দেড়": "equation_of_sare_and_der", "দের" : "equation_of_sare_and_der"
                    }

    bn_hundreds_2 = {i.replace(i[-1], "শত"): v for i, v in bn_hundreds_1.items()}
    bn_hundreds_3 = {i.replace(i[-1], "শো"): v for i, v in bn_hundreds_1.items()}

    bn_hundreds = {**bn_hundreds_1, **bn_hundreds_2, **bn_hundreds_3}
    hundreds = list(bn_hundreds.keys())
    checking_adjust = list(adjust_number.keys())
    checking_conjugative_number = list(conjugative_number.keys())

    
    
    _abbreviations = {
        "en": [
            (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
            for x in [
                ("mrs", "misess"),
                ("mr", "mister"),
                ("dr", "doctor"),
                ("st", "saint"),
                ("co", "company"),
                ("jr", "junior"),
                ("maj", "major"),
                ("gen", "general"),
                ("drs", "doctors"),
                ("rev", "reverend"),
                ("lt", "lieutenant"),
                ("hon", "honorable"),
                ("sgt", "sergeant"),
                ("capt", "captain"),
                ("esq", "esquire"),
                ("ltd", "limited"),
                ("col", "colonel"),
                ("ft", "fort"),
            ]
        ],
        "bn": [
            (re.compile(r"%s" % x[0], re.IGNORECASE), x[1])
            for x in [
                ("সাঃ", "সাল্লাল্লাহু আলাইহি ওয়া সাল্লাম"),                  
                ("আঃ", "আলাইহিস সালাম"),
                ("রাঃ", "রাদিআল্লাহু আনহু"),
                ("রহঃ", "রহমাতুল্লাহি আলাইহি"),
                ("রহিঃ", "রহিমাহুল্লাহ"),
                ("হাফিঃ", "হাফিযাহুল্লাহ"),
                ("দাঃবাঃ", "দামাত বারাকাতুহুম,দামাত বারাকাতুল্লাহ"),
                ("মোঃ",  "মোহাম্মদ"),
                ("মোসাঃ",  "মোসাম্মত"),
                ("মোছাঃ", "মোছাম্মত"),
                ("আ:" , "আব্দুর"),
                ("ডাঃ" , "ডাক্তার"),
            ]
        ]
    }

    _symbols = {
            "en": [
                (re.compile(r"%s" % re.escape(x[0]), re.IGNORECASE), x[1])
                for x in [
                    ("&", " and "),
                    ("@", " at "),
                    ("%", " percent "),
                    ("#", " hash "),
                    ("°", " degree ")
                ]
            ],
            "bn": [
                (re.compile(r"%s" % re.escape(x[0]), re.IGNORECASE), x[1])
                for x in [
                    ("&", " এবং"),
                    ("@", " এট দা রেট"),
                    ("%", " পারসেন্ট"),
                    ("#", " হ্যাশ"),
                    ("°", " ডিগ্রী")
                ]
            ],
        }

    
    _ordinal_re = {
        "en": re.compile(r"([0-9]+)(st|nd|rd|th)"),
        "bn": [
                (re.compile(r"%s" % re.escape(x[0]), re.IGNORECASE), x[1])
                for x in [
                    ("১ম", "প্রথম"),
                    ("২য়", "দ্বিতীয়"),
                    ("৩য়", "তৃতীয়"),
                    ("৪র্থ", "চতুর্থ"),
                    ("৫ম","পঞ্চম"),
                    ("৬ষ্ঠ", "ষষ্ঠ"),
                    ("৭ম", "সপ্তম"),
                    ("৮ম", "অষ্টম"),
                    ("৯ম", "নবম"),
                    ("১০ম", "দশম")
                ]
            ],
        }
    
    
    _whitespace_re = re.compile(r"\s+")
    
    
    _bangla_numeric_words = {
        'zero':'শূন্য',
        'one':'এক',
        'two':'দুই',
        'three':'তিন',
        'four':'চার',
        'five':'পাঁচ',
        'six':'ছয়',
        'seven':'সাত',
        'eight':'আট',
        'nine':'নয়',
        "hundred" : "শত", 
        "thousand" : "হাজার", 
        "lakh" : "লক্ষ", 
        "crore" : "কোটি" ,
        "ten" : "দশ",
        "eleven" : "এগারো",
        "twelve" : "বারো",
        "thirteen" : "তেরো",
        "fourteen" : "চৌদ্দ",
        "fifteen" : "পনেরো",
        "sixteen" : "ষোল",
        "seventeen" : "সতেরো",
        "eighteen" : "আঠারো",
        "nineteen" : "উনিশ",
        "twenty" : "বিশ",
        "twenty-one" : "একুশ",
        "twenty-two" : "বাইশ",
        "twenty-three" : "তেইশ",
        "twenty-four" : "চব্বিশ",
        "twenty-five" : "পঁচিশ",
        "twenty-six" : "ছাব্বিশ",
        "twenty-seven" : "সাতাশ",
        "twenty-eight" : "আঠাশ",
        "twenty-nine" : "ঊনত্রিশ",
        "thirty" : "ত্রিশ",
        "thirty-one" : "একত্রিশ",
        "thirty-two" : "বত্রিশ",
        "thirty-three" : "তেত্রিশ",
        "thirty-four" : "চৌত্রিশ",
        "thirty-five" : "পঁয়ত্রিশ",
        "thirty-six" : "ছত্রিশ",
        "thirty-seven" : "সাইত্রিশ",
        "thirty-eight" : "আটত্রিশ",
        "thirty-nine" : "ঊনচল্লিশ",
        "forty" : "চল্লিশ",
        "forty-one" : "একচল্লিশ",
        "forty-two" : "বেয়াল্লিশ",
        "forty-three" : "তেতাল্লিশ",
        "forty-four" : "চুয়াল্লিশ",
        "forty-five" : "পঁয়তাল্লিশ",
        "forty-six" : "ছেচল্লিশ",
        "forty-seven" : "সাতচল্লিশ",
        "forty-eight" : "আটচল্লিশ",
        "forty-nine" : "ঊনপঞ্চাশ",
        "fifty" : "পঞ্চাশ",
        "fifty-one" : "একান্ন",
        "fifty-two" : "বায়ান্ন",
        "fifty-three" : "তেপ্পান্ন",
        "fifty-four" : "চুয়ান্ন",
        "fifty-five" : "পঞ্চান্ন",
        "fifty-six" : "ছাপ্পান্ন",
        "fifty-seven" : "সাতান্ন",
        "fifty-eight" : "আটান্ন",
        "fifty-nine" : "ঊনষাট",
        "sixty" : "ষাট",
        "sixty-one" : "একষট্টি",
        "sixty-two" : "বাষট্টি",
        "sixty-three" : "তেষট্টি",
        "sixty-four" : "চৌষট্টি",
        "sixty-five" : "পঁয়ষট্টি",
        "sixty-six" : "ছেষট্টি",
        "sixty-seven" : "সাতষট্টি",
        "sixty-eight" : "আটষট্টি",
        "sixty-nine" : "ঊনসত্তর",
        "seventy" : "সত্তর",
        "seventy-one" : "একাত্তর",
        "seventy-two" : "বাহাত্তর",
        "seventy-three" : "তেয়াত্তর",
        "seventy-four" : "চুয়াত্তর",
        "seventy-five" : "পঁচাত্তর",
        "seventy-six" : "ছিয়াত্তর",
        "seventy-seven" : "সাতাত্তর",
        "seventy-eight" : "আটাত্তর",
        "seventy-nine" : "ঊনআশি",
        "eighty" : "আশি",
        "eighty-one" : "একাশি",
        "eighty-two" : "বিরাশি",
        "eighty-three" : "তিরাশি",
        "eighty-four" : "চুরাশি",
        "eighty-five" : "পঁচাশি",
        "eighty-six" : "ছিয়াশি",
        "eighty-seven" : "সাতাশি",
        "eighty-eight" : "আটাশি",
        "eighty-nine" : "ঊননব্বই",
        "ninety" : "নব্বই",
        "ninety-one" : "একানব্বই",
        "ninety-two" : "বিরানব্বই",
        "ninety-three" : "তিরানব্বই",
        "ninety-four" : "চুরানব্বই",
        "ninety-five" : "পঁচানব্বই",
        "ninety-six" : "ছিয়ানব্বই",
        "ninety-seven" : "সাতানব্বই",
        "ninety-eight" : "আটানব্বই",
        "ninety-nine" : "নিরানব্বই"
    }