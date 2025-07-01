import datetime

QUOTES = [
    {
        "tamil": "அறிவற்றங் காக்குங் கருவி செறுவார்க்கும் உள்ளழிக்க லாகா அரண்",
        "english": "Wisdom is a weapon to ward off destruction; it is an inner fortress which enemies cannot destroy.",
        "source": "Thirukkural 421"
    },
    {
        "tamil": "அஞ்சாமை ஈகை அறிவூக்கம் இந்நான்கும் எஞ்சாமை வேந்தர்க் கியல்பு",
        "english": "Never to fail in fearlessness, liberality, wisdom, and energy is the kingly character.",
        "source": "Thirukkural 382"
    },
    {
        "tamil": "வினைவலியும் தன்வலியும் மாற்றான் வலியும் துணைவலியும் தூக்கிச் செயல்",
        "english": "Weigh strength of self, enemy, allies, and action — only then move forward.",
        "source": "Thirukkural 471"
    },
    {
        "tamil": "குணம்நாடிக் குற்றமும் நாடி அவற்றுள் மிகைநாடி மிக்க கொளல்",
        "english": "Weigh one’s virtues and faults, choose the greater — that is wisdom.",
        "source": "Thirukkural 504"
    },
    {
        "tamil": "நாநலம் என்னும் நலனுடைமை அந்நலம் யாநலத்து உள்ளதூஉம் அன்று",
        "english": "Speech of goodness is the greatest of all virtues — none compares.",
        "source": "Thirukkural 641"
    },
    {
        "tamil": "வினைத்திட்பம் என்பது ஒருவன் மனத்திட்பம் மற்றைய எல்லாம் பிற",
        "english": "Action’s strength is mind’s firmness; all other powers are secondary.",
        "source": "Thirukkural 661"
    },
    {
        "tamil": "பொருளல் லவரைப் பொருளாகச் செய்யும் பொருளல்லது இல்லை பொருள்",
        "english": "Only wealth can turn the worthless into worthy.",
        "source": "Thirukkural 751"
    },
    {
        "tamil": "பொருளென்னும் பொய்யா விளக்கம் இருளறுக்கும் எண்ணிய தேயத்துச் சென்று",
        "english": "Wealth is an unfailing lamp that removes darkness wherever it goes.",
        "source": "Thirukkural 753"
    },
    {
        "tamil": "அறன்ஈனும் இன்பமும் ஈனும் திறனறிந்து தீதின்றி வந்த பொருள்",
        "english": "Rightly earned wealth brings both virtue and delight.",
        "source": "Thirukkural 754"
    },
    {
        "tamil": "நீ தூங்கும் போது பணம் சம்பாதிக்க வழி கண்டுபிடிக்கவில்லை என்றால், வாழ்நாளெல்லாம் வேலை செய்ய வேண்டியதுதான்.",
        "english": "If you don't find a way to make money while you sleep, you will work until you die.",
        "source": "Warren Buffett"
    },
    {
        "tamil": "நீங்களாக உங்களை மேம்படுத்துவது உங்கள் செய்யக்கூடிய சிறந்த முதலீடாகும். நீங்கள் அதிகம் கற்றுக்கொண்டால், அதிகம் சம்பாதிப்பீர்கள்.",
        "english": "The best investment you can make is an investment in yourself. The more you learn, the more you'll earn.",
        "source": "Warren Buffett"
    },
    {
        "tamil": "செலவுசெய்த பிறகு சேமிக்காதீர்கள். சேமித்த பிறகு தான் செலவுசெய்யுங்கள்.",
        "english": "Do not save what is left after spending, but spend what is left after saving.",
        "source": "Warren Buffett"
    },
    {
        "tamil": "ஒரு நபரிடம் மூன்று விஷயங்களை பாருங்கள்: அறிவு, ஆற்றல், நேர்மை. நேர்மை இல்லையென்றால், மற்ற இரண்டு ஒன்றும் பயனில்லை.",
        "english": "Look for 3 things in a person: Intelligence, Energy & Integrity. If they lack integrity, the rest doesn't matter.",
        "source": "Warren Buffett"
    }

]

def get_quote():
    # Show quote based on current date (rotate daily)
    index = datetime.datetime.now().timetuple().tm_yday % len(QUOTES)
    return QUOTES[index]
