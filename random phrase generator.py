import random

# se = re.compile(r'\W*\b\w{1,2}\b')
# yut = se.sub('', fre)
# print(yut)

word1 = ["truth", "lot", "east", "turn", "put", "key", "class", "particular", "phone", "movement", "position",
         "private", "consumer", "violence", "administration", "market", "game", "drive", "common", "include", "star",
         "level", "under", "cover", "expert", "sexual", "participant", "doctor", "require", "activity", "southern",
         "example", "themselves", "organization", "scene", "must", "impact", "mother", "writer", "role", "develop",
         "likely", "down", "enjoy", "pain", "second", "argue", "assume", "win", "exactly", "visit", "morning",
         "tonight", "its", "choose", "style", "moment", "force", "radio", "husband", "necessary", "power", "nothing",
         "any", "cup", "reflect", "theory", "outside", "speak", "car", "remain", "spend", "system", "thing",
         "including", "five", "difficult", "career", "above", "feeling", "create"]

word2 = ["throw", "four", "few", "attorney", "interview", "death", "worry", "before", "imagine", "hit", "son", "night",
         "claim", "parent", "nice", "song", "record", "there", "war", "catch", "evidence", "interest", "also",
         "society", "issue", "check", "live", "voice", "much", "usually", "page", "church", "avoid", "form", "business",
         "pretty", "try", "industry", "gun", "safe", "think", "significant", "question", "prepare", "spring", "space",
         "television", "herself", "hundred", "none", "score", "three", "among", "film", "hard", "thus", "she", "least",
         "across", "play", "reach", "someone", "finish", "difference", "need", "which", "lie", "modern", "material",
         "direction", "full", "meeting", "strategy", "hold", "why", "civil", "treat", "cut", "then", "toward",
         "picture", "point", "dinner"]

word3 = ["news", "place", "treatment", "offer", "lead", "south", "stage", "rich", "young", "professor", "everybody",
         "memory", "event", "beautiful", "fly", "sure", "recently", "plant", "traditional", "answer", "table", "kind",
         "rise", "enough", "nearly", "former", "remove", "really", "country", "site", "daughter", "water", "current",
         "design", "myself", "degree", "past", "learn", "adult", "successful", "recent", "today", "see", "how", "feel",
         "big", "realize", "white", "rock", "maybe", "thousand", "arm", "tell", "idea", "camera", "size", "watch",
         "process", "top", "what", "study", "professional", "hotel", "victim", "beyond", "agreement", "begin", "sense",
         "several", "house", "standard", "attention", "firm", "fund", "focus", "could", "threat", "positive",
         "computer", "bring"]

word4 = ["certain", "contain", "oil", "box", "economy", "suffer", "job", "leg", "structure", "provide", "employee",
         "card", "member", "old", "deal", "once", "close", "official", "trial", "couple", "cancer", "easy", "step",
         "end", "rest", "company", "raise", "building", "painting", "start", "travel", "friend", "foot", "media",
         "energy", "loss", "response", "because", "ready", "Congress", "somebody", "people", "set", "shoulder",
         "available", "discussion", "say", "prove", "collection", "data", "born", "heat", "case", "vote", "father",
         "look", "culture", "next", "family", "dog", "than", "state", "action", "like", "accept", "American",
         "decision", "program", "analysis", "value", "your", "west", "road", "area", "many", "possible", "too", "well",
         "capital", "wish", "short", "machine", "language", "method", "call", "garden"]

word5 = ["piece", "goal", "group", "anyone", "draw", "determine", "green", "forward", "source", "recognize", "pressure",
         "agency", "would", "director", "statement", "teacher", "pass", "politics", "establish", "hear", "better",
         "stock", "reason", "research", "ability", "item", "Mrs", "tough", "problem", "fight", "newspaper", "good",
         "summer", "clearly", "during", "later", "work", "move", "may", "cell", "sing", "increase", "world", "clear",
         "consider", "foreign", "build", "development", "wife", "debate", "often", "others", "billion", "front",
         "leader", "admit", "his", "anything", "rule", "audience", "and", "measure", "early", "still", "with", "talk",
         "here", "child", "tend", "special", "western", "make", "authority", "little", "only", "black", "the",
         "control", "man", "personal", "left", "main", "choice", "know", "however"]

word6 = ["other", "throughout", "officer", "training", "plan", "law", "want", "bit", "hair", "new", "term",
         "generation", "buy", "suggest", "type", "improve", "unit", "from", "boy", "change", "against", "music", "wait",
         "lay", "yeah", "weapon", "history", "share", "town", "food", "eight", "return", "probably", "health", "shot",
         "care", "quite", "success", "again", "technology", "bar", "low", "section", "campaign", "simply", "experience",
         "behind", "fish", "expect", "huge", "lose", "stand", "total", "middle", "them", "shoot", "message", "property",
         "final", "individual", "that", "line", "artist", "legal", "letter", "major", "window", "million", "read",
         "have", "practice", "magazine", "minute", "their", "range", "peace", "where", "according", "drop", "number",
         "eye", "especially", "rather"]

