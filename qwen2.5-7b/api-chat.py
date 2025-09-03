import requests
import json
from llm import Qwen2_5_LLM_WithMemory

if __name__ == '__main__':
    # this is only for test. Please use the real user query in your application
    c = [[92.65,95.6,89.7],[93.6,96.0,91.2],[97.7,98.6,96.8],[90.7,87.2,94.2],[89.9,84.5,95.3]]
    a = "太极拳"
    b = ["虚领顶劲：头颈似向上提升，并保持正直，要松而不僵可转动，头颈部与身躯、四肢要上下一致，自始至终顶劲不可丢。劲正直了，身体的重心就能保持稳定。",
        "含胸拔背、沉肩垂肘：指胸、背、肩、肘的姿势，胸要含、要虚、要松，不能挺，肩不能耸而要沉，肘不能抬而要下垂，全身要自然放松。"
    ]
    initial_memory = [
        {"user": "系统", "model":
            "接下来，你将扮演一名动作评价专家，目标是尽可能详细易懂的回答我的提问，根据我的动作评价结果，向我提出改善建议。"
            "关键指示：请你在回答的时候，紧密围绕我的问题回答，不要回答太多和问题相关性较弱的内容"},
        {"user": "系统", "model": f"我选择了{a}动作,该动作的要领时{b}"},
        {"user": "系统", "model": f"本次评估中，我的{a}得分分为标准度和幅度两方面，分数范围[0,100]。标准度代表：与标准视频相比，在相同时间段内，用户动作和标准视频里动作类型的相似程度；幅度代表：与标准视频相比，用户动作的变化幅度与标准视频的变化幅度相似程度。用户的得分将按顺序，分为左臂、右臂、中部、左腿、右腿给出，其中每个得分将由一个数组给出，数组内的三项分别代表该部分用户的总分、标准度得分和变化幅度得分。"},
        {"user": "系统", "model": f"我的得分数组为{c}"}
    ]
    llm = Qwen2_5_LLM_WithMemory(mode_name_or_path="your-path",initial_memory=initial_memory)
    while True:
        prompt = input("请输入：")
        if prompt == "exit":
            break
        print(llm(prompt))