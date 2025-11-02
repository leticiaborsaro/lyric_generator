import word_bank
import random

adj = word_bank.adj
adv = word_bank.adv
nouns = word_bank.nouns
verbs = word_bank.verbs

def generate_line():
     # for n in range(len(word_bank.verbs)):
     #   print(f"I {random.choice(word_bank.verbs['past_emotion'])} you")

    print(f"We were {random.choice(adj[random.choice(list(adj.keys()))])} {random.choice(nouns[random.choice(list(nouns.keys()))])} made to {random.choice(adv[random.choice(list(adv.keys()))])} {random.choice(verbs[random.choice(list(verbs.keys()))])}")
    #ex: we were beautiful stars made to constantly bleed

if __name__ == "__main__":
    generate_line()


    # I (verb) you
    # I felt (verb)
    # You (verb)
    # We were (nouns or verbs)