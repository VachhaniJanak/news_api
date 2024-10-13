import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_path = 'summarize/model_ckpt'
checkpoint = 't5-small'


class MODEL:
	def __init__(self, max_length=1024, min_length=64, length_penalty=4, num_beams=16, no_repeat_ngram_size=4,
	             early_stopping=True):
		self.tokenizer = T5Tokenizer.from_pretrained(checkpoint, legacy=False)
		self.model = T5ForConditionalGeneration.from_pretrained(model_path, )
		self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

		self.max_length = max_length
		self.min_length = min_length
		self.length_penalty = length_penalty
		self.num_beams = num_beams
		self.no_repeat_ngram_size = no_repeat_ngram_size
		self.early_stopping = early_stopping

	def get_summary(self, inputs: str) -> str:
		inputs = self.tokenize_it(input_text=inputs)

		ids = self.model.generate(
			inputs, max_length=self.max_length, min_length=self.min_length,
			length_penalty=self.length_penalty, num_beams=self.num_beams,
			no_repeat_ngram_size=self.no_repeat_ngram_size,
			early_stopping=self.early_stopping)

		return self.decode_token(ids=ids[0])

	def tokenize_it(self, input_text: str):
		return self.tokenizer.encode(input_text, return_tensors="pt", max_length=2048, truncation=True).to(self.device)

	def decode_token(self, ids) -> str:
		return self.tokenizer.decode(ids, skip_special_tokens=True)
