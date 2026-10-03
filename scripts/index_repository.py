from app.indexing.repository_indexer import RepositoryIndexer


repository_path = "data"


indexer = RepositoryIndexer()

indexer.index_repository(repository_path)