word7 = ["ten", "economic", "happen", "note", "fail", "upon", "week", "information", "near", "dead", "season", "coach",
         "meet", "produce", "sometimes", "land", "popular", "international", "body", "school", "until", "prevent",
         "north", "smile", "per", "investment", "through", "relate", "attack", "add", "quickly", "most", "wear",
         "character", "best", "entire", "ago", "something", "seat", "year", "political", "report", "thought", "floor",
         "first", "either", "important", "home", "executive", "reality", "responsibility", "trouble", "kill",
         "cultural", "true", "long", "center", "serious", "public", "account", "conference", "article", "fear", "life",
         "detail", "allow", "door", "agree", "population", "within", "animal", "day", "environmental", "strong",
         "approach", "bad", "not", "reveal", "agent", "small", "our", "follow", "image", "her"]
word8 = ["Democrat", "eat", "both", "run", "field", "less", "natural", "miss", "guy", "each", "identify", "staff",
         "almost", "you", "subject", "just", "might", "room", "wide", "beat", "after", "soon", "military", "century",
         "air", "alone", "ahead", "over", "local", "sex", "around", "itself", "more", "service", "fill", "woman",
         "party", "physical", "same", "mean", "out", "laugh", "single", "along", "gas", "baby", "various", "marriage",
         "some", "series", "situation", "medical", "real", "who", "indeed", "surface", "love", "become", "break",
         "education", "last", "own", "bill", "those", "kid", "region", "push", "suddenly", "happy", "already", "show",
         "maintain", "street", "high", "when", "six", "national", "wrong", "light", "defense", "concern", "side",
         "serve", "central", "period", "specific", "listen", "team", "city"]

word9 = ["glass", "arrive", "together", "matter", "sort", "fall", "whose", "challenge", "fact", "test", "pay", "reduce",
         "security", "stay", "great", "operation", "free", "yourself", "shake", "back", "two", "let", "one", "seven",
         "mind", "hand", "pull", "stuff", "station", "store", "appear", "base", "cold", "blood", "give", "whatever",
         "tree", "board", "word", "trip", "purpose", "discuss", "carry", "science", "open", "sell", "between", "these",
         "art", "hope", "model", "teach", "police", "part", "without", "relationship", "charge", "represent",
         "particularly", "support", "discover", "simple", "head", "about", "nation", "now", "manager", "fast", "take",
         "finger", "pick", "save", "very", "seek", "nor", "age", "decide", "seem", "hot", "citizen", "disease",
         "respond", "story", "this", "onto", "name"]

word10 = ["worker", "production", "deep", "democratic", "third", "yard", "view", "they", "never", "receive", "whom",
          "election", "hospital", "although", "write", "involve", "budget", "red", "forget", "community", "explain",
          "figure", "network", "describe", "fire", "while", "trade", "dark", "lawyer", "order", "sound", "customer",
          "face", "general", "price", "instead", "hour", "management", "kitchen", "heart", "wall", "ball",
          "opportunity", "financial", "soldier", "keep", "partner", "institution", "office", "cost", "everyone",
          "himself", "heavy", "wind", "but", "tax", "movie", "person", "right", "sea", "understand", "time", "sister",
          "skill", "paper", "protect", "social", "commercial", "risk", "weight", "join", "enter", "certainly",
          "despite", "player", "task", "growth", "all"]

word11 = ["apply", "compare", "die", "wonder", "evening", "chance", "affect", "speech", "senior", "ask", "effect",
          "mission" "mouth", "address", "sit", "yet", "notice", "ever", "such", "mention", "will", "exist", "court",
          "walk", "act", "bag", "rate", "dream", "way", "yes", "perform", "color", "crime", "another", "actually",
          "every", "chair", "quality", "author", "send", "everything", "hang", "get", "candidate", "can", "performance",
          "amount", "bank", "student", "thank", "grow", "since", "use", "product", "into", "president", "large",
          "perhaps", "effort", "else", "month", "though", "fine", "federal", "race", "half", "away"]

word12 = ["different", "government", "finally", "human", "college", "option", "factor", "present", "similar", "decade",
          "sign", "should", "brother", "whole", "ground", "him", "far", "for", "Republican", "policy", "cause",
          "inside", "patient", "girl", "majority", "project", "skin", "able", "help", "sport", "course", "interesting",
          "guess", "book", "nature", "benefit", "whether", "scientist", "stop", "poor", "pattern", "believe",
          "indicate", "bed", "behavior", "edge", "manage", "owner", "leave", "off", "remember", "list", "future",
          "come", "condition", "always", "drug", "result", "money", "late", "environment", "resource", "blue", "find",
          "even", "continue", "occur", "religious", "knowledge"]
free = word9 + word12 + word11 + word10 + word8 + word7 + word5 + word6 + word4 + word2 + word1 + word3
phrase_length = 12
secret_phrase = ' '.join(random.sample(free, phrase_length))
print(secret_phrase)
