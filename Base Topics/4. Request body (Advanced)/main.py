from pydantic import BaseModel
from typing import List, Tuple


class GitRepository(BaseModel):
    name: str
    tags: List[str] = []
    versions: Tuple[str] = ('1.1', '1.21', '1.3.8')


print(GitRepository(name='Test Repo', tags=['Python', 'FastAPI']))