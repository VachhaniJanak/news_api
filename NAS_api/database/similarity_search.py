import chromadb
from sentence_transformers import SentenceTransformer


def display_warn(message: str, l=10):
	print('\033[93m' + '[' + "@" * l, message, "@" * l + ']' + '\033[0m')


class VectorDB:
	def __init__(self, path) -> None:
		self.__model = SentenceTransformer('all-MiniLM-L6-v2')
		self.__client = chromadb.PersistentClient(path=str(path))
		self.__articles_collection = self.__client.get_or_create_collection(name="articles")

	def create(self, article_id: int, document: str, headline: str) -> bool | None:
		try:
			embedding = self.__model.encode(document).tolist()
			self.__articles_collection.add(
				documents=[headline],
				ids=[str(article_id)],
				embeddings=[embedding]
			)
		except Exception as e:
			display_warn(message=str(e) + 'Class -> VectorDB : func -> create')
			return False

	def get_by_id(self, article_id: int = 0, top_n: int = 0) -> tuple[int, ...] | bool:
		try:
			embedd = self.__articles_collection.get(ids=[str(article_id)], include=['embeddings'])['embeddings']
			ids = self.__articles_collection.query(
				query_embeddings=embedd,
				n_results=top_n,
			)['ids'][0]
			return tuple(int(id) for id in ids)
		except Exception as e:
			display_warn(message=str(e) + 'Class -> VectorDB : func -> get_by_id')
			return False

	def get_by_query(self, query: str, top_n: int = 0) -> tuple[int, ...] | bool:
		try:
			embedd = self.__model.encode(query).tolist()
			ids = self.__articles_collection.query(
				query_embeddings=embedd,
				n_results=top_n,
			)['ids'][0]
			return tuple(int(id) for id in ids)
		except Exception as e:
			display_warn(message=str(e) + 'Class -> VectorDB : func -> get_query')
			return False

	def delete_by_ids(self, articles_ids: tuple[int]) -> bool:
		try:
			self.__articles_collection.delete(ids=[str(article_id) for article_id in articles_ids])
			return True
		except Exception as e:
			display_warn(message=str(e) + 'Class -> VectorDB : func -> delete_by_ids')
			return False
