# [U2-Net: Going Deeper with Nested U-Structure for Salient Object Detection](https://arxiv.org/abs/2005.09007)

## Metadata

- Authors: **[Xuebin Qin](https://arxiv.org/search/cs?searchtype=author&query=Qin%2C+X)**, **[Zichen Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang%2C+Z)**, **[Chenyang Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang%2C+C)**, **[Masood Dehghan](https://arxiv.org/search/cs?searchtype=author&query=Dehghan%2C+M)**, **[Osmar R. Zaiane](https://arxiv.org/search/cs?searchtype=author&query=Zaiane%2C+O+R)**, **[Martin Jagersand](https://arxiv.org/search/cs?searchtype=author&query=Jagersand%2C+M)**
- Year: 2020
- Category: Computer Vision and Pattern Recognition
- Topics: Salient Object Detection, Deep Learning, U-Net Architecture
- Keywords: U2-Net, Nested U-Structure, Residual U-block (RSU), Salient Object Detection, Multi-scale Features

## Summary

- **目的**: 提案されたU2-Netは、既存のバックボーンに依存せずに、視覚的に顕著な物体を高精度で検出するための深層学習ベースのネットワークを設計することを目的とする。このネットワークは、深い構造と高解像度の特徴マップを維持しながら、計算コストとメモリの要件を抑制する。
- **手法**: 提案手法は二重のU字構造（Nested U-Structure）を採用し、Residual U-block (RSU)を用いて多段階での特徴統合を行う。RSUは、ローカルおよびグローバルな文脈情報を効果的に抽出し、ネットワーク全体の計算負荷を抑える。
- **成果**: 提案されたU2-Netおよびその小型モデルU2-Net†は、6つのSODデータセットで競争力のある性能を達成し、計算効率の高いリアルタイム処理を実現している。

## **Algorithm**

### 数式

- **損失関数**  
  トレーニングでは深いスーパービジョン戦略を用い、サイド出力と融合出力の損失を最小化する。  
  損失関数全体は以下のように定義される:
  $$
  L = \sum_{m=1}^M w_{\text{side}}^{(m)} \ell_{\text{side}}^{(m)} + w_{\text{fuse}} \ell_{\text{fuse}}
  $$
  各項についてはバイナリクロスエントロピー損失lが使用される:
  $$
  \ell = -\sum_{r,c}\left[ P_G(r,c)\log P_S(r,c) + (1 - P_G(r,c))\log(1 - P_S(r,c)) \right]
  $$
  ここで、P_G(r,c)はグラウンドトゥルースのピクセル値、P_S(r,c)は予測確率値。

### アルゴリズム

1. **Residual U-Block (RSU)**:
   - RSUは、入力特徴マップをローカルおよびグローバルな特徴に分解し、再統合するモジュール。
   - 深さ \(L\) のU字型エンコーダーデコーダー構造を採用。
   - 残差接続により、マルチスケール特徴とローカル特徴を効果的に結合。

2. **U2-Net構造**:
   - トップレベルはU字構造で、各ステージにRSUブロックを配置。
   - 6ステージのエンコーダーと5ステージのデコーダーで構成される。
   - サイド出力の融合により、最終的な顕著性マップを生成。

## **Implementation**

- **実装**:
  - リポジトリ: [U2-Net GitHub](https://github.com/NathanUA/U-2-Net)
  - フレームワーク: PyTorch
  - データセット:
    - 訓練: DUTS-TR (21,106画像、水平反転データ拡張)
    - 評価: DUT-OMRON, DUTS-TE, HKU-IS, ECSSD, PASCAL-S, SOD
  - ハードウェア: GTX 1080Ti GPU
  - 学習条件:
    - 最適化手法: Adam Optimizer
    - 初期学習率: 0.001
    - バッチサイズ: 12
    - 訓練時間: 約120時間

- **検証結果**:
  - 定量的性能評価:
    - モデルサイズ: U2-Net (176.3 MB), U2-Net† (4.7 MB)
    - FPS: 30 (U2-Net), 40 (U2-Net†)
    - 各データセットでの最大Fβスコア、MAE、構造的評価(S-measure)などでSOTA達成。

## **Applications**

- **応用**:
  - 画像セグメンテーション
  - 自動運転における物体検出
  - 画像編集ツールでの前景抽出
- **課題**:
  - モバイル環境でのさらなる速度向上
  - 多様性のあるより大規模なデータセットの必要性

## **Results**

- **定量的評価**:
  $$
  \begin{align*}
  \text{DUT-OMRON: } & \text{maxF}_\beta = 0.823, \text{MAE} = 0.054 \\
  \text{HKU-IS: } & \text{maxF}_\beta = 0.935, \text{MAE} = 0.031
  \end{align*}
  $$
- **定性的評価**:
  - 小型物体、大型物体、境界に接する物体の正確な分割を実現。

## **Notes**

- **気づき**:
  - RSUブロックの効率性がモデル性能を向上。
  - ネスト構造の採用により、計算効率が改善。
- **次のステップ**:
  - モバイル向け最適化
  - 新しい損失関数やモジュールの導入

## Next Paper

- [BASNet: Boundary-Aware Salient Object Detection](https://arxiv.org/abs/1903.09588)
  - 境界認識の導入による顕著性検出の改善を詳細に議論。
- [CPD: Cascaded Partial Decoder for Fast and Accurate Salient Object Detection](https://arxiv.org/abs/1904.03895)
  - 高速かつ正確な顕著性検出に関する革新を示す。
- [PoolNet: Exploring the Potential of Pooling for Salient Object Detection](https://arxiv.org/abs/1904.09146)
  - グローバル特徴統合の手法としてのプーリングの利用を探究。