from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#  CORS origins
origins = [
    "http://localhost:3000",  
]

#  CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: dict):
    num_nodes = len(pipeline.get('nodes', []))
    num_edges = len(pipeline.get('edges', []))
    is_dag = check_if_dag(pipeline)  
    return {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': is_dag}

def check_if_dag(pipeline):
   
    return True
