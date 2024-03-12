from tokenizers import Tokenizer, models, trainers
from tokenizers.pre_tokenizers import Whitespace

with open("data/training_clean.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

tokenizer_model = models.BPE()

tokenizer = Tokenizer(tokenizer_model)

tokenizer.pre_tokenizer = Whitespace()

trainer = trainers.BpeTrainer(special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"])
tokenizer.train_from_iterator(data, trainer=trainer)

tokenizer.save("vi_tokenizer.json")