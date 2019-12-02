from collections import defaultdict
def tree(): return defaultdict(tree)
dic = tree()
dic['a']['b']
dic['a']['b']['c']
dic['a']['b']['d']
dic['a']['e']
def dicts(t): return {k: dicts(t[k]) for k in t}
print(dicts(dic))