from fastapi import FastAPI
from pydantic import BaseModel

from app.context.context_builder import ContextBuilder
from app.llm.client import LLMClient
from prompts.codebase_prompt import build_prompt
from app.retrieval.retriever import CodeRetriever


app = FastAPI(
    title="RepoPilot",
    description="AI Codebase Understanding & Debugging Assistant",
    version="0.1.0",
)


class AskRequest(BaseModel):
    query: str
    top_k: int = 3


class Source(BaseModel):
    file_path: str
    symbol_name: str
    start_line: int
    end_line: int
    score: float


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]


retriever = CodeRetriever()
context_builder = ContextBuilder()
llm = LLMClient()


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "RepoPilot",
    }


@app.post("/ask", response_model=AskResponse)
def ask_codebase(request: AskRequest):

    if not request.query.strip():
        return AskResponse(
            answer="Please provide a question.",
            sources=[],
        )

    retrieved_chunks = retriever.search(
        query=request.query,
        top_k=request.top_k,
    )

    context = context_builder.build(
        retrieved_chunks
    )

    prompt = build_prompt(
        query=request.query,
        context=context,
    )

    answer = llm.generate(prompt)

    sources = [
        Source(
            file_path=chunk["file_path"],
            symbol_name=chunk["symbol_name"],
            start_line=chunk["start_line"],
            end_line=chunk["end_line"],
            score=chunk["score"],
        )
        for chunk in retrieved_chunks
    ]

    return AskResponse(
        answer=answer,
        sources=sources,
    )