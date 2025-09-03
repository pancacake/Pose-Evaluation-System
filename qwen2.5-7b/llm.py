cuda from langchain.llms.base import LLM
from typing import Any, List, Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, LlamaTokenizerFast
import torch


class Qwen2_5_LLM_WithMemory(LLM):
    tokenizer: AutoTokenizer = None
    model: AutoModelForCausalLM = None
    memory: List[dict] = None

    def __init__(self, mode_name_or_path: str, initial_memory: Optional[List[dict]] = None):
        super().__init__()
        print("正在从本地加载模型...")
        self.tokenizer = AutoTokenizer.from_pretrained(mode_name_or_path, use_fast=False)
        self.model = AutoModelForCausalLM.from_pretrained(mode_name_or_path, torch_dtype=torch.bfloat16,
                                                          device_map="auto")
        self.model.generation_config = GenerationConfig.from_pretrained(mode_name_or_path)
        # 初始化记忆
        self.memory = initial_memory if initial_memory is not None else []
        print("完成本地模型的加载")

    def _call(self, prompt: str, stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None,
              **kwargs: Any):
        # 将记忆中的内容与当前输入结合
        context = " ".join([f"User: {entry['user']} Model: {entry['model']}" for entry in self.memory])
        full_prompt = context + f" User: {prompt}"
        messages = [{"role": "user", "content": full_prompt}]
        input_ids = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        model_inputs = self.tokenizer([input_ids], return_tensors="pt").to('cuda')
        generated_ids = self.model.generate(model_inputs.input_ids, attention_mask=model_inputs['attention_mask'],
                                            max_new_tokens=512)
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        # 将当前对话加入记忆
        self.memory.append({"user": prompt, "model": response})

        return response

    @property
    def _llm_type(self) -> str:
        return "Qwen2_5_LLM_WithMemory"

