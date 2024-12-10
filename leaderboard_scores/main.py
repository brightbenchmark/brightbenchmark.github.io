scores = {
    'raw': {
        'bm25': 14.3,
        'bge': 13.6,
        'inst-l': 14.0,
        'sbert': 14.6,
        'e5': 17.5,
        'sfr': 18.0,
        'inst-xl': 18.6,
        'grit': 20.6,
        'qwen': 22.1,
        'cohere': 16.3,
        'openai': 17.6,
        'voyage': 17.6,
        'google': 19.5
    },
    'gpt4-reason': {
        'bm25': 26.5,
        'bge': 21.6,
        'inst-l': 22.9,
        'sbert': 17.5,
        'e5': 21.8,
        'sfr': 21.7,
        'inst-xl': 26.2,
        'grit': 24.0,
        'qwen': 24.5,
        'cohere': 22.3,
        'openai': 23.1,
        'voyage': 24.4,
        'google': 25.8,
    },
    'llama3-reason': {
        'bm25': 25.3,
        'bge': 20.3,
        'inst-l': 22.3,
        'sbert': 16.1,
        'e5': 19.6,
        'sfr': 19.7,
        'inst-xl': 25.8,
        'grit': 20.5,
        'qwen': 23.1,
        'cohere': 21.9,
        'openai': 22.0,
        'voyage': 22.8,
        'google': 24.5,
    },
    'claude-reason': {
        'bm25': 26.3,
        'bge': 20.7,
        'inst-l': 21.6,
        'sbert': 16.1,
        'e5': 21.1,
        'sfr': 21.5,
        'inst-xl': 25.8,
        'grit': 22.8,
        'qwen': 24.5,
        'cohere': 21.5,
        'openai': 22.6,
        'voyage': 22.8,
        'google': 25.0,
    },
    'grit-reason': {
        'bm25': 19.1,
        'bge': 15.7,
        'inst-l': 15.7,
        'sbert': 13.7,
        'e5': 17.5,
        'sfr': 17.2,
        'inst-xl': 22.1,
        'grit': 18.1,
        'qwen': 19.7,
        'cohere': 16.0,
        'openai': 17.8,
        'voyage': 18.5,
        'google': 19.3,
    },
    'gemini-reason': {
        'bm25': 23.5,
        'bge': 18.4,
        'inst-l': 20.4,
        'sbert': 15.3,
        'e5': 19.3,
        'sfr': 19.9,
        'inst-xl': 24.0,
        'grit': 20.5,
        'qwen': 22.3,
        'cohere': 19.5,
        'openai': 21.2,
        'voyage': 22.1,
        'google': 22.5,
    },
    'google-rerank': {
        'minilm': {
            'top-10': 16.0,
            'top-100': 9.2
        },
        'gemini': {
            'top-10': 20.1,
        },
        'gpt4': {
            'top-10': 21.5,
            'top-100': 22.6
        },
    },
    'bm25-rerank': {
        'minilm': {
            'top-10': 13.1,
            'top-100': 8.3
        },
        'gemini': {
            'top-10': 15.7,
        },
        'gpt4': {
            'top-10': 17.4,
            'top-100': 17.0
        },
    }
}

from utils import raw_template,retrieval_model_map,reasoning_model_map,reasoning_template,reranking_template,reranking_model_map
strs = []
for k,v in scores.items():
    if k=='raw':
        for model,score in v.items():
            strs.append([raw_template,{
                'retrieval_model': retrieval_model_map[model]['model'],
                'institution':  retrieval_model_map[model]['institution'],
                'score': score
            }])
    elif 'reason' in k:
        cur_reasoning_model = k.split('-')[0]
        for model,score in v.items():
            strs.append([reasoning_template, {
                'retrieval_model': retrieval_model_map[model]['model'],
                'institution': retrieval_model_map[model]['institution'],
                'reasoning_model': reasoning_model_map[cur_reasoning_model],
                'score': score
            }])
    elif 'rerank' in k:
        cur_retrieval_model = k.split('-')[0]
        for rerank_model,d in v.items():
            for topk,score in d.items():
                strs.append([reranking_template, {
                    'retrieval_model': retrieval_model_map[cur_retrieval_model]['model'],
                    'institution': retrieval_model_map[cur_retrieval_model]['institution'],
                    'topk': topk,
                    'reranking_model': reranking_model_map[rerank_model],
                    'score': score
                }])
    else:
        raise ValueError('unsupported')
strs = sorted(strs,key=lambda x:x[1]['score'],reverse=True)
print(len(strs))
with open('html.txt','w') as f:
    for idx,s in enumerate(strs):
        s[1]['rank'] = idx+3
        f.write(s[0].format(**s[1])+'\n\n')
