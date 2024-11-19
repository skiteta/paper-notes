# [Tell Me More! Towards Implicit User Intention Understanding of Language Model Driven Agents](https://arxiv.org/abs/2402.09205)

## Metadata

- Authors: [[Cheng Qian](https://arxiv.org/search/cs?searchtype=author&query=Qian,+C), [Bingxiang He](https://arxiv.org/search/cs?searchtype=author&query=He,+B), [Zhong Zhuang](https://arxiv.org/search/cs?searchtype=author&query=Zhuang,+Z), [Jia Deng](https://arxiv.org/search/cs?searchtype=author&query=Deng,+J), [Yujia Qin](https://arxiv.org/search/cs?searchtype=author&query=Qin,+Y), [Xin Cong](https://arxiv.org/search/cs?searchtype=author&query=Cong,+X), [Zhong Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Z), [Jie Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+J), [Yankai Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+Y), [Zhiyuan Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Z), [Maosong Sun](https://arxiv.org/search/cs?searchtype=author&query=Sun,+M)]
- Year: 2024
- Category: Computation and Language
- Topics: [LLM, agent]
- Keyword: [IN3]

## Summary

- 目的: 
  - 従来のエージェントモデルでは、ユーザーから曖昧なタスク指示に対して対応できず結果に乖離が生じているケースがある。そのため今回、IN3（Intention In Interaction）という曖昧な質問に対する対応を評価するデータセットを構築し、またエージェントの上流部分にIN3でチューニングしたモデルを統合し、評価を行うことでタスクへの対応能力向上に寄与するかを検証しようとしている。

- 手法: 
  - 一般的なエージェントタスクから数百のカテゴリーを選定し、それぞれに曖昧さ、詳細の欠落、詳細の重要度を設定したIN3というデータセットを構築する。
  - Mistral7BをIN3で学習したモデルをMistral-Interactとし、XAgentフレームワークの上流部分に統合する。
  - Mistral -InteractがGPT-4やLLaMaなどのモデルより対話能力が優れているかを、モデルの命令理解と命令実行の側面から評価し確認する。

- 成果: 
  - モデルのロバストな意図理解を促すというタスクに焦点を当て、現在のエージェント設計においてユーザーとの対話の質を考慮するよう設定したIN3データセットをベンチマークとして公開した。
  - 意図理解に特化したモデルをエージェントの上流部分に適用することで、小規模なモデルでもGPT-4やLLaMAなどのモデルより、対話能力の向上に寄与することが確認できた。
  - 意図理解などの対話能力に関する評価指標を二つ（命令理解、命令実行）設けた。
  - XAgentフレームワークのの包括的な実験とケーススタディを通して今手法の実行可能性を示した。


## **Algorithm**

- 数式:

  - 

- アルゴリズム:

  1. 

## **Implementation**

- 実装:
  - 
- 検証結果:
  - 

## **Applications**

- 応用:
  - 
- 課題:
  - 

## **Resuls**

- 

## **Notes**

- 気づき:
- 次のステップ: 