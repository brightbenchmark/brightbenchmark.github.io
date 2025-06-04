scores = {
    'raw': {
        'bm25': 14.5,
        'bge': 13.7,
        'inst-l': 14.2,
        'sbert': 14.9,
        'e5': 17.9,
        'sfr': 18.3,
        'inst-xl': 18.9,
        'grit': 21.0,
        'qwen': 22.5,
        'cohere': 16.6,
        'openai': 17.9,
        'voyage': 17.9,
        'google': 20.0
    },
    'gpt4-reason': {
        'bm25': 27.0,
        'bge': 22.0,
        'inst-l': 23.5,
        'sbert': 17.7,
        'e5': 22.1,
        'sfr': 22.0,
        'inst-xl': 26.9,
        'grit': 24.5,
        'qwen': 24.8,
        'cohere': 22.6,
        'openai': 23.3,
        'voyage': 24.7,
        'google': 26.2,
    },
    'llama3-reason': {
        'bm25': 25.7,
        'bge': 20.7,
        'inst-l': 22.7,
        'sbert': 16.3,
        'e5': 19.9,
        'sfr': 20.0,
        'inst-xl': 26.3,
        'grit': 20.9,
        'qwen': 23.4,
        'cohere': 22.2,
        'openai': 22.1,
        'voyage': 22.9,
        'google': 24.9,
    },
    'claude-reason': {
        'bm25': 26.8,
        'bge': 21.1,
        'inst-l': 22.1,
        'sbert': 16.4,
        'e5': 21.4,
        'sfr': 21.7,
        'inst-xl': 26.4,
        'grit': 23.4,
        'qwen': 24.8,
        'cohere': 21.9,
        'openai': 22.7,
        'voyage': 23.1,
        'google': 25.6,
    },
    'grit-reason': {
        'bm25': 19.4,
        'bge': 16.0,
        'inst-l': 15.8,
        'sbert': 13.9,
        'e5': 17.6,
        'sfr': 17.4,
        'inst-xl': 22.4,
        'grit': 18.3,
        'qwen': 19.9,
        'cohere': 16.4,
        'openai': 18.0,
        'voyage': 18.7,
        'google': 19.6,
    },
    'gemini-reason': {
        'bm25': 23.9,
        'bge': 18.7,
        'inst-l': 20.8,
        'sbert': 15.5,
        'e5': 19.6,
        'sfr': 20.1,
        'inst-xl': 24.5,
        'grit': 20.7,
        'qwen': 22.6,
        'cohere': 19.8,
        'openai': 21.5,
        'voyage': 22.4,
        'google': 23.0,
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
strs += [[
    '''                    <tr>
                   <td>
                      <p>{rank}</p>
                      <span class="date label label-default">Apr 30, 2025</span>
                   </td>
                          <td style="word-break:break-word;">
                            <a class="link" href="https://arxiv.org/pdf/2504.03947">Qwen1.5-7B with InteRank-3B re-ranking</a>
                            <p style="font-size: 15;"> <i> University of Massachusetts Amherst </i> </p>
                          </td>
                   <td><b>27.4</b></td>
                </tr>''',
    {
        'score': 27.4
    }
],
    [
    '''                    <tr>
                   <td>
                      <p>{rank}</p>
                      <span class="date label label-default">Apr 29, 2025</span>
                   </td>
                          <td style="word-break:break-word;">
                            <a class="link" href="https://arxiv.org/pdf/2504.20595">ReasonIR with reranker</a>
                            <p style="font-size: 15;"> <i> Meta, University of Washington, etc. </i> </p>
                          </td>
                   <td><b>36.9</b></td>
                </tr>''',
    {
        'score': 36.9
    }
],
    [
    '''                    <tr>
                   <td>
                      <p>{rank}</p>
                      <span class="date label label-default">May 14, 2025</span>
                   </td>
                          <td style="word-break:break-word;">
                            <a class="link" href="https://x.com/zach_nussbaum/status/1922427785710121186">BM25 with GPT4 reasoning and Qwen QWQ reranking</a>
                            <p style="font-size: 15;"> <i> Zach Nussbaum (NomicAI) </i> </p>
                          </td>
                   <td><b>37.8</b></td>
                </tr>''',
    {
        'score': 37.8
    }
],
    [
    '''                    <tr>
                   <td>
                      <p>{rank}</p>
                      <span class="date label label-default">Oct 22, 2024</span>
                   </td>
                          <td style="word-break:break-word;">
                            <a class="link" href="https://openreview.net/pdf?id=tZiMLgsHMu">JudgeRank</a>
                            <p style="font-size: 15;"> <i> ICLR submission </i> </p>
                          </td>
                   <td><b>35.8</b></td>
                </tr>''',
    {
        'score': 35.8
    }
],

[
    '''                    <tr>
                   <td>
                      <p>{rank}</p>
                      <span class="date label label-default">Aug 28, 2024</span>
                   </td>
                          <td style="word-break:break-word;">
                            <a class="link" href="https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf">BM25</a>, with <a class="link" href="https://openai.com/index/gpt-4/">GPT-4</a> reasoning and top-100 reranking by <a class="link" href="https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4">Llama-3.1-70B</a>
                            <p style="font-size: 15;"> <i> Salesforce Research (proprietary code) </i> </p>
                          </td>
                   <td><b>30.4</b></td>
                </tr>''',
    {
        'score': 30.4
    }
],

    [
        '''                       <tr>
                       <td>
                          <p>{rank}</p>
                          <span class="date label label-default">May 10, 2025</span>
                       </td>
                              <td style="word-break:break-word;">
                                <a class="link" href="https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf">BM25</a> with <a class="link" href="https://github.com/bigai-nlco/TongSearch_Reasoner">TongSearch Reasoner 7B</a> Reasoning
                                <p style="font-size: 15;"> <i> Beijing Institute for General Artificial Intelligence (BIGAI) </i> </p>
                              </td>
                       <td><b>27.9</b></td>
                    </tr>''',
        {
            'score': 27.9
        }
    ],
[
        '''                       <tr>
                       <td>
                          <p>{rank}</p>
                          <span class="date label label-default">May 10, 2025</span>
                       </td>
                              <td style="word-break:break-word;">
                                <a class="link" href="https://huggingface.co/ByteDance-Seed/Seed1.5-Embedding">Seed1.5-Embedding</a>
                                <p style="font-size: 15;"> <i> ByteDance </i> </p>
                              </td>
                       <td><b>27.2</b></td>
                    </tr>''',
        {
            'score': 27.2
        }
    ],
    [
        '''                       <tr>
                       <td>
                          <p>{rank}</p>
                          <span class="date label label-default">May 10, 2025</span>
                       </td>
                              <td style="word-break:break-word;">
                                <a class="link" href="https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf">BM25</a> with <a class="link" href="https://github.com/bigai-nlco/TongSearch_Reasoner">TongSearch Reasoner 1.5B</a> Reasoning
                                <p style="font-size: 15;"> <i> Beijing Institute for General Artificial Intelligence (BIGAI) </i> </p>
                              </td>
                       <td><b>24.6</b></td>
                    </tr>''',
        {
            'score': 24.6
        }
    ],
    [
        '''                       <tr>
                       <td>
                          <p>{rank}</p>
                          <span class="date label label-default">May 29, 2025</span>
                       </td>
                              <td style="word-break:break-word;">
                                <a class="link" href="https://huggingface.co/ielabgroup/Rank-R1-32B-v0.2">ReasonIR with Rank-R1</a>
                                <p style="font-size: 15;"> <i> CSIRO, University of Waterloo, The University of Queensland </i> </p>
                              </td>
                       <td><b>38.8</b></td>
                    </tr>''',
        {
            'score': 38.8
        }
    ],
    [
        '''                       <tr>
                       <td>
                          <p>{rank}</p>
                          <span class="date label label-default">June 2, 2025</span>
                       </td>
                              <td style="word-break:break-word;">
                                <a class="link" href="https://github.com/jataware/ezbright/">XRR2</a>
                                <p style="font-size: 15;"> <i> Jataware Corp </i> </p>
                              </td>
                       <td><b>40.3</b></td>
                    </tr>''',
        {
            'score': 40.3
        }
    ],
    [
        '''                       <tr>
                       <td>
                          <p>{rank}</p>
                          <span class="date label label-default">June 4, 2025</span>
                       </td>
                              <td style="word-break:break-word;">
                                <a class="link" href="https://github.com/bigai-nlco/TongSearch_Reasoner">ReasonIR with TongSearch Reasoner 7B Reasoning and reranker</a>
                                <p style="font-size: 15;"> <i> Beijing Institute for General Artificial Intelligence (BIGAI) </i> </p>
                              </td>
                       <td><b>38.3</b></td>
                    </tr>''',
        {
            'score': 38.3
        }
    ]
]
strs = sorted(strs,key=lambda x:x[1]['score'],reverse=True)
print(len(strs))
with open('html.txt','w') as f:
    for idx,s in enumerate(strs):
        s[1]['rank'] = idx+1
        f.write(s[0].format(**s[1])+'\n\n')
