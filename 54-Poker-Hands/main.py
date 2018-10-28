def str2hands(s):
    s = s.strip().split()
    new = []
    for i in [0,1]:
        hand = []
        for card in s[i*5:(i+1)*5]:
            val = card[0]
            if val in "JQKA":
                val = 11 + "JQKA".index(val)
            else:
                val = int(val)
            card = (val,card[1])
            hand.append(card)
        new.append(hand)
    return new[0],new[1]

def handscore(hand):
    ranks = [x[0] for x in hand]
    suits = [x[1] for x in hand]
    if any([all([x == suit for x in suits]) for suit in "HCSD"]):
        return 9
