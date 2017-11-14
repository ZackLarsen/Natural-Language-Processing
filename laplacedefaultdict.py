#########Construct unigram model with LaPlace smoothing##########
def unigram(tokens):
    model = collections.defaultdict(lambda: 0.01)
    for f in tokens:
        try:
            model[f] += 1
        except KeyError:
            model[f] = 1
            continue
    for word in model:
        model[word] = model[word]/float(len(model))
    return model
#unigrams = unigram(token_list)
#print unigrams.values()

