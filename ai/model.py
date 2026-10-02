import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from app.config import AI_MODEL_NAME, AI_USE_LOCAL, AI_MODEL_PATH

class GossipModel:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.is_loaded = False

    def load_model(self):
        if self.is_loaded:
            return

        model_path = AI_MODEL_PATH if AI_USE_LOCAL else AI_MODEL_NAME

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto" if torch.cuda.is_available() else None
        )
        self.is_loaded = True

    def generate_summary(self, posts: list) -> str:
        if not self.is_loaded:
            self.load_model()

        prompt = self._build_summary_prompt(posts)
        inputs = self.tokenizer(prompt, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.7,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def predict_relationship(self, person_a: str, person_b: str, context: str) -> dict:
        if not self.is_loaded:
            self.load_model()

        prompt = f"""根据以下信息，推断{person_a}和{person_b}之间的关系：

上下文：{context}

请分析他们可能的关系类型（朋友、CP、同学、陌生人等），并给出置信度。

关系类型：
置信度："""

        inputs = self.tokenizer(prompt, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.5,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"analysis": response}

    def predict_gossip(self, gossip_content: str) -> dict:
        if not self.is_loaded:
            self.load_model()

        prompt = f"""请分析以下八卦内容，预测其真实性（0-100%）和可能的发展趋势：

八卦内容：{gossip_content}

真实性预测：
发展趋势："""

        inputs = self.tokenizer(prompt, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.5,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"analysis": response}

    def _build_summary_prompt(self, posts: list) -> str:
        post_texts = "\n".join([f"- {p.get('content', '')}" for p in posts[:20]])
        return f"""请根据以下八卦帖子，生成一份本周八卦总结。

要求：
1. 使用新闻稿风格，稍微掺杂一点有趣的语言
2. 严禁使用 emoji
3. 对每条八卦进行简要总结
4. 标注"AI生成"、"仅供娱乐"、"请注意甄别"

帖子内容：
{post_texts}

总结："""

gossip_model = GossipModel()
