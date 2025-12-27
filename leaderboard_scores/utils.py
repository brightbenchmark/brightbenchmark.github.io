reasoning_template = '''                    <tr>
                   <td>
                      <p>{rank}</p>
                      <span class="date label label-default">July 11, 2024</span>
                   </td>
                          <td style="word-break:break-word;">
                            {retrieval_model}, with {reasoning_model} reasoning
                            <p style="font-size: 15;"> <i> {institution} </i> </p>
                          </td>
                   <td><b>{score}</b></td>
                </tr>'''
reranking_template = '''                    <tr>
                       <td>
                          <p>{rank}</p>
                          <span class="date label label-default">July 11, 2024</span>
                       </td>
                              <td style="word-break:break-word;">
                                {retrieval_model}, {topk} reranking by {reranking_model}
                                <p style="font-size: 15;"> <i> {institution} </i> </p>
                              </td>
                       <td><b>{score}</b></td>
                    </tr>'''
raw_template = '''                    <tr>
                       <td>
                          <p>{rank}</p>
                          <span class="date label label-default">July 11, 2024</span>
                       </td>
                              <td style="word-break:break-word;">
                                {retrieval_model}
                                <p style="font-size: 15;"> <i> {institution} </i> </p>
                              </td>
                       <td><b>{score}</b></td>
                    </tr>'''

retrieval_model_map = {
    'Google-Gecko-Text_Embedding-004': {
        'model': '<a class="link" href="https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings">Google-Gecko-Text_Embedding-004</a>',
        'institution': 'Google cloud AI'
    },
    'bm25': {
        'model': '<a class="link" href="https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf">BM25</a>',
        'institution': 'Microsoft'
    },
    'qwen': {
        'model': '<a class="link" href="https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct">gte-Qwen1.5-7B-instruct</a>',
        'institution': 'Alibaba'
    },
    'e5': {
        'model': '<a class="link" href="https://huggingface.co/intfloat/e5-mistral-7b-instruct">e5-mistral-7b-instruct</a>',
        'institution': 'Microsoft'
    },
    'sfr': {
        'model': '<a class="link" href="https://huggingface.co/Salesforce/SFR-Embedding-Mistral">SFR-Embedding-Mistral</a>',
        'institution': 'Salesforce'
    },
    'inst-xl': {
        'model': '<a class="link" href="https://huggingface.co/hkunlp/instructor-xl">instructor-xl</a>',
        'institution': 'The University of Hong Kong, University of Washington'
    },
    'google': {
        'model': '<a class="link" href="https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings#latest_Retrievers">google-gecko.text-embedding-preview-0409, dim=768</a>',
        'institution': 'Google'
    },
    'bge': {
        'model': '<a class="link" href="https://huggingface.co/BAAI/bge-large-en-v1.5">bge-large-en-v1.5</a>',
        'institution': 'Beijing Academy of Artificial Intelligence'
    },
    'grit': {
        'model': '<a class="link" href="https://huggingface.co/GritLM/GritLM-7B">GritLM-7B</a>',
        'institution': 'ContextualAI, The University of Hong Kong, Microsoft'
    },
    'cohere': {
        'model': '<a class="link" href="https://huggingface.co/Cohere/Cohere-embed-english-v3.0">Cohere-embed-english-v3.0</a>',
        'institution': 'Cohere'
    },
    'inst-l': {
        'model': '<a class="link" href="https://huggingface.co/hkunlp/instructor-large">instructor-large</a>',
        'institution': 'The University of Hong Kong, University of Washington'
    },
    'openai': {
        'model': '<a class="link" href="https://openai.com/blog/new-embedding-Retrievers-and-api-updates">text-embedding-3-large</a>',
        'institution': 'OpenAI'
    },
    'voyage': {
        'model': '<a class="link" href="https://docs.voyageai.com/embeddings/">voyage-large-2-instruct</a>',
        'institution': 'Voyage AI'
    },
    'sbert': {
        'model': '<a class="link" href="https://huggingface.co/sentence-transformers/all-mpnet-base-v2">sentence-transformers</a>',
        'institution': 'Technische Universität Darmstadt',
    },
    'INF-X-Retriever': {
        'model': '<a class="link" href="https://yaoyichen.github.io/INF-X-Retriever">INF-X-Retriever</a>',
        'institution': 'INF',
    }
}
reasoning_model_map = {
    'gpt4': '<a class="link" href="https://openai.com/index/gpt-4/">gpt-4-0125-preview</a>',
    'llama3': '<a class="link" href="https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct">Llama-3-70B-Instruct</a>',
    'gemini': '<a class="link" href="https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemini-pro?pli=1">Gemini-1.0-pro</a>',
    'grit': '<a class="link" href="https://huggingface.co/GritLM/GritLM-7B">GritLM-7B</a>',
    'claude': '<a class="link" href="https://www.anthropic.com/news/claude-3-family">Claude-3-Opus</a>'
}
reranking_model_map = {
    'claude': '<a class="link" href="https://www.anthropic.com/news/claude-3-family">Claude-3-Opus</a>',
    'gpt4': '<a class="link" href="https://openai.com/index/gpt-4/">gpt-4-0125-preview</a>',
    'gemini': '<a class="link" href="https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemini-pro?pli=1">Gemini-1.0-pro</a>',
    'minilm': '<a class="link" href="https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-12-v2">MiniLM</a>'
}

