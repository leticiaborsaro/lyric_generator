# Creating dictionaries with specific words to be used later.
# Still needs to be further improved, cleaned and categorized.

# Enhanced word bank with better categorization while keeping all original words

adv = {
    "temporal": ["forever", "tonight", "right now", "tomorrow", "today", "one day"],
    "intensity": ["slowly", "passionately", "intimately", "completely", "fiercely", "terribly", "hopelessly", "madly"],
    "manner": ["gently", "softly", "quietly", "boldly", "freely"],
    "frequency": ["always", "never", "constantly", "rarely", "often"]
}

adj = {
    "positive_emotion": ["beautiful", "blissful", "perfect", "wonderful", "sweet", "radiant", "joyful", "peaceful"],
    "emotional_depth": ["true", "unbreakable", "pure", "honest", "familiar", "boundless", "profound", "eternal"],
    "melancholy": ["fading", "empty", "silent", "tragic", "broken", "weary", "lonely", "lost"],
    "physical_descriptors": ["warm", "cold", "soft", "hard", "bright", "dark", "heavy", "light"],
    "abstract_qualities": ["mysterious", "ancient", "timeless", "fleeting", "distant"]
}

verbs = {
    # felt, tried, dreamed, longed don't work naturally with "I _ you", fought needs to be 'fought for'
    "past_emotion": ["felt", "cherished", "loved", "longed", "knew", "tried", "fought", "remembered", "dreamed"],
    # dream doesn't work without 'of _'
    "present_emotion": ["feel", "cherish", "love", "long", "know", "try", "fight", "remember", "dream", "bleed"],
    # change and transform doesn't fit here, stay sounds weird, growing doesn't always work
    "future_state": ["fade", "remain", "never change", "change", "stay", "fight", "try", "endure", "transform"],
    # below, needs to be: I am _ , I was _ , We are _ , This is _ , My heart is _
    "continuous_action": ["bleeding", "aching", "hoping", "yearning", "waiting", "searching", "becoming", "growing"],
    #
    "present_action": ["adore", "belong with", "follow", "keep", "know", "need", "promise", "hold", "wait", "trust", "believe"],
    "physical_actions": ["touch", "embrace", "hold", "caress", "kiss", "whisper", "breathe"],
    "metaphorical_actions": ["shatter", "mend", "illuminate", "shadow", "echo", "haunt"]
}


nouns = {
    "beloved_references": ["darling", "dearest", "heart", "dream", "everything", "lover", "soul", "angel", "treasure"],
    "internal_states": ["scars", "shadow", "secrets", "desire", "ache", "bones", "wound", "light", "memory", "hope"],
    "natural_elements": ["moon", "stars", "sun", "ocean", "river", "storm", "fire", "rain"],
    "time_references": ["moment", "lifetime", "dawn", "dusk", "midnight", "season", "eternity"],
    "abstract_concepts": ["destiny", "fate", "truth", "beauty", "pain", "joy", "freedom"]
}