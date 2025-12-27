scores = {
    'raw': {
        'bm25': 11.4,
        'bge': 14.8,
        'inst-l': 18.2,
        'sbert': 17.4,
        'e5': 25.5,
        'sfr': 26.0,
        'inst-xl': 17.8,
        'grit': 26.0,
        'qwen': 27.8,
        'cohere': 18.4,
        'openai': 21.9,
        'voyage': 24.6,
        'google': 22.4,
        'Google-Gecko-Text_Embedding-004': 33.2,
        'INF-X-Retriever': 54.6
    }
}

from utils import raw_template,retrieval_model_map
strs = []
for k,v in scores.items():
    if k=='raw':
        for model,score in v.items():
            strs.append([raw_template,{
                'retrieval_model': retrieval_model_map[model]['model'],
                'institution':  retrieval_model_map[model]['institution'],
                'score': score
            }])
    else:
        raise ValueError('unsupported')
strs = sorted(strs,key=lambda x:x[1]['score'],reverse=True)
print(len(strs))
with open('html_long.txt','w') as f:
    for idx,s in enumerate(strs):
        s[1]['rank'] = idx+1
        f.write(s[0].format(**s[1])+'\n\n')