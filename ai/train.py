"""
Gossip Model Training Script
用于微调开源模型以适应八卦场景
"""

import os
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from app.config import AI_MODEL_NAME, AI_MODEL_PATH

class GossipDataset(Dataset):
    def __init__(self, data_path: str, tokenizer, max_length: int = 512):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.data = self._load_data(data_path)

    def _load_data(self, data_path: str):
        import json
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        text = f"八卦内容：{item['content']}\n总结：{item['summary']}"
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        encoding["labels"] = encoding["input_ids"].clone()
        return {k: v.squeeze() for k, v in encoding.items()}

def train_model(
    data_path: str = "./data/gossip_train.json",
    output_dir: str = AI_MODEL_PATH,
    num_epochs: int = 3,
    batch_size: int = 4,
    learning_rate: float = 2e-5
):
    tokenizer = AutoTokenizer.from_pretrained(AI_MODEL_NAME, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        AI_MODEL_NAME,
        trust_remote_code=True,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )

    dataset = GossipDataset(data_path, tokenizer)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=num_epochs,
        per_device_train_batch_size=batch_size,
        learning_rate=learning_rate,
        save_steps=500,
        save_total_limit=2,
        logging_steps=100,
        fp16=torch.cuda.is_available(),
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    )

    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"Model saved to {output_dir}")

if __name__ == "__main__":
    train_model()
