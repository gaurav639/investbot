---
tags:
- mteb
- transformers
- sentence-transformers
- modernbert
base_model: answerdotai/ModernBERT-base
model-index:
- name: cde-small-v2
  results:
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 86.01490000000001
    - type: f1
      value: 80.938
    - type: f1_weighted
      value: 86.9232
    - type: ap
      value: 54.949099999999994
    - type: ap_weighted
      value: 54.949099999999994
    - type: main_score
      value: 86.01490000000001
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 96.0223
    - type: f1
      value: 96.0206
    - type: f1_weighted
      value: 96.0206
    - type: ap
      value: 93.8301
    - type: ap_weighted
      value: 93.8301
    - type: main_score
      value: 96.0223
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 55.096000000000004
    - type: f1
      value: 54.4353
    - type: f1_weighted
      value: 54.4353
    - type: main_score
      value: 55.096000000000004
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: ndcg_at_1
      value: 54.125
    - type: ndcg_at_3
      value: 69.009
    - type: ndcg_at_5
      value: 72.722
    - type: ndcg_at_10
      value: 74.957
    - type: ndcg_at_20
      value: 75.801
    - type: ndcg_at_100
      value: 75.986
    - type: ndcg_at_1000
      value: 76.015
    - type: map_at_1
      value: 54.125
    - type: map_at_3
      value: 65.375
    - type: map_at_5
      value: 67.448
    - type: map_at_10
      value: 68.38499999999999
    - type: map_at_20
      value: 68.636
    - type: map_at_100
      value: 68.66600000000001
    - type: map_at_1000
      value: 68.66799999999999
    - type: recall_at_1
      value: 54.125
    - type: recall_at_3
      value: 79.51599999999999
    - type: recall_at_5
      value: 88.478
    - type: recall_at_10
      value: 95.306
    - type: recall_at_20
      value: 98.506
    - type: recall_at_100
      value: 99.431
    - type: recall_at_1000
      value: 99.644
    - type: precision_at_1
      value: 54.125
    - type: precision_at_3
      value: 26.505000000000003
    - type: precision_at_5
      value: 17.696
    - type: precision_at_10
      value: 9.531
    - type: precision_at_20
      value: 4.925
    - type: precision_at_100
      value: 0.9939999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 54.623
    - type: mrr_at_3
      value: 65.505
    - type: mrr_at_5
      value: 67.6174
    - type: mrr_at_10
      value: 68.5664
    - type: mrr_at_20
      value: 68.8173
    - type: mrr_at_100
      value: 68.8476
    - type: mrr_at_1000
      value: 68.8489
    - type: nauc_ndcg_at_1_max
      value: -14.4789
    - type: nauc_ndcg_at_1_std
      value: -25.5432
    - type: nauc_ndcg_at_1_diff1
      value: 23.7267
    - type: nauc_ndcg_at_3_max
      value: -8.1401
    - type: nauc_ndcg_at_3_std
      value: -22.9099
    - type: nauc_ndcg_at_3_diff1
      value: 21.069499999999998
    - type: nauc_ndcg_at_5_max
      value: -8.4301
    - type: nauc_ndcg_at_5_std
      value: -22.9185
    - type: nauc_ndcg_at_5_diff1
      value: 21.229100000000003
    - type: nauc_ndcg_at_10_max
      value: -8.6651
    - type: nauc_ndcg_at_10_std
      value: -23.5444
    - type: nauc_ndcg_at_10_diff1
      value: 21.9585
    - type: nauc_ndcg_at_20_max
      value: -9.285400000000001
    - type: nauc_ndcg_at_20_std
      value: -23.4297
    - type: nauc_ndcg_at_20_diff1
      value: 21.6731
    - type: nauc_ndcg_at_100_max
      value: -9.8693
    - type: nauc_ndcg_at_100_std
      value: -23.313
    - type: nauc_ndcg_at_100_diff1
      value: 21.5888
    - type: nauc_ndcg_at_1000_max
      value: -9.9675
    - type: nauc_ndcg_at_1000_std
      value: -23.3522
    - type: nauc_ndcg_at_1000_diff1
      value: 21.5714
    - type: nauc_map_at_1_max
      value: -14.4789
    - type: nauc_map_at_1_std
      value: -25.5432
    - type: nauc_map_at_1_diff1
      value: 23.7267
    - type: nauc_map_at_3_max
      value: -10.0484
    - type: nauc_map_at_3_std
      value: -23.3575
    - type: nauc_map_at_3_diff1
      value: 21.329
    - type: nauc_map_at_5_max
      value: -10.3514
    - type: nauc_map_at_5_std
      value: -23.3955
    - type: nauc_map_at_5_diff1
      value: 21.3531
    - type: nauc_map_at_10_max
      value: -10.484200000000001
    - type: nauc_map_at_10_std
      value: -23.6726
    - type: nauc_map_at_10_diff1
      value: 21.6458
    - type: nauc_map_at_20_max
      value: -10.638499999999999
    - type: nauc_map_at_20_std
      value: -23.6588
    - type: nauc_map_at_20_diff1
      value: 21.576600000000003
    - type: nauc_map_at_100_max
      value: -10.717400000000001
    - type: nauc_map_at_100_std
      value: -23.6559
    - type: nauc_map_at_100_diff1
      value: 21.5688
    - type: nauc_map_at_1000_max
      value: -10.7203
    - type: nauc_map_at_1000_std
      value: -23.6557
    - type: nauc_map_at_1000_diff1
      value: 21.5682
    - type: nauc_recall_at_1_max
      value: -14.4789
    - type: nauc_recall_at_1_std
      value: -25.5432
    - type: nauc_recall_at_1_diff1
      value: 23.7267
    - type: nauc_recall_at_3_max
      value: -0.2134
    - type: nauc_recall_at_3_std
      value: -21.251800000000003
    - type: nauc_recall_at_3_diff1
      value: 20.3069
    - type: nauc_recall_at_5_max
      value: 4.109100000000001
    - type: nauc_recall_at_5_std
      value: -20.1382
    - type: nauc_recall_at_5_diff1
      value: 21.1976
    - type: nauc_recall_at_10_max
      value: 18.3416
    - type: nauc_recall_at_10_std
      value: -22.9791
    - type: nauc_recall_at_10_diff1
      value: 29.4668
    - type: nauc_recall_at_20_max
      value: 45.3219
    - type: nauc_recall_at_20_std
      value: -14.8366
    - type: nauc_recall_at_20_diff1
      value: 31.829800000000002
    - type: nauc_recall_at_100_max
      value: 38.8075
    - type: nauc_recall_at_100_std
      value: 25.4176
    - type: nauc_recall_at_100_diff1
      value: 32.2733
    - type: nauc_recall_at_1000_max
      value: 28.1372
    - type: nauc_recall_at_1000_std
      value: 35.442
    - type: nauc_recall_at_1000_diff1
      value: 31.8247
    - type: nauc_precision_at_1_max
      value: -14.4789
    - type: nauc_precision_at_1_std
      value: -25.5432
    - type: nauc_precision_at_1_diff1
      value: 23.7267
    - type: nauc_precision_at_3_max
      value: -0.2134
    - type: nauc_precision_at_3_std
      value: -21.251800000000003
    - type: nauc_precision_at_3_diff1
      value: 20.3069
    - type: nauc_precision_at_5_max
      value: 4.109100000000001
    - type: nauc_precision_at_5_std
      value: -20.1382
    - type: nauc_precision_at_5_diff1
      value: 21.1976
    - type: nauc_precision_at_10_max
      value: 18.3416
    - type: nauc_precision_at_10_std
      value: -22.9791
    - type: nauc_precision_at_10_diff1
      value: 29.4668
    - type: nauc_precision_at_20_max
      value: 45.3219
    - type: nauc_precision_at_20_std
      value: -14.8366
    - type: nauc_precision_at_20_diff1
      value: 31.829800000000002
    - type: nauc_precision_at_100_max
      value: 38.8075
    - type: nauc_precision_at_100_std
      value: 25.4176
    - type: nauc_precision_at_100_diff1
      value: 32.2733
    - type: nauc_precision_at_1000_max
      value: 28.1372
    - type: nauc_precision_at_1000_std
      value: 35.442
    - type: nauc_precision_at_1000_diff1
      value: 31.8247
    - type: nauc_mrr_at_1_max
      value: -14.066600000000001
    - type: nauc_mrr_at_1_std
      value: -25.0145
    - type: nauc_mrr_at_1_diff1
      value: 22.361900000000002
    - type: nauc_mrr_at_3_max
      value: -10.6465
    - type: nauc_mrr_at_3_std
      value: -23.4323
    - type: nauc_mrr_at_3_diff1
      value: 19.758899999999997
    - type: nauc_mrr_at_5_max
      value: -10.7144
    - type: nauc_mrr_at_5_std
      value: -23.2823
    - type: nauc_mrr_at_5_diff1
      value: 19.8552
    - type: nauc_mrr_at_10_max
      value: -10.7815
    - type: nauc_mrr_at_10_std
      value: -23.51
    - type: nauc_mrr_at_10_diff1
      value: 20.157
    - type: nauc_mrr_at_20_max
      value: -10.9391
    - type: nauc_mrr_at_20_std
      value: -23.4946
    - type: nauc_mrr_at_20_diff1
      value: 20.072400000000002
    - type: nauc_mrr_at_100_max
      value: -11.018500000000001
    - type: nauc_mrr_at_100_std
      value: -23.491400000000002
    - type: nauc_mrr_at_100_diff1
      value: 20.0627
    - type: nauc_mrr_at_1000_max
      value: -11.0214
    - type: nauc_mrr_at_1000_std
      value: -23.491300000000003
    - type: nauc_mrr_at_1000_diff1
      value: 20.061999999999998
    - type: main_score
      value: 74.957
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 50.5269
    - type: v_measure_std
      value: 14.0094
    - type: main_score
      value: 50.5269
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 41.620200000000004
    - type: v_measure_std
      value: 14.4842
    - type: main_score
      value: 41.620200000000004
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions (default)
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: map
      value: 61.790299999999995
    - type: mrr
      value: 75.8156
    - type: nAUC_map_max
      value: 26.151200000000003
    - type: nAUC_map_std
      value: 15.8953
    - type: nAUC_map_diff1
      value: 5.0684
    - type: nAUC_mrr_max
      value: 36.9643
    - type: nAUC_mrr_std
      value: 19.0749
    - type: nAUC_mrr_diff1
      value: 15.549399999999999
    - type: main_score
      value: 61.790299999999995
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: pearson
      value: 88.41590000000001
    - type: spearman
      value: 86.7116
    - type: cosine_pearson
      value: 88.41590000000001
    - type: cosine_spearman
      value: 86.7116
    - type: manhattan_pearson
      value: 86.2045
    - type: manhattan_spearman
      value: 85.7248
    - type: euclidean_pearson
      value: 86.2336
    - type: euclidean_spearman
      value: 85.861
    - type: main_score
      value: 86.7116
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 88.3052
    - type: f1
      value: 88.2617
    - type: f1_weighted
      value: 88.2617
    - type: main_score
      value: 88.3052
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 45.4377
    - type: v_measure_std
      value: 0.8543000000000001
    - type: main_score
      value: 45.4377
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 39.6472
    - type: v_measure_std
      value: 0.7081999999999999
    - type: main_score
      value: 39.6472
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: ndcg_at_1
      value: 39.342
    - type: ndcg_at_3
      value: 44.718999999999994
    - type: ndcg_at_5
      value: 47.449999999999996
    - type: ndcg_at_10
      value: 50.17
    - type: ndcg_at_20
      value: 52.366
    - type: ndcg_at_100
      value: 55.400000000000006
    - type: ndcg_at_1000
      value: 57.13399999999999
    - type: map_at_1
      value: 32.300000000000004
    - type: map_at_3
      value: 39.937
    - type: map_at_5
      value: 42.141
    - type: map_at_10
      value: 43.681
    - type: map_at_20
      value: 44.516
    - type: map_at_100
      value: 45.14
    - type: map_at_1000
      value: 45.25
    - type: recall_at_1
      value: 32.300000000000004
    - type: recall_at_3
      value: 47.12
    - type: recall_at_5
      value: 54.581
    - type: recall_at_10
      value: 62.873000000000005
    - type: recall_at_20
      value: 70.604
    - type: recall_at_100
      value: 84.465
    - type: recall_at_1000
      value: 95.299
    - type: precision_at_1
      value: 39.342
    - type: precision_at_3
      value: 21.459
    - type: precision_at_5
      value: 15.622
    - type: precision_at_10
      value: 9.514
    - type: precision_at_20
      value: 5.665
    - type: precision_at_100
      value: 1.5150000000000001
    - type: precision_at_1000
      value: 0.19499999999999998
    - type: mrr_at_1
      value: 39.3419
    - type: mrr_at_3
      value: 46.805
    - type: mrr_at_5
      value: 48.5861
    - type: mrr_at_10
      value: 49.6697
    - type: mrr_at_20
      value: 50.131
    - type: mrr_at_100
      value: 50.373599999999996
    - type: mrr_at_1000
      value: 50.4106
    - type: nauc_ndcg_at_1_max
      value: 40.0004
    - type: nauc_ndcg_at_1_std
      value: -1.8753
    - type: nauc_ndcg_at_1_diff1
      value: 45.9146
    - type: nauc_ndcg_at_3_max
      value: 41.3777
    - type: nauc_ndcg_at_3_std
      value: -1.2817
    - type: nauc_ndcg_at_3_diff1
      value: 42.710100000000004
    - type: nauc_ndcg_at_5_max
      value: 42.4211
    - type: nauc_ndcg_at_5_std
      value: -0.6910999999999999
    - type: nauc_ndcg_at_5_diff1
      value: 42.9048
    - type: nauc_ndcg_at_10_max
      value: 42.609399999999994
    - type: nauc_ndcg_at_10_std
      value: 0.4398
    - type: nauc_ndcg_at_10_diff1
      value: 42.4967
    - type: nauc_ndcg_at_20_max
      value: 42.7921
    - type: nauc_ndcg_at_20_std
      value: 0.9266
    - type: nauc_ndcg_at_20_diff1
      value: 42.701899999999995
    - type: nauc_ndcg_at_100_max
      value: 43.4878
    - type: nauc_ndcg_at_100_std
      value: 2.2893
    - type: nauc_ndcg_at_100_diff1
      value: 42.735
    - type: nauc_ndcg_at_1000_max
      value: 43.3776
    - type: nauc_ndcg_at_1000_std
      value: 2.1375
    - type: nauc_ndcg_at_1000_diff1
      value: 42.6437
    - type: nauc_map_at_1_max
      value: 37.573499999999996
    - type: nauc_map_at_1_std
      value: -1.4611
    - type: nauc_map_at_1_diff1
      value: 50.0479
    - type: nauc_map_at_3_max
      value: 40.5952
    - type: nauc_map_at_3_std
      value: -1.7034
    - type: nauc_map_at_3_diff1
      value: 45.7247
    - type: nauc_map_at_5_max
      value: 41.3854
    - type: nauc_map_at_5_std
      value: -1.5435
    - type: nauc_map_at_5_diff1
      value: 45.278400000000005
    - type: nauc_map_at_10_max
      value: 41.7269
    - type: nauc_map_at_10_std
      value: -1.0763
    - type: nauc_map_at_10_diff1
      value: 45.0862
    - type: nauc_map_at_20_max
      value: 42.0241
    - type: nauc_map_at_20_std
      value: -0.8463999999999999
    - type: nauc_map_at_20_diff1
      value: 45.1365
    - type: nauc_map_at_100_max
      value: 42.248200000000004
    - type: nauc_map_at_100_std
      value: -0.6139
    - type: nauc_map_at_100_diff1
      value: 45.0658
    - type: nauc_map_at_1000_max
      value: 42.2442
    - type: nauc_map_at_1000_std
      value: -0.6187
    - type: nauc_map_at_1000_diff1
      value: 45.0382
    - type: nauc_recall_at_1_max
      value: 37.573499999999996
    - type: nauc_recall_at_1_std
      value: -1.4611
    - type: nauc_recall_at_1_diff1
      value: 50.0479
    - type: nauc_recall_at_3_max
      value: 39.9536
    - type: nauc_recall_at_3_std
      value: -0.132
    - type: nauc_recall_at_3_diff1
      value: 39.6892
    - type: nauc_recall_at_5_max
      value: 41.428799999999995
    - type: nauc_recall_at_5_std
      value: 1.2703
    - type: nauc_recall_at_5_diff1
      value: 38.2213
    - type: nauc_recall_at_10_max
      value: 41.3254
    - type: nauc_recall_at_10_std
      value: 4.9163
    - type: nauc_recall_at_10_diff1
      value: 35.1215
    - type: nauc_recall_at_20_max
      value: 41.3807
    - type: nauc_recall_at_20_std
      value: 7.3897
    - type: nauc_recall_at_20_diff1
      value: 33.7864
    - type: nauc_recall_at_100_max
      value: 49.6612
    - type: nauc_recall_at_100_std
      value: 25.1511
    - type: nauc_recall_at_100_diff1
      value: 33.968199999999996
    - type: nauc_recall_at_1000_max
      value: 71.2452
    - type: nauc_recall_at_1000_std
      value: 68.7065
    - type: nauc_recall_at_1000_diff1
      value: 33.0124
    - type: nauc_precision_at_1_max
      value: 40.0004
    - type: nauc_precision_at_1_std
      value: -1.8753
    - type: nauc_precision_at_1_diff1
      value: 45.9146
    - type: nauc_precision_at_3_max
      value: 36.741800000000005
    - type: nauc_precision_at_3_std
      value: -1.2777
    - type: nauc_precision_at_3_diff1
      value: 23.3539
    - type: nauc_precision_at_5_max
      value: 32.9756
    - type: nauc_precision_at_5_std
      value: -0.1613
    - type: nauc_precision_at_5_diff1
      value: 15.866
    - type: nauc_precision_at_10_max
      value: 25.7284
    - type: nauc_precision_at_10_std
      value: 2.7586
    - type: nauc_precision_at_10_diff1
      value: 6.579899999999999
    - type: nauc_precision_at_20_max
      value: 18.8213
    - type: nauc_precision_at_20_std
      value: 3.6470000000000002
    - type: nauc_precision_at_20_diff1
      value: -0.45690000000000003
    - type: nauc_precision_at_100_max
      value: 5.7518
    - type: nauc_precision_at_100_std
      value: 3.4711
    - type: nauc_precision_at_100_diff1
      value: -12.380700000000001
    - type: nauc_precision_at_1000_max
      value: -8.6862
    - type: nauc_precision_at_1000_std
      value: -4.5796
    - type: nauc_precision_at_1000_diff1
      value: -19.9355
    - type: nauc_mrr_at_1_max
      value: 40.0004
    - type: nauc_mrr_at_1_std
      value: -1.8753
    - type: nauc_mrr_at_1_diff1
      value: 45.9146
    - type: nauc_mrr_at_3_max
      value: 40.686
    - type: nauc_mrr_at_3_std
      value: -0.8626999999999999
    - type: nauc_mrr_at_3_diff1
      value: 41.4552
    - type: nauc_mrr_at_5_max
      value: 41.2445
    - type: nauc_mrr_at_5_std
      value: -0.7058
    - type: nauc_mrr_at_5_diff1
      value: 41.7244
    - type: nauc_mrr_at_10_max
      value: 41.1575
    - type: nauc_mrr_at_10_std
      value: -0.44489999999999996
    - type: nauc_mrr_at_10_diff1
      value: 41.355199999999996
    - type: nauc_mrr_at_20_max
      value: 41.1548
    - type: nauc_mrr_at_20_std
      value: -0.33
    - type: nauc_mrr_at_20_diff1
      value: 41.444199999999995
    - type: nauc_mrr_at_100_max
      value: 41.1908
    - type: nauc_mrr_at_100_std
      value: -0.3263
    - type: nauc_mrr_at_100_diff1
      value: 41.505900000000004
    - type: nauc_mrr_at_1000_max
      value: 41.1935
    - type: nauc_mrr_at_1000_std
      value: -0.3216
    - type: nauc_mrr_at_1000_diff1
      value: 41.5128
    - type: main_score
      value: 50.17
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval (default)
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: ndcg_at_1
      value: 42.102000000000004
    - type: ndcg_at_3
      value: 45.741
    - type: ndcg_at_5
      value: 47.734
    - type: ndcg_at_10
      value: 49.732
    - type: ndcg_at_20
      value: 51.295
    - type: ndcg_at_100
      value: 53.935
    - type: ndcg_at_1000
      value: 55.765
    - type: map_at_1
      value: 33.306999999999995
    - type: map_at_3
      value: 40.953
    - type: map_at_5
      value: 42.731
    - type: map_at_10
      value: 44.022
    - type: map_at_20
      value: 44.693
    - type: map_at_100
      value: 45.259
    - type: map_at_1000
      value: 45.383
    - type: recall_at_1
      value: 33.306999999999995
    - type: recall_at_3
      value: 47.127
    - type: recall_at_5
      value: 52.89
    - type: recall_at_10
      value: 59.16400000000001
    - type: recall_at_20
      value: 64.85
    - type: recall_at_100
      value: 77.206
    - type: recall_at_1000
      value: 88.701
    - type: precision_at_1
      value: 42.102000000000004
    - type: precision_at_3
      value: 21.975
    - type: precision_at_5
      value: 15.465000000000002
    - type: precision_at_10
      value: 9.229
    - type: precision_at_20
      value: 5.404
    - type: precision_at_100
      value: 1.461
    - type: precision_at_1000
      value: 0.192
    - type: mrr_at_1
      value: 42.1019
    - type: mrr_at_3
      value: 48.322700000000005
    - type: mrr_at_5
      value: 49.593399999999995
    - type: mrr_at_10
      value: 50.364399999999996
    - type: mrr_at_20
      value: 50.7215
    - type: mrr_at_100
      value: 50.962300000000006
    - type: mrr_at_1000
      value: 50.9999
    - type: nauc_ndcg_at_1_max
      value: 40.6054
    - type: nauc_ndcg_at_1_std
      value: -3.4602
    - type: nauc_ndcg_at_1_diff1
      value: 54.0346
    - type: nauc_ndcg_at_3_max
      value: 40.0946
    - type: nauc_ndcg_at_3_std
      value: -3.7981000000000003
    - type: nauc_ndcg_at_3_diff1
      value: 49.2481
    - type: nauc_ndcg_at_5_max
      value: 40.198699999999995
    - type: nauc_ndcg_at_5_std
      value: -3.2983
    - type: nauc_ndcg_at_5_diff1
      value: 48.7252
    - type: nauc_ndcg_at_10_max
      value: 40.6072
    - type: nauc_ndcg_at_10_std
      value: -3.472
    - type: nauc_ndcg_at_10_diff1
      value: 48.7302
    - type: nauc_ndcg_at_20_max
      value: 41.0897
    - type: nauc_ndcg_at_20_std
      value: -2.8645
    - type: nauc_ndcg_at_20_diff1
      value: 48.8834
    - type: nauc_ndcg_at_100_max
      value: 41.450900000000004
    - type: nauc_ndcg_at_100_std
      value: -1.3305
    - type: nauc_ndcg_at_100_diff1
      value: 48.2699
    - type: nauc_ndcg_at_1000_max
      value: 41.4853
    - type: nauc_ndcg_at_1000_std
      value: -0.7634
    - type: nauc_ndcg_at_1000_diff1
      value: 48.28
    - type: nauc_map_at_1_max
      value: 31.776100000000003
    - type: nauc_map_at_1_std
      value: -12.5085
    - type: nauc_map_at_1_diff1
      value: 56.84630000000001
    - type: nauc_map_at_3_max
      value: 36.3131
    - type: nauc_map_at_3_std
      value: -9.3976
    - type: nauc_map_at_3_diff1
      value: 52.4471
    - type: nauc_map_at_5_max
      value: 37.330799999999996
    - type: nauc_map_at_5_std
      value: -8.0619
    - type: nauc_map_at_5_diff1
      value: 51.692800000000005
    - type: nauc_map_at_10_max
      value: 38.406400000000005
    - type: nauc_map_at_10_std
      value: -7.1754
    - type: nauc_map_at_10_diff1
      value: 51.46849999999999
    - type: nauc_map_at_20_max
      value: 38.940000000000005
    - type: nauc_map_at_20_std
      value: -6.4747
    - type: nauc_map_at_20_diff1
      value: 51.34570000000001
    - type: nauc_map_at_100_max
      value: 39.3424
    - type: nauc_map_at_100_std
      value: -5.7301
    - type: nauc_map_at_100_diff1
      value: 51.0633
    - type: nauc_map_at_1000_max
      value: 39.3905
    - type: nauc_map_at_1000_std
      value: -5.5938
    - type: nauc_map_at_1000_diff1
      value: 51.04109999999999
    - type: nauc_recall_at_1_max
      value: 31.776100000000003
    - type: nauc_recall_at_1_std
      value: -12.5085
    - type: nauc_recall_at_1_diff1
      value: 56.84630000000001
    - type: nauc_recall_at_3_max
      value: 35.702
    - type: nauc_recall_at_3_std
      value: -7.3138
    - type: nauc_recall_at_3_diff1
      value: 46.3454
    - type: nauc_recall_at_5_max
      value: 36.459399999999995
    - type: nauc_recall_at_5_std
      value: -4.678100000000001
    - type: nauc_recall_at_5_diff1
      value: 43.6423
    - type: nauc_recall_at_10_max
      value: 37.3534
    - type: nauc_recall_at_10_std
      value: -4.0492
    - type: nauc_recall_at_10_diff1
      value: 41.7513
    - type: nauc_recall_at_20_max
      value: 39.379999999999995
    - type: nauc_recall_at_20_std
      value: -1.0078
    - type: nauc_recall_at_20_diff1
      value: 41.638
    - type: nauc_recall_at_100_max
      value: 40.705799999999996
    - type: nauc_recall_at_100_std
      value: 8.9477
    - type: nauc_recall_at_100_diff1
      value: 35.7987
    - type: nauc_recall_at_1000_max
      value: 41.560399999999994
    - type: nauc_recall_at_1000_std
      value: 19.6108
    - type: nauc_recall_at_1000_diff1
      value: 30.694399999999998
    - type: nauc_precision_at_1_max
      value: 40.6054
    - type: nauc_precision_at_1_std
      value: -3.4602
    - type: nauc_precision_at_1_diff1
      value: 54.0346
    - type: nauc_precision_at_3_max
      value: 42.0217
    - type: nauc_precision_at_3_std
      value: 10.3896
    - type: nauc_precision_at_3_diff1
      value: 26.7498
    - type: nauc_precision_at_5_max
      value: 40.4414
    - type: nauc_precision_at_5_std
      value: 18.177599999999998
    - type: nauc_precision_at_5_diff1
      value: 16.9455
    - type: nauc_precision_at_10_max
      value: 38.921
    - type: nauc_precision_at_10_std
      value: 24.1093
    - type: nauc_precision_at_10_diff1
      value: 8.4258
    - type: nauc_precision_at_20_max
      value: 34.620200000000004
    - type: nauc_precision_at_20_std
      value: 29.351399999999998
    - type: nauc_precision_at_20_diff1
      value: 0.15360000000000001
    - type: nauc_precision_at_100_max
      value: 25.230000000000004
    - type: nauc_precision_at_100_std
      value: 36.8424
    - type: nauc_precision_at_100_diff1
      value: -12.225900000000001
    - type: nauc_precision_at_1000_max
      value: 13.1715
    - type: nauc_precision_at_1000_std
      value: 34.7096
    - type: nauc_precision_at_1000_diff1
      value: -16.5331
    - type: nauc_mrr_at_1_max
      value: 40.6054
    - type: nauc_mrr_at_1_std
      value: -3.4602
    - type: nauc_mrr_at_1_diff1
      value: 54.0346
    - type: nauc_mrr_at_3_max
      value: 42.2127
    - type: nauc_mrr_at_3_std
      value: -1.0392000000000001
    - type: nauc_mrr_at_3_diff1
      value: 49.748
    - type: nauc_mrr_at_5_max
      value: 42.2638
    - type: nauc_mrr_at_5_std
      value: -0.40049999999999997
    - type: nauc_mrr_at_5_diff1
      value: 49.3009
    - type: nauc_mrr_at_10_max
      value: 42.0477
    - type: nauc_mrr_at_10_std
      value: -0.6505000000000001
    - type: nauc_mrr_at_10_diff1
      value: 49.0978
    - type: nauc_mrr_at_20_max
      value: 42.0895
    - type: nauc_mrr_at_20_std
      value: -0.5649000000000001
    - type: nauc_mrr_at_20_diff1
      value: 49.1893
    - type: nauc_mrr_at_100_max
      value: 42.0951
    - type: nauc_mrr_at_100_std
      value: -0.5555
    - type: nauc_mrr_at_100_diff1
      value: 49.2047
    - type: nauc_mrr_at_1000_max
      value: 42.0946
    - type: nauc_mrr_at_1000_std
      value: -0.5584
    - type: nauc_mrr_at_1000_diff1
      value: 49.207699999999996
    - type: main_score
      value: 49.732
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval (default)
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: ndcg_at_1
      value: 48.276
    - type: ndcg_at_3
      value: 53.727000000000004
    - type: ndcg_at_5
      value: 56.511
    - type: ndcg_at_10
      value: 59.023
    - type: ndcg_at_20
      value: 60.802
    - type: ndcg_at_100
      value: 62.980999999999995
    - type: ndcg_at_1000
      value: 64.13600000000001
    - type: map_at_1
      value: 42.347
    - type: map_at_3
      value: 50.349999999999994
    - type: map_at_5
      value: 52.276999999999994
    - type: map_at_10
      value: 53.6
    - type: map_at_20
      value: 54.217000000000006
    - type: map_at_100
      value: 54.605000000000004
    - type: map_at_1000
      value: 54.663
    - type: recall_at_1
      value: 42.347
    - type: recall_at_3
      value: 57.499
    - type: recall_at_5
      value: 64.269
    - type: recall_at_10
      value: 71.568
    - type: recall_at_20
      value: 78.125
    - type: recall_at_100
      value: 88.699
    - type: recall_at_1000
      value: 96.887
    - type: precision_at_1
      value: 48.276
    - type: precision_at_3
      value: 23.49
    - type: precision_at_5
      value: 16.262999999999998
    - type: precision_at_10
      value: 9.322999999999999
    - type: precision_at_20
      value: 5.21
    - type: precision_at_100
      value: 1.22
    - type: precision_at_1000
      value: 0.136
    - type: mrr_at_1
      value: 48.2759
    - type: mrr_at_3
      value: 54.5246
    - type: mrr_at_5
      value: 56.0982
    - type: mrr_at_10
      value: 56.961
    - type: mrr_at_20
      value: 57.391400000000004
    - type: mrr_at_100
      value: 57.6295
    - type: mrr_at_1000
      value: 57.66139999999999
    - type: nauc_ndcg_at_1_max
      value: 43.5037
    - type: nauc_ndcg_at_1_std
      value: -7.6921
    - type: nauc_ndcg_at_1_diff1
      value: 58.544700000000006
    - type: nauc_ndcg_at_3_max
      value: 44.630900000000004
    - type: nauc_ndcg_at_3_std
      value: -6.260300000000001
    - type: nauc_ndcg_at_3_diff1
      value: 56.120999999999995
    - type: nauc_ndcg_at_5_max
      value: 45.1267
    - type: nauc_ndcg_at_5_std
      value: -5.5512
    - type: nauc_ndcg_at_5_diff1
      value: 54.8272
    - type: nauc_ndcg_at_10_max
      value: 45.691199999999995
    - type: nauc_ndcg_at_10_std
      value: -4.1767
    - type: nauc_ndcg_at_10_diff1
      value: 53.8565
    - type: nauc_ndcg_at_20_max
      value: 46.0581
    - type: nauc_ndcg_at_20_std
      value: -2.4019
    - type: nauc_ndcg_at_20_diff1
      value: 53.67150000000001
    - type: nauc_ndcg_at_100_max
      value: 46.3071
    - type: nauc_ndcg_at_100_std
      value: -1.856
    - type: nauc_ndcg_at_100_diff1
      value: 54.2616
    - type: nauc_ndcg_at_1000_max
      value: 46.3054
    - type: nauc_ndcg_at_1000_std
      value: -2.4795000000000003
    - type: nauc_ndcg_at_1000_diff1
      value: 54.6332
    - type: nauc_map_at_1_max
      value: 37.3915
    - type: nauc_map_at_1_std
      value: -9.6709
    - type: nauc_map_at_1_diff1
      value: 59.0807
    - type: nauc_map_at_3_max
      value: 42.3532
    - type: nauc_map_at_3_std
      value: -8.4634
    - type: nauc_map_at_3_diff1
      value: 57.342400000000005
    - type: nauc_map_at_5_max
      value: 43.065799999999996
    - type: nauc_map_at_5_std
      value: -7.430000000000001
    - type: nauc_map_at_5_diff1
      value: 56.5453
    - type: nauc_map_at_10_max
      value: 43.4845
    - type: nauc_map_at_10_std
      value: -6.5406
    - type: nauc_map_at_10_diff1
      value: 55.959199999999996
    - type: nauc_map_at_20_max
      value: 43.8265
    - type: nauc_map_at_20_std
      value: -5.8393
    - type: nauc_map_at_20_diff1
      value: 55.8438
    - type: nauc_map_at_100_max
      value: 44.014399999999995
    - type: nauc_map_at_100_std
      value: -5.6227
    - type: nauc_map_at_100_diff1
      value: 55.8762
    - type: nauc_map_at_1000_max
      value: 44.0386
    - type: nauc_map_at_1000_std
      value: -5.6262
    - type: nauc_map_at_1000_diff1
      value: 55.888099999999994
    - type: nauc_recall_at_1_max
      value: 37.3915
    - type: nauc_recall_at_1_std
      value: -9.6709
    - type: nauc_recall_at_1_diff1
      value: 59.0807
    - type: nauc_recall_at_3_max
      value: 43.8264
    - type: nauc_recall_at_3_std
      value: -6.309099999999999
    - type: nauc_recall_at_3_diff1
      value: 53.4872
    - type: nauc_recall_at_5_max
      value: 44.237300000000005
    - type: nauc_recall_at_5_std
      value: -4.1856
    - type: nauc_recall_at_5_diff1
      value: 49.3654
    - type: nauc_recall_at_10_max
      value: 46.7914
    - type: nauc_recall_at_10_std
      value: 1.3229
    - type: nauc_recall_at_10_diff1
      value: 45.1973
    - type: nauc_recall_at_20_max
      value: 49.560500000000005
    - type: nauc_recall_at_20_std
      value: 11.9406
    - type: nauc_recall_at_20_diff1
      value: 42.821999999999996
    - type: nauc_recall_at_100_max
      value: 53.3482
    - type: nauc_recall_at_100_std
      value: 27.375
    - type: nauc_recall_at_100_diff1
      value: 44.0535
    - type: nauc_recall_at_1000_max
      value: 64.18
    - type: nauc_recall_at_1000_std
      value: 53.603699999999996
    - type: nauc_recall_at_1000_diff1
      value: 50.1113
    - type: nauc_precision_at_1_max
      value: 43.5037
    - type: nauc_precision_at_1_std
      value: -7.6921
    - type: nauc_precision_at_1_diff1
      value: 58.544700000000006
    - type: nauc_precision_at_3_max
      value: 41.9145
    - type: nauc_precision_at_3_std
      value: 0.6891999999999999
    - type: nauc_precision_at_3_diff1
      value: 35.0689
    - type: nauc_precision_at_5_max
      value: 38.553399999999996
    - type: nauc_precision_at_5_std
      value: 6.1493
    - type: nauc_precision_at_5_diff1
      value: 23.127
    - type: nauc_precision_at_10_max
      value: 34.076699999999995
    - type: nauc_precision_at_10_std
      value: 12.673300000000001
    - type: nauc_precision_at_10_diff1
      value: 10.7967
    - type: nauc_precision_at_20_max
      value: 31.9315
    - type: nauc_precision_at_20_std
      value: 21.0503
    - type: nauc_precision_at_20_diff1
      value: 1.9767
    - type: nauc_precision_at_100_max
      value: 24.287300000000002
    - type: nauc_precision_at_100_std
      value: 24.5746
    - type: nauc_precision_at_100_diff1
      value: -9.751700000000001
    - type: nauc_precision_at_1000_max
      value: 19.252
    - type: nauc_precision_at_1000_std
      value: 21.0394
    - type: nauc_precision_at_1000_diff1
      value: -16.8851
    - type: nauc_mrr_at_1_max
      value: 43.5037
    - type: nauc_mrr_at_1_std
      value: -7.6921
    - type: nauc_mrr_at_1_diff1
      value: 58.544700000000006
    - type: nauc_mrr_at_3_max
      value: 45.9732
    - type: nauc_mrr_at_3_std
      value: -5.3982
    - type: nauc_mrr_at_3_diff1
      value: 56.1002
    - type: nauc_mrr_at_5_max
      value: 45.9223
    - type: nauc_mrr_at_5_std
      value: -5.3386000000000005
    - type: nauc_mrr_at_5_diff1
      value: 55.196
    - type: nauc_mrr_at_10_max
      value: 46.1619
    - type: nauc_mrr_at_10_std
      value: -4.965
    - type: nauc_mrr_at_10_diff1
      value: 55.081199999999995
    - type: nauc_mrr_at_20_max
      value: 46.238600000000005
    - type: nauc_mrr_at_20_std
      value: -4.5938
    - type: nauc_mrr_at_20_diff1
      value: 55.0906
    - type: nauc_mrr_at_100_max
      value: 46.2087
    - type: nauc_mrr_at_100_std
      value: -4.6099
    - type: nauc_mrr_at_100_diff1
      value: 55.1922
    - type: nauc_mrr_at_1000_max
      value: 46.2022
    - type: nauc_mrr_at_1000_std
      value: -4.6231
    - type: nauc_mrr_at_1000_diff1
      value: 55.209399999999995
    - type: main_score
      value: 59.023
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval (default)
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: ndcg_at_1
      value: 27.797
    - type: ndcg_at_3
      value: 34.787
    - type: ndcg_at_5
      value: 37.326
    - type: ndcg_at_10
      value: 39.583
    - type: ndcg_at_20
      value: 41.677
    - type: ndcg_at_100
      value: 44.932
    - type: ndcg_at_1000
      value: 46.893
    - type: map_at_1
      value: 26.209
    - type: map_at_3
      value: 32.365
    - type: map_at_5
      value: 33.819
    - type: map_at_10
      value: 34.827999999999996
    - type: map_at_20
      value: 35.447
    - type: map_at_100
      value: 35.93
    - type: map_at_1000
      value: 36.007
    - type: recall_at_1
      value: 26.209
    - type: recall_at_3
      value: 39.562999999999995
    - type: recall_at_5
      value: 45.594
    - type: recall_at_10
      value: 52.236000000000004
    - type: recall_at_20
      value: 60.019
    - type: recall_at_100
      value: 76.6
    - type: recall_at_1000
      value: 91.389
    - type: precision_at_1
      value: 27.797
    - type: precision_at_3
      value: 14.539
    - type: precision_at_5
      value: 10.215
    - type: precision_at_10
      value: 5.944
    - type: precision_at_20
      value: 3.469
    - type: precision_at_100
      value: 0.907
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: mrr_at_1
      value: 27.796599999999998
    - type: mrr_at_3
      value: 34.2373
    - type: mrr_at_5
      value: 35.762699999999995
    - type: mrr_at_10
      value: 36.6849
    - type: mrr_at_20
      value: 37.257600000000004
    - type: mrr_at_100
      value: 37.6676
    - type: mrr_at_1000
      value: 37.723800000000004
    - type: nauc_ndcg_at_1_max
      value: 27.845599999999997
    - type: nauc_ndcg_at_1_std
      value: -8.0177
    - type: nauc_ndcg_at_1_diff1
      value: 44.9034
    - type: nauc_ndcg_at_3_max
      value: 28.7984
    - type: nauc_ndcg_at_3_std
      value: -6.7625
    - type: nauc_ndcg_at_3_diff1
      value: 38.344
    - type: nauc_ndcg_at_5_max
      value: 29.8333
    - type: nauc_ndcg_at_5_std
      value: -5.305
    - type: nauc_ndcg_at_5_diff1
      value: 37.8077
    - type: nauc_ndcg_at_10_max
      value: 30.0319
    - type: nauc_ndcg_at_10_std
      value: -3.7874
    - type: nauc_ndcg_at_10_diff1
      value: 36.7867
    - type: nauc_ndcg_at_20_max
      value: 29.768499999999996
    - type: nauc_ndcg_at_20_std
      value: -4.4994
    - type: nauc_ndcg_at_20_diff1
      value: 36.2424
    - type: nauc_ndcg_at_100_max
      value: 29.6882
    - type: nauc_ndcg_at_100_std
      value: -3.0686999999999998
    - type: nauc_ndcg_at_100_diff1
      value: 35.5097
    - type: nauc_ndcg_at_1000_max
      value: 30.0696
    - type: nauc_ndcg_at_1000_std
      value: -3.0852
    - type: nauc_ndcg_at_1000_diff1
      value: 36.168
    - type: nauc_map_at_1_max
      value: 26.105800000000002
    - type: nauc_map_at_1_std
      value: -9.0379
    - type: nauc_map_at_1_diff1
      value: 46.5148
    - type: nauc_map_at_3_max
      value: 27.851100000000002
    - type: nauc_map_at_3_std
      value: -7.6508
    - type: nauc_map_at_3_diff1
      value: 40.441
    - type: nauc_map_at_5_max
      value: 28.498600000000003
    - type: nauc_map_at_5_std
      value: -6.8919
    - type: nauc_map_at_5_diff1
      value: 40.2012
    - type: nauc_map_at_10_max
      value: 28.754
    - type: nauc_map_at_10_std
      value: -6.1987
    - type: nauc_map_at_10_diff1
      value: 39.7856
    - type: nauc_map_at_20_max
      value: 28.7468
    - type: nauc_map_at_20_std
      value: -6.372999999999999
    - type: nauc_map_at_20_diff1
      value: 39.7445
    - type: nauc_map_at_100_max
      value: 28.762999999999998
    - type: nauc_map_at_100_std
      value: -6.1504
    - type: nauc_map_at_100_diff1
      value: 39.643699999999995
    - type: nauc_map_at_1000_max
      value: 28.7886
    - type: nauc_map_at_1000_std
      value: -6.1426
    - type: nauc_map_at_1000_diff1
      value: 39.6637
    - type: nauc_recall_at_1_max
      value: 26.105800000000002
    - type: nauc_recall_at_1_std
      value: -9.0379
    - type: nauc_recall_at_1_diff1
      value: 46.5148
    - type: nauc_recall_at_3_max
      value: 28.845399999999998
    - type: nauc_recall_at_3_std
      value: -4.6356
    - type: nauc_recall_at_3_diff1
      value: 32.9931
    - type: nauc_recall_at_5_max
      value: 31.3996
    - type: nauc_recall_at_5_std
      value: -1.7656
    - type: nauc_recall_at_5_diff1
      value: 31.254199999999997
    - type: nauc_recall_at_10_max
      value: 31.406
    - type: nauc_recall_at_10_std
      value: 2.6767
    - type: nauc_recall_at_10_diff1
      value: 27.5627
    - type: nauc_recall_at_20_max
      value: 29.6752
    - type: nauc_recall_at_20_std
      value: 0.0991
    - type: nauc_recall_at_20_diff1
      value: 24.0771
    - type: nauc_recall_at_100_max
      value: 28.4217
    - type: nauc_recall_at_100_std
      value: 12.0071
    - type: nauc_recall_at_100_diff1
      value: 13.231100000000001
    - type: nauc_recall_at_1000_max
      value: 35.8245
    - type: nauc_recall_at_1000_std
      value: 30.705
    - type: nauc_recall_at_1000_diff1
      value: 2.7809
    - type: nauc_precision_at_1_max
      value: 27.845599999999997
    - type: nauc_precision_at_1_std
      value: -8.0177
    - type: nauc_precision_at_1_diff1
      value: 44.9034
    - type: nauc_precision_at_3_max
      value: 32.706
    - type: nauc_precision_at_3_std
      value: -3.9037
    - type: nauc_precision_at_3_diff1
      value: 29.921599999999998
    - type: nauc_precision_at_5_max
      value: 34.192
    - type: nauc_precision_at_5_std
      value: -0.5177
    - type: nauc_precision_at_5_diff1
      value: 28.4206
    - type: nauc_precision_at_10_max
      value: 33.6132
    - type: nauc_precision_at_10_std
      value: 4.372
    - type: nauc_precision_at_10_diff1
      value: 23.5257
    - type: nauc_precision_at_20_max
      value: 31.1237
    - type: nauc_precision_at_20_std
      value: 1.9191
    - type: nauc_precision_at_20_diff1
      value: 18.445700000000002
    - type: nauc_precision_at_100_max
      value: 22.5504
    - type: nauc_precision_at_100_std
      value: 11.1776
    - type: nauc_precision_at_100_diff1
      value: 3.3670999999999998
    - type: nauc_precision_at_1000_max
      value: 13.5905
    - type: nauc_precision_at_1000_std
      value: 12.9311
    - type: nauc_precision_at_1000_diff1
      value: -8.054699999999999
    - type: nauc_mrr_at_1_max
      value: 27.845599999999997
    - type: nauc_mrr_at_1_std
      value: -8.0177
    - type: nauc_mrr_at_1_diff1
      value: 44.9034
    - type: nauc_mrr_at_3_max
      value: 29.1589
    - type: nauc_mrr_at_3_std
      value: -6.4891000000000005
    - type: nauc_mrr_at_3_diff1
      value: 39.088699999999996
    - type: nauc_mrr_at_5_max
      value: 29.9228
    - type: nauc_mrr_at_5_std
      value: -5.6324
    - type: nauc_mrr_at_5_diff1
      value: 38.862
    - type: nauc_mrr_at_10_max
      value: 29.907600000000002
    - type: nauc_mrr_at_10_std
      value: -5.148
    - type: nauc_mrr_at_10_diff1
      value: 38.4778
    - type: nauc_mrr_at_20_max
      value: 29.8398
    - type: nauc_mrr_at_20_std
      value: -5.3067
    - type: nauc_mrr_at_20_diff1
      value: 38.275999999999996
    - type: nauc_mrr_at_100_max
      value: 29.828100000000003
    - type: nauc_mrr_at_100_std
      value: -5.1385
    - type: nauc_mrr_at_100_diff1
      value: 38.2314
    - type: nauc_mrr_at_1000_max
      value: 29.8443
    - type: nauc_mrr_at_1000_std
      value: -5.146
    - type: nauc_mrr_at_1000_diff1
      value: 38.2581
    - type: main_score
      value: 39.583
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval (default)
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: ndcg_at_1
      value: 22.015
    - type: ndcg_at_3
      value: 25.941
    - type: ndcg_at_5
      value: 28.469
    - type: ndcg_at_10
      value: 31.391000000000002
    - type: ndcg_at_20
      value: 33.485
    - type: ndcg_at_100
      value: 37.145
    - type: ndcg_at_1000
      value: 39.909
    - type: map_at_1
      value: 17.580000000000002
    - type: map_at_3
      value: 22.900000000000002
    - type: map_at_5
      value: 24.498
    - type: map_at_10
      value: 25.823
    - type: map_at_20
      value: 26.429000000000002
    - type: map_at_100
      value: 27.029999999999998
    - type: map_at_1000
      value: 27.147
    - type: recall_at_1
      value: 17.580000000000002
    - type: recall_at_3
      value: 29.355999999999998
    - type: recall_at_5
      value: 35.634
    - type: recall_at_10
      value: 44.336
    - type: recall_at_20
      value: 51.661
    - type: recall_at_100
      value: 68.766
    - type: recall_at_1000
      value: 88.429
    - type: precision_at_1
      value: 22.015
    - type: precision_at_3
      value: 12.520999999999999
    - type: precision_at_5
      value: 9.254
    - type: precision_at_10
      value: 5.784000000000001
    - type: precision_at_20
      value: 3.514
    - type: precision_at_100
      value: 1.019
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: mrr_at_1
      value: 22.0149
    - type: mrr_at_3
      value: 27.5705
    - type: mrr_at_5
      value: 29.168699999999998
    - type: mrr_at_10
      value: 30.352
    - type: mrr_at_20
      value: 30.968200000000003
    - type: mrr_at_100
      value: 31.3807
    - type: mrr_at_1000
      value: 31.4469
    - type: nauc_ndcg_at_1_max
      value: 21.2985
    - type: nauc_ndcg_at_1_std
      value: -4.6632
    - type: nauc_ndcg_at_1_diff1
      value: 36.1703
    - type: nauc_ndcg_at_3_max
      value: 23.2761
    - type: nauc_ndcg_at_3_std
      value: -2.9883
    - type: nauc_ndcg_at_3_diff1
      value: 31.11
    - type: nauc_ndcg_at_5_max
      value: 22.697400000000002
    - type: nauc_ndcg_at_5_std
      value: -2.6858
    - type: nauc_ndcg_at_5_diff1
      value: 29.1155
    - type: nauc_ndcg_at_10_max
      value: 21.745
    - type: nauc_ndcg_at_10_std
      value: -2.1321
    - type: nauc_ndcg_at_10_diff1
      value: 27.6691
    - type: nauc_ndcg_at_20_max
      value: 22.368
    - type: nauc_ndcg_at_20_std
      value: -1.1924000000000001
    - type: nauc_ndcg_at_20_diff1
      value: 27.453100000000003
    - type: nauc_ndcg_at_100_max
      value: 23.1279
    - type: nauc_ndcg_at_100_std
      value: 0.1931
    - type: nauc_ndcg_at_100_diff1
      value: 27.2613
    - type: nauc_ndcg_at_1000_max
      value: 23.5609
    - type: nauc_ndcg_at_1000_std
      value: 0.4277
    - type: nauc_ndcg_at_1000_diff1
      value: 27.898
    - type: nauc_map_at_1_max
      value: 22.1777
    - type: nauc_map_at_1_std
      value: -3.6511
    - type: nauc_map_at_1_diff1
      value: 35.193799999999996
    - type: nauc_map_at_3_max
      value: 22.6711
    - type: nauc_map_at_3_std
      value: -3.2921
    - type: nauc_map_at_3_diff1
      value: 31.647199999999998
    - type: nauc_map_at_5_max
      value: 22.3125
    - type: nauc_map_at_5_std
      value: -3.3684
    - type: nauc_map_at_5_diff1
      value: 30.6346
    - type: nauc_map_at_10_max
      value: 22.1293
    - type: nauc_map_at_10_std
      value: -3.0963000000000003
    - type: nauc_map_at_10_diff1
      value: 29.9676
    - type: nauc_map_at_20_max
      value: 22.345599999999997
    - type: nauc_map_at_20_std
      value: -2.7918
    - type: nauc_map_at_20_diff1
      value: 29.873300000000004
    - type: nauc_map_at_100_max
      value: 22.547600000000003
    - type: nauc_map_at_100_std
      value: -2.5456
    - type: nauc_map_at_100_diff1
      value: 29.8869
    - type: nauc_map_at_1000_max
      value: 22.5777
    - type: nauc_map_at_1000_std
      value: -2.5162
    - type: nauc_map_at_1000_diff1
      value: 29.9082
    - type: nauc_recall_at_1_max
      value: 22.1777
    - type: nauc_recall_at_1_std
      value: -3.6511
    - type: nauc_recall_at_1_diff1
      value: 35.193799999999996
    - type: nauc_recall_at_3_max
      value: 22.8589
    - type: nauc_recall_at_3_std
      value: -1.541
    - type: nauc_recall_at_3_diff1
      value: 26.8307
    - type: nauc_recall_at_5_max
      value: 21.2508
    - type: nauc_recall_at_5_std
      value: -1.6594000000000002
    - type: nauc_recall_at_5_diff1
      value: 23.0152
    - type: nauc_recall_at_10_max
      value: 18.4227
    - type: nauc_recall_at_10_std
      value: -0.29610000000000003
    - type: nauc_recall_at_10_diff1
      value: 19.0389
    - type: nauc_recall_at_20_max
      value: 20.0064
    - type: nauc_recall_at_20_std
      value: 2.6574
    - type: nauc_recall_at_20_diff1
      value: 18.1572
    - type: nauc_recall_at_100_max
      value: 22.8024
    - type: nauc_recall_at_100_std
      value: 11.629100000000001
    - type: nauc_recall_at_100_diff1
      value: 13.7353
    - type: nauc_recall_at_1000_max
      value: 33.8158
    - type: nauc_recall_at_1000_std
      value: 28.807
    - type: nauc_recall_at_1000_diff1
      value: 10.385900000000001
    - type: nauc_precision_at_1_max
      value: 21.2985
    - type: nauc_precision_at_1_std
      value: -4.6632
    - type: nauc_precision_at_1_diff1
      value: 36.1703
    - type: nauc_precision_at_3_max
      value: 23.8607
    - type: nauc_precision_at_3_std
      value: -1.2343
    - type: nauc_precision_at_3_diff1
      value: 26.056600000000003
    - type: nauc_precision_at_5_max
      value: 22.3303
    - type: nauc_precision_at_5_std
      value: -0.6769
    - type: nauc_precision_at_5_diff1
      value: 21.1393
    - type: nauc_precision_at_10_max
      value: 18.9603
    - type: nauc_precision_at_10_std
      value: 0.9261
    - type: nauc_precision_at_10_diff1
      value: 15.4373
    - type: nauc_precision_at_20_max
      value: 18.1666
    - type: nauc_precision_at_20_std
      value: 3.9616
    - type: nauc_precision_at_20_diff1
      value: 11.2774
    - type: nauc_precision_at_100_max
      value: 13.095399999999998
    - type: nauc_precision_at_100_std
      value: 7.7341999999999995
    - type: nauc_precision_at_100_diff1
      value: 3.3591999999999995
    - type: nauc_precision_at_1000_max
      value: 3.0223
    - type: nauc_precision_at_1000_std
      value: 4.3308
    - type: nauc_precision_at_1000_diff1
      value: -1.0134
    - type: nauc_mrr_at_1_max
      value: 21.2985
    - type: nauc_mrr_at_1_std
      value: -4.6632
    - type: nauc_mrr_at_1_diff1
      value: 36.1703
    - type: nauc_mrr_at_3_max
      value: 23.1376
    - type: nauc_mrr_at_3_std
      value: -3.228
    - type: nauc_mrr_at_3_diff1
      value: 33.150800000000004
    - type: nauc_mrr_at_5_max
      value: 22.7773
    - type: nauc_mrr_at_5_std
      value: -2.9971
    - type: nauc_mrr_at_5_diff1
      value: 31.8828
    - type: nauc_mrr_at_10_max
      value: 22.15
    - type: nauc_mrr_at_10_std
      value: -2.8863
    - type: nauc_mrr_at_10_diff1
      value: 31.465799999999998
    - type: nauc_mrr_at_20_max
      value: 22.3119
    - type: nauc_mrr_at_20_std
      value: -2.6858
    - type: nauc_mrr_at_20_diff1
      value: 31.446600000000004
    - type: nauc_mrr_at_100_max
      value: 22.3597
    - type: nauc_mrr_at_100_std
      value: -2.6425
    - type: nauc_mrr_at_100_diff1
      value: 31.4728
    - type: nauc_mrr_at_1000_max
      value: 22.3731
    - type: nauc_mrr_at_1000_std
      value: -2.6344
    - type: nauc_mrr_at_1000_diff1
      value: 31.489299999999997
    - type: main_score
      value: 31.391000000000002
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval (default)
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: ndcg_at_1
      value: 38.690999999999995
    - type: ndcg_at_3
      value: 43.519000000000005
    - type: ndcg_at_5
      value: 45.862
    - type: ndcg_at_10
      value: 48.542
    - type: ndcg_at_20
      value: 50.40599999999999
    - type: ndcg_at_100
      value: 53.766000000000005
    - type: ndcg_at_1000
      value: 55.657000000000004
    - type: map_at_1
      value: 31.696
    - type: map_at_3
      value: 39.228
    - type: map_at_5
      value: 41.046
    - type: map_at_10
      value: 42.539
    - type: map_at_20
      value: 43.199
    - type: map_at_100
      value: 43.799
    - type: map_at_1000
      value: 43.902
    - type: recall_at_1
      value: 31.696
    - type: recall_at_3
      value: 46.482
    - type: recall_at_5
      value: 52.800999999999995
    - type: recall_at_10
      value: 60.650999999999996
    - type: recall_at_20
      value: 67.007
    - type: recall_at_100
      value: 82.669
    - type: recall_at_1000
      value: 95.02199999999999
    - type: precision_at_1
      value: 38.690999999999995
    - type: precision_at_3
      value: 20.404
    - type: precision_at_5
      value: 14.321
    - type: precision_at_10
      value: 8.709999999999999
    - type: precision_at_20
      value: 5.01
    - type: precision_at_100
      value: 1.315
    - type: precision_at_1000
      value: 0.165
    - type: mrr_at_1
      value: 38.690999999999995
    - type: mrr_at_3
      value: 45.684999999999995
    - type: mrr_at_5
      value: 47.1575
    - type: mrr_at_10
      value: 48.1562
    - type: mrr_at_20
      value: 48.582
    - type: mrr_at_100
      value: 48.9294
    - type: mrr_at_1000
      value: 48.968
    - type: nauc_ndcg_at_1_max
      value: 38.6678
    - type: nauc_ndcg_at_1_std
      value: -0.7451
    - type: nauc_ndcg_at_1_diff1
      value: 54.51089999999999
    - type: nauc_ndcg_at_3_max
      value: 38.5936
    - type: nauc_ndcg_at_3_std
      value: -1.185
    - type: nauc_ndcg_at_3_diff1
      value: 50.5312
    - type: nauc_ndcg_at_5_max
      value: 38.0602
    - type: nauc_ndcg_at_5_std
      value: -1.8034999999999999
    - type: nauc_ndcg_at_5_diff1
      value: 49.2837
    - type: nauc_ndcg_at_10_max
      value: 38.342
    - type: nauc_ndcg_at_10_std
      value: -0.9533
    - type: nauc_ndcg_at_10_diff1
      value: 49.0239
    - type: nauc_ndcg_at_20_max
      value: 39.2226
    - type: nauc_ndcg_at_20_std
      value: 0.6093999999999999
    - type: nauc_ndcg_at_20_diff1
      value: 48.7193
    - type: nauc_ndcg_at_100_max
      value: 39.3235
    - type: nauc_ndcg_at_100_std
      value: 2.3982
    - type: nauc_ndcg_at_100_diff1
      value: 48.5831
    - type: nauc_ndcg_at_1000_max
      value: 39.8333
    - type: nauc_ndcg_at_1000_std
      value: 2.4336
    - type: nauc_ndcg_at_1000_diff1
      value: 48.802099999999996
    - type: nauc_map_at_1_max
      value: 33.9405
    - type: nauc_map_at_1_std
      value: -3.9303999999999997
    - type: nauc_map_at_1_diff1
      value: 55.7491
    - type: nauc_map_at_3_max
      value: 36.550399999999996
    - type: nauc_map_at_3_std
      value: -2.7818
    - type: nauc_map_at_3_diff1
      value: 51.7018
    - type: nauc_map_at_5_max
      value: 36.999500000000005
    - type: nauc_map_at_5_std
      value: -2.7546999999999997
    - type: nauc_map_at_5_diff1
      value: 51.011300000000006
    - type: nauc_map_at_10_max
      value: 37.4157
    - type: nauc_map_at_10_std
      value: -1.9426999999999999
    - type: nauc_map_at_10_diff1
      value: 50.8876
    - type: nauc_map_at_20_max
      value: 37.729
    - type: nauc_map_at_20_std
      value: -1.3641999999999999
    - type: nauc_map_at_20_diff1
      value: 50.6926
    - type: nauc_map_at_100_max
      value: 37.7894
    - type: nauc_map_at_100_std
      value: -1.0082
    - type: nauc_map_at_100_diff1
      value: 50.6244
    - type: nauc_map_at_1000_max
      value: 37.8313
    - type: nauc_map_at_1000_std
      value: -0.9648
    - type: nauc_map_at_1000_diff1
      value: 50.6292
    - type: nauc_recall_at_1_max
      value: 33.9405
    - type: nauc_recall_at_1_std
      value: -3.9303999999999997
    - type: nauc_recall_at_1_diff1
      value: 55.7491
    - type: nauc_recall_at_3_max
      value: 35.6518
    - type: nauc_recall_at_3_std
      value: -3.166
    - type: nauc_recall_at_3_diff1
      value: 47.0684
    - type: nauc_recall_at_5_max
      value: 34.9043
    - type: nauc_recall_at_5_std
      value: -3.3676
    - type: nauc_recall_at_5_diff1
      value: 43.152499999999996
    - type: nauc_recall_at_10_max
      value: 35.2134
    - type: nauc_recall_at_10_std
      value: -1.0841
    - type: nauc_recall_at_10_diff1
      value: 41.1852
    - type: nauc_recall_at_20_max
      value: 37.417699999999996
    - type: nauc_recall_at_20_std
      value: 4.1923
    - type: nauc_recall_at_20_diff1
      value: 39.1819
    - type: nauc_recall_at_100_max
      value: 36.471900000000005
    - type: nauc_recall_at_100_std
      value: 19.8322
    - type: nauc_recall_at_100_diff1
      value: 34.0503
    - type: nauc_recall_at_1000_max
      value: 51.3256
    - type: nauc_recall_at_1000_std
      value: 46.2018
    - type: nauc_recall_at_1000_diff1
      value: 25.4702
    - type: nauc_precision_at_1_max
      value: 38.6678
    - type: nauc_precision_at_1_std
      value: -0.7451
    - type: nauc_precision_at_1_diff1
      value: 54.51089999999999
    - type: nauc_precision_at_3_max
      value: 39.763
    - type: nauc_precision_at_3_std
      value: 5.3316
    - type: nauc_precision_at_3_diff1
      value: 34.5965
    - type: nauc_precision_at_5_max
      value: 35.8709
    - type: nauc_precision_at_5_std
      value: 5.8021
    - type: nauc_precision_at_5_diff1
      value: 25.3427
    - type: nauc_precision_at_10_max
      value: 30.9008
    - type: nauc_precision_at_10_std
      value: 11.5405
    - type: nauc_precision_at_10_diff1
      value: 15.775
    - type: nauc_precision_at_20_max
      value: 28.403200000000002
    - type: nauc_precision_at_20_std
      value: 18.1899
    - type: nauc_precision_at_20_diff1
      value: 6.8557999999999995
    - type: nauc_precision_at_100_max
      value: 15.776499999999999
    - type: nauc_precision_at_100_std
      value: 21.5746
    - type: nauc_precision_at_100_diff1
      value: -7.0051000000000005
    - type: nauc_precision_at_1000_max
      value: 6.2587
    - type: nauc_precision_at_1000_std
      value: 18.0076
    - type: nauc_precision_at_1000_diff1
      value: -17.366400000000002
    - type: nauc_mrr_at_1_max
      value: 38.6678
    - type: nauc_mrr_at_1_std
      value: -0.7451
    - type: nauc_mrr_at_1_diff1
      value: 54.51089999999999
    - type: nauc_mrr_at_3_max
      value: 40.489399999999996
    - type: nauc_mrr_at_3_std
      value: -0.3225
    - type: nauc_mrr_at_3_diff1
      value: 51.41480000000001
    - type: nauc_mrr_at_5_max
      value: 40.1627
    - type: nauc_mrr_at_5_std
      value: -0.16219999999999998
    - type: nauc_mrr_at_5_diff1
      value: 50.560300000000005
    - type: nauc_mrr_at_10_max
      value: 40.125899999999994
    - type: nauc_mrr_at_10_std
      value: 0.0545
    - type: nauc_mrr_at_10_diff1
      value: 50.3771
    - type: nauc_mrr_at_20_max
      value: 40.2183
    - type: nauc_mrr_at_20_std
      value: 0.2818
    - type: nauc_mrr_at_20_diff1
      value: 50.387
    - type: nauc_mrr_at_100_max
      value: 40.201100000000004
    - type: nauc_mrr_at_100_std
      value: 0.43350000000000005
    - type: nauc_mrr_at_100_diff1
      value: 50.395100000000006
    - type: nauc_mrr_at_1000_max
      value: 40.2026
    - type: nauc_mrr_at_1000_std
      value: 0.42129999999999995
    - type: nauc_mrr_at_1000_diff1
      value: 50.405199999999994
    - type: main_score
      value: 48.542
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval (default)
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: ndcg_at_1
      value: 33.333
    - type: ndcg_at_3
      value: 39.431
    - type: ndcg_at_5
      value: 42.120000000000005
    - type: ndcg_at_10
      value: 44.968
    - type: ndcg_at_20
      value: 47.099000000000004
    - type: ndcg_at_100
      value: 50.288
    - type: ndcg_at_1000
      value: 52.371
    - type: map_at_1
      value: 27.087
    - type: map_at_3
      value: 35.203
    - type: map_at_5
      value: 37.230999999999995
    - type: map_at_10
      value: 38.693
    - type: map_at_20
      value: 39.425
    - type: map_at_100
      value: 40.001
    - type: map_at_1000
      value: 40.119
    - type: recall_at_1
      value: 27.087
    - type: recall_at_3
      value: 42.846000000000004
    - type: recall_at_5
      value: 49.846000000000004
    - type: recall_at_10
      value: 58.083
    - type: recall_at_20
      value: 65.615
    - type: recall_at_100
      value: 80.831
    - type: recall_at_1000
      value: 94.474
    - type: precision_at_1
      value: 33.333
    - type: precision_at_3
      value: 19.139999999999997
    - type: precision_at_5
      value: 13.858
    - type: precision_at_10
      value: 8.413
    - type: precision_at_20
      value: 4.926
    - type: precision_at_100
      value: 1.275
    - type: precision_at_1000
      value: 0.165
    - type: mrr_at_1
      value: 33.3333
    - type: mrr_at_3
      value: 41.0959
    - type: mrr_at_5
      value: 42.6826
    - type: mrr_at_10
      value: 43.819900000000004
    - type: mrr_at_20
      value: 44.3087
    - type: mrr_at_100
      value: 44.6693
    - type: mrr_at_1000
      value: 44.7164
    - type: nauc_ndcg_at_1_max
      value: 36.037
    - type: nauc_ndcg_at_1_std
      value: -0.2425
    - type: nauc_ndcg_at_1_diff1
      value: 46.9443
    - type: nauc_ndcg_at_3_max
      value: 33.5311
    - type: nauc_ndcg_at_3_std
      value: 1.2205000000000001
    - type: nauc_ndcg_at_3_diff1
      value: 38.8166
    - type: nauc_ndcg_at_5_max
      value: 34.3091
    - type: nauc_ndcg_at_5_std
      value: 2.8846
    - type: nauc_ndcg_at_5_diff1
      value: 38.222899999999996
    - type: nauc_ndcg_at_10_max
      value: 34.443400000000004
    - type: nauc_ndcg_at_10_std
      value: 3.5393
    - type: nauc_ndcg_at_10_diff1
      value: 37.9537
    - type: nauc_ndcg_at_20_max
      value: 34.929500000000004
    - type: nauc_ndcg_at_20_std
      value: 4.4444
    - type: nauc_ndcg_at_20_diff1
      value: 37.811099999999996
    - type: nauc_ndcg_at_100_max
      value: 35.6285
    - type: nauc_ndcg_at_100_std
      value: 6.356199999999999
    - type: nauc_ndcg_at_100_diff1
      value: 37.4749
    - type: nauc_ndcg_at_1000_max
      value: 35.8451
    - type: nauc_ndcg_at_1000_std
      value: 6.1044
    - type: nauc_ndcg_at_1000_diff1
      value: 38.5065
    - type: nauc_map_at_1_max
      value: 30.017100000000003
    - type: nauc_map_at_1_std
      value: -5.056299999999999
    - type: nauc_map_at_1_diff1
      value: 46.4338
    - type: nauc_map_at_3_max
      value: 31.936999999999998
    - type: nauc_map_at_3_std
      value: -1.0591
    - type: nauc_map_at_3_diff1
      value: 39.8778
    - type: nauc_map_at_5_max
      value: 32.859100000000005
    - type: nauc_map_at_5_std
      value: 0.42050000000000004
    - type: nauc_map_at_5_diff1
      value: 39.7368
    - type: nauc_map_at_10_max
      value: 33.042899999999996
    - type: nauc_map_at_10_std
      value: 0.8545
    - type: nauc_map_at_10_diff1
      value: 39.5713
    - type: nauc_map_at_20_max
      value: 33.3227
    - type: nauc_map_at_20_std
      value: 1.3109000000000002
    - type: nauc_map_at_20_diff1
      value: 39.5833
    - type: nauc_map_at_100_max
      value: 33.537
    - type: nauc_map_at_100_std
      value: 1.7505
    - type: nauc_map_at_100_diff1
      value: 39.6109
    - type: nauc_map_at_1000_max
      value: 33.578
    - type: nauc_map_at_1000_std
      value: 1.7679
    - type: nauc_map_at_1000_diff1
      value: 39.677299999999995
    - type: nauc_recall_at_1_max
      value: 30.017100000000003
    - type: nauc_recall_at_1_std
      value: -5.056299999999999
    - type: nauc_recall_at_1_diff1
      value: 46.4338
    - type: nauc_recall_at_3_max
      value: 31.3062
    - type: nauc_recall_at_3_std
      value: 1.6736
    - type: nauc_recall_at_3_diff1
      value: 32.743
    - type: nauc_recall_at_5_max
      value: 32.7338
    - type: nauc_recall_at_5_std
      value: 5.9388000000000005
    - type: nauc_recall_at_5_diff1
      value: 30.8784
    - type: nauc_recall_at_10_max
      value: 32.9312
    - type: nauc_recall_at_10_std
      value: 8.1993
    - type: nauc_recall_at_10_diff1
      value: 29.4248
    - type: nauc_recall_at_20_max
      value: 33.9206
    - type: nauc_recall_at_20_std
      value: 10.673
    - type: nauc_recall_at_20_diff1
      value: 27.377200000000002
    - type: nauc_recall_at_100_max
      value: 37.119
    - type: nauc_recall_at_100_std
      value: 24.6249
    - type: nauc_recall_at_100_diff1
      value: 19.403699999999997
    - type: nauc_recall_at_1000_max
      value: 52.2307
    - type: nauc_recall_at_1000_std
      value: 53.405199999999994
    - type: nauc_recall_at_1000_diff1
      value: 24.122799999999998
    - type: nauc_precision_at_1_max
      value: 36.037
    - type: nauc_precision_at_1_std
      value: -0.2425
    - type: nauc_precision_at_1_diff1
      value: 46.9443
    - type: nauc_precision_at_3_max
      value: 34.110600000000005
    - type: nauc_precision_at_3_std
      value: 8.7398
    - type: nauc_precision_at_3_diff1
      value: 27.441
    - type: nauc_precision_at_5_max
      value: 33.0042
    - type: nauc_precision_at_5_std
      value: 13.7932
    - type: nauc_precision_at_5_diff1
      value: 23.011300000000002
    - type: nauc_precision_at_10_max
      value: 28.8408
    - type: nauc_precision_at_10_std
      value: 14.4897
    - type: nauc_precision_at_10_diff1
      value: 18.0244
    - type: nauc_precision_at_20_max
      value: 25.5054
    - type: nauc_precision_at_20_std
      value: 16.5918
    - type: nauc_precision_at_20_diff1
      value: 14.665500000000002
    - type: nauc_precision_at_100_max
      value: 18.084400000000002
    - type: nauc_precision_at_100_std
      value: 20.7595
    - type: nauc_precision_at_100_diff1
      value: 6.2877
    - type: nauc_precision_at_1000_max
      value: 6.778099999999999
    - type: nauc_precision_at_1000_std
      value: 9.0734
    - type: nauc_precision_at_1000_diff1
      value: 5.6030999999999995
    - type: nauc_mrr_at_1_max
      value: 36.037
    - type: nauc_mrr_at_1_std
      value: -0.2425
    - type: nauc_mrr_at_1_diff1
      value: 46.9443
    - type: nauc_mrr_at_3_max
      value: 36.0423
    - type: nauc_mrr_at_3_std
      value: 3.0699
    - type: nauc_mrr_at_3_diff1
      value: 40.6527
    - type: nauc_mrr_at_5_max
      value: 36.3279
    - type: nauc_mrr_at_5_std
      value: 4.0948
    - type: nauc_mrr_at_5_diff1
      value: 40.1667
    - type: nauc_mrr_at_10_max
      value: 36.3884
    - type: nauc_mrr_at_10_std
      value: 4.5214
    - type: nauc_mrr_at_10_diff1
      value: 40.3499
    - type: nauc_mrr_at_20_max
      value: 36.3977
    - type: nauc_mrr_at_20_std
      value: 4.4357
    - type: nauc_mrr_at_20_diff1
      value: 40.342800000000004
    - type: nauc_mrr_at_100_max
      value: 36.422900000000006
    - type: nauc_mrr_at_100_std
      value: 4.501200000000001
    - type: nauc_mrr_at_100_diff1
      value: 40.3487
    - type: nauc_mrr_at_1000_max
      value: 36.4317
    - type: nauc_mrr_at_1000_std
      value: 4.4942
    - type: nauc_mrr_at_1000_diff1
      value: 40.3843
    - type: main_score
      value: 44.968
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: CQADupstackRetrieval_is_a_combined_dataset
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: main_score
      value: 42.51058333333334
    - type: ndcg_at_10
      value: 42.51058333333334
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval (default)
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: ndcg_at_1
      value: 28.066999999999997
    - type: ndcg_at_3
      value: 33.326
    - type: ndcg_at_5
      value: 35.432
    - type: ndcg_at_10
      value: 37.711
    - type: ndcg_at_20
      value: 39.377
    - type: ndcg_at_100
      value: 42.437999999999995
    - type: ndcg_at_1000
      value: 44.653999999999996
    - type: map_at_1
      value: 24.91
    - type: map_at_3
      value: 30.641000000000002
    - type: map_at_5
      value: 32.003
    - type: map_at_10
      value: 33.027
    - type: map_at_20
      value: 33.52
    - type: map_at_100
      value: 33.958
    - type: map_at_1000
      value: 34.048
    - type: recall_at_1
      value: 24.91
    - type: recall_at_3
      value: 36.931000000000004
    - type: recall_at_5
      value: 42.257
    - type: recall_at_10
      value: 49.248
    - type: recall_at_20
      value: 55.504
    - type: recall_at_100
      value: 71.086
    - type: recall_at_1000
      value: 87.209
    - type: precision_at_1
      value: 28.066999999999997
    - type: precision_at_3
      value: 14.571000000000002
    - type: precision_at_5
      value: 10.152999999999999
    - type: precision_at_10
      value: 5.982
    - type: precision_at_20
      value: 3.405
    - type: precision_at_100
      value: 0.903
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: mrr_at_1
      value: 28.067500000000003
    - type: mrr_at_3
      value: 33.8957
    - type: mrr_at_5
      value: 35.0997
    - type: mrr_at_10
      value: 36.0272
    - type: mrr_at_20
      value: 36.4454
    - type: mrr_at_100
      value: 36.8325
    - type: mrr_at_1000
      value: 36.8906
    - type: nauc_ndcg_at_1_max
      value: 41.64
    - type: nauc_ndcg_at_1_std
      value: -3.0991999999999997
    - type: nauc_ndcg_at_1_diff1
      value: 52.059
    - type: nauc_ndcg_at_3_max
      value: 38.3407
    - type: nauc_ndcg_at_3_std
      value: -2.0187
    - type: nauc_ndcg_at_3_diff1
      value: 44.6053
    - type: nauc_ndcg_at_5_max
      value: 39.5482
    - type: nauc_ndcg_at_5_std
      value: 0.6605
    - type: nauc_ndcg_at_5_diff1
      value: 44.1187
    - type: nauc_ndcg_at_10_max
      value: 40.2625
    - type: nauc_ndcg_at_10_std
      value: 1.6514999999999997
    - type: nauc_ndcg_at_10_diff1
      value: 43.170500000000004
    - type: nauc_ndcg_at_20_max
      value: 40.067
    - type: nauc_ndcg_at_20_std
      value: 2.1887
    - type: nauc_ndcg_at_20_diff1
      value: 42.8359
    - type: nauc_ndcg_at_100_max
      value: 41.749900000000004
    - type: nauc_ndcg_at_100_std
      value: 4.3462
    - type: nauc_ndcg_at_100_diff1
      value: 42.1422
    - type: nauc_ndcg_at_1000_max
      value: 41.4899
    - type: nauc_ndcg_at_1000_std
      value: 3.9956
    - type: nauc_ndcg_at_1000_diff1
      value: 42.4235
    - type: nauc_map_at_1_max
      value: 39.1049
    - type: nauc_map_at_1_std
      value: -7.072000000000001
    - type: nauc_map_at_1_diff1
      value: 53.76840000000001
    - type: nauc_map_at_3_max
      value: 38.3832
    - type: nauc_map_at_3_std
      value: -4.0869
    - type: nauc_map_at_3_diff1
      value: 46.848600000000005
    - type: nauc_map_at_5_max
      value: 39.4646
    - type: nauc_map_at_5_std
      value: -2.0288
    - type: nauc_map_at_5_diff1
      value: 46.3888
    - type: nauc_map_at_10_max
      value: 39.8593
    - type: nauc_map_at_10_std
      value: -1.4203000000000001
    - type: nauc_map_at_10_diff1
      value: 45.9306
    - type: nauc_map_at_20_max
      value: 39.835300000000004
    - type: nauc_map_at_20_std
      value: -1.2231
    - type: nauc_map_at_20_diff1
      value: 45.8283
    - type: nauc_map_at_100_max
      value: 40.1343
    - type: nauc_map_at_100_std
      value: -0.9245
    - type: nauc_map_at_100_diff1
      value: 45.7762
    - type: nauc_map_at_1000_max
      value: 40.1356
    - type: nauc_map_at_1000_std
      value: -0.9329000000000001
    - type: nauc_map_at_1000_diff1
      value: 45.785
    - type: nauc_recall_at_1_max
      value: 39.1049
    - type: nauc_recall_at_1_std
      value: -7.072000000000001
    - type: nauc_recall_at_1_diff1
      value: 53.76840000000001
    - type: nauc_recall_at_3_max
      value: 34.5115
    - type: nauc_recall_at_3_std
      value: -1.5186
    - type: nauc_recall_at_3_diff1
      value: 39.2881
    - type: nauc_recall_at_5_max
      value: 36.8705
    - type: nauc_recall_at_5_std
      value: 5.2115
    - type: nauc_recall_at_5_diff1
      value: 37.2112
    - type: nauc_recall_at_10_max
      value: 38.9486
    - type: nauc_recall_at_10_std
      value: 8.558
    - type: nauc_recall_at_10_diff1
      value: 34.027499999999996
    - type: nauc_recall_at_20_max
      value: 37.4174
    - type: nauc_recall_at_20_std
      value: 10.7121
    - type: nauc_recall_at_20_diff1
      value: 31.6372
    - type: nauc_recall_at_100_max
      value: 45.7135
    - type: nauc_recall_at_100_std
      value: 26.958900000000003
    - type: nauc_recall_at_100_diff1
      value: 22.6293
    - type: nauc_recall_at_1000_max
      value: 45.8455
    - type: nauc_recall_at_1000_std
      value: 41.8128
    - type: nauc_recall_at_1000_diff1
      value: 11.1735
    - type: nauc_precision_at_1_max
      value: 41.64
    - type: nauc_precision_at_1_std
      value: -3.0991999999999997
    - type: nauc_precision_at_1_diff1
      value: 52.059
    - type: nauc_precision_at_3_max
      value: 37.5109
    - type: nauc_precision_at_3_std
      value: 4.5869
    - type: nauc_precision_at_3_diff1
      value: 35.604200000000006
    - type: nauc_precision_at_5_max
      value: 39.441500000000005
    - type: nauc_precision_at_5_std
      value: 12.413499999999999
    - type: nauc_precision_at_5_diff1
      value: 31.566699999999997
    - type: nauc_precision_at_10_max
      value: 39.3943
    - type: nauc_precision_at_10_std
      value: 14.4375
    - type: nauc_precision_at_10_diff1
      value: 26.4044
    - type: nauc_precision_at_20_max
      value: 34.6082
    - type: nauc_precision_at_20_std
      value: 15.573899999999998
    - type: nauc_precision_at_20_diff1
      value: 21.3312
    - type: nauc_precision_at_100_max
      value: 33.6787
    - type: nauc_precision_at_100_std
      value: 24.4628
    - type: nauc_precision_at_100_diff1
      value: 9.238399999999999
    - type: nauc_precision_at_1000_max
      value: 15.7002
    - type: nauc_precision_at_1000_std
      value: 17.6244
    - type: nauc_precision_at_1000_diff1
      value: -2.8333
    - type: nauc_mrr_at_1_max
      value: 41.64
    - type: nauc_mrr_at_1_std
      value: -3.0991999999999997
    - type: nauc_mrr_at_1_diff1
      value: 52.059
    - type: nauc_mrr_at_3_max
      value: 40.2887
    - type: nauc_mrr_at_3_std
      value: -0.48650000000000004
    - type: nauc_mrr_at_3_diff1
      value: 46.2812
    - type: nauc_mrr_at_5_max
      value: 40.792899999999996
    - type: nauc_mrr_at_5_std
      value: 0.7635000000000001
    - type: nauc_mrr_at_5_diff1
      value: 45.8179
    - type: nauc_mrr_at_10_max
      value: 40.970099999999995
    - type: nauc_mrr_at_10_std
      value: 0.9508000000000001
    - type: nauc_mrr_at_10_diff1
      value: 45.4065
    - type: nauc_mrr_at_20_max
      value: 40.9322
    - type: nauc_mrr_at_20_std
      value: 1.0284
    - type: nauc_mrr_at_20_diff1
      value: 45.440999999999995
    - type: nauc_mrr_at_100_max
      value: 41.1209
    - type: nauc_mrr_at_100_std
      value: 1.2597
    - type: nauc_mrr_at_100_diff1
      value: 45.3654
    - type: nauc_mrr_at_1000_max
      value: 41.1143
    - type: nauc_mrr_at_1000_std
      value: 1.2467000000000001
    - type: nauc_mrr_at_1000_diff1
      value: 45.3792
    - type: main_score
      value: 37.711
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval (default)
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: ndcg_at_1
      value: 21.37
    - type: ndcg_at_3
      value: 25.308000000000003
    - type: ndcg_at_5
      value: 27.211999999999996
    - type: ndcg_at_10
      value: 29.759999999999998
    - type: ndcg_at_20
      value: 31.806
    - type: ndcg_at_100
      value: 35.148
    - type: ndcg_at_1000
      value: 38.115
    - type: map_at_1
      value: 17.635
    - type: map_at_3
      value: 22.537
    - type: map_at_5
      value: 23.834
    - type: map_at_10
      value: 24.984
    - type: map_at_20
      value: 25.613999999999997
    - type: map_at_100
      value: 26.125
    - type: map_at_1000
      value: 26.256
    - type: recall_at_1
      value: 17.635
    - type: recall_at_3
      value: 27.759
    - type: recall_at_5
      value: 32.688
    - type: recall_at_10
      value: 40.326
    - type: recall_at_20
      value: 47.865
    - type: recall_at_100
      value: 64.43799999999999
    - type: recall_at_1000
      value: 85.589
    - type: precision_at_1
      value: 21.37
    - type: precision_at_3
      value: 11.928999999999998
    - type: precision_at_5
      value: 8.679
    - type: precision_at_10
      value: 5.502
    - type: precision_at_20
      value: 3.345
    - type: precision_at_100
      value: 0.962
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: mrr_at_1
      value: 21.3696
    - type: mrr_at_3
      value: 26.4854
    - type: mrr_at_5
      value: 27.726
    - type: mrr_at_10
      value: 28.842499999999998
    - type: mrr_at_20
      value: 29.3902
    - type: mrr_at_100
      value: 29.7846
    - type: mrr_at_1000
      value: 29.860799999999998
    - type: nauc_ndcg_at_1_max
      value: 31.770300000000002
    - type: nauc_ndcg_at_1_std
      value: -4.784999999999999
    - type: nauc_ndcg_at_1_diff1
      value: 42.290499999999994
    - type: nauc_ndcg_at_3_max
      value: 31.1434
    - type: nauc_ndcg_at_3_std
      value: -2.8424
    - type: nauc_ndcg_at_3_diff1
      value: 36.7329
    - type: nauc_ndcg_at_5_max
      value: 31.1525
    - type: nauc_ndcg_at_5_std
      value: -2.2824
    - type: nauc_ndcg_at_5_diff1
      value: 35.517199999999995
    - type: nauc_ndcg_at_10_max
      value: 31.3549
    - type: nauc_ndcg_at_10_std
      value: -1.089
    - type: nauc_ndcg_at_10_diff1
      value: 34.9647
    - type: nauc_ndcg_at_20_max
      value: 31.3283
    - type: nauc_ndcg_at_20_std
      value: -0.5032
    - type: nauc_ndcg_at_20_diff1
      value: 34.73
    - type: nauc_ndcg_at_100_max
      value: 31.3324
    - type: nauc_ndcg_at_100_std
      value: 0.8308
    - type: nauc_ndcg_at_100_diff1
      value: 34.0739
    - type: nauc_ndcg_at_1000_max
      value: 31.563799999999997
    - type: nauc_ndcg_at_1000_std
      value: 1.0345
    - type: nauc_ndcg_at_1000_diff1
      value: 34.321400000000004
    - type: nauc_map_at_1_max
      value: 29.935299999999998
    - type: nauc_map_at_1_std
      value: -4.6685
    - type: nauc_map_at_1_diff1
      value: 43.6434
    - type: nauc_map_at_3_max
      value: 30.476
    - type: nauc_map_at_3_std
      value: -3.3331
    - type: nauc_map_at_3_diff1
      value: 38.6884
    - type: nauc_map_at_5_max
      value: 30.625200000000003
    - type: nauc_map_at_5_std
      value: -3.0722
    - type: nauc_map_at_5_diff1
      value: 37.845
    - type: nauc_map_at_10_max
      value: 30.8581
    - type: nauc_map_at_10_std
      value: -2.5201000000000002
    - type: nauc_map_at_10_diff1
      value: 37.5217
    - type: nauc_map_at_20_max
      value: 30.9267
    - type: nauc_map_at_20_std
      value: -2.3167
    - type: nauc_map_at_20_diff1
      value: 37.4216
    - type: nauc_map_at_100_max
      value: 31.0064
    - type: nauc_map_at_100_std
      value: -2.0629999999999997
    - type: nauc_map_at_100_diff1
      value: 37.3075
    - type: nauc_map_at_1000_max
      value: 31.0478
    - type: nauc_map_at_1000_std
      value: -2.0301
    - type: nauc_map_at_1000_diff1
      value: 37.3077
    - type: nauc_recall_at_1_max
      value: 29.935299999999998
    - type: nauc_recall_at_1_std
      value: -4.6685
    - type: nauc_recall_at_1_diff1
      value: 43.6434
    - type: nauc_recall_at_3_max
      value: 29.2327
    - type: nauc_recall_at_3_std
      value: -1.8466
    - type: nauc_recall_at_3_diff1
      value: 32.5214
    - type: nauc_recall_at_5_max
      value: 28.8576
    - type: nauc_recall_at_5_std
      value: -0.8358000000000001
    - type: nauc_recall_at_5_diff1
      value: 29.329499999999996
    - type: nauc_recall_at_10_max
      value: 28.8851
    - type: nauc_recall_at_10_std
      value: 2.3084000000000002
    - type: nauc_recall_at_10_diff1
      value: 27.3001
    - type: nauc_recall_at_20_max
      value: 28.0772
    - type: nauc_recall_at_20_std
      value: 4.2632
    - type: nauc_recall_at_20_diff1
      value: 25.6873
    - type: nauc_recall_at_100_max
      value: 27.4461
    - type: nauc_recall_at_100_std
      value: 11.9175
    - type: nauc_recall_at_100_diff1
      value: 20.7784
    - type: nauc_recall_at_1000_max
      value: 27.1262
    - type: nauc_recall_at_1000_std
      value: 24.4024
    - type: nauc_recall_at_1000_diff1
      value: 14.5445
    - type: nauc_precision_at_1_max
      value: 31.770300000000002
    - type: nauc_precision_at_1_std
      value: -4.784999999999999
    - type: nauc_precision_at_1_diff1
      value: 42.290499999999994
    - type: nauc_precision_at_3_max
      value: 32.5608
    - type: nauc_precision_at_3_std
      value: -1.3823999999999999
    - type: nauc_precision_at_3_diff1
      value: 30.9278
    - type: nauc_precision_at_5_max
      value: 32.0685
    - type: nauc_precision_at_5_std
      value: -0.2231
    - type: nauc_precision_at_5_diff1
      value: 26.8139
    - type: nauc_precision_at_10_max
      value: 31.8615
    - type: nauc_precision_at_10_std
      value: 3.3291
    - type: nauc_precision_at_10_diff1
      value: 22.608800000000002
    - type: nauc_precision_at_20_max
      value: 30.250799999999998
    - type: nauc_precision_at_20_std
      value: 5.242
    - type: nauc_precision_at_20_diff1
      value: 19.532
    - type: nauc_precision_at_100_max
      value: 25.2481
    - type: nauc_precision_at_100_std
      value: 9.711599999999999
    - type: nauc_precision_at_100_diff1
      value: 9.5108
    - type: nauc_precision_at_1000_max
      value: 19.072
    - type: nauc_precision_at_1000_std
      value: 9.0718
    - type: nauc_precision_at_1000_diff1
      value: -0.21090000000000003
    - type: nauc_mrr_at_1_max
      value: 31.770300000000002
    - type: nauc_mrr_at_1_std
      value: -4.784999999999999
    - type: nauc_mrr_at_1_diff1
      value: 42.290499999999994
    - type: nauc_mrr_at_3_max
      value: 31.5869
    - type: nauc_mrr_at_3_std
      value: -3.2058999999999997
    - type: nauc_mrr_at_3_diff1
      value: 37.3799
    - type: nauc_mrr_at_5_max
      value: 31.675199999999997
    - type: nauc_mrr_at_5_std
      value: -2.7127
    - type: nauc_mrr_at_5_diff1
      value: 36.5429
    - type: nauc_mrr_at_10_max
      value: 31.7662
    - type: nauc_mrr_at_10_std
      value: -2.314
    - type: nauc_mrr_at_10_diff1
      value: 36.3532
    - type: nauc_mrr_at_20_max
      value: 31.771300000000004
    - type: nauc_mrr_at_20_std
      value: -2.1448
    - type: nauc_mrr_at_20_diff1
      value: 36.3367
    - type: nauc_mrr_at_100_max
      value: 31.767899999999997
    - type: nauc_mrr_at_100_std
      value: -2.0333
    - type: nauc_mrr_at_100_diff1
      value: 36.2815
    - type: nauc_mrr_at_1000_max
      value: 31.7795
    - type: nauc_mrr_at_1000_std
      value: -2.0261
    - type: nauc_mrr_at_1000_diff1
      value: 36.2999
    - type: main_score
      value: 29.759999999999998
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval (default)
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: ndcg_at_1
      value: 33.302
    - type: ndcg_at_3
      value: 38.403
    - type: ndcg_at_5
      value: 40.319
    - type: ndcg_at_10
      value: 42.834
    - type: ndcg_at_20
      value: 44.932
    - type: ndcg_at_100
      value: 47.833
    - type: ndcg_at_1000
      value: 50.157
    - type: map_at_1
      value: 28.457
    - type: map_at_3
      value: 35.184
    - type: map_at_5
      value: 36.532
    - type: map_at_10
      value: 37.714
    - type: map_at_20
      value: 38.340999999999994
    - type: map_at_100
      value: 38.797
    - type: map_at_1000
      value: 38.903999999999996
    - type: recall_at_1
      value: 28.457
    - type: recall_at_3
      value: 41.937999999999995
    - type: recall_at_5
      value: 46.911
    - type: recall_at_10
      value: 54.303000000000004
    - type: recall_at_20
      value: 61.906000000000006
    - type: recall_at_100
      value: 76.074
    - type: recall_at_1000
      value: 92.191
    - type: precision_at_1
      value: 33.302
    - type: precision_at_3
      value: 17.382
    - type: precision_at_5
      value: 11.922
    - type: precision_at_10
      value: 7.08
    - type: precision_at_20
      value: 4.137
    - type: precision_at_100
      value: 1.064
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: mrr_at_1
      value: 33.3022
    - type: mrr_at_3
      value: 39.5056
    - type: mrr_at_5
      value: 40.7276
    - type: mrr_at_10
      value: 41.7227
    - type: mrr_at_20
      value: 42.270799999999994
    - type: mrr_at_100
      value: 42.5991
    - type: mrr_at_1000
      value: 42.653999999999996
    - type: nauc_ndcg_at_1_max
      value: 41.5343
    - type: nauc_ndcg_at_1_std
      value: -2.8242
    - type: nauc_ndcg_at_1_diff1
      value: 55.388099999999994
    - type: nauc_ndcg_at_3_max
      value: 41.531800000000004
    - type: nauc_ndcg_at_3_std
      value: -0.0958
    - type: nauc_ndcg_at_3_diff1
      value: 50.5951
    - type: nauc_ndcg_at_5_max
      value: 41.0756
    - type: nauc_ndcg_at_5_std
      value: 0.7116
    - type: nauc_ndcg_at_5_diff1
      value: 49.0397
    - type: nauc_ndcg_at_10_max
      value: 40.5656
    - type: nauc_ndcg_at_10_std
      value: 1.2275
    - type: nauc_ndcg_at_10_diff1
      value: 48.1935
    - type: nauc_ndcg_at_20_max
      value: 39.967000000000006
    - type: nauc_ndcg_at_20_std
      value: 1.2213
    - type: nauc_ndcg_at_20_diff1
      value: 47.5459
    - type: nauc_ndcg_at_100_max
      value: 40.2487
    - type: nauc_ndcg_at_100_std
      value: 2.6310000000000002
    - type: nauc_ndcg_at_100_diff1
      value: 47.3499
    - type: nauc_ndcg_at_1000_max
      value: 40.802
    - type: nauc_ndcg_at_1000_std
      value: 2.9029
    - type: nauc_ndcg_at_1000_diff1
      value: 47.893299999999996
    - type: nauc_map_at_1_max
      value: 40.0689
    - type: nauc_map_at_1_std
      value: -3.2761
    - type: nauc_map_at_1_diff1
      value: 56.685399999999994
    - type: nauc_map_at_3_max
      value: 41.350500000000004
    - type: nauc_map_at_3_std
      value: -0.6871999999999999
    - type: nauc_map_at_3_diff1
      value: 52.737100000000005
    - type: nauc_map_at_5_max
      value: 41.1119
    - type: nauc_map_at_5_std
      value: -0.23340000000000002
    - type: nauc_map_at_5_diff1
      value: 51.5269
    - type: nauc_map_at_10_max
      value: 40.860400000000006
    - type: nauc_map_at_10_std
      value: -0.08760000000000001
    - type: nauc_map_at_10_diff1
      value: 51.01369999999999
    - type: nauc_map_at_20_max
      value: 40.5859
    - type: nauc_map_at_20_std
      value: -0.154
    - type: nauc_map_at_20_diff1
      value: 50.744699999999995
    - type: nauc_map_at_100_max
      value: 40.646300000000004
    - type: nauc_map_at_100_std
      value: 0.10189999999999999
    - type: nauc_map_at_100_diff1
      value: 50.7085
    - type: nauc_map_at_1000_max
      value: 40.6731
    - type: nauc_map_at_1000_std
      value: 0.1394
    - type: nauc_map_at_1000_diff1
      value: 50.708
    - type: nauc_recall_at_1_max
      value: 40.0689
    - type: nauc_recall_at_1_std
      value: -3.2761
    - type: nauc_recall_at_1_diff1
      value: 56.685399999999994
    - type: nauc_recall_at_3_max
      value: 40.5338
    - type: nauc_recall_at_3_std
      value: 1.4996
    - type: nauc_recall_at_3_diff1
      value: 46.9882
    - type: nauc_recall_at_5_max
      value: 39.745999999999995
    - type: nauc_recall_at_5_std
      value: 3.7415
    - type: nauc_recall_at_5_diff1
      value: 42.7628
    - type: nauc_recall_at_10_max
      value: 37.6122
    - type: nauc_recall_at_10_std
      value: 5.1345
    - type: nauc_recall_at_10_diff1
      value: 39.2683
    - type: nauc_recall_at_20_max
      value: 34.9745
    - type: nauc_recall_at_20_std
      value: 5.7971
    - type: nauc_recall_at_20_diff1
      value: 35.6486
    - type: nauc_recall_at_100_max
      value: 35.1278
    - type: nauc_recall_at_100_std
      value: 16.569
    - type: nauc_recall_at_100_diff1
      value: 30.4082
    - type: nauc_recall_at_1000_max
      value: 48.1561
    - type: nauc_recall_at_1000_std
      value: 46.2123
    - type: nauc_recall_at_1000_diff1
      value: 28.9314
    - type: nauc_precision_at_1_max
      value: 41.5343
    - type: nauc_precision_at_1_std
      value: -2.8242
    - type: nauc_precision_at_1_diff1
      value: 55.388099999999994
    - type: nauc_precision_at_3_max
      value: 37.9897
    - type: nauc_precision_at_3_std
      value: 2.563
    - type: nauc_precision_at_3_diff1
      value: 37.253
    - type: nauc_precision_at_5_max
      value: 33.9735
    - type: nauc_precision_at_5_std
      value: 3.5601000000000003
    - type: nauc_precision_at_5_diff1
      value: 29.017300000000002
    - type: nauc_precision_at_10_max
      value: 27.8221
    - type: nauc_precision_at_10_std
      value: 4.3591999999999995
    - type: nauc_precision_at_10_diff1
      value: 20.7948
    - type: nauc_precision_at_20_max
      value: 21.0119
    - type: nauc_precision_at_20_std
      value: 4.4604
    - type: nauc_precision_at_20_diff1
      value: 12.5115
    - type: nauc_precision_at_100_max
      value: 11.1615
    - type: nauc_precision_at_100_std
      value: 10.1361
    - type: nauc_precision_at_100_diff1
      value: -2.5748
    - type: nauc_precision_at_1000_max
      value: -3.5173
    - type: nauc_precision_at_1000_std
      value: 6.248
    - type: nauc_precision_at_1000_diff1
      value: -17.6147
    - type: nauc_mrr_at_1_max
      value: 41.5343
    - type: nauc_mrr_at_1_std
      value: -2.8242
    - type: nauc_mrr_at_1_diff1
      value: 55.388099999999994
    - type: nauc_mrr_at_3_max
      value: 41.599199999999996
    - type: nauc_mrr_at_3_std
      value: -0.5716
    - type: nauc_mrr_at_3_diff1
      value: 50.932100000000005
    - type: nauc_mrr_at_5_max
      value: 41.2312
    - type: nauc_mrr_at_5_std
      value: -0.2443
    - type: nauc_mrr_at_5_diff1
      value: 49.9174
    - type: nauc_mrr_at_10_max
      value: 41.0053
    - type: nauc_mrr_at_10_std
      value: 0.0628
    - type: nauc_mrr_at_10_diff1
      value: 49.6375
    - type: nauc_mrr_at_20_max
      value: 40.930499999999995
    - type: nauc_mrr_at_20_std
      value: -0.063
    - type: nauc_mrr_at_20_diff1
      value: 49.6391
    - type: nauc_mrr_at_100_max
      value: 40.9473
    - type: nauc_mrr_at_100_std
      value: 0.0646
    - type: nauc_mrr_at_100_diff1
      value: 49.6701
    - type: nauc_mrr_at_1000_max
      value: 40.9676
    - type: nauc_mrr_at_1000_std
      value: 0.0838
    - type: nauc_mrr_at_1000_diff1
      value: 49.695299999999996
    - type: main_score
      value: 42.834
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: ndcg_at_1
      value: 32.411
    - type: ndcg_at_3
      value: 37.911
    - type: ndcg_at_5
      value: 39.983000000000004
    - type: ndcg_at_10
      value: 42.321999999999996
    - type: ndcg_at_20
      value: 44.855000000000004
    - type: ndcg_at_100
      value: 48.515
    - type: ndcg_at_1000
      value: 50.845
    - type: map_at_1
      value: 27.062
    - type: map_at_3
      value: 33.689
    - type: map_at_5
      value: 35.161
    - type: map_at_10
      value: 36.492000000000004
    - type: map_at_20
      value: 37.486999999999995
    - type: map_at_100
      value: 38.235
    - type: map_at_1000
      value: 38.421
    - type: recall_at_1
      value: 27.062
    - type: recall_at_3
      value: 40.459
    - type: recall_at_5
      value: 46.221000000000004
    - type: recall_at_10
      value: 53.348
    - type: recall_at_20
      value: 62.852
    - type: recall_at_100
      value: 80.582
    - type: recall_at_1000
      value: 95.14099999999999
    - type: precision_at_1
      value: 32.411
    - type: precision_at_3
      value: 17.984
    - type: precision_at_5
      value: 12.767000000000001
    - type: precision_at_10
      value: 7.945
    - type: precision_at_20
      value: 5.0
    - type: precision_at_100
      value: 1.534
    - type: precision_at_1000
      value: 0.234
    - type: mrr_at_1
      value: 32.4111
    - type: mrr_at_3
      value: 38.8011
    - type: mrr_at_5
      value: 40.2437
    - type: mrr_at_10
      value: 41.1494
    - type: mrr_at_20
      value: 41.8962
    - type: mrr_at_100
      value: 42.275800000000004
    - type: mrr_at_1000
      value: 42.3273
    - type: nauc_ndcg_at_1_max
      value: 27.961799999999997
    - type: nauc_ndcg_at_1_std
      value: 1.9207999999999998
    - type: nauc_ndcg_at_1_diff1
      value: 47.9837
    - type: nauc_ndcg_at_3_max
      value: 28.009099999999997
    - type: nauc_ndcg_at_3_std
      value: 1.212
    - type: nauc_ndcg_at_3_diff1
      value: 42.1361
    - type: nauc_ndcg_at_5_max
      value: 27.304299999999998
    - type: nauc_ndcg_at_5_std
      value: 1.4559
    - type: nauc_ndcg_at_5_diff1
      value: 40.8799
    - type: nauc_ndcg_at_10_max
      value: 26.0726
    - type: nauc_ndcg_at_10_std
      value: 1.5731
    - type: nauc_ndcg_at_10_diff1
      value: 38.9119
    - type: nauc_ndcg_at_20_max
      value: 28.139799999999997
    - type: nauc_ndcg_at_20_std
      value: 3.0962
    - type: nauc_ndcg_at_20_diff1
      value: 39.0918
    - type: nauc_ndcg_at_100_max
      value: 29.0945
    - type: nauc_ndcg_at_100_std
      value: 5.6239
    - type: nauc_ndcg_at_100_diff1
      value: 39.4526
    - type: nauc_ndcg_at_1000_max
      value: 28.7139
    - type: nauc_ndcg_at_1000_std
      value: 4.3576
    - type: nauc_ndcg_at_1000_diff1
      value: 40.1353
    - type: nauc_map_at_1_max
      value: 26.4001
    - type: nauc_map_at_1_std
      value: -2.4035
    - type: nauc_map_at_1_diff1
      value: 50.6355
    - type: nauc_map_at_3_max
      value: 27.6775
    - type: nauc_map_at_3_std
      value: -1.2323
    - type: nauc_map_at_3_diff1
      value: 45.1028
    - type: nauc_map_at_5_max
      value: 27.7501
    - type: nauc_map_at_5_std
      value: -1.0206
    - type: nauc_map_at_5_diff1
      value: 44.137100000000004
    - type: nauc_map_at_10_max
      value: 27.3169
    - type: nauc_map_at_10_std
      value: -0.6242
    - type: nauc_map_at_10_diff1
      value: 42.992799999999995
    - type: nauc_map_at_20_max
      value: 27.9088
    - type: nauc_map_at_20_std
      value: 0.369
    - type: nauc_map_at_20_diff1
      value: 42.7076
    - type: nauc_map_at_100_max
      value: 28.0018
    - type: nauc_map_at_100_std
      value: 1.0477999999999998
    - type: nauc_map_at_100_diff1
      value: 42.663000000000004
    - type: nauc_map_at_1000_max
      value: 27.8892
    - type: nauc_map_at_1000_std
      value: 1.0114
    - type: nauc_map_at_1000_diff1
      value: 42.6802
    - type: nauc_recall_at_1_max
      value: 26.4001
    - type: nauc_recall_at_1_std
      value: -2.4035
    - type: nauc_recall_at_1_diff1
      value: 50.6355
    - type: nauc_recall_at_3_max
      value: 26.4415
    - type: nauc_recall_at_3_std
      value: 0.6093000000000001
    - type: nauc_recall_at_3_diff1
      value: 38.3001
    - type: nauc_recall_at_5_max
      value: 25.5757
    - type: nauc_recall_at_5_std
      value: 1.7046999999999999
    - type: nauc_recall_at_5_diff1
      value: 33.9953
    - type: nauc_recall_at_10_max
      value: 21.9077
    - type: nauc_recall_at_10_std
      value: 2.4832
    - type: nauc_recall_at_10_diff1
      value: 27.6569
    - type: nauc_recall_at_20_max
      value: 27.9785
    - type: nauc_recall_at_20_std
      value: 8.717
    - type: nauc_recall_at_20_diff1
      value: 26.076
    - type: nauc_recall_at_100_max
      value: 32.8372
    - type: nauc_recall_at_100_std
      value: 28.644799999999996
    - type: nauc_recall_at_100_diff1
      value: 22.3344
    - type: nauc_recall_at_1000_max
      value: 43.087199999999996
    - type: nauc_recall_at_1000_std
      value: 38.6013
    - type: nauc_recall_at_1000_diff1
      value: 19.057399999999998
    - type: nauc_precision_at_1_max
      value: 27.961799999999997
    - type: nauc_precision_at_1_std
      value: 1.9207999999999998
    - type: nauc_precision_at_1_diff1
      value: 47.9837
    - type: nauc_precision_at_3_max
      value: 26.680999999999997
    - type: nauc_precision_at_3_std
      value: 6.4623
    - type: nauc_precision_at_3_diff1
      value: 26.0754
    - type: nauc_precision_at_5_max
      value: 23.0766
    - type: nauc_precision_at_5_std
      value: 8.0635
    - type: nauc_precision_at_5_diff1
      value: 18.249399999999998
    - type: nauc_precision_at_10_max
      value: 14.0187
    - type: nauc_precision_at_10_std
      value: 10.793999999999999
    - type: nauc_precision_at_10_diff1
      value: 5.7888
    - type: nauc_precision_at_20_max
      value: 12.065
    - type: nauc_precision_at_20_std
      value: 15.728800000000001
    - type: nauc_precision_at_20_diff1
      value: -0.7351
    - type: nauc_precision_at_100_max
      value: -0.4148
    - type: nauc_precision_at_100_std
      value: 17.0201
    - type: nauc_precision_at_100_diff1
      value: -8.088099999999999
    - type: nauc_precision_at_1000_max
      value: -18.342
    - type: nauc_precision_at_1000_std
      value: 5.6757
    - type: nauc_precision_at_1000_diff1
      value: -13.869200000000001
    - type: nauc_mrr_at_1_max
      value: 27.961799999999997
    - type: nauc_mrr_at_1_std
      value: 1.9207999999999998
    - type: nauc_mrr_at_1_diff1
      value: 47.9837
    - type: nauc_mrr_at_3_max
      value: 27.7754
    - type: nauc_mrr_at_3_std
      value: 2.2727
    - type: nauc_mrr_at_3_diff1
      value: 42.864999999999995
    - type: nauc_mrr_at_5_max
      value: 27.7453
    - type: nauc_mrr_at_5_std
      value: 2.7718
    - type: nauc_mrr_at_5_diff1
      value: 41.9633
    - type: nauc_mrr_at_10_max
      value: 27.308300000000003
    - type: nauc_mrr_at_10_std
      value: 3.089
    - type: nauc_mrr_at_10_diff1
      value: 41.3641
    - type: nauc_mrr_at_20_max
      value: 27.814299999999996
    - type: nauc_mrr_at_20_std
      value: 3.2985
    - type: nauc_mrr_at_20_diff1
      value: 41.6228
    - type: nauc_mrr_at_100_max
      value: 27.8378
    - type: nauc_mrr_at_100_std
      value: 3.517
    - type: nauc_mrr_at_100_diff1
      value: 41.7328
    - type: nauc_mrr_at_1000_max
      value: 27.8277
    - type: nauc_mrr_at_1000_std
      value: 3.4743000000000004
    - type: nauc_mrr_at_1000_diff1
      value: 41.7584
    - type: main_score
      value: 42.321999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval (default)
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: ndcg_at_1
      value: 23.105
    - type: ndcg_at_3
      value: 28.781000000000002
    - type: ndcg_at_5
      value: 31.338
    - type: ndcg_at_10
      value: 34.091
    - type: ndcg_at_20
      value: 36.046
    - type: ndcg_at_100
      value: 39.556999999999995
    - type: ndcg_at_1000
      value: 41.647
    - type: map_at_1
      value: 21.448
    - type: map_at_3
      value: 26.527
    - type: map_at_5
      value: 28.02
    - type: map_at_10
      value: 29.204
    - type: map_at_20
      value: 29.774
    - type: map_at_100
      value: 30.278
    - type: map_at_1000
      value: 30.364
    - type: recall_at_1
      value: 21.448
    - type: recall_at_3
      value: 33.167
    - type: recall_at_5
      value: 39.156
    - type: recall_at_10
      value: 47.277
    - type: recall_at_20
      value: 54.639
    - type: recall_at_100
      value: 72.809
    - type: recall_at_1000
      value: 88.099
    - type: precision_at_1
      value: 23.105
    - type: precision_at_3
      value: 12.138
    - type: precision_at_5
      value: 8.834999999999999
    - type: precision_at_10
      value: 5.434
    - type: precision_at_20
      value: 3.189
    - type: precision_at_100
      value: 0.8710000000000001
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: mrr_at_1
      value: 23.1054
    - type: mrr_at_3
      value: 28.5582
    - type: mrr_at_5
      value: 30.0462
    - type: mrr_at_10
      value: 31.1854
    - type: mrr_at_20
      value: 31.6775
    - type: mrr_at_100
      value: 32.1183
    - type: mrr_at_1000
      value: 32.1723
    - type: nauc_ndcg_at_1_max
      value: 30.894
    - type: nauc_ndcg_at_1_std
      value: 0.8228
    - type: nauc_ndcg_at_1_diff1
      value: 50.571600000000004
    - type: nauc_ndcg_at_3_max
      value: 24.9603
    - type: nauc_ndcg_at_3_std
      value: -0.3032
    - type: nauc_ndcg_at_3_diff1
      value: 43.803799999999995
    - type: nauc_ndcg_at_5_max
      value: 26.1479
    - type: nauc_ndcg_at_5_std
      value: 0.3038
    - type: nauc_ndcg_at_5_diff1
      value: 42.5296
    - type: nauc_ndcg_at_10_max
      value: 26.0992
    - type: nauc_ndcg_at_10_std
      value: 1.2644
    - type: nauc_ndcg_at_10_diff1
      value: 41.943000000000005
    - type: nauc_ndcg_at_20_max
      value: 26.132300000000004
    - type: nauc_ndcg_at_20_std
      value: 1.798
    - type: nauc_ndcg_at_20_diff1
      value: 41.1586
    - type: nauc_ndcg_at_100_max
      value: 26.4048
    - type: nauc_ndcg_at_100_std
      value: 3.7023
    - type: nauc_ndcg_at_100_diff1
      value: 41.3297
    - type: nauc_ndcg_at_1000_max
      value: 26.889200000000002
    - type: nauc_ndcg_at_1000_std
      value: 3.7087000000000003
    - type: nauc_ndcg_at_1000_diff1
      value: 41.716300000000004
    - type: nauc_map_at_1_max
      value: 27.5981
    - type: nauc_map_at_1_std
      value: 0.387
    - type: nauc_map_at_1_diff1
      value: 48.6362
    - type: nauc_map_at_3_max
      value: 24.8521
    - type: nauc_map_at_3_std
      value: -0.414
    - type: nauc_map_at_3_diff1
      value: 44.766600000000004
    - type: nauc_map_at_5_max
      value: 25.937900000000003
    - type: nauc_map_at_5_std
      value: -0.054900000000000004
    - type: nauc_map_at_5_diff1
      value: 44.0302
    - type: nauc_map_at_10_max
      value: 26.018
    - type: nauc_map_at_10_std
      value: 0.3584
    - type: nauc_map_at_10_diff1
      value: 43.7009
    - type: nauc_map_at_20_max
      value: 26.0129
    - type: nauc_map_at_20_std
      value: 0.5091
    - type: nauc_map_at_20_diff1
      value: 43.4823
    - type: nauc_map_at_100_max
      value: 26.1059
    - type: nauc_map_at_100_std
      value: 0.7867999999999999
    - type: nauc_map_at_100_diff1
      value: 43.4867
    - type: nauc_map_at_1000_max
      value: 26.131500000000003
    - type: nauc_map_at_1000_std
      value: 0.8026
    - type: nauc_map_at_1000_diff1
      value: 43.5097
    - type: nauc_recall_at_1_max
      value: 27.5981
    - type: nauc_recall_at_1_std
      value: 0.387
    - type: nauc_recall_at_1_diff1
      value: 48.6362
    - type: nauc_recall_at_3_max
      value: 21.7315
    - type: nauc_recall_at_3_std
      value: -1.0671
    - type: nauc_recall_at_3_diff1
      value: 39.4999
    - type: nauc_recall_at_5_max
      value: 23.994699999999998
    - type: nauc_recall_at_5_std
      value: 0.0779
    - type: nauc_recall_at_5_diff1
      value: 36.9505
    - type: nauc_recall_at_10_max
      value: 23.2468
    - type: nauc_recall_at_10_std
      value: 2.654
    - type: nauc_recall_at_10_diff1
      value: 35.158899999999996
    - type: nauc_recall_at_20_max
      value: 23.28
    - type: nauc_recall_at_20_std
      value: 4.8041
    - type: nauc_recall_at_20_diff1
      value: 31.547399999999996
    - type: nauc_recall_at_100_max
      value: 21.7186
    - type: nauc_recall_at_100_std
      value: 17.083000000000002
    - type: nauc_recall_at_100_diff1
      value: 29.229899999999997
    - type: nauc_recall_at_1000_max
      value: 28.9168
    - type: nauc_recall_at_1000_std
      value: 29.9591
    - type: nauc_recall_at_1000_diff1
      value: 27.0436
    - type: nauc_precision_at_1_max
      value: 30.894
    - type: nauc_precision_at_1_std
      value: 0.8228
    - type: nauc_precision_at_1_diff1
      value: 50.571600000000004
    - type: nauc_precision_at_3_max
      value: 25.076999999999998
    - type: nauc_precision_at_3_std
      value: 0.39890000000000003
    - type: nauc_precision_at_3_diff1
      value: 40.618300000000005
    - type: nauc_precision_at_5_max
      value: 29.274299999999997
    - type: nauc_precision_at_5_std
      value: 3.02
    - type: nauc_precision_at_5_diff1
      value: 35.3233
    - type: nauc_precision_at_10_max
      value: 28.1411
    - type: nauc_precision_at_10_std
      value: 6.628100000000001
    - type: nauc_precision_at_10_diff1
      value: 30.949700000000004
    - type: nauc_precision_at_20_max
      value: 25.974999999999998
    - type: nauc_precision_at_20_std
      value: 8.3134
    - type: nauc_precision_at_20_diff1
      value: 25.324799999999996
    - type: nauc_precision_at_100_max
      value: 22.682
    - type: nauc_precision_at_100_std
      value: 20.4648
    - type: nauc_precision_at_100_diff1
      value: 13.2139
    - type: nauc_precision_at_1000_max
      value: 2.8796
    - type: nauc_precision_at_1000_std
      value: 10.6158
    - type: nauc_precision_at_1000_diff1
      value: -11.8614
    - type: nauc_mrr_at_1_max
      value: 30.894
    - type: nauc_mrr_at_1_std
      value: 0.8228
    - type: nauc_mrr_at_1_diff1
      value: 50.571600000000004
    - type: nauc_mrr_at_3_max
      value: 27.8993
    - type: nauc_mrr_at_3_std
      value: 0.5541
    - type: nauc_mrr_at_3_diff1
      value: 46.307900000000004
    - type: nauc_mrr_at_5_max
      value: 28.4404
    - type: nauc_mrr_at_5_std
      value: 0.8992
    - type: nauc_mrr_at_5_diff1
      value: 45.405699999999996
    - type: nauc_mrr_at_10_max
      value: 28.492099999999997
    - type: nauc_mrr_at_10_std
      value: 1.3769
    - type: nauc_mrr_at_10_diff1
      value: 45.163
    - type: nauc_mrr_at_20_max
      value: 28.4509
    - type: nauc_mrr_at_20_std
      value: 1.4745
    - type: nauc_mrr_at_20_diff1
      value: 44.9459
    - type: nauc_mrr_at_100_max
      value: 28.533199999999997
    - type: nauc_mrr_at_100_std
      value: 1.7016
    - type: nauc_mrr_at_100_diff1
      value: 45.0053
    - type: nauc_mrr_at_1000_max
      value: 28.5364
    - type: nauc_mrr_at_1000_std
      value: 1.6894
    - type: nauc_mrr_at_1000_diff1
      value: 45.0407
    - type: main_score
      value: 34.091
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER (default)
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: ndcg_at_1
      value: 32.964
    - type: ndcg_at_3
      value: 28.116000000000003
    - type: ndcg_at_5
      value: 29.932
    - type: ndcg_at_10
      value: 33.207
    - type: ndcg_at_20
      value: 35.730000000000004
    - type: ndcg_at_100
      value: 40.251999999999995
    - type: ndcg_at_1000
      value: 43.463
    - type: map_at_1
      value: 14.846
    - type: map_at_3
      value: 20.683
    - type: map_at_5
      value: 22.753999999999998
    - type: map_at_10
      value: 24.413
    - type: map_at_20
      value: 25.355
    - type: map_at_100
      value: 26.243
    - type: map_at_1000
      value: 26.43
    - type: recall_at_1
      value: 14.846
    - type: recall_at_3
      value: 25.368000000000002
    - type: recall_at_5
      value: 31.159
    - type: recall_at_10
      value: 38.391
    - type: recall_at_20
      value: 45.366
    - type: recall_at_100
      value: 62.597
    - type: recall_at_1000
      value: 80.448
    - type: precision_at_1
      value: 32.964
    - type: precision_at_3
      value: 20.782
    - type: precision_at_5
      value: 15.595999999999998
    - type: precision_at_10
      value: 9.98
    - type: precision_at_20
      value: 6.091
    - type: precision_at_100
      value: 1.7760000000000002
    - type: precision_at_1000
      value: 0.23700000000000002
    - type: mrr_at_1
      value: 32.9642
    - type: mrr_at_3
      value: 41.9001
    - type: mrr_at_5
      value: 43.4701
    - type: mrr_at_10
      value: 44.6392
    - type: mrr_at_20
      value: 45.129999999999995
    - type: mrr_at_100
      value: 45.4343
    - type: mrr_at_1000
      value: 45.4726
    - type: nauc_ndcg_at_1_max
      value: 31.2733
    - type: nauc_ndcg_at_1_std
      value: 17.8778
    - type: nauc_ndcg_at_1_diff1
      value: 30.7939
    - type: nauc_ndcg_at_3_max
      value: 35.7233
    - type: nauc_ndcg_at_3_std
      value: 20.499200000000002
    - type: nauc_ndcg_at_3_diff1
      value: 26.6175
    - type: nauc_ndcg_at_5_max
      value: 36.5593
    - type: nauc_ndcg_at_5_std
      value: 20.5487
    - type: nauc_ndcg_at_5_diff1
      value: 24.8006
    - type: nauc_ndcg_at_10_max
      value: 38.1663
    - type: nauc_ndcg_at_10_std
      value: 23.8688
    - type: nauc_ndcg_at_10_diff1
      value: 23.7262
    - type: nauc_ndcg_at_20_max
      value: 38.719
    - type: nauc_ndcg_at_20_std
      value: 26.4556
    - type: nauc_ndcg_at_20_diff1
      value: 22.7078
    - type: nauc_ndcg_at_100_max
      value: 40.396100000000004
    - type: nauc_ndcg_at_100_std
      value: 29.325200000000002
    - type: nauc_ndcg_at_100_diff1
      value: 22.7562
    - type: nauc_ndcg_at_1000_max
      value: 40.4082
    - type: nauc_ndcg_at_1000_std
      value: 29.595
    - type: nauc_ndcg_at_1000_diff1
      value: 22.8439
    - type: nauc_map_at_1_max
      value: 33.0891
    - type: nauc_map_at_1_std
      value: 13.3677
    - type: nauc_map_at_1_diff1
      value: 34.1515
    - type: nauc_map_at_3_max
      value: 35.384
    - type: nauc_map_at_3_std
      value: 17.637
    - type: nauc_map_at_3_diff1
      value: 28.4007
    - type: nauc_map_at_5_max
      value: 36.0659
    - type: nauc_map_at_5_std
      value: 18.5628
    - type: nauc_map_at_5_diff1
      value: 26.5464
    - type: nauc_map_at_10_max
      value: 37.2578
    - type: nauc_map_at_10_std
      value: 20.617
    - type: nauc_map_at_10_diff1
      value: 25.926199999999998
    - type: nauc_map_at_20_max
      value: 37.500299999999996
    - type: nauc_map_at_20_std
      value: 21.851300000000002
    - type: nauc_map_at_20_diff1
      value: 25.3292
    - type: nauc_map_at_100_max
      value: 37.933299999999996
    - type: nauc_map_at_100_std
      value: 22.6615
    - type: nauc_map_at_100_diff1
      value: 25.259500000000003
    - type: nauc_map_at_1000_max
      value: 37.9165
    - type: nauc_map_at_1000_std
      value: 22.7028
    - type: nauc_map_at_1000_diff1
      value: 25.239299999999997
    - type: nauc_recall_at_1_max
      value: 33.0891
    - type: nauc_recall_at_1_std
      value: 13.3677
    - type: nauc_recall_at_1_diff1
      value: 34.1515
    - type: nauc_recall_at_3_max
      value: 35.282000000000004
    - type: nauc_recall_at_3_std
      value: 18.8367
    - type: nauc_recall_at_3_diff1
      value: 24.2501
    - type: nauc_recall_at_5_max
      value: 34.3122
    - type: nauc_recall_at_5_std
      value: 18.5093
    - type: nauc_recall_at_5_diff1
      value: 18.8749
    - type: nauc_recall_at_10_max
      value: 36.2395
    - type: nauc_recall_at_10_std
      value: 24.2952
    - type: nauc_recall_at_10_diff1
      value: 16.3158
    - type: nauc_recall_at_20_max
      value: 35.6255
    - type: nauc_recall_at_20_std
      value: 29.56
    - type: nauc_recall_at_20_diff1
      value: 12.856699999999998
    - type: nauc_recall_at_100_max
      value: 39.016600000000004
    - type: nauc_recall_at_100_std
      value: 37.9984
    - type: nauc_recall_at_100_diff1
      value: 10.807
    - type: nauc_recall_at_1000_max
      value: 42.7582
    - type: nauc_recall_at_1000_std
      value: 46.9593
    - type: nauc_recall_at_1000_diff1
      value: 8.1464
    - type: nauc_precision_at_1_max
      value: 31.2733
    - type: nauc_precision_at_1_std
      value: 17.8778
    - type: nauc_precision_at_1_diff1
      value: 30.7939
    - type: nauc_precision_at_3_max
      value: 35.2819
    - type: nauc_precision_at_3_std
      value: 25.9018
    - type: nauc_precision_at_3_diff1
      value: 18.4633
    - type: nauc_precision_at_5_max
      value: 32.7525
    - type: nauc_precision_at_5_std
      value: 25.5596
    - type: nauc_precision_at_5_diff1
      value: 11.241
    - type: nauc_precision_at_10_max
      value: 32.4574
    - type: nauc_precision_at_10_std
      value: 31.1815
    - type: nauc_precision_at_10_diff1
      value: 6.3983
    - type: nauc_precision_at_20_max
      value: 29.522100000000002
    - type: nauc_precision_at_20_std
      value: 34.4644
    - type: nauc_precision_at_20_diff1
      value: 1.9328
    - type: nauc_precision_at_100_max
      value: 25.594299999999997
    - type: nauc_precision_at_100_std
      value: 36.7783
    - type: nauc_precision_at_100_diff1
      value: -1.9514
    - type: nauc_precision_at_1000_max
      value: 14.3931
    - type: nauc_precision_at_1000_std
      value: 28.8585
    - type: nauc_precision_at_1000_diff1
      value: -7.264600000000001
    - type: nauc_mrr_at_1_max
      value: 31.2733
    - type: nauc_mrr_at_1_std
      value: 17.8778
    - type: nauc_mrr_at_1_diff1
      value: 30.7939
    - type: nauc_mrr_at_3_max
      value: 34.4613
    - type: nauc_mrr_at_3_std
      value: 21.529
    - type: nauc_mrr_at_3_diff1
      value: 27.369
    - type: nauc_mrr_at_5_max
      value: 34.5965
    - type: nauc_mrr_at_5_std
      value: 21.7303
    - type: nauc_mrr_at_5_diff1
      value: 26.521800000000002
    - type: nauc_mrr_at_10_max
      value: 34.6792
    - type: nauc_mrr_at_10_std
      value: 22.4157
    - type: nauc_mrr_at_10_diff1
      value: 26.2542
    - type: nauc_mrr_at_20_max
      value: 34.746
    - type: nauc_mrr_at_20_std
      value: 22.586000000000002
    - type: nauc_mrr_at_20_diff1
      value: 26.305600000000002
    - type: nauc_mrr_at_100_max
      value: 34.7901
    - type: nauc_mrr_at_100_std
      value: 22.5625
    - type: nauc_mrr_at_100_diff1
      value: 26.429599999999997
    - type: nauc_mrr_at_1000_max
      value: 34.779700000000005
    - type: nauc_mrr_at_1000_std
      value: 22.5434
    - type: nauc_mrr_at_1000_diff1
      value: 26.437300000000004
    - type: main_score
      value: 33.207
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: ndcg_at_1
      value: 51.87500000000001
    - type: ndcg_at_3
      value: 42.552
    - type: ndcg_at_5
      value: 39.946
    - type: ndcg_at_10
      value: 37.897999999999996
    - type: ndcg_at_20
      value: 37.153000000000006
    - type: ndcg_at_100
      value: 42.012
    - type: ndcg_at_1000
      value: 49.202
    - type: map_at_1
      value: 7.869
    - type: map_at_3
      value: 12.307
    - type: map_at_5
      value: 14.394000000000002
    - type: map_at_10
      value: 17.175
    - type: map_at_20
      value: 19.689
    - type: map_at_100
      value: 23.857999999999997
    - type: map_at_1000
      value: 25.417
    - type: recall_at_1
      value: 7.869
    - type: recall_at_3
      value: 13.566
    - type: recall_at_5
      value: 17.403
    - type: recall_at_10
      value: 22.811999999999998
    - type: recall_at_20
      value: 29.378999999999998
    - type: recall_at_100
      value: 48.353
    - type: recall_at_1000
      value: 70.801
    - type: precision_at_1
      value: 62.5
    - type: precision_at_3
      value: 45.417
    - type: precision_at_5
      value: 38.15
    - type: precision_at_10
      value: 29.95
    - type: precision_at_20
      value: 22.462
    - type: precision_at_100
      value: 9.703000000000001
    - type: precision_at_1000
      value: 2.027
    - type: mrr_at_1
      value: 62.5
    - type: mrr_at_3
      value: 68.625
    - type: mrr_at_5
      value: 70.0625
    - type: mrr_at_10
      value: 70.60549999999999
    - type: mrr_at_20
      value: 70.934
    - type: mrr_at_100
      value: 71.0742
    - type: mrr_at_1000
      value: 71.0797
    - type: nauc_ndcg_at_1_max
      value: 41.436499999999995
    - type: nauc_ndcg_at_1_std
      value: 26.6537
    - type: nauc_ndcg_at_1_diff1
      value: 41.362500000000004
    - type: nauc_ndcg_at_3_max
      value: 38.2075
    - type: nauc_ndcg_at_3_std
      value: 28.1899
    - type: nauc_ndcg_at_3_diff1
      value: 29.353299999999997
    - type: nauc_ndcg_at_5_max
      value: 36.592
    - type: nauc_ndcg_at_5_std
      value: 27.9763
    - type: nauc_ndcg_at_5_diff1
      value: 30.2168
    - type: nauc_ndcg_at_10_max
      value: 36.2032
    - type: nauc_ndcg_at_10_std
      value: 26.7501
    - type: nauc_ndcg_at_10_diff1
      value: 33.409499999999994
    - type: nauc_ndcg_at_20_max
      value: 33.981
    - type: nauc_ndcg_at_20_std
      value: 25.5934
    - type: nauc_ndcg_at_20_diff1
      value: 33.3985
    - type: nauc_ndcg_at_100_max
      value: 36.448
    - type: nauc_ndcg_at_100_std
      value: 32.3459
    - type: nauc_ndcg_at_100_diff1
      value: 33.2002
    - type: nauc_ndcg_at_1000_max
      value: 40.2408
    - type: nauc_ndcg_at_1000_std
      value: 38.6683
    - type: nauc_ndcg_at_1000_diff1
      value: 31.9563
    - type: nauc_map_at_1_max
      value: 8.8384
    - type: nauc_map_at_1_std
      value: -12.18
    - type: nauc_map_at_1_diff1
      value: 42.5949
    - type: nauc_map_at_3_max
      value: 10.4264
    - type: nauc_map_at_3_std
      value: -6.4437
    - type: nauc_map_at_3_diff1
      value: 31.555
    - type: nauc_map_at_5_max
      value: 12.4445
    - type: nauc_map_at_5_std
      value: -3.5782000000000003
    - type: nauc_map_at_5_diff1
      value: 29.8594
    - type: nauc_map_at_10_max
      value: 16.9699
    - type: nauc_map_at_10_std
      value: 2.0362999999999998
    - type: nauc_map_at_10_diff1
      value: 29.737599999999997
    - type: nauc_map_at_20_max
      value: 21.4809
    - type: nauc_map_at_20_std
      value: 9.0494
    - type: nauc_map_at_20_diff1
      value: 30.0806
    - type: nauc_map_at_100_max
      value: 29.0583
    - type: nauc_map_at_100_std
      value: 22.3292
    - type: nauc_map_at_100_diff1
      value: 29.9971
    - type: nauc_map_at_1000_max
      value: 30.4654
    - type: nauc_map_at_1000_std
      value: 25.208799999999997
    - type: nauc_map_at_1000_diff1
      value: 29.3623
    - type: nauc_recall_at_1_max
      value: 8.8384
    - type: nauc_recall_at_1_std
      value: -12.18
    - type: nauc_recall_at_1_diff1
      value: 42.5949
    - type: nauc_recall_at_3_max
      value: 7.692400000000001
    - type: nauc_recall_at_3_std
      value: -7.5964
    - type: nauc_recall_at_3_diff1
      value: 27.5878
    - type: nauc_recall_at_5_max
      value: 7.3506
    - type: nauc_recall_at_5_std
      value: -7.152799999999999
    - type: nauc_recall_at_5_diff1
      value: 25.565199999999997
    - type: nauc_recall_at_10_max
      value: 13.009
    - type: nauc_recall_at_10_std
      value: -0.6829
    - type: nauc_recall_at_10_diff1
      value: 25.8442
    - type: nauc_recall_at_20_max
      value: 15.329
    - type: nauc_recall_at_20_std
      value: 5.9502
    - type: nauc_recall_at_20_diff1
      value: 24.584400000000002
    - type: nauc_recall_at_100_max
      value: 26.1527
    - type: nauc_recall_at_100_std
      value: 28.8597
    - type: nauc_recall_at_100_diff1
      value: 23.5886
    - type: nauc_recall_at_1000_max
      value: 32.736
    - type: nauc_recall_at_1000_std
      value: 41.5612
    - type: nauc_recall_at_1000_diff1
      value: 21.8267
    - type: nauc_precision_at_1_max
      value: 56.4401
    - type: nauc_precision_at_1_std
      value: 39.5242
    - type: nauc_precision_at_1_diff1
      value: 44.307
    - type: nauc_precision_at_3_max
      value: 44.521100000000004
    - type: nauc_precision_at_3_std
      value: 42.4366
    - type: nauc_precision_at_3_diff1
      value: 13.569899999999999
    - type: nauc_precision_at_5_max
      value: 42.3594
    - type: nauc_precision_at_5_std
      value: 44.4758
    - type: nauc_precision_at_5_diff1
      value: 10.2733
    - type: nauc_precision_at_10_max
      value: 41.260000000000005
    - type: nauc_precision_at_10_std
      value: 47.2496
    - type: nauc_precision_at_10_diff1
      value: 9.393799999999999
    - type: nauc_precision_at_20_max
      value: 39.8169
    - type: nauc_precision_at_20_std
      value: 49.8068
    - type: nauc_precision_at_20_diff1
      value: 8.7204
    - type: nauc_precision_at_100_max
      value: 30.9015
    - type: nauc_precision_at_100_std
      value: 46.853899999999996
    - type: nauc_precision_at_100_diff1
      value: 2.0425
    - type: nauc_precision_at_1000_max
      value: 5.3395
    - type: nauc_precision_at_1000_std
      value: 17.8995
    - type: nauc_precision_at_1000_diff1
      value: -13.3583
    - type: nauc_mrr_at_1_max
      value: 56.4401
    - type: nauc_mrr_at_1_std
      value: 39.5242
    - type: nauc_mrr_at_1_diff1
      value: 44.307
    - type: nauc_mrr_at_3_max
      value: 56.97990000000001
    - type: nauc_mrr_at_3_std
      value: 42.138
    - type: nauc_mrr_at_3_diff1
      value: 41.5078
    - type: nauc_mrr_at_5_max
      value: 56.234399999999994
    - type: nauc_mrr_at_5_std
      value: 41.3617
    - type: nauc_mrr_at_5_diff1
      value: 41.227599999999995
    - type: nauc_mrr_at_10_max
      value: 56.6701
    - type: nauc_mrr_at_10_std
      value: 41.6424
    - type: nauc_mrr_at_10_diff1
      value: 41.814800000000005
    - type: nauc_mrr_at_20_max
      value: 56.6094
    - type: nauc_mrr_at_20_std
      value: 41.7269
    - type: nauc_mrr_at_20_diff1
      value: 41.8099
    - type: nauc_mrr_at_100_max
      value: 56.623900000000006
    - type: nauc_mrr_at_100_std
      value: 41.6436
    - type: nauc_mrr_at_100_diff1
      value: 41.7734
    - type: nauc_mrr_at_1000_max
      value: 56.6269
    - type: nauc_mrr_at_1000_std
      value: 41.6455
    - type: nauc_mrr_at_1000_diff1
      value: 41.7701
    - type: main_score
      value: 37.897999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 63.235
    - type: f1
      value: 59.071799999999996
    - type: f1_weighted
      value: 64.6776
    - type: main_score
      value: 63.235
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: ndcg_at_1
      value: 83.498
    - type: ndcg_at_3
      value: 86.69200000000001
    - type: ndcg_at_5
      value: 87.787
    - type: ndcg_at_10
      value: 88.31
    - type: ndcg_at_20
      value: 88.595
    - type: ndcg_at_100
      value: 88.905
    - type: ndcg_at_1000
      value: 89.09700000000001
    - type: map_at_1
      value: 77.41
    - type: map_at_3
      value: 83.673
    - type: map_at_5
      value: 84.464
    - type: map_at_10
      value: 84.748
    - type: map_at_20
      value: 84.863
    - type: map_at_100
      value: 84.929
    - type: map_at_1000
      value: 84.941
    - type: recall_at_1
      value: 77.41
    - type: recall_at_3
      value: 90.027
    - type: recall_at_5
      value: 92.804
    - type: recall_at_10
      value: 94.377
    - type: recall_at_20
      value: 95.321
    - type: recall_at_100
      value: 96.646
    - type: recall_at_1000
      value: 97.77900000000001
    - type: precision_at_1
      value: 83.498
    - type: precision_at_3
      value: 32.728
    - type: precision_at_5
      value: 20.375
    - type: precision_at_10
      value: 10.424999999999999
    - type: precision_at_20
      value: 5.305
    - type: precision_at_100
      value: 1.0919999999999999
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: mrr_at_1
      value: 83.4983
    - type: mrr_at_3
      value: 89.1189
    - type: mrr_at_5
      value: 89.6395
    - type: mrr_at_10
      value: 89.79899999999999
    - type: mrr_at_20
      value: 89.8266
    - type: mrr_at_100
      value: 89.8373
    - type: mrr_at_1000
      value: 89.8376
    - type: nauc_ndcg_at_1_max
      value: 31.5238
    - type: nauc_ndcg_at_1_std
      value: -2.2584
    - type: nauc_ndcg_at_1_diff1
      value: 74.5023
    - type: nauc_ndcg_at_3_max
      value: 24.1127
    - type: nauc_ndcg_at_3_std
      value: -2.6446
    - type: nauc_ndcg_at_3_diff1
      value: 49.2508
    - type: nauc_ndcg_at_5_max
      value: 23.6616
    - type: nauc_ndcg_at_5_std
      value: -1.3849
    - type: nauc_ndcg_at_5_diff1
      value: 47.106300000000005
    - type: nauc_ndcg_at_10_max
      value: 24.0605
    - type: nauc_ndcg_at_10_std
      value: -0.4336
    - type: nauc_ndcg_at_10_diff1
      value: 46.9328
    - type: nauc_ndcg_at_20_max
      value: 24.7393
    - type: nauc_ndcg_at_20_std
      value: 0.2855
    - type: nauc_ndcg_at_20_diff1
      value: 47.6414
    - type: nauc_ndcg_at_100_max
      value: 25.228099999999998
    - type: nauc_ndcg_at_100_std
      value: 0.5433
    - type: nauc_ndcg_at_100_diff1
      value: 48.7128
    - type: nauc_ndcg_at_1000_max
      value: 25.7762
    - type: nauc_ndcg_at_1000_std
      value: 0.7018
    - type: nauc_ndcg_at_1000_diff1
      value: 49.6639
    - type: nauc_map_at_1_max
      value: 22.7408
    - type: nauc_map_at_1_std
      value: -1.3189
    - type: nauc_map_at_1_diff1
      value: 54.049400000000006
    - type: nauc_map_at_3_max
      value: 22.6962
    - type: nauc_map_at_3_std
      value: -1.9411
    - type: nauc_map_at_3_diff1
      value: 47.3787
    - type: nauc_map_at_5_max
      value: 22.8472
    - type: nauc_map_at_5_std
      value: -1.2210999999999999
    - type: nauc_map_at_5_diff1
      value: 46.8099
    - type: nauc_map_at_10_max
      value: 23.1253
    - type: nauc_map_at_10_std
      value: -0.8166
    - type: nauc_map_at_10_diff1
      value: 46.961000000000006
    - type: nauc_map_at_20_max
      value: 23.336299999999998
    - type: nauc_map_at_20_std
      value: -0.6204000000000001
    - type: nauc_map_at_20_diff1
      value: 47.2216
    - type: nauc_map_at_100_max
      value: 23.4294
    - type: nauc_map_at_100_std
      value: -0.5717
    - type: nauc_map_at_100_diff1
      value: 47.3991
    - type: nauc_map_at_1000_max
      value: 23.4583
    - type: nauc_map_at_1000_std
      value: -0.5559999999999999
    - type: nauc_map_at_1000_diff1
      value: 47.4426
    - type: nauc_recall_at_1_max
      value: 22.7408
    - type: nauc_recall_at_1_std
      value: -1.3189
    - type: nauc_recall_at_1_diff1
      value: 54.049400000000006
    - type: nauc_recall_at_3_max
      value: 17.4806
    - type: nauc_recall_at_3_std
      value: -3.1338
    - type: nauc_recall_at_3_diff1
      value: 26.4903
    - type: nauc_recall_at_5_max
      value: 13.660400000000001
    - type: nauc_recall_at_5_std
      value: 1.3013000000000001
    - type: nauc_recall_at_5_diff1
      value: 12.3123
    - type: nauc_recall_at_10_max
      value: 13.4502
    - type: nauc_recall_at_10_std
      value: 7.7186
    - type: nauc_recall_at_10_diff1
      value: 2.9850000000000003
    - type: nauc_recall_at_20_max
      value: 16.927400000000002
    - type: nauc_recall_at_20_std
      value: 15.0728
    - type: nauc_recall_at_20_diff1
      value: 0.3826
    - type: nauc_recall_at_100_max
      value: 19.942899999999998
    - type: nauc_recall_at_100_std
      value: 23.5429
    - type: nauc_recall_at_100_diff1
      value: -3.4923
    - type: nauc_recall_at_1000_max
      value: 31.8901
    - type: nauc_recall_at_1000_std
      value: 37.6917
    - type: nauc_recall_at_1000_diff1
      value: -3.8215
    - type: nauc_precision_at_1_max
      value: 31.5238
    - type: nauc_precision_at_1_std
      value: -2.2584
    - type: nauc_precision_at_1_diff1
      value: 74.5023
    - type: nauc_precision_at_3_max
      value: 21.2432
    - type: nauc_precision_at_3_std
      value: -4.3431
    - type: nauc_precision_at_3_diff1
      value: 27.9237
    - type: nauc_precision_at_5_max
      value: 12.6046
    - type: nauc_precision_at_5_std
      value: 1.9817
    - type: nauc_precision_at_5_diff1
      value: 4.920100000000001
    - type: nauc_precision_at_10_max
      value: 11.452900000000001
    - type: nauc_precision_at_10_std
      value: 7.691199999999999
    - type: nauc_precision_at_10_diff1
      value: -2.363
    - type: nauc_precision_at_20_max
      value: 10.7846
    - type: nauc_precision_at_20_std
      value: 9.517100000000001
    - type: nauc_precision_at_20_diff1
      value: -3.3125
    - type: nauc_precision_at_100_max
      value: 9.1886
    - type: nauc_precision_at_100_std
      value: 9.5228
    - type: nauc_precision_at_100_diff1
      value: -1.9271
    - type: nauc_precision_at_1000_max
      value: 8.9731
    - type: nauc_precision_at_1000_std
      value: 8.952200000000001
    - type: nauc_precision_at_1000_diff1
      value: 1.226
    - type: nauc_mrr_at_1_max
      value: 31.5238
    - type: nauc_mrr_at_1_std
      value: -2.2584
    - type: nauc_mrr_at_1_diff1
      value: 74.5023
    - type: nauc_mrr_at_3_max
      value: 32.1889
    - type: nauc_mrr_at_3_std
      value: -4.9427
    - type: nauc_mrr_at_3_diff1
      value: 72.74080000000001
    - type: nauc_mrr_at_5_max
      value: 32.0768
    - type: nauc_mrr_at_5_std
      value: -4.4333
    - type: nauc_mrr_at_5_diff1
      value: 72.8939
    - type: nauc_mrr_at_10_max
      value: 32.1312
    - type: nauc_mrr_at_10_std
      value: -4.1756
    - type: nauc_mrr_at_10_diff1
      value: 73.0284
    - type: nauc_mrr_at_20_max
      value: 32.163199999999996
    - type: nauc_mrr_at_20_std
      value: -4.0634999999999994
    - type: nauc_mrr_at_20_diff1
      value: 73.0685
    - type: nauc_mrr_at_100_max
      value: 32.118
    - type: nauc_mrr_at_100_std
      value: -4.0852
    - type: nauc_mrr_at_100_diff1
      value: 73.0722
    - type: nauc_mrr_at_1000_max
      value: 32.1164
    - type: nauc_mrr_at_1000_std
      value: -4.0867
    - type: nauc_mrr_at_1000_diff1
      value: 73.0722
    - type: main_score
      value: 88.31
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: ndcg_at_1
      value: 48.302
    - type: ndcg_at_3
      value: 44.882
    - type: ndcg_at_5
      value: 45.898
    - type: ndcg_at_10
      value: 48.28
    - type: ndcg_at_20
      value: 51.536
    - type: ndcg_at_100
      value: 55.461000000000006
    - type: ndcg_at_1000
      value: 57.938
    - type: map_at_1
      value: 24.324
    - type: map_at_3
      value: 35.225
    - type: map_at_5
      value: 37.962
    - type: map_at_10
      value: 40.054
    - type: map_at_20
      value: 41.399
    - type: map_at_100
      value: 42.321
    - type: map_at_1000
      value: 42.476
    - type: recall_at_1
      value: 24.324
    - type: recall_at_3
      value: 41.036
    - type: recall_at_5
      value: 46.844
    - type: recall_at_10
      value: 54.75
    - type: recall_at_20
      value: 64.86800000000001
    - type: recall_at_100
      value: 80.413
    - type: recall_at_1000
      value: 95.242
    - type: precision_at_1
      value: 48.302
    - type: precision_at_3
      value: 29.835
    - type: precision_at_5
      value: 21.852
    - type: precision_at_10
      value: 13.333
    - type: precision_at_20
      value: 8.017000000000001
    - type: precision_at_100
      value: 2.068
    - type: precision_at_1000
      value: 0.25
    - type: mrr_at_1
      value: 48.302499999999995
    - type: mrr_at_3
      value: 55.0669
    - type: mrr_at_5
      value: 56.208800000000004
    - type: mrr_at_10
      value: 57.128299999999996
    - type: mrr_at_20
      value: 57.6631
    - type: mrr_at_100
      value: 57.897
    - type: mrr_at_1000
      value: 57.9236
    - type: nauc_ndcg_at_1_max
      value: 35.3012
    - type: nauc_ndcg_at_1_std
      value: -10.4163
    - type: nauc_ndcg_at_1_diff1
      value: 49.8902
    - type: nauc_ndcg_at_3_max
      value: 33.3967
    - type: nauc_ndcg_at_3_std
      value: -6.623900000000001
    - type: nauc_ndcg_at_3_diff1
      value: 39.811600000000006
    - type: nauc_ndcg_at_5_max
      value: 32.1592
    - type: nauc_ndcg_at_5_std
      value: -7.155799999999999
    - type: nauc_ndcg_at_5_diff1
      value: 39.4895
    - type: nauc_ndcg_at_10_max
      value: 32.6943
    - type: nauc_ndcg_at_10_std
      value: -5.543
    - type: nauc_ndcg_at_10_diff1
      value: 39.4015
    - type: nauc_ndcg_at_20_max
      value: 33.247
    - type: nauc_ndcg_at_20_std
      value: -3.5911
    - type: nauc_ndcg_at_20_diff1
      value: 40.1093
    - type: nauc_ndcg_at_100_max
      value: 35.8738
    - type: nauc_ndcg_at_100_std
      value: -0.0625
    - type: nauc_ndcg_at_100_diff1
      value: 40.1993
    - type: nauc_ndcg_at_1000_max
      value: 36.105
    - type: nauc_ndcg_at_1000_std
      value: -1.2023000000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 40.9404
    - type: nauc_map_at_1_max
      value: 15.893099999999999
    - type: nauc_map_at_1_std
      value: -10.817400000000001
    - type: nauc_map_at_1_diff1
      value: 42.2743
    - type: nauc_map_at_3_max
      value: 24.8811
    - type: nauc_map_at_3_std
      value: -8.8756
    - type: nauc_map_at_3_diff1
      value: 40.2234
    - type: nauc_map_at_5_max
      value: 28.198
    - type: nauc_map_at_5_std
      value: -8.2681
    - type: nauc_map_at_5_diff1
      value: 39.8233
    - type: nauc_map_at_10_max
      value: 29.8969
    - type: nauc_map_at_10_std
      value: -7.2732
    - type: nauc_map_at_10_diff1
      value: 39.056200000000004
    - type: nauc_map_at_20_max
      value: 30.438900000000004
    - type: nauc_map_at_20_std
      value: -6.2997
    - type: nauc_map_at_20_diff1
      value: 39.2282
    - type: nauc_map_at_100_max
      value: 31.2085
    - type: nauc_map_at_100_std
      value: -5.4389
    - type: nauc_map_at_100_diff1
      value: 39.2156
    - type: nauc_map_at_1000_max
      value: 31.2581
    - type: nauc_map_at_1000_std
      value: -5.4575
    - type: nauc_map_at_1000_diff1
      value: 39.256099999999996
    - type: nauc_recall_at_1_max
      value: 15.893099999999999
    - type: nauc_recall_at_1_std
      value: -10.817400000000001
    - type: nauc_recall_at_1_diff1
      value: 42.2743
    - type: nauc_recall_at_3_max
      value: 20.7605
    - type: nauc_recall_at_3_std
      value: -7.9595
    - type: nauc_recall_at_3_diff1
      value: 33.0679
    - type: nauc_recall_at_5_max
      value: 24.532899999999998
    - type: nauc_recall_at_5_std
      value: -7.535
    - type: nauc_recall_at_5_diff1
      value: 32.5104
    - type: nauc_recall_at_10_max
      value: 26.8851
    - type: nauc_recall_at_10_std
      value: -2.7628
    - type: nauc_recall_at_10_diff1
      value: 28.9325
    - type: nauc_recall_at_20_max
      value: 25.8328
    - type: nauc_recall_at_20_std
      value: 3.2887
    - type: nauc_recall_at_20_diff1
      value: 28.417399999999997
    - type: nauc_recall_at_100_max
      value: 36.079699999999995
    - type: nauc_recall_at_100_std
      value: 27.093099999999996
    - type: nauc_recall_at_100_diff1
      value: 26.377299999999998
    - type: nauc_recall_at_1000_max
      value: 47.7952
    - type: nauc_recall_at_1000_std
      value: 53.0751
    - type: nauc_recall_at_1000_diff1
      value: 32.7248
    - type: nauc_precision_at_1_max
      value: 35.3012
    - type: nauc_precision_at_1_std
      value: -10.4163
    - type: nauc_precision_at_1_diff1
      value: 49.8902
    - type: nauc_precision_at_3_max
      value: 39.9322
    - type: nauc_precision_at_3_std
      value: 0.2644
    - type: nauc_precision_at_3_diff1
      value: 26.600600000000004
    - type: nauc_precision_at_5_max
      value: 40.3902
    - type: nauc_precision_at_5_std
      value: 2.3505000000000003
    - type: nauc_precision_at_5_diff1
      value: 19.7771
    - type: nauc_precision_at_10_max
      value: 39.415299999999995
    - type: nauc_precision_at_10_std
      value: 6.5885
    - type: nauc_precision_at_10_diff1
      value: 13.7527
    - type: nauc_precision_at_20_max
      value: 37.2422
    - type: nauc_precision_at_20_std
      value: 12.9599
    - type: nauc_precision_at_20_diff1
      value: 9.6751
    - type: nauc_precision_at_100_max
      value: 35.6967
    - type: nauc_precision_at_100_std
      value: 19.8202
    - type: nauc_precision_at_100_diff1
      value: 1.6320999999999999
    - type: nauc_precision_at_1000_max
      value: 28.9716
    - type: nauc_precision_at_1000_std
      value: 15.8223
    - type: nauc_precision_at_1000_diff1
      value: -3.3576
    - type: nauc_mrr_at_1_max
      value: 35.3012
    - type: nauc_mrr_at_1_std
      value: -10.4163
    - type: nauc_mrr_at_1_diff1
      value: 49.8902
    - type: nauc_mrr_at_3_max
      value: 36.6979
    - type: nauc_mrr_at_3_std
      value: -7.6057
    - type: nauc_mrr_at_3_diff1
      value: 48.1421
    - type: nauc_mrr_at_5_max
      value: 37.0712
    - type: nauc_mrr_at_5_std
      value: -7.4076
    - type: nauc_mrr_at_5_diff1
      value: 47.7326
    - type: nauc_mrr_at_10_max
      value: 37.4375
    - type: nauc_mrr_at_10_std
      value: -6.875299999999999
    - type: nauc_mrr_at_10_diff1
      value: 47.7446
    - type: nauc_mrr_at_20_max
      value: 37.473
    - type: nauc_mrr_at_20_std
      value: -6.694799999999999
    - type: nauc_mrr_at_20_diff1
      value: 47.8238
    - type: nauc_mrr_at_100_max
      value: 37.453599999999994
    - type: nauc_mrr_at_100_std
      value: -6.612500000000001
    - type: nauc_mrr_at_100_diff1
      value: 47.8186
    - type: nauc_mrr_at_1000_max
      value: 37.4367
    - type: nauc_mrr_at_1000_std
      value: -6.6572000000000005
    - type: nauc_mrr_at_1000_diff1
      value: 47.8333
    - type: main_score
      value: 48.28
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: ndcg_at_1
      value: 82.836
    - type: ndcg_at_3
      value: 60.80799999999999
    - type: ndcg_at_5
      value: 62.719
    - type: ndcg_at_10
      value: 64.464
    - type: ndcg_at_20
      value: 65.613
    - type: ndcg_at_100
      value: 67.244
    - type: ndcg_at_1000
      value: 68.633
    - type: map_at_1
      value: 41.418
    - type: map_at_3
      value: 51.913
    - type: map_at_5
      value: 53.45100000000001
    - type: map_at_10
      value: 54.50899999999999
    - type: map_at_20
      value: 54.981
    - type: map_at_100
      value: 55.315000000000005
    - type: map_at_1000
      value: 55.387
    - type: recall_at_1
      value: 41.418
    - type: recall_at_3
      value: 55.206
    - type: recall_at_5
      value: 58.987
    - type: recall_at_10
      value: 63.369
    - type: recall_at_20
      value: 67.07
    - type: recall_at_100
      value: 74.29400000000001
    - type: recall_at_1000
      value: 83.504
    - type: precision_at_1
      value: 82.836
    - type: precision_at_3
      value: 36.803999999999995
    - type: precision_at_5
      value: 23.595
    - type: precision_at_10
      value: 12.674
    - type: precision_at_20
      value: 6.707000000000001
    - type: precision_at_100
      value: 1.486
    - type: precision_at_1000
      value: 0.167
    - type: mrr_at_1
      value: 82.8359
    - type: mrr_at_3
      value: 86.7207
    - type: mrr_at_5
      value: 87.1062
    - type: mrr_at_10
      value: 87.3533
    - type: mrr_at_20
      value: 87.4411
    - type: mrr_at_100
      value: 87.4944
    - type: mrr_at_1000
      value: 87.5012
    - type: nauc_ndcg_at_1_max
      value: 55.378400000000006
    - type: nauc_ndcg_at_1_std
      value: -8.999799999999999
    - type: nauc_ndcg_at_1_diff1
      value: 81.65289999999999
    - type: nauc_ndcg_at_3_max
      value: 27.530900000000003
    - type: nauc_ndcg_at_3_std
      value: -1.4845000000000002
    - type: nauc_ndcg_at_3_diff1
      value: 28.8078
    - type: nauc_ndcg_at_5_max
      value: 24.8019
    - type: nauc_ndcg_at_5_std
      value: -0.6705
    - type: nauc_ndcg_at_5_diff1
      value: 25.1054
    - type: nauc_ndcg_at_10_max
      value: 22.6678
    - type: nauc_ndcg_at_10_std
      value: 0.8309000000000001
    - type: nauc_ndcg_at_10_diff1
      value: 22.1137
    - type: nauc_ndcg_at_20_max
      value: 21.601200000000002
    - type: nauc_ndcg_at_20_std
      value: 1.6587
    - type: nauc_ndcg_at_20_diff1
      value: 20.9774
    - type: nauc_ndcg_at_100_max
      value: 20.258499999999998
    - type: nauc_ndcg_at_100_std
      value: 2.4681
    - type: nauc_ndcg_at_100_diff1
      value: 19.4499
    - type: nauc_ndcg_at_1000_max
      value: 20.4564
    - type: nauc_ndcg_at_1000_std
      value: 2.8757
    - type: nauc_ndcg_at_1000_diff1
      value: 19.674500000000002
    - type: nauc_map_at_1_max
      value: 55.378400000000006
    - type: nauc_map_at_1_std
      value: -8.999799999999999
    - type: nauc_map_at_1_diff1
      value: 81.65289999999999
    - type: nauc_map_at_3_max
      value: 22.8016
    - type: nauc_map_at_3_std
      value: -1.3432
    - type: nauc_map_at_3_diff1
      value: 21.9107
    - type: nauc_map_at_5_max
      value: 21.0041
    - type: nauc_map_at_5_std
      value: -0.8455
    - type: nauc_map_at_5_diff1
      value: 19.5463
    - type: nauc_map_at_10_max
      value: 19.9533
    - type: nauc_map_at_10_std
      value: -0.058
    - type: nauc_map_at_10_diff1
      value: 18.075
    - type: nauc_map_at_20_max
      value: 19.5951
    - type: nauc_map_at_20_std
      value: 0.2562
    - type: nauc_map_at_20_diff1
      value: 17.71
    - type: nauc_map_at_100_max
      value: 19.3598
    - type: nauc_map_at_100_std
      value: 0.42960000000000004
    - type: nauc_map_at_100_diff1
      value: 17.461299999999998
    - type: nauc_map_at_1000_max
      value: 19.359
    - type: nauc_map_at_1000_std
      value: 0.451
    - type: nauc_map_at_1000_diff1
      value: 17.4648
    - type: nauc_recall_at_1_max
      value: 55.378400000000006
    - type: nauc_recall_at_1_std
      value: -8.999799999999999
    - type: nauc_recall_at_1_diff1
      value: 81.65289999999999
    - type: nauc_recall_at_3_max
      value: 18.226
    - type: nauc_recall_at_3_std
      value: 0.7939999999999999
    - type: nauc_recall_at_3_diff1
      value: 12.2289
    - type: nauc_recall_at_5_max
      value: 12.998999999999999
    - type: nauc_recall_at_5_std
      value: 2.1354
    - type: nauc_recall_at_5_diff1
      value: 5.6548
    - type: nauc_recall_at_10_max
      value: 7.985200000000001
    - type: nauc_recall_at_10_std
      value: 5.3194
    - type: nauc_recall_at_10_diff1
      value: -0.9107000000000001
    - type: nauc_recall_at_20_max
      value: 4.3701
    - type: nauc_recall_at_20_std
      value: 7.6056
    - type: nauc_recall_at_20_diff1
      value: -4.7479000000000005
    - type: nauc_recall_at_100_max
      value: -2.7925
    - type: nauc_recall_at_100_std
      value: 11.228200000000001
    - type: nauc_recall_at_100_diff1
      value: -13.4144
    - type: nauc_recall_at_1000_max
      value: -7.6068
    - type: nauc_recall_at_1000_std
      value: 17.0487
    - type: nauc_recall_at_1000_diff1
      value: -21.2775
    - type: nauc_precision_at_1_max
      value: 55.378400000000006
    - type: nauc_precision_at_1_std
      value: -8.999799999999999
    - type: nauc_precision_at_1_diff1
      value: 81.65289999999999
    - type: nauc_precision_at_3_max
      value: 18.226
    - type: nauc_precision_at_3_std
      value: 0.7939999999999999
    - type: nauc_precision_at_3_diff1
      value: 12.2289
    - type: nauc_precision_at_5_max
      value: 12.998999999999999
    - type: nauc_precision_at_5_std
      value: 2.1354
    - type: nauc_precision_at_5_diff1
      value: 5.6548
    - type: nauc_precision_at_10_max
      value: 7.985200000000001
    - type: nauc_precision_at_10_std
      value: 5.3194
    - type: nauc_precision_at_10_diff1
      value: -0.9107000000000001
    - type: nauc_precision_at_20_max
      value: 4.3701
    - type: nauc_precision_at_20_std
      value: 7.6056
    - type: nauc_precision_at_20_diff1
      value: -4.7479000000000005
    - type: nauc_precision_at_100_max
      value: -2.7925
    - type: nauc_precision_at_100_std
      value: 11.228200000000001
    - type: nauc_precision_at_100_diff1
      value: -13.4144
    - type: nauc_precision_at_1000_max
      value: -7.6068
    - type: nauc_precision_at_1000_std
      value: 17.0487
    - type: nauc_precision_at_1000_diff1
      value: -21.2775
    - type: nauc_mrr_at_1_max
      value: 55.378400000000006
    - type: nauc_mrr_at_1_std
      value: -8.999799999999999
    - type: nauc_mrr_at_1_diff1
      value: 81.65289999999999
    - type: nauc_mrr_at_3_max
      value: 58.457
    - type: nauc_mrr_at_3_std
      value: -6.3487
    - type: nauc_mrr_at_3_diff1
      value: 80.559
    - type: nauc_mrr_at_5_max
      value: 58.4461
    - type: nauc_mrr_at_5_std
      value: -5.9587
    - type: nauc_mrr_at_5_diff1
      value: 80.6051
    - type: nauc_mrr_at_10_max
      value: 58.42659999999999
    - type: nauc_mrr_at_10_std
      value: -5.6473
    - type: nauc_mrr_at_10_diff1
      value: 80.6628
    - type: nauc_mrr_at_20_max
      value: 58.3928
    - type: nauc_mrr_at_20_std
      value: -5.6386
    - type: nauc_mrr_at_20_diff1
      value: 80.7154
    - type: nauc_mrr_at_100_max
      value: 58.341699999999996
    - type: nauc_mrr_at_100_std
      value: -5.6933
    - type: nauc_mrr_at_100_diff1
      value: 80.7071
    - type: nauc_mrr_at_1000_max
      value: 58.3298
    - type: nauc_mrr_at_1000_std
      value: -5.7103
    - type: nauc_mrr_at_1000_diff1
      value: 80.7062
    - type: main_score
      value: 64.464
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 94.9352
    - type: f1
      value: 94.9327
    - type: f1_weighted
      value: 94.9327
    - type: ap
      value: 92.00789999999999
    - type: ap_weighted
      value: 92.00789999999999
    - type: main_score
      value: 94.9352
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MSMARCO (default)
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: dev
      type: mteb/msmarco
    metrics:
    - type: ndcg_at_1
      value: 21.504
    - type: ndcg_at_3
      value: 32.328
    - type: ndcg_at_5
      value: 36.452
    - type: ndcg_at_10
      value: 40.325
    - type: ndcg_at_20
      value: 43.07
    - type: ndcg_at_100
      value: 46.23
    - type: ndcg_at_1000
      value: 47.369
    - type: map_at_1
      value: 20.909
    - type: map_at_3
      value: 29.353
    - type: map_at_5
      value: 31.661
    - type: map_at_10
      value: 33.28
    - type: map_at_20
      value: 34.06
    - type: map_at_100
      value: 34.52
    - type: map_at_1000
      value: 34.567
    - type: recall_at_1
      value: 20.909
    - type: recall_at_3
      value: 40.339000000000006
    - type: recall_at_5
      value: 50.259
    - type: recall_at_10
      value: 62.059
    - type: recall_at_20
      value: 72.693
    - type: recall_at_100
      value: 89.269
    - type: recall_at_1000
      value: 97.933
    - type: precision_at_1
      value: 21.504
    - type: precision_at_3
      value: 13.944999999999999
    - type: precision_at_5
      value: 10.461
    - type: precision_at_10
      value: 6.491
    - type: precision_at_20
      value: 3.818
    - type: precision_at_100
      value: 0.943
    - type: precision_at_1000
      value: 0.104
    - type: mrr_at_1
      value: 21.5043
    - type: mrr_at_3
      value: 29.978500000000004
    - type: mrr_at_5
      value: 32.251400000000004
    - type: mrr_at_10
      value: 33.8389
    - type: mrr_at_20
      value: 34.5788
    - type: mrr_at_100
      value: 35.010200000000005
    - type: mrr_at_1000
      value: 35.051100000000005
    - type: nauc_ndcg_at_1_max
      value: -1.0808
    - type: nauc_ndcg_at_1_std
      value: -22.361900000000002
    - type: nauc_ndcg_at_1_diff1
      value: 36.9204
    - type: nauc_ndcg_at_3_max
      value: -2.0822
    - type: nauc_ndcg_at_3_std
      value: -25.852999999999998
    - type: nauc_ndcg_at_3_diff1
      value: 30.8521
    - type: nauc_ndcg_at_5_max
      value: -2.0332
    - type: nauc_ndcg_at_5_std
      value: -26.375
    - type: nauc_ndcg_at_5_diff1
      value: 30.1887
    - type: nauc_ndcg_at_10_max
      value: -2.2974
    - type: nauc_ndcg_at_10_std
      value: -26.712000000000003
    - type: nauc_ndcg_at_10_diff1
      value: 30.1484
    - type: nauc_ndcg_at_20_max
      value: -1.825
    - type: nauc_ndcg_at_20_std
      value: -25.4078
    - type: nauc_ndcg_at_20_diff1
      value: 30.1416
    - type: nauc_ndcg_at_100_max
      value: -1.2328000000000001
    - type: nauc_ndcg_at_100_std
      value: -23.2039
    - type: nauc_ndcg_at_100_diff1
      value: 30.348399999999998
    - type: nauc_ndcg_at_1000_max
      value: -1.2148
    - type: nauc_ndcg_at_1000_std
      value: -23.8282
    - type: nauc_ndcg_at_1000_diff1
      value: 30.704900000000002
    - type: nauc_map_at_1_max
      value: -1.3643
    - type: nauc_map_at_1_std
      value: -22.5875
    - type: nauc_map_at_1_diff1
      value: 36.7618
    - type: nauc_map_at_3_max
      value: -2.0389999999999997
    - type: nauc_map_at_3_std
      value: -25.2612
    - type: nauc_map_at_3_diff1
      value: 32.171499999999995
    - type: nauc_map_at_5_max
      value: -2.0125
    - type: nauc_map_at_5_std
      value: -25.605800000000002
    - type: nauc_map_at_5_diff1
      value: 31.8081
    - type: nauc_map_at_10_max
      value: -2.1288
    - type: nauc_map_at_10_std
      value: -25.7592
    - type: nauc_map_at_10_diff1
      value: 31.8241
    - type: nauc_map_at_20_max
      value: -2.0061
    - type: nauc_map_at_20_std
      value: -25.4037
    - type: nauc_map_at_20_diff1
      value: 31.836799999999997
    - type: nauc_map_at_100_max
      value: -1.9212
    - type: nauc_map_at_100_std
      value: -25.0965
    - type: nauc_map_at_100_diff1
      value: 31.8741
    - type: nauc_map_at_1000_max
      value: -1.9189
    - type: nauc_map_at_1000_std
      value: -25.111800000000002
    - type: nauc_map_at_1000_diff1
      value: 31.8865
    - type: nauc_recall_at_1_max
      value: -1.3643
    - type: nauc_recall_at_1_std
      value: -22.5875
    - type: nauc_recall_at_1_diff1
      value: 36.7618
    - type: nauc_recall_at_3_max
      value: -2.4667000000000003
    - type: nauc_recall_at_3_std
      value: -27.6077
    - type: nauc_recall_at_3_diff1
      value: 27.2784
    - type: nauc_recall_at_5_max
      value: -2.3782
    - type: nauc_recall_at_5_std
      value: -28.6853
    - type: nauc_recall_at_5_diff1
      value: 25.5971
    - type: nauc_recall_at_10_max
      value: -3.2792000000000003
    - type: nauc_recall_at_10_std
      value: -29.9584
    - type: nauc_recall_at_10_diff1
      value: 24.7197
    - type: nauc_recall_at_20_max
      value: -1.2229999999999999
    - type: nauc_recall_at_20_std
      value: -24.479799999999997
    - type: nauc_recall_at_20_diff1
      value: 23.377100000000002
    - type: nauc_recall_at_100_max
      value: 6.815
    - type: nauc_recall_at_100_std
      value: 5.1981
    - type: nauc_recall_at_100_diff1
      value: 18.5723
    - type: nauc_recall_at_1000_max
      value: 38.1041
    - type: nauc_recall_at_1000_std
      value: 54.1207
    - type: nauc_recall_at_1000_diff1
      value: 6.8622000000000005
    - type: nauc_precision_at_1_max
      value: -1.0808
    - type: nauc_precision_at_1_std
      value: -22.361900000000002
    - type: nauc_precision_at_1_diff1
      value: 36.9204
    - type: nauc_precision_at_3_max
      value: -2.2124
    - type: nauc_precision_at_3_std
      value: -27.3546
    - type: nauc_precision_at_3_diff1
      value: 27.108700000000002
    - type: nauc_precision_at_5_max
      value: -1.8263000000000003
    - type: nauc_precision_at_5_std
      value: -27.977899999999998
    - type: nauc_precision_at_5_diff1
      value: 24.8638
    - type: nauc_precision_at_10_max
      value: -2.2207
    - type: nauc_precision_at_10_std
      value: -27.9458
    - type: nauc_precision_at_10_diff1
      value: 22.851
    - type: nauc_precision_at_20_max
      value: 0.5773999999999999
    - type: nauc_precision_at_20_std
      value: -20.118
    - type: nauc_precision_at_20_diff1
      value: 19.5377
    - type: nauc_precision_at_100_max
      value: 9.327399999999999
    - type: nauc_precision_at_100_std
      value: 8.4253
    - type: nauc_precision_at_100_diff1
      value: 8.33
    - type: nauc_precision_at_1000_max
      value: 15.6001
    - type: nauc_precision_at_1000_std
      value: 18.066
    - type: nauc_precision_at_1000_diff1
      value: -4.5068
    - type: nauc_mrr_at_1_max
      value: -1.0808
    - type: nauc_mrr_at_1_std
      value: -22.361900000000002
    - type: nauc_mrr_at_1_diff1
      value: 36.9204
    - type: nauc_mrr_at_3_max
      value: -1.6818
    - type: nauc_mrr_at_3_std
      value: -24.8193
    - type: nauc_mrr_at_3_diff1
      value: 32.159
    - type: nauc_mrr_at_5_max
      value: -1.6575
    - type: nauc_mrr_at_5_std
      value: -25.0817
    - type: nauc_mrr_at_5_diff1
      value: 31.800800000000002
    - type: nauc_mrr_at_10_max
      value: -1.7668
    - type: nauc_mrr_at_10_std
      value: -25.196800000000003
    - type: nauc_mrr_at_10_diff1
      value: 31.8144
    - type: nauc_mrr_at_20_max
      value: -1.6674000000000002
    - type: nauc_mrr_at_20_std
      value: -24.8741
    - type: nauc_mrr_at_20_diff1
      value: 31.8324
    - type: nauc_mrr_at_100_max
      value: -1.6053000000000002
    - type: nauc_mrr_at_100_std
      value: -24.6091
    - type: nauc_mrr_at_100_diff1
      value: 31.883
    - type: nauc_mrr_at_1000_max
      value: -1.6053000000000002
    - type: nauc_mrr_at_1000_std
      value: -24.627
    - type: nauc_mrr_at_1000_diff1
      value: 31.896200000000004
    - type: main_score
      value: 40.325
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 96.311
    - type: f1
      value: 96.0432
    - type: f1_weighted
      value: 96.3129
    - type: main_score
      value: 96.311
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 86.5048
    - type: f1
      value: 67.3883
    - type: f1_weighted
      value: 88.2687
    - type: main_score
      value: 86.5048
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 75.7902
    - type: f1
      value: 73.2351
    - type: f1_weighted
      value: 75.5894
    - type: main_score
      value: 75.7902
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 77.3571
    - type: f1
      value: 77.3086
    - type: f1_weighted
      value: 77.235
    - type: main_score
      value: 77.3571
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 39.4623
    - type: v_measure_std
      value: 1.3405
    - type: main_score
      value: 39.4623
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 37.5047
    - type: v_measure_std
      value: 1.2052
    - type: main_score
      value: 37.5047
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: map
      value: 28.9125
    - type: mrr
      value: 29.656900000000004
    - type: nAUC_map_max
      value: -21.7929
    - type: nAUC_map_std
      value: -4.2712
    - type: nAUC_map_diff1
      value: 11.698500000000001
    - type: nAUC_mrr_max
      value: -16.4251
    - type: nAUC_mrr_std
      value: -2.1364
    - type: nAUC_mrr_diff1
      value: 11.3017
    - type: main_score
      value: 28.9125
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus (default)
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: ndcg_at_1
      value: 44.737
    - type: ndcg_at_3
      value: 40.943000000000005
    - type: ndcg_at_5
      value: 38.914
    - type: ndcg_at_10
      value: 35.762
    - type: ndcg_at_20
      value: 33.274
    - type: ndcg_at_100
      value: 32.861000000000004
    - type: ndcg_at_1000
      value: 41.509
    - type: map_at_1
      value: 5.792
    - type: map_at_3
      value: 9.506
    - type: map_at_5
      value: 11.213
    - type: map_at_10
      value: 13.165
    - type: map_at_20
      value: 14.663
    - type: map_at_100
      value: 16.885
    - type: map_at_1000
      value: 18.368000000000002
    - type: recall_at_1
      value: 5.792
    - type: recall_at_3
      value: 10.517
    - type: recall_at_5
      value: 13.296
    - type: recall_at_10
      value: 17.37
    - type: recall_at_20
      value: 21.22
    - type: recall_at_100
      value: 33.953
    - type: recall_at_1000
      value: 65.462
    - type: precision_at_1
      value: 46.749
    - type: precision_at_3
      value: 38.596000000000004
    - type: precision_at_5
      value: 34.303
    - type: precision_at_10
      value: 26.779999999999998
    - type: precision_at_20
      value: 19.830000000000002
    - type: precision_at_100
      value: 8.466999999999999
    - type: precision_at_1000
      value: 2.12
    - type: mrr_at_1
      value: 46.7492
    - type: mrr_at_3
      value: 54.02479999999999
    - type: mrr_at_5
      value: 55.031
    - type: mrr_at_10
      value: 55.8081
    - type: mrr_at_20
      value: 56.143699999999995
    - type: mrr_at_100
      value: 56.4018
    - type: mrr_at_1000
      value: 56.4497
    - type: nauc_ndcg_at_1_max
      value: 54.4799
    - type: nauc_ndcg_at_1_std
      value: 19.8188
    - type: nauc_ndcg_at_1_diff1
      value: 35.095
    - type: nauc_ndcg_at_3_max
      value: 49.5282
    - type: nauc_ndcg_at_3_std
      value: 19.1444
    - type: nauc_ndcg_at_3_diff1
      value: 25.074800000000003
    - type: nauc_ndcg_at_5_max
      value: 50.437200000000004
    - type: nauc_ndcg_at_5_std
      value: 21.5019
    - type: nauc_ndcg_at_5_diff1
      value: 21.414
    - type: nauc_ndcg_at_10_max
      value: 46.907199999999996
    - type: nauc_ndcg_at_10_std
      value: 22.5521
    - type: nauc_ndcg_at_10_diff1
      value: 19.0604
    - type: nauc_ndcg_at_20_max
      value: 47.216
    - type: nauc_ndcg_at_20_std
      value: 24.535
    - type: nauc_ndcg_at_20_diff1
      value: 18.3393
    - type: nauc_ndcg_at_100_max
      value: 47.647
    - type: nauc_ndcg_at_100_std
      value: 25.7305
    - type: nauc_ndcg_at_100_diff1
      value: 20.5066
    - type: nauc_ndcg_at_1000_max
      value: 53.0034
    - type: nauc_ndcg_at_1000_std
      value: 32.229600000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 21.729799999999997
    - type: nauc_map_at_1_max
      value: 18.8513
    - type: nauc_map_at_1_std
      value: -13.5714
    - type: nauc_map_at_1_diff1
      value: 42.4674
    - type: nauc_map_at_3_max
      value: 19.8798
    - type: nauc_map_at_3_std
      value: -12.600700000000002
    - type: nauc_map_at_3_diff1
      value: 34.545700000000004
    - type: nauc_map_at_5_max
      value: 24.756800000000002
    - type: nauc_map_at_5_std
      value: -7.959099999999999
    - type: nauc_map_at_5_diff1
      value: 29.1707
    - type: nauc_map_at_10_max
      value: 28.1916
    - type: nauc_map_at_10_std
      value: -3.1498
    - type: nauc_map_at_10_diff1
      value: 25.1522
    - type: nauc_map_at_20_max
      value: 31.9354
    - type: nauc_map_at_20_std
      value: 2.319
    - type: nauc_map_at_20_diff1
      value: 22.778100000000002
    - type: nauc_map_at_100_max
      value: 35.938700000000004
    - type: nauc_map_at_100_std
      value: 9.3661
    - type: nauc_map_at_100_diff1
      value: 21.2726
    - type: nauc_map_at_1000_max
      value: 36.8531
    - type: nauc_map_at_1000_std
      value: 12.0615
    - type: nauc_map_at_1000_diff1
      value: 19.761699999999998
    - type: nauc_recall_at_1_max
      value: 18.8513
    - type: nauc_recall_at_1_std
      value: -13.5714
    - type: nauc_recall_at_1_diff1
      value: 42.4674
    - type: nauc_recall_at_3_max
      value: 17.405
    - type: nauc_recall_at_3_std
      value: -11.779399999999999
    - type: nauc_recall_at_3_diff1
      value: 31.8655
    - type: nauc_recall_at_5_max
      value: 22.8368
    - type: nauc_recall_at_5_std
      value: -4.7815
    - type: nauc_recall_at_5_diff1
      value: 23.4258
    - type: nauc_recall_at_10_max
      value: 23.6849
    - type: nauc_recall_at_10_std
      value: 0.1013
    - type: nauc_recall_at_10_diff1
      value: 18.4986
    - type: nauc_recall_at_20_max
      value: 27.289400000000004
    - type: nauc_recall_at_20_std
      value: 7.126200000000001
    - type: nauc_recall_at_20_diff1
      value: 14.6343
    - type: nauc_recall_at_100_max
      value: 26.9683
    - type: nauc_recall_at_100_std
      value: 16.145899999999997
    - type: nauc_recall_at_100_diff1
      value: 9.705
    - type: nauc_recall_at_1000_max
      value: 18.4336
    - type: nauc_recall_at_1000_std
      value: 18.2245
    - type: nauc_recall_at_1000_diff1
      value: 2.3923
    - type: nauc_precision_at_1_max
      value: 56.8886
    - type: nauc_precision_at_1_std
      value: 22.122
    - type: nauc_precision_at_1_diff1
      value: 33.3152
    - type: nauc_precision_at_3_max
      value: 47.759299999999996
    - type: nauc_precision_at_3_std
      value: 23.3157
    - type: nauc_precision_at_3_diff1
      value: 14.015
    - type: nauc_precision_at_5_max
      value: 48.8089
    - type: nauc_precision_at_5_std
      value: 28.7149
    - type: nauc_precision_at_5_diff1
      value: 6.0146999999999995
    - type: nauc_precision_at_10_max
      value: 41.620200000000004
    - type: nauc_precision_at_10_std
      value: 32.275999999999996
    - type: nauc_precision_at_10_diff1
      value: -0.6839
    - type: nauc_precision_at_20_max
      value: 39.6123
    - type: nauc_precision_at_20_std
      value: 37.4586
    - type: nauc_precision_at_20_diff1
      value: -4.5309
    - type: nauc_precision_at_100_max
      value: 25.199700000000004
    - type: nauc_precision_at_100_std
      value: 34.449400000000004
    - type: nauc_precision_at_100_diff1
      value: -9.290700000000001
    - type: nauc_precision_at_1000_max
      value: 8.876000000000001
    - type: nauc_precision_at_1000_std
      value: 20.748
    - type: nauc_precision_at_1000_diff1
      value: -12.327399999999999
    - type: nauc_mrr_at_1_max
      value: 56.717600000000004
    - type: nauc_mrr_at_1_std
      value: 20.7515
    - type: nauc_mrr_at_1_diff1
      value: 33.3152
    - type: nauc_mrr_at_3_max
      value: 57.90689999999999
    - type: nauc_mrr_at_3_std
      value: 25.1369
    - type: nauc_mrr_at_3_diff1
      value: 31.157
    - type: nauc_mrr_at_5_max
      value: 59.2569
    - type: nauc_mrr_at_5_std
      value: 27.054000000000002
    - type: nauc_mrr_at_5_diff1
      value: 30.840400000000002
    - type: nauc_mrr_at_10_max
      value: 59.44819999999999
    - type: nauc_mrr_at_10_std
      value: 27.903299999999998
    - type: nauc_mrr_at_10_diff1
      value: 31.4959
    - type: nauc_mrr_at_20_max
      value: 59.7104
    - type: nauc_mrr_at_20_std
      value: 28.2328
    - type: nauc_mrr_at_20_diff1
      value: 31.330099999999998
    - type: nauc_mrr_at_100_max
      value: 59.573600000000006
    - type: nauc_mrr_at_100_std
      value: 28.044900000000002
    - type: nauc_mrr_at_100_diff1
      value: 31.305100000000003
    - type: nauc_mrr_at_1000_max
      value: 59.5608
    - type: nauc_mrr_at_1000_std
      value: 28.0034
    - type: nauc_mrr_at_1000_diff1
      value: 31.314199999999996
    - type: main_score
      value: 35.762
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ (default)
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: ndcg_at_1
      value: 39.89
    - type: ndcg_at_3
      value: 51.121
    - type: ndcg_at_5
      value: 55.184
    - type: ndcg_at_10
      value: 58.63699999999999
    - type: ndcg_at_20
      value: 60.659
    - type: ndcg_at_100
      value: 62.429
    - type: ndcg_at_1000
      value: 62.965
    - type: map_at_1
      value: 35.361
    - type: map_at_3
      value: 47.071000000000005
    - type: map_at_5
      value: 49.571
    - type: map_at_10
      value: 51.178999999999995
    - type: map_at_20
      value: 51.827999999999996
    - type: map_at_100
      value: 52.117000000000004
    - type: map_at_1000
      value: 52.141000000000005
    - type: recall_at_1
      value: 35.361
    - type: recall_at_3
      value: 59.40299999999999
    - type: recall_at_5
      value: 68.721
    - type: recall_at_10
      value: 78.64
    - type: recall_at_20
      value: 86.066
    - type: recall_at_100
      value: 94.865
    - type: recall_at_1000
      value: 98.79299999999999
    - type: precision_at_1
      value: 39.89
    - type: precision_at_3
      value: 23.078000000000003
    - type: precision_at_5
      value: 16.182
    - type: precision_at_10
      value: 9.363000000000001
    - type: precision_at_20
      value: 5.165
    - type: precision_at_100
      value: 1.15
    - type: precision_at_1000
      value: 0.12
    - type: mrr_at_1
      value: 39.8899
    - type: mrr_at_3
      value: 50.507000000000005
    - type: mrr_at_5
      value: 52.4899
    - type: mrr_at_10
      value: 53.761700000000005
    - type: mrr_at_20
      value: 54.223600000000005
    - type: mrr_at_100
      value: 54.427800000000005
    - type: mrr_at_1000
      value: 54.443299999999994
    - type: nauc_ndcg_at_1_max
      value: 19.524
    - type: nauc_ndcg_at_1_std
      value: -5.1782
    - type: nauc_ndcg_at_1_diff1
      value: 35.5793
    - type: nauc_ndcg_at_3_max
      value: 24.2974
    - type: nauc_ndcg_at_3_std
      value: -5.2507
    - type: nauc_ndcg_at_3_diff1
      value: 29.9937
    - type: nauc_ndcg_at_5_max
      value: 26.502100000000002
    - type: nauc_ndcg_at_5_std
      value: -3.6393
    - type: nauc_ndcg_at_5_diff1
      value: 30.0319
    - type: nauc_ndcg_at_10_max
      value: 26.66
    - type: nauc_ndcg_at_10_std
      value: -2.3816
    - type: nauc_ndcg_at_10_diff1
      value: 30.678100000000004
    - type: nauc_ndcg_at_20_max
      value: 26.9991
    - type: nauc_ndcg_at_20_std
      value: -1.5933
    - type: nauc_ndcg_at_20_diff1
      value: 30.824
    - type: nauc_ndcg_at_100_max
      value: 26.879199999999997
    - type: nauc_ndcg_at_100_std
      value: -0.8982
    - type: nauc_ndcg_at_100_diff1
      value: 31.338
    - type: nauc_ndcg_at_1000_max
      value: 26.2157
    - type: nauc_ndcg_at_1000_std
      value: -1.6907999999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 31.428099999999997
    - type: nauc_map_at_1_max
      value: 17.2868
    - type: nauc_map_at_1_std
      value: -7.0931
    - type: nauc_map_at_1_diff1
      value: 35.9826
    - type: nauc_map_at_3_max
      value: 23.0406
    - type: nauc_map_at_3_std
      value: -5.973599999999999
    - type: nauc_map_at_3_diff1
      value: 31.9658
    - type: nauc_map_at_5_max
      value: 24.3828
    - type: nauc_map_at_5_std
      value: -4.8592
    - type: nauc_map_at_5_diff1
      value: 31.9392
    - type: nauc_map_at_10_max
      value: 24.4782
    - type: nauc_map_at_10_std
      value: -4.2431
    - type: nauc_map_at_10_diff1
      value: 32.130399999999995
    - type: nauc_map_at_20_max
      value: 24.5589
    - type: nauc_map_at_20_std
      value: -3.9991
    - type: nauc_map_at_20_diff1
      value: 32.201299999999996
    - type: nauc_map_at_100_max
      value: 24.5696
    - type: nauc_map_at_100_std
      value: -3.8531999999999997
    - type: nauc_map_at_100_diff1
      value: 32.284
    - type: nauc_map_at_1000_max
      value: 24.546599999999998
    - type: nauc_map_at_1000_std
      value: -3.8784
    - type: nauc_map_at_1000_diff1
      value: 32.2879
    - type: nauc_recall_at_1_max
      value: 17.2868
    - type: nauc_recall_at_1_std
      value: -7.0931
    - type: nauc_recall_at_1_diff1
      value: 35.9826
    - type: nauc_recall_at_3_max
      value: 26.753300000000003
    - type: nauc_recall_at_3_std
      value: -5.1822
    - type: nauc_recall_at_3_diff1
      value: 24.4274
    - type: nauc_recall_at_5_max
      value: 32.697900000000004
    - type: nauc_recall_at_5_std
      value: -1.4673
    - type: nauc_recall_at_5_diff1
      value: 23.5655
    - type: nauc_recall_at_10_max
      value: 35.22
    - type: nauc_recall_at_10_std
      value: 3.6904
    - type: nauc_recall_at_10_diff1
      value: 24.5926
    - type: nauc_recall_at_20_max
      value: 42.0975
    - type: nauc_recall_at_20_std
      value: 11.574
    - type: nauc_recall_at_20_diff1
      value: 23.5964
    - type: nauc_recall_at_100_max
      value: 62.5657
    - type: nauc_recall_at_100_std
      value: 45.2673
    - type: nauc_recall_at_100_diff1
      value: 26.6811
    - type: nauc_recall_at_1000_max
      value: 78.6598
    - type: nauc_recall_at_1000_std
      value: 70.7318
    - type: nauc_recall_at_1000_diff1
      value: 29.530099999999997
    - type: nauc_precision_at_1_max
      value: 19.524
    - type: nauc_precision_at_1_std
      value: -5.1782
    - type: nauc_precision_at_1_diff1
      value: 35.5793
    - type: nauc_precision_at_3_max
      value: 27.230999999999998
    - type: nauc_precision_at_3_std
      value: 0.13649999999999998
    - type: nauc_precision_at_3_diff1
      value: 18.817500000000003
    - type: nauc_precision_at_5_max
      value: 28.734700000000004
    - type: nauc_precision_at_5_std
      value: 5.1929
    - type: nauc_precision_at_5_diff1
      value: 14.3006
    - type: nauc_precision_at_10_max
      value: 25.3071
    - type: nauc_precision_at_10_std
      value: 11.0166
    - type: nauc_precision_at_10_diff1
      value: 9.481
    - type: nauc_precision_at_20_max
      value: 22.5098
    - type: nauc_precision_at_20_std
      value: 15.695400000000001
    - type: nauc_precision_at_20_diff1
      value: 4.5483
    - type: nauc_precision_at_100_max
      value: 15.834999999999999
    - type: nauc_precision_at_100_std
      value: 21.391099999999998
    - type: nauc_precision_at_100_diff1
      value: -2.3594
    - type: nauc_precision_at_1000_max
      value: 7.2892
    - type: nauc_precision_at_1000_std
      value: 16.1876
    - type: nauc_precision_at_1000_diff1
      value: -6.698900000000001
    - type: nauc_mrr_at_1_max
      value: 19.524
    - type: nauc_mrr_at_1_std
      value: -5.1782
    - type: nauc_mrr_at_1_diff1
      value: 35.5793
    - type: nauc_mrr_at_3_max
      value: 23.3415
    - type: nauc_mrr_at_3_std
      value: -3.7981000000000003
    - type: nauc_mrr_at_3_diff1
      value: 30.531799999999997
    - type: nauc_mrr_at_5_max
      value: 24.2743
    - type: nauc_mrr_at_5_std
      value: -3.1985
    - type: nauc_mrr_at_5_diff1
      value: 30.7564
    - type: nauc_mrr_at_10_max
      value: 24.1952
    - type: nauc_mrr_at_10_std
      value: -2.9042
    - type: nauc_mrr_at_10_diff1
      value: 31.2183
    - type: nauc_mrr_at_20_max
      value: 24.2339
    - type: nauc_mrr_at_20_std
      value: -2.8143000000000002
    - type: nauc_mrr_at_20_diff1
      value: 31.252999999999997
    - type: nauc_mrr_at_100_max
      value: 24.1954
    - type: nauc_mrr_at_100_std
      value: -2.7797
    - type: nauc_mrr_at_100_diff1
      value: 31.3283
    - type: nauc_mrr_at_1000_max
      value: 24.1793
    - type: nauc_mrr_at_1000_std
      value: -2.7987
    - type: nauc_mrr_at_1000_diff1
      value: 31.330099999999998
    - type: main_score
      value: 58.63699999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval (default)
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: ndcg_at_1
      value: 83.33
    - type: ndcg_at_3
      value: 87.21900000000001
    - type: ndcg_at_5
      value: 88.725
    - type: ndcg_at_10
      value: 89.848
    - type: ndcg_at_20
      value: 90.426
    - type: ndcg_at_100
      value: 90.881
    - type: ndcg_at_1000
      value: 90.947
    - type: map_at_1
      value: 72.354
    - type: map_at_3
      value: 83.447
    - type: map_at_5
      value: 85.3
    - type: map_at_10
      value: 86.33800000000001
    - type: map_at_20
      value: 86.752
    - type: map_at_100
      value: 86.952
    - type: map_at_1000
      value: 86.965
    - type: recall_at_1
      value: 72.354
    - type: recall_at_3
      value: 88.726
    - type: recall_at_5
      value: 93.07900000000001
    - type: recall_at_10
      value: 96.392
    - type: recall_at_20
      value: 98.185
    - type: recall_at_100
      value: 99.737
    - type: recall_at_1000
      value: 99.994
    - type: precision_at_1
      value: 83.33
    - type: precision_at_3
      value: 38.163000000000004
    - type: precision_at_5
      value: 25.054
    - type: precision_at_10
      value: 13.600000000000001
    - type: precision_at_20
      value: 7.199999999999999
    - type: precision_at_100
      value: 1.539
    - type: precision_at_1000
      value: 0.157
    - type: mrr_at_1
      value: 83.33
    - type: mrr_at_3
      value: 88.2583
    - type: mrr_at_5
      value: 88.8703
    - type: mrr_at_10
      value: 89.1146
    - type: mrr_at_20
      value: 89.1631
    - type: mrr_at_100
      value: 89.1825
    - type: mrr_at_1000
      value: 89.1829
    - type: nauc_ndcg_at_1_max
      value: 35.1345
    - type: nauc_ndcg_at_1_std
      value: -51.2196
    - type: nauc_ndcg_at_1_diff1
      value: 78.4909
    - type: nauc_ndcg_at_3_max
      value: 32.547399999999996
    - type: nauc_ndcg_at_3_std
      value: -59.377500000000005
    - type: nauc_ndcg_at_3_diff1
      value: 76.46300000000001
    - type: nauc_ndcg_at_5_max
      value: 33.5504
    - type: nauc_ndcg_at_5_std
      value: -60.3836
    - type: nauc_ndcg_at_5_diff1
      value: 76.9467
    - type: nauc_ndcg_at_10_max
      value: 34.1371
    - type: nauc_ndcg_at_10_std
      value: -59.3526
    - type: nauc_ndcg_at_10_diff1
      value: 77.1373
    - type: nauc_ndcg_at_20_max
      value: 34.5537
    - type: nauc_ndcg_at_20_std
      value: -57.8514
    - type: nauc_ndcg_at_20_diff1
      value: 77.2059
    - type: nauc_ndcg_at_100_max
      value: 34.8817
    - type: nauc_ndcg_at_100_std
      value: -55.6778
    - type: nauc_ndcg_at_100_diff1
      value: 77.08080000000001
    - type: nauc_ndcg_at_1000_max
      value: 35.0003
    - type: nauc_ndcg_at_1000_std
      value: -55.292699999999996
    - type: nauc_ndcg_at_1000_diff1
      value: 77.078
    - type: nauc_map_at_1_max
      value: 24.889400000000002
    - type: nauc_map_at_1_std
      value: -50.5244
    - type: nauc_map_at_1_diff1
      value: 80.9461
    - type: nauc_map_at_3_max
      value: 30.461899999999996
    - type: nauc_map_at_3_std
      value: -61.017999999999994
    - type: nauc_map_at_3_diff1
      value: 77.8986
    - type: nauc_map_at_5_max
      value: 31.995800000000003
    - type: nauc_map_at_5_std
      value: -61.0579
    - type: nauc_map_at_5_diff1
      value: 77.6265
    - type: nauc_map_at_10_max
      value: 32.9371
    - type: nauc_map_at_10_std
      value: -59.662099999999995
    - type: nauc_map_at_10_diff1
      value: 77.3695
    - type: nauc_map_at_20_max
      value: 33.3268
    - type: nauc_map_at_20_std
      value: -58.4642
    - type: nauc_map_at_20_diff1
      value: 77.2616
    - type: nauc_map_at_100_max
      value: 33.481300000000005
    - type: nauc_map_at_100_std
      value: -57.51349999999999
    - type: nauc_map_at_100_diff1
      value: 77.1762
    - type: nauc_map_at_1000_max
      value: 33.51
    - type: nauc_map_at_1000_std
      value: -57.4361
    - type: nauc_map_at_1000_diff1
      value: 77.173
    - type: nauc_recall_at_1_max
      value: 24.889400000000002
    - type: nauc_recall_at_1_std
      value: -50.5244
    - type: nauc_recall_at_1_diff1
      value: 80.9461
    - type: nauc_recall_at_3_max
      value: 26.490399999999998
    - type: nauc_recall_at_3_std
      value: -70.6466
    - type: nauc_recall_at_3_diff1
      value: 74.3857
    - type: nauc_recall_at_5_max
      value: 28.3327
    - type: nauc_recall_at_5_std
      value: -77.8455
    - type: nauc_recall_at_5_diff1
      value: 73.348
    - type: nauc_recall_at_10_max
      value: 30.476999999999997
    - type: nauc_recall_at_10_std
      value: -84.933
    - type: nauc_recall_at_10_diff1
      value: 73.7724
    - type: nauc_recall_at_20_max
      value: 31.954700000000003
    - type: nauc_recall_at_20_std
      value: -88.4871
    - type: nauc_recall_at_20_diff1
      value: 75.3748
    - type: nauc_recall_at_100_max
      value: 26.290799999999997
    - type: nauc_recall_at_100_std
      value: -86.7429
    - type: nauc_recall_at_100_diff1
      value: 71.1186
    - type: nauc_recall_at_1000_max
      value: -46.823100000000004
    - type: nauc_recall_at_1000_std
      value: -34.474
    - type: nauc_recall_at_1000_diff1
      value: 43.9622
    - type: nauc_precision_at_1_max
      value: 35.1345
    - type: nauc_precision_at_1_std
      value: -51.2196
    - type: nauc_precision_at_1_diff1
      value: 78.4909
    - type: nauc_precision_at_3_max
      value: 5.0033
    - type: nauc_precision_at_3_std
      value: 6.1183000000000005
    - type: nauc_precision_at_3_diff1
      value: -23.093
    - type: nauc_precision_at_5_max
      value: 0.8462000000000001
    - type: nauc_precision_at_5_std
      value: 19.284599999999998
    - type: nauc_precision_at_5_diff1
      value: -34.740700000000004
    - type: nauc_precision_at_10_max
      value: -2.476
    - type: nauc_precision_at_10_std
      value: 30.449900000000003
    - type: nauc_precision_at_10_diff1
      value: -41.373
    - type: nauc_precision_at_20_max
      value: -4.067
    - type: nauc_precision_at_20_std
      value: 37.2089
    - type: nauc_precision_at_20_diff1
      value: -43.4846
    - type: nauc_precision_at_100_max
      value: -5.4187
    - type: nauc_precision_at_100_std
      value: 44.7639
    - type: nauc_precision_at_100_diff1
      value: -44.9325
    - type: nauc_precision_at_1000_max
      value: -5.309
    - type: nauc_precision_at_1000_std
      value: 46.4094
    - type: nauc_precision_at_1000_diff1
      value: -45.0127
    - type: nauc_mrr_at_1_max
      value: 35.1345
    - type: nauc_mrr_at_1_std
      value: -51.2196
    - type: nauc_mrr_at_1_diff1
      value: 78.4909
    - type: nauc_mrr_at_3_max
      value: 35.5355
    - type: nauc_mrr_at_3_std
      value: -54.636399999999995
    - type: nauc_mrr_at_3_diff1
      value: 77.537
    - type: nauc_mrr_at_5_max
      value: 35.8853
    - type: nauc_mrr_at_5_std
      value: -54.1871
    - type: nauc_mrr_at_5_diff1
      value: 77.6977
    - type: nauc_mrr_at_10_max
      value: 35.8488
    - type: nauc_mrr_at_10_std
      value: -53.825599999999994
    - type: nauc_mrr_at_10_diff1
      value: 77.7459
    - type: nauc_mrr_at_20_max
      value: 35.7887
    - type: nauc_mrr_at_20_std
      value: -53.778800000000004
    - type: nauc_mrr_at_20_diff1
      value: 77.7606
    - type: nauc_mrr_at_100_max
      value: 35.7656
    - type: nauc_mrr_at_100_std
      value: -53.74640000000001
    - type: nauc_mrr_at_100_diff1
      value: 77.7597
    - type: nauc_mrr_at_1000_max
      value: 35.7642
    - type: nauc_mrr_at_1000_std
      value: -53.744899999999994
    - type: nauc_mrr_at_1000_diff1
      value: 77.7598
    - type: main_score
      value: 89.848
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: v_measure
      value: 58.794599999999996
    - type: v_measure_std
      value: 3.7606
    - type: main_score
      value: 58.794599999999996
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P (default)
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: v_measure
      value: 65.4871
    - type: v_measure_std
      value: 13.1853
    - type: main_score
      value: 65.4871
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS (default)
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: ndcg_at_1
      value: 26.0
    - type: ndcg_at_3
      value: 21.369
    - type: ndcg_at_5
      value: 18.865000000000002
    - type: ndcg_at_10
      value: 22.847
    - type: ndcg_at_20
      value: 25.817
    - type: ndcg_at_100
      value: 31.824
    - type: ndcg_at_1000
      value: 37.997
    - type: map_at_1
      value: 5.268
    - type: map_at_3
      value: 9.604
    - type: map_at_5
      value: 11.797
    - type: map_at_10
      value: 13.891
    - type: map_at_20
      value: 15.062000000000001
    - type: map_at_100
      value: 16.323
    - type: map_at_1000
      value: 16.71
    - type: recall_at_1
      value: 5.268
    - type: recall_at_3
      value: 12.203
    - type: recall_at_5
      value: 16.963
    - type: recall_at_10
      value: 24.29
    - type: recall_at_20
      value: 31.267
    - type: recall_at_100
      value: 50.727
    - type: recall_at_1000
      value: 80.67800000000001
    - type: precision_at_1
      value: 26.0
    - type: precision_at_3
      value: 20.067
    - type: precision_at_5
      value: 16.74
    - type: precision_at_10
      value: 11.97
    - type: precision_at_20
      value: 7.7
    - type: precision_at_100
      value: 2.4979999999999998
    - type: precision_at_1000
      value: 0.398
    - type: mrr_at_1
      value: 26.0
    - type: mrr_at_3
      value: 34.2833
    - type: mrr_at_5
      value: 35.9333
    - type: mrr_at_10
      value: 37.5791
    - type: mrr_at_20
      value: 38.1301
    - type: mrr_at_100
      value: 38.556200000000004
    - type: mrr_at_1000
      value: 38.606899999999996
    - type: nauc_ndcg_at_1_max
      value: 21.9327
    - type: nauc_ndcg_at_1_std
      value: 8.761800000000001
    - type: nauc_ndcg_at_1_diff1
      value: 22.0695
    - type: nauc_ndcg_at_3_max
      value: 27.475300000000004
    - type: nauc_ndcg_at_3_std
      value: 11.126
    - type: nauc_ndcg_at_3_diff1
      value: 17.1458
    - type: nauc_ndcg_at_5_max
      value: 28.116200000000003
    - type: nauc_ndcg_at_5_std
      value: 13.919799999999999
    - type: nauc_ndcg_at_5_diff1
      value: 15.894400000000001
    - type: nauc_ndcg_at_10_max
      value: 30.3757
    - type: nauc_ndcg_at_10_std
      value: 17.2527
    - type: nauc_ndcg_at_10_diff1
      value: 14.1508
    - type: nauc_ndcg_at_20_max
      value: 31.451600000000003
    - type: nauc_ndcg_at_20_std
      value: 19.9009
    - type: nauc_ndcg_at_20_diff1
      value: 13.5029
    - type: nauc_ndcg_at_100_max
      value: 33.9342
    - type: nauc_ndcg_at_100_std
      value: 25.7798
    - type: nauc_ndcg_at_100_diff1
      value: 14.335500000000001
    - type: nauc_ndcg_at_1000_max
      value: 33.5581
    - type: nauc_ndcg_at_1000_std
      value: 25.082300000000004
    - type: nauc_ndcg_at_1000_diff1
      value: 14.223099999999999
    - type: nauc_map_at_1_max
      value: 22.0412
    - type: nauc_map_at_1_std
      value: 8.932
    - type: nauc_map_at_1_diff1
      value: 22.2384
    - type: nauc_map_at_3_max
      value: 26.761400000000002
    - type: nauc_map_at_3_std
      value: 9.1566
    - type: nauc_map_at_3_diff1
      value: 17.2375
    - type: nauc_map_at_5_max
      value: 27.7594
    - type: nauc_map_at_5_std
      value: 12.6506
    - type: nauc_map_at_5_diff1
      value: 15.739600000000001
    - type: nauc_map_at_10_max
      value: 29.6498
    - type: nauc_map_at_10_std
      value: 15.2716
    - type: nauc_map_at_10_diff1
      value: 14.638000000000002
    - type: nauc_map_at_20_max
      value: 30.1827
    - type: nauc_map_at_20_std
      value: 16.7742
    - type: nauc_map_at_20_diff1
      value: 14.0863
    - type: nauc_map_at_100_max
      value: 31.3787
    - type: nauc_map_at_100_std
      value: 19.3168
    - type: nauc_map_at_100_diff1
      value: 14.3807
    - type: nauc_map_at_1000_max
      value: 31.3749
    - type: nauc_map_at_1000_std
      value: 19.4008
    - type: nauc_map_at_1000_diff1
      value: 14.3151
    - type: nauc_recall_at_1_max
      value: 22.0412
    - type: nauc_recall_at_1_std
      value: 8.932
    - type: nauc_recall_at_1_diff1
      value: 22.2384
    - type: nauc_recall_at_3_max
      value: 29.4548
    - type: nauc_recall_at_3_std
      value: 12.4116
    - type: nauc_recall_at_3_diff1
      value: 14.9834
    - type: nauc_recall_at_5_max
      value: 28.7014
    - type: nauc_recall_at_5_std
      value: 16.1355
    - type: nauc_recall_at_5_diff1
      value: 12.4951
    - type: nauc_recall_at_10_max
      value: 31.2425
    - type: nauc_recall_at_10_std
      value: 21.3563
    - type: nauc_recall_at_10_diff1
      value: 9.0205
    - type: nauc_recall_at_20_max
      value: 31.478
    - type: nauc_recall_at_20_std
      value: 25.4813
    - type: nauc_recall_at_20_diff1
      value: 7.3628
    - type: nauc_recall_at_100_max
      value: 33.596199999999996
    - type: nauc_recall_at_100_std
      value: 37.5122
    - type: nauc_recall_at_100_diff1
      value: 8.3252
    - type: nauc_recall_at_1000_max
      value: 30.4869
    - type: nauc_recall_at_1000_std
      value: 38.8306
    - type: nauc_recall_at_1000_diff1
      value: 4.6079
    - type: nauc_precision_at_1_max
      value: 21.9327
    - type: nauc_precision_at_1_std
      value: 8.761800000000001
    - type: nauc_precision_at_1_diff1
      value: 22.0695
    - type: nauc_precision_at_3_max
      value: 29.608600000000003
    - type: nauc_precision_at_3_std
      value: 12.3347
    - type: nauc_precision_at_3_diff1
      value: 14.810200000000002
    - type: nauc_precision_at_5_max
      value: 28.8061
    - type: nauc_precision_at_5_std
      value: 16.0502
    - type: nauc_precision_at_5_diff1
      value: 12.251900000000001
    - type: nauc_precision_at_10_max
      value: 31.3513
    - type: nauc_precision_at_10_std
      value: 21.226300000000002
    - type: nauc_precision_at_10_diff1
      value: 8.772499999999999
    - type: nauc_precision_at_20_max
      value: 31.692999999999998
    - type: nauc_precision_at_20_std
      value: 25.4628
    - type: nauc_precision_at_20_diff1
      value: 7.1315
    - type: nauc_precision_at_100_max
      value: 33.3115
    - type: nauc_precision_at_100_std
      value: 36.888799999999996
    - type: nauc_precision_at_100_diff1
      value: 7.820100000000001
    - type: nauc_precision_at_1000_max
      value: 29.1927
    - type: nauc_precision_at_1000_std
      value: 36.2523
    - type: nauc_precision_at_1000_diff1
      value: 3.5833999999999997
    - type: nauc_mrr_at_1_max
      value: 21.9327
    - type: nauc_mrr_at_1_std
      value: 8.761800000000001
    - type: nauc_mrr_at_1_diff1
      value: 22.0695
    - type: nauc_mrr_at_3_max
      value: 26.1187
    - type: nauc_mrr_at_3_std
      value: 12.5639
    - type: nauc_mrr_at_3_diff1
      value: 19.642599999999998
    - type: nauc_mrr_at_5_max
      value: 25.8562
    - type: nauc_mrr_at_5_std
      value: 12.495000000000001
    - type: nauc_mrr_at_5_diff1
      value: 19.3465
    - type: nauc_mrr_at_10_max
      value: 26.218200000000003
    - type: nauc_mrr_at_10_std
      value: 13.1243
    - type: nauc_mrr_at_10_diff1
      value: 18.9542
    - type: nauc_mrr_at_20_max
      value: 26.422099999999997
    - type: nauc_mrr_at_20_std
      value: 13.4214
    - type: nauc_mrr_at_20_diff1
      value: 19.0105
    - type: nauc_mrr_at_100_max
      value: 26.338
    - type: nauc_mrr_at_100_std
      value: 13.4264
    - type: nauc_mrr_at_100_diff1
      value: 18.9729
    - type: nauc_mrr_at_1000_max
      value: 26.3327
    - type: nauc_mrr_at_1000_std
      value: 13.3904
    - type: nauc_mrr_at_1000_diff1
      value: 19.004199999999997
    - type: main_score
      value: 22.847
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: pearson
      value: 81.13050000000001
    - type: spearman
      value: 79.01310000000001
    - type: cosine_pearson
      value: 81.13050000000001
    - type: cosine_spearman
      value: 79.01310000000001
    - type: manhattan_pearson
      value: 79.03999999999999
    - type: manhattan_spearman
      value: 79.1744
    - type: euclidean_pearson
      value: 79.0977
    - type: euclidean_spearman
      value: 79.2268
    - type: main_score
      value: 79.01310000000001
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: pearson
      value: 86.9675
    - type: spearman
      value: 80.3531
    - type: cosine_pearson
      value: 86.9675
    - type: cosine_spearman
      value: 80.3531
    - type: manhattan_pearson
      value: 82.2315
    - type: manhattan_spearman
      value: 79.7004
    - type: euclidean_pearson
      value: 82.3305
    - type: euclidean_spearman
      value: 79.8601
    - type: main_score
      value: 80.3531
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: pearson
      value: 85.6041
    - type: spearman
      value: 86.0453
    - type: cosine_pearson
      value: 85.6041
    - type: cosine_spearman
      value: 86.0453
    - type: manhattan_pearson
      value: 85.2548
    - type: manhattan_spearman
      value: 85.8908
    - type: euclidean_pearson
      value: 85.253
    - type: euclidean_spearman
      value: 85.9181
    - type: main_score
      value: 86.0453
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: pearson
      value: 82.8792
    - type: spearman
      value: 82.9681
    - type: cosine_pearson
      value: 82.8792
    - type: cosine_spearman
      value: 82.9681
    - type: manhattan_pearson
      value: 81.4789
    - type: manhattan_spearman
      value: 82.4797
    - type: euclidean_pearson
      value: 81.4674
    - type: euclidean_spearman
      value: 82.4547
    - type: main_score
      value: 82.9681
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: pearson
      value: 87.5356
    - type: spearman
      value: 88.06540000000001
    - type: cosine_pearson
      value: 87.5356
    - type: cosine_spearman
      value: 88.06540000000001
    - type: manhattan_pearson
      value: 87.10759999999999
    - type: manhattan_spearman
      value: 87.75309999999999
    - type: euclidean_pearson
      value: 87.1489
    - type: euclidean_spearman
      value: 87.7857
    - type: main_score
      value: 88.06540000000001
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: pearson
      value: 85.0208
    - type: spearman
      value: 86.0136
    - type: cosine_pearson
      value: 85.0208
    - type: cosine_spearman
      value: 86.0136
    - type: manhattan_pearson
      value: 85.22
    - type: manhattan_spearman
      value: 86.1101
    - type: euclidean_pearson
      value: 85.2043
    - type: euclidean_spearman
      value: 86.113
    - type: main_score
      value: 86.0136
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 89.4083
    - type: spearman
      value: 88.9498
    - type: cosine_pearson
      value: 89.4083
    - type: cosine_spearman
      value: 88.9498
    - type: manhattan_pearson
      value: 89.46539999999999
    - type: manhattan_spearman
      value: 88.8754
    - type: euclidean_pearson
      value: 89.4326
    - type: euclidean_spearman
      value: 88.8148
    - type: main_score
      value: 88.9498
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 66.60770000000001
    - type: spearman
      value: 67.1515
    - type: cosine_pearson
      value: 66.60770000000001
    - type: cosine_spearman
      value: 67.1515
    - type: manhattan_pearson
      value: 66.5604
    - type: manhattan_spearman
      value: 66.4621
    - type: euclidean_pearson
      value: 66.4628
    - type: euclidean_spearman
      value: 66.2979
    - type: main_score
      value: 67.1515
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: pearson
      value: 86.86399999999999
    - type: spearman
      value: 87.7139
    - type: cosine_pearson
      value: 86.86399999999999
    - type: cosine_spearman
      value: 87.7139
    - type: manhattan_pearson
      value: 86.6602
    - type: manhattan_spearman
      value: 87.2606
    - type: euclidean_pearson
      value: 86.5924
    - type: euclidean_spearman
      value: 87.241
    - type: main_score
      value: 87.7139
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR (default)
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: map
      value: 84.37360000000001
    - type: mrr
      value: 95.6275
    - type: nAUC_map_max
      value: 52.991699999999994
    - type: nAUC_map_std
      value: 66.8168
    - type: nAUC_map_diff1
      value: -3.2009999999999996
    - type: nAUC_mrr_max
      value: 85.7492
    - type: nAUC_mrr_std
      value: 77.3543
    - type: nAUC_mrr_diff1
      value: 38.014700000000005
    - type: main_score
      value: 84.37360000000001
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: ndcg_at_1
      value: 60.667
    - type: ndcg_at_3
      value: 68.209
    - type: ndcg_at_5
      value: 71.409
    - type: ndcg_at_10
      value: 73.476
    - type: ndcg_at_20
      value: 74.339
    - type: ndcg_at_100
      value: 75.57000000000001
    - type: ndcg_at_1000
      value: 75.955
    - type: map_at_1
      value: 58.178
    - type: map_at_3
      value: 65.71900000000001
    - type: map_at_5
      value: 67.73
    - type: map_at_10
      value: 68.821
    - type: map_at_20
      value: 69.07600000000001
    - type: map_at_100
      value: 69.245
    - type: map_at_1000
      value: 69.258
    - type: recall_at_1
      value: 58.178
    - type: recall_at_3
      value: 73.172
    - type: recall_at_5
      value: 81.0
    - type: recall_at_10
      value: 86.867
    - type: recall_at_20
      value: 90.267
    - type: recall_at_100
      value: 96.933
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 60.667
    - type: precision_at_3
      value: 26.444000000000003
    - type: precision_at_5
      value: 18.0
    - type: precision_at_10
      value: 9.866999999999999
    - type: precision_at_20
      value: 5.133
    - type: precision_at_100
      value: 1.097
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: mrr_at_1
      value: 60.6667
    - type: mrr_at_3
      value: 67.1667
    - type: mrr_at_5
      value: 68.85
    - type: mrr_at_10
      value: 69.4799
    - type: mrr_at_20
      value: 69.6658
    - type: mrr_at_100
      value: 69.8134
    - type: mrr_at_1000
      value: 69.8257
    - type: nauc_ndcg_at_1_max
      value: 49.3608
    - type: nauc_ndcg_at_1_std
      value: 12.742400000000002
    - type: nauc_ndcg_at_1_diff1
      value: 74.5012
    - type: nauc_ndcg_at_3_max
      value: 49.524499999999996
    - type: nauc_ndcg_at_3_std
      value: 7.7241
    - type: nauc_ndcg_at_3_diff1
      value: 72.0127
    - type: nauc_ndcg_at_5_max
      value: 51.897099999999995
    - type: nauc_ndcg_at_5_std
      value: 12.8641
    - type: nauc_ndcg_at_5_diff1
      value: 69.7789
    - type: nauc_ndcg_at_10_max
      value: 55.1141
    - type: nauc_ndcg_at_10_std
      value: 17.136499999999998
    - type: nauc_ndcg_at_10_diff1
      value: 68.8711
    - type: nauc_ndcg_at_20_max
      value: 54.74719999999999
    - type: nauc_ndcg_at_20_std
      value: 17.0485
    - type: nauc_ndcg_at_20_diff1
      value: 69.4701
    - type: nauc_ndcg_at_100_max
      value: 53.7619
    - type: nauc_ndcg_at_100_std
      value: 15.335299999999998
    - type: nauc_ndcg_at_100_diff1
      value: 70.34479999999999
    - type: nauc_ndcg_at_1000_max
      value: 53.4516
    - type: nauc_ndcg_at_1000_std
      value: 14.7843
    - type: nauc_ndcg_at_1000_diff1
      value: 70.6041
    - type: nauc_map_at_1_max
      value: 44.9654
    - type: nauc_map_at_1_std
      value: 5.9821
    - type: nauc_map_at_1_diff1
      value: 76.2581
    - type: nauc_map_at_3_max
      value: 47.515299999999996
    - type: nauc_map_at_3_std
      value: 6.2703
    - type: nauc_map_at_3_diff1
      value: 73.5279
    - type: nauc_map_at_5_max
      value: 49.805899999999994
    - type: nauc_map_at_5_std
      value: 10.1001
    - type: nauc_map_at_5_diff1
      value: 72.1812
    - type: nauc_map_at_10_max
      value: 51.9276
    - type: nauc_map_at_10_std
      value: 12.698200000000002
    - type: nauc_map_at_10_diff1
      value: 71.6343
    - type: nauc_map_at_20_max
      value: 51.8856
    - type: nauc_map_at_20_std
      value: 12.814800000000002
    - type: nauc_map_at_20_diff1
      value: 71.78179999999999
    - type: nauc_map_at_100_max
      value: 51.7504
    - type: nauc_map_at_100_std
      value: 12.5353
    - type: nauc_map_at_100_diff1
      value: 71.8854
    - type: nauc_map_at_1000_max
      value: 51.739900000000006
    - type: nauc_map_at_1000_std
      value: 12.519
    - type: nauc_map_at_1000_diff1
      value: 71.8964
    - type: nauc_recall_at_1_max
      value: 44.9654
    - type: nauc_recall_at_1_std
      value: 5.9821
    - type: nauc_recall_at_1_diff1
      value: 76.2581
    - type: nauc_recall_at_3_max
      value: 47.9306
    - type: nauc_recall_at_3_std
      value: 3.5374000000000003
    - type: nauc_recall_at_3_diff1
      value: 68.4552
    - type: nauc_recall_at_5_max
      value: 54.374
    - type: nauc_recall_at_5_std
      value: 17.646700000000003
    - type: nauc_recall_at_5_diff1
      value: 60.5644
    - type: nauc_recall_at_10_max
      value: 69.6484
    - type: nauc_recall_at_10_std
      value: 38.3671
    - type: nauc_recall_at_10_diff1
      value: 54.39580000000001
    - type: nauc_recall_at_20_max
      value: 70.0061
    - type: nauc_recall_at_20_std
      value: 42.403999999999996
    - type: nauc_recall_at_20_diff1
      value: 55.3831
    - type: nauc_recall_at_100_max
      value: 69.02629999999999
    - type: nauc_recall_at_100_std
      value: 43.850699999999996
    - type: nauc_recall_at_100_diff1
      value: 57.837
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 49.3608
    - type: nauc_precision_at_1_std
      value: 12.742400000000002
    - type: nauc_precision_at_1_diff1
      value: 74.5012
    - type: nauc_precision_at_3_max
      value: 45.2627
    - type: nauc_precision_at_3_std
      value: 15.5113
    - type: nauc_precision_at_3_diff1
      value: 44.5108
    - type: nauc_precision_at_5_max
      value: 48.4003
    - type: nauc_precision_at_5_std
      value: 35.3791
    - type: nauc_precision_at_5_diff1
      value: 19.7518
    - type: nauc_precision_at_10_max
      value: 46.688
    - type: nauc_precision_at_10_std
      value: 47.9876
    - type: nauc_precision_at_10_diff1
      value: 0.1083
    - type: nauc_precision_at_20_max
      value: 41.281400000000005
    - type: nauc_precision_at_20_std
      value: 49.0662
    - type: nauc_precision_at_20_diff1
      value: -6.2035
    - type: nauc_precision_at_100_max
      value: 30.0167
    - type: nauc_precision_at_100_std
      value: 47.2561
    - type: nauc_precision_at_100_diff1
      value: -22.8584
    - type: nauc_precision_at_1000_max
      value: 23.724999999999998
    - type: nauc_precision_at_1000_std
      value: 45.342
    - type: nauc_precision_at_1000_diff1
      value: -33.29
    - type: nauc_mrr_at_1_max
      value: 49.3608
    - type: nauc_mrr_at_1_std
      value: 12.742400000000002
    - type: nauc_mrr_at_1_diff1
      value: 74.5012
    - type: nauc_mrr_at_3_max
      value: 51.1718
    - type: nauc_mrr_at_3_std
      value: 11.739700000000001
    - type: nauc_mrr_at_3_diff1
      value: 71.5992
    - type: nauc_mrr_at_5_max
      value: 52.2421
    - type: nauc_mrr_at_5_std
      value: 14.127
    - type: nauc_mrr_at_5_diff1
      value: 70.57
    - type: nauc_mrr_at_10_max
      value: 52.5587
    - type: nauc_mrr_at_10_std
      value: 14.5207
    - type: nauc_mrr_at_10_diff1
      value: 70.55709999999999
    - type: nauc_mrr_at_20_max
      value: 52.3699
    - type: nauc_mrr_at_20_std
      value: 14.310300000000002
    - type: nauc_mrr_at_20_diff1
      value: 70.6993
    - type: nauc_mrr_at_100_max
      value: 52.2734
    - type: nauc_mrr_at_100_std
      value: 14.0848
    - type: nauc_mrr_at_100_diff1
      value: 70.8146
    - type: nauc_mrr_at_1000_max
      value: 52.2622
    - type: nauc_mrr_at_1000_std
      value: 14.0715
    - type: nauc_mrr_at_1000_diff1
      value: 70.8239
    - type: main_score
      value: 73.476
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 99.87819999999999
    - type: similarity_accuracy_threshold
      value: 74.8
    - type: similarity_f1
      value: 93.79729999999999
    - type: similarity_f1_threshold
      value: 74.6812
    - type: similarity_precision
      value: 94.6083
    - type: similarity_recall
      value: 93.0
    - type: similarity_ap
      value: 97.1971
    - type: cosine_accuracy
      value: 99.87819999999999
    - type: cosine_accuracy_threshold
      value: 74.8
    - type: cosine_f1
      value: 93.79729999999999
    - type: cosine_f1_threshold
      value: 74.6812
    - type: cosine_precision
      value: 94.6083
    - type: cosine_recall
      value: 93.0
    - type: cosine_ap
      value: 97.1971
    - type: manhattan_accuracy
      value: 99.8792
    - type: manhattan_accuracy_threshold
      value: 47567.8925
    - type: manhattan_f1
      value: 93.8508
    - type: manhattan_f1_threshold
      value: 47567.8925
    - type: manhattan_precision
      value: 94.6138
    - type: manhattan_recall
      value: 93.10000000000001
    - type: manhattan_ap
      value: 97.2177
    - type: euclidean_accuracy
      value: 99.8812
    - type: euclidean_accuracy_threshold
      value: 2164.0619
    - type: euclidean_f1
      value: 93.9759
    - type: euclidean_f1_threshold
      value: 2164.0619
    - type: euclidean_precision
      value: 94.35480000000001
    - type: euclidean_recall
      value: 93.60000000000001
    - type: euclidean_ap
      value: 97.2412
    - type: dot_accuracy
      value: 99.8446
    - type: dot_accuracy_threshold
      value: 68470.2454
    - type: dot_f1
      value: 91.9939
    - type: dot_f1_threshold
      value: 68470.2454
    - type: dot_precision
      value: 93.8606
    - type: dot_recall
      value: 90.2
    - type: dot_ap
      value: 96.36829999999999
    - type: max_accuracy
      value: 99.8812
    - type: max_f1
      value: 93.9759
    - type: max_precision
      value: 94.6138
    - type: max_recall
      value: 93.60000000000001
    - type: max_ap
      value: 97.2412
    - type: main_score
      value: 97.2412
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: v_measure
      value: 70.04010000000001
    - type: v_measure_std
      value: 3.9558999999999997
    - type: main_score
      value: 70.04010000000001
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P (default)
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: v_measure
      value: 42.4207
    - type: v_measure_std
      value: 1.3677
    - type: main_score
      value: 42.4207
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions (default)
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: map
      value: 52.7026
    - type: mrr
      value: 53.5668
    - type: nAUC_map_max
      value: 12.1758
    - type: nAUC_map_std
      value: 6.7148
    - type: nAUC_map_diff1
      value: 39.881499999999996
    - type: nAUC_mrr_max
      value: 13.0771
    - type: nAUC_mrr_std
      value: 7.7001
    - type: nAUC_mrr_diff1
      value: 39.6391
    - type: main_score
      value: 52.7026
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval (default)
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: pearson
      value: 31.346400000000003
    - type: spearman
      value: 31.5967
    - type: cosine_spearman
      value: 31.5967
    - type: cosine_pearson
      value: 31.346400000000003
    - type: dot_spearman
      value: 28.5388
    - type: dot_pearson
      value: 31.005300000000002
    - type: main_score
      value: 31.5967
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID (default)
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: ndcg_at_1
      value: 87.0
    - type: ndcg_at_3
      value: 84.693
    - type: ndcg_at_5
      value: 82.211
    - type: ndcg_at_10
      value: 80.55
    - type: ndcg_at_20
      value: 77.766
    - type: ndcg_at_100
      value: 62.881
    - type: ndcg_at_1000
      value: 56.510000000000005
    - type: map_at_1
      value: 0.251
    - type: map_at_3
      value: 0.7000000000000001
    - type: map_at_5
      value: 1.124
    - type: map_at_10
      value: 2.114
    - type: map_at_20
      value: 3.837
    - type: map_at_100
      value: 12.903999999999998
    - type: map_at_1000
      value: 31.184
    - type: recall_at_1
      value: 0.251
    - type: recall_at_3
      value: 0.72
    - type: recall_at_5
      value: 1.179
    - type: recall_at_10
      value: 2.271
    - type: recall_at_20
      value: 4.242
    - type: recall_at_100
      value: 16.012999999999998
    - type: recall_at_1000
      value: 53.556000000000004
    - type: precision_at_1
      value: 92.0
    - type: precision_at_3
      value: 88.667
    - type: precision_at_5
      value: 86.8
    - type: precision_at_10
      value: 85.8
    - type: precision_at_20
      value: 82.39999999999999
    - type: precision_at_100
      value: 64.8
    - type: precision_at_1000
      value: 24.832
    - type: mrr_at_1
      value: 92.0
    - type: mrr_at_3
      value: 95.0
    - type: mrr_at_5
      value: 95.0
    - type: mrr_at_10
      value: 95.0
    - type: mrr_at_20
      value: 95.0
    - type: mrr_at_100
      value: 95.0
    - type: mrr_at_1000
      value: 95.0
    - type: nauc_ndcg_at_1_max
      value: 73.7596
    - type: nauc_ndcg_at_1_std
      value: 52.21130000000001
    - type: nauc_ndcg_at_1_diff1
      value: -8.4225
    - type: nauc_ndcg_at_3_max
      value: 68.513
    - type: nauc_ndcg_at_3_std
      value: 61.9698
    - type: nauc_ndcg_at_3_diff1
      value: -13.079099999999999
    - type: nauc_ndcg_at_5_max
      value: 60.7482
    - type: nauc_ndcg_at_5_std
      value: 66.56830000000001
    - type: nauc_ndcg_at_5_diff1
      value: -12.947500000000002
    - type: nauc_ndcg_at_10_max
      value: 57.4673
    - type: nauc_ndcg_at_10_std
      value: 65.25999999999999
    - type: nauc_ndcg_at_10_diff1
      value: -14.4235
    - type: nauc_ndcg_at_20_max
      value: 61.1214
    - type: nauc_ndcg_at_20_std
      value: 73.60640000000001
    - type: nauc_ndcg_at_20_diff1
      value: -18.1836
    - type: nauc_ndcg_at_100_max
      value: 55.3917
    - type: nauc_ndcg_at_100_std
      value: 80.9228
    - type: nauc_ndcg_at_100_diff1
      value: -13.6584
    - type: nauc_ndcg_at_1000_max
      value: 61.6035
    - type: nauc_ndcg_at_1000_std
      value: 77.73299999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 9.456199999999999
    - type: nauc_map_at_1_max
      value: 3.0159
    - type: nauc_map_at_1_std
      value: -6.6826
    - type: nauc_map_at_1_diff1
      value: 19.3295
    - type: nauc_map_at_3_max
      value: 11.3326
    - type: nauc_map_at_3_std
      value: 0.2297
    - type: nauc_map_at_3_diff1
      value: 18.4889
    - type: nauc_map_at_5_max
      value: 12.8623
    - type: nauc_map_at_5_std
      value: 3.1086
    - type: nauc_map_at_5_diff1
      value: 15.2538
    - type: nauc_map_at_10_max
      value: 15.9145
    - type: nauc_map_at_10_std
      value: 5.8626
    - type: nauc_map_at_10_diff1
      value: 11.5455
    - type: nauc_map_at_20_max
      value: 24.6148
    - type: nauc_map_at_20_std
      value: 17.161199999999997
    - type: nauc_map_at_20_diff1
      value: 7.6256
    - type: nauc_map_at_100_max
      value: 42.070299999999996
    - type: nauc_map_at_100_std
      value: 48.926700000000004
    - type: nauc_map_at_100_diff1
      value: 0.16
    - type: nauc_map_at_1000_max
      value: 63.9887
    - type: nauc_map_at_1000_std
      value: 81.2657
    - type: nauc_map_at_1000_diff1
      value: 4.1088
    - type: nauc_recall_at_1_max
      value: 3.0159
    - type: nauc_recall_at_1_std
      value: -6.6826
    - type: nauc_recall_at_1_diff1
      value: 19.3295
    - type: nauc_recall_at_3_max
      value: 7.7778
    - type: nauc_recall_at_3_std
      value: -3.3724
    - type: nauc_recall_at_3_diff1
      value: 17.9181
    - type: nauc_recall_at_5_max
      value: 6.716900000000001
    - type: nauc_recall_at_5_std
      value: -2.6891000000000003
    - type: nauc_recall_at_5_diff1
      value: 16.3817
    - type: nauc_recall_at_10_max
      value: 7.7518
    - type: nauc_recall_at_10_std
      value: -1.9855
    - type: nauc_recall_at_10_diff1
      value: 13.4496
    - type: nauc_recall_at_20_max
      value: 14.4895
    - type: nauc_recall_at_20_std
      value: 7.2935
    - type: nauc_recall_at_20_diff1
      value: 11.2986
    - type: nauc_recall_at_100_max
      value: 29.8636
    - type: nauc_recall_at_100_std
      value: 33.5546
    - type: nauc_recall_at_100_diff1
      value: 7.0793
    - type: nauc_recall_at_1000_max
      value: 57.184000000000005
    - type: nauc_recall_at_1000_std
      value: 65.3208
    - type: nauc_recall_at_1000_diff1
      value: 15.7381
    - type: nauc_precision_at_1_max
      value: 93.4641
    - type: nauc_precision_at_1_std
      value: 80.6839
    - type: nauc_precision_at_1_diff1
      value: 21.592
    - type: nauc_precision_at_3_max
      value: 87.6596
    - type: nauc_precision_at_3_std
      value: 71.28370000000001
    - type: nauc_precision_at_3_diff1
      value: -0.5263
    - type: nauc_precision_at_5_max
      value: 69.3194
    - type: nauc_precision_at_5_std
      value: 67.4507
    - type: nauc_precision_at_5_diff1
      value: 5.8362
    - type: nauc_precision_at_10_max
      value: 62.393299999999996
    - type: nauc_precision_at_10_std
      value: 62.443599999999996
    - type: nauc_precision_at_10_diff1
      value: -5.3395
    - type: nauc_precision_at_20_max
      value: 63.4842
    - type: nauc_precision_at_20_std
      value: 68.95599999999999
    - type: nauc_precision_at_20_diff1
      value: -13.494100000000001
    - type: nauc_precision_at_100_max
      value: 59.24549999999999
    - type: nauc_precision_at_100_std
      value: 81.3779
    - type: nauc_precision_at_100_diff1
      value: -11.0792
    - type: nauc_precision_at_1000_max
      value: 44.8354
    - type: nauc_precision_at_1000_std
      value: 55.232099999999996
    - type: nauc_precision_at_1000_diff1
      value: -1.4931
    - type: nauc_mrr_at_1_max
      value: 93.4641
    - type: nauc_mrr_at_1_std
      value: 80.6839
    - type: nauc_mrr_at_1_diff1
      value: 21.592
    - type: nauc_mrr_at_3_max
      value: 93.8998
    - type: nauc_mrr_at_3_std
      value: 79.3962
    - type: nauc_mrr_at_3_diff1
      value: 19.3371
    - type: nauc_mrr_at_5_max
      value: 93.8998
    - type: nauc_mrr_at_5_std
      value: 79.3962
    - type: nauc_mrr_at_5_diff1
      value: 19.3371
    - type: nauc_mrr_at_10_max
      value: 93.8998
    - type: nauc_mrr_at_10_std
      value: 79.3962
    - type: nauc_mrr_at_10_diff1
      value: 19.3371
    - type: nauc_mrr_at_20_max
      value: 93.8998
    - type: nauc_mrr_at_20_std
      value: 79.3962
    - type: nauc_mrr_at_20_diff1
      value: 19.3371
    - type: nauc_mrr_at_100_max
      value: 93.8998
    - type: nauc_mrr_at_100_std
      value: 79.3962
    - type: nauc_mrr_at_100_diff1
      value: 19.3371
    - type: nauc_mrr_at_1000_max
      value: 93.8998
    - type: nauc_mrr_at_1000_std
      value: 79.3962
    - type: nauc_mrr_at_1000_diff1
      value: 19.3371
    - type: main_score
      value: 80.55
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020 (default)
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: ndcg_at_1
      value: 18.367
    - type: ndcg_at_3
      value: 23.105999999999998
    - type: ndcg_at_5
      value: 22.423000000000002
    - type: ndcg_at_10
      value: 21.83
    - type: ndcg_at_20
      value: 23.534
    - type: ndcg_at_100
      value: 33.332
    - type: ndcg_at_1000
      value: 44.842999999999996
    - type: map_at_1
      value: 1.52
    - type: map_at_3
      value: 3.811
    - type: map_at_5
      value: 5.4879999999999995
    - type: map_at_10
      value: 8.204
    - type: map_at_20
      value: 10.387
    - type: map_at_100
      value: 13.633000000000001
    - type: map_at_1000
      value: 15.156
    - type: recall_at_1
      value: 1.52
    - type: recall_at_3
      value: 5.466
    - type: recall_at_5
      value: 8.927
    - type: recall_at_10
      value: 15.237
    - type: recall_at_20
      value: 22.841
    - type: recall_at_100
      value: 44.586999999999996
    - type: recall_at_1000
      value: 79.199
    - type: precision_at_1
      value: 20.408
    - type: precision_at_3
      value: 25.169999999999998
    - type: precision_at_5
      value: 23.673
    - type: precision_at_10
      value: 20.408
    - type: precision_at_20
      value: 16.531000000000002
    - type: precision_at_100
      value: 7.204000000000001
    - type: precision_at_1000
      value: 1.473
    - type: mrr_at_1
      value: 20.4082
    - type: mrr_at_3
      value: 35.374100000000006
    - type: mrr_at_5
      value: 37.7211
    - type: mrr_at_10
      value: 39.7068
    - type: mrr_at_20
      value: 40.6272
    - type: mrr_at_100
      value: 40.7905
    - type: mrr_at_1000
      value: 40.805
    - type: nauc_ndcg_at_1_max
      value: -25.3799
    - type: nauc_ndcg_at_1_std
      value: -27.8526
    - type: nauc_ndcg_at_1_diff1
      value: 11.5616
    - type: nauc_ndcg_at_3_max
      value: -31.987900000000003
    - type: nauc_ndcg_at_3_std
      value: -18.1926
    - type: nauc_ndcg_at_3_diff1
      value: 15.4188
    - type: nauc_ndcg_at_5_max
      value: -29.2499
    - type: nauc_ndcg_at_5_std
      value: -18.8992
    - type: nauc_ndcg_at_5_diff1
      value: 9.677
    - type: nauc_ndcg_at_10_max
      value: -25.427899999999998
    - type: nauc_ndcg_at_10_std
      value: -19.0155
    - type: nauc_ndcg_at_10_diff1
      value: 1.5350000000000001
    - type: nauc_ndcg_at_20_max
      value: -25.007800000000003
    - type: nauc_ndcg_at_20_std
      value: -6.626899999999999
    - type: nauc_ndcg_at_20_diff1
      value: -2.0142
    - type: nauc_ndcg_at_100_max
      value: -24.7187
    - type: nauc_ndcg_at_100_std
      value: 18.587899999999998
    - type: nauc_ndcg_at_100_diff1
      value: -7.925599999999999
    - type: nauc_ndcg_at_1000_max
      value: -20.9609
    - type: nauc_ndcg_at_1000_std
      value: 27.360400000000002
    - type: nauc_ndcg_at_1000_diff1
      value: -5.3411
    - type: nauc_map_at_1_max
      value: -26.3166
    - type: nauc_map_at_1_std
      value: -27.701900000000002
    - type: nauc_map_at_1_diff1
      value: 14.4953
    - type: nauc_map_at_3_max
      value: -19.4984
    - type: nauc_map_at_3_std
      value: -26.0187
    - type: nauc_map_at_3_diff1
      value: 18.9316
    - type: nauc_map_at_5_max
      value: -17.6688
    - type: nauc_map_at_5_std
      value: -27.4662
    - type: nauc_map_at_5_diff1
      value: 16.3786
    - type: nauc_map_at_10_max
      value: -9.727
    - type: nauc_map_at_10_std
      value: -25.4592
    - type: nauc_map_at_10_diff1
      value: 8.434999999999999
    - type: nauc_map_at_20_max
      value: -14.2879
    - type: nauc_map_at_20_std
      value: -17.5881
    - type: nauc_map_at_20_diff1
      value: 2.4941
    - type: nauc_map_at_100_max
      value: -15.804499999999999
    - type: nauc_map_at_100_std
      value: -2.6222
    - type: nauc_map_at_100_diff1
      value: -4.3869
    - type: nauc_map_at_1000_max
      value: -15.4637
    - type: nauc_map_at_1000_std
      value: 1.8402000000000003
    - type: nauc_map_at_1000_diff1
      value: -5.3595
    - type: nauc_recall_at_1_max
      value: -26.3166
    - type: nauc_recall_at_1_std
      value: -27.701900000000002
    - type: nauc_recall_at_1_diff1
      value: 14.4953
    - type: nauc_recall_at_3_max
      value: -18.4525
    - type: nauc_recall_at_3_std
      value: -22.7019
    - type: nauc_recall_at_3_diff1
      value: 14.5105
    - type: nauc_recall_at_5_max
      value: -16.8608
    - type: nauc_recall_at_5_std
      value: -26.2799
    - type: nauc_recall_at_5_diff1
      value: 6.910299999999999
    - type: nauc_recall_at_10_max
      value: -11.498700000000001
    - type: nauc_recall_at_10_std
      value: -22.290499999999998
    - type: nauc_recall_at_10_diff1
      value: -1.6997000000000002
    - type: nauc_recall_at_20_max
      value: -16.319
    - type: nauc_recall_at_20_std
      value: -2.6968
    - type: nauc_recall_at_20_diff1
      value: -8.5511
    - type: nauc_recall_at_100_max
      value: -17.741
    - type: nauc_recall_at_100_std
      value: 36.1914
    - type: nauc_recall_at_100_diff1
      value: -20.1127
    - type: nauc_recall_at_1000_max
      value: 3.4278999999999997
    - type: nauc_recall_at_1000_std
      value: 65.7558
    - type: nauc_recall_at_1000_diff1
      value: -15.537899999999999
    - type: nauc_precision_at_1_max
      value: -27.3245
    - type: nauc_precision_at_1_std
      value: -28.615000000000002
    - type: nauc_precision_at_1_diff1
      value: 16.2275
    - type: nauc_precision_at_3_max
      value: -32.1286
    - type: nauc_precision_at_3_std
      value: -14.0653
    - type: nauc_precision_at_3_diff1
      value: 15.6075
    - type: nauc_precision_at_5_max
      value: -27.176299999999998
    - type: nauc_precision_at_5_std
      value: -15.5885
    - type: nauc_precision_at_5_diff1
      value: 7.3431999999999995
    - type: nauc_precision_at_10_max
      value: -26.9241
    - type: nauc_precision_at_10_std
      value: -11.737
    - type: nauc_precision_at_10_diff1
      value: -7.630000000000001
    - type: nauc_precision_at_20_max
      value: -26.901999999999997
    - type: nauc_precision_at_20_std
      value: 23.7519
    - type: nauc_precision_at_20_diff1
      value: -21.343799999999998
    - type: nauc_precision_at_100_max
      value: -16.9757
    - type: nauc_precision_at_100_std
      value: 70.6663
    - type: nauc_precision_at_100_diff1
      value: -32.3231
    - type: nauc_precision_at_1000_max
      value: 20.8431
    - type: nauc_precision_at_1000_std
      value: 37.8016
    - type: nauc_precision_at_1000_diff1
      value: -9.911200000000001
    - type: nauc_mrr_at_1_max
      value: -27.3245
    - type: nauc_mrr_at_1_std
      value: -28.615000000000002
    - type: nauc_mrr_at_1_diff1
      value: 16.2275
    - type: nauc_mrr_at_3_max
      value: -33.332499999999996
    - type: nauc_mrr_at_3_std
      value: -21.543499999999998
    - type: nauc_mrr_at_3_diff1
      value: 15.7577
    - type: nauc_mrr_at_5_max
      value: -34.56
    - type: nauc_mrr_at_5_std
      value: -21.0279
    - type: nauc_mrr_at_5_diff1
      value: 10.4699
    - type: nauc_mrr_at_10_max
      value: -35.4396
    - type: nauc_mrr_at_10_std
      value: -22.6385
    - type: nauc_mrr_at_10_diff1
      value: 8.4536
    - type: nauc_mrr_at_20_max
      value: -34.0343
    - type: nauc_mrr_at_20_std
      value: -21.4022
    - type: nauc_mrr_at_20_diff1
      value: 10.7134
    - type: nauc_mrr_at_100_max
      value: -34.190799999999996
    - type: nauc_mrr_at_100_std
      value: -21.5996
    - type: nauc_mrr_at_100_diff1
      value: 10.9828
    - type: nauc_mrr_at_1000_max
      value: -34.1503
    - type: nauc_mrr_at_1000_std
      value: -21.662300000000002
    - type: nauc_mrr_at_1000_diff1
      value: 10.96
    - type: main_score
      value: 21.83
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 81.4014
    - type: f1
      value: 64.3103
    - type: f1_weighted
      value: 85.0047
    - type: ap
      value: 22.2804
    - type: ap_weighted
      value: 22.2804
    - type: main_score
      value: 81.4014
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification (default)
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 66.4403
    - type: f1
      value: 66.8774
    - type: f1_weighted
      value: 65.9999
    - type: main_score
      value: 66.4403
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering (default)
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: v_measure
      value: 53.3153
    - type: v_measure_std
      value: 1.2923
    - type: main_score
      value: 53.3153
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015 (default)
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 85.22380000000001
    - type: similarity_accuracy_threshold
      value: 74.7432
    - type: similarity_f1
      value: 66.2828
    - type: similarity_f1_threshold
      value: 69.9472
    - type: similarity_precision
      value: 60.765299999999996
    - type: similarity_recall
      value: 72.9024
    - type: similarity_ap
      value: 72.0492
    - type: cosine_accuracy
      value: 85.22380000000001
    - type: cosine_accuracy_threshold
      value: 74.7432
    - type: cosine_f1
      value: 66.2828
    - type: cosine_f1_threshold
      value: 69.9472
    - type: cosine_precision
      value: 60.765299999999996
    - type: cosine_recall
      value: 72.9024
    - type: cosine_ap
      value: 72.0492
    - type: manhattan_accuracy
      value: 85.10459999999999
    - type: manhattan_accuracy_threshold
      value: 48810.3699
    - type: manhattan_f1
      value: 65.7133
    - type: manhattan_f1_threshold
      value: 53724.462900000006
    - type: manhattan_precision
      value: 60.3399
    - type: manhattan_recall
      value: 72.1372
    - type: manhattan_ap
      value: 71.3681
    - type: euclidean_accuracy
      value: 85.1404
    - type: euclidean_accuracy_threshold
      value: 2203.8609
    - type: euclidean_f1
      value: 65.8107
    - type: euclidean_f1_threshold
      value: 2445.96
    - type: euclidean_precision
      value: 59.8875
    - type: euclidean_recall
      value: 73.0343
    - type: euclidean_ap
      value: 71.3938
    - type: dot_accuracy
      value: 84.8781
    - type: dot_accuracy_threshold
      value: 74077.38040000001
    - type: dot_f1
      value: 65.3706
    - type: dot_f1_threshold
      value: 69501.5808
    - type: dot_precision
      value: 60.58559999999999
    - type: dot_recall
      value: 70.97630000000001
    - type: dot_ap
      value: 71.0091
    - type: max_accuracy
      value: 85.22380000000001
    - type: max_f1
      value: 66.2828
    - type: max_precision
      value: 60.765299999999996
    - type: max_recall
      value: 73.0343
    - type: max_ap
      value: 72.0492
    - type: main_score
      value: 72.0492
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus (default)
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 89.145
    - type: similarity_accuracy_threshold
      value: 65.00280000000001
    - type: similarity_f1
      value: 78.78150000000001
    - type: similarity_f1_threshold
      value: 61.2185
    - type: similarity_precision
      value: 75.0279
    - type: similarity_recall
      value: 82.9304
    - type: similarity_ap
      value: 86.39949999999999
    - type: cosine_accuracy
      value: 89.145
    - type: cosine_accuracy_threshold
      value: 65.00280000000001
    - type: cosine_f1
      value: 78.78150000000001
    - type: cosine_f1_threshold
      value: 61.2185
    - type: cosine_precision
      value: 75.0279
    - type: cosine_recall
      value: 82.9304
    - type: cosine_ap
      value: 86.39949999999999
    - type: manhattan_accuracy
      value: 89.05579999999999
    - type: manhattan_accuracy_threshold
      value: 55381.189
    - type: manhattan_f1
      value: 78.6152
    - type: manhattan_f1_threshold
      value: 58447.6685
    - type: manhattan_precision
      value: 74.77080000000001
    - type: manhattan_recall
      value: 82.8765
    - type: manhattan_ap
      value: 86.2899
    - type: euclidean_accuracy
      value: 89.1179
    - type: euclidean_accuracy_threshold
      value: 2552.2853999999998
    - type: euclidean_f1
      value: 78.6816
    - type: euclidean_f1_threshold
      value: 2660.0677
    - type: euclidean_precision
      value: 74.4317
    - type: euclidean_recall
      value: 83.4463
    - type: euclidean_ap
      value: 86.3158
    - type: dot_accuracy
      value: 88.81710000000001
    - type: dot_accuracy_threshold
      value: 58383.1421
    - type: dot_f1
      value: 78.2367
    - type: dot_f1_threshold
      value: 54826.550299999995
    - type: dot_precision
      value: 73.7657
    - type: dot_recall
      value: 83.2846
    - type: dot_ap
      value: 85.5699
    - type: max_accuracy
      value: 89.145
    - type: max_f1
      value: 78.78150000000001
    - type: max_precision
      value: 75.0279
    - type: max_recall
      value: 83.4463
    - type: max_ap
      value: 86.39949999999999
    - type: main_score
      value: 86.39949999999999
    task:
      type: PairClassification
---

# cde-small-v2

> [!NOTE]
> **Note on parameter count:** Although HuggingFace reports the size of this model as 281M params, really it can be thought of as 140M. That's because our weights actually contain the weights of two models (dubbed "first stage" and "second stage"), and only the second-stage model is used to compute embeddings at search time.

<a href="https://github.com/jxmorris12/cde">Github</a>

Our new model that naturally integrates "context tokens" into the embedding process. As of January 13th, 2025, `cde-small-v2` is the best small model (under 400M params) on the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) for text embedding models, with an average score of 65.58.

👉  <b><a href="https://colab.research.google.com/drive/1r8xwbp7_ySL9lP-ve4XMJAHjidB9UkbL?usp=sharing">Try on Colab</a></b>
<br>
👉  <b><a href="https://arxiv.org/abs/2410.02525">Contextual Document Embeddings (ArXiv)</a></b>

![CDE Overview Figure](https://i.imgur.com/LyXJZjM.png)

<br>
<hr>

# How to use `cde-small-v2`

Our embedding model needs to be used in *two stages*. The first stage is to gather some dataset information by embedding a subset of the corpus using our "first-stage" model. The second stage is to actually embed queries and documents, conditioning on the corpus information from the first stage. Note that we can do the first stage part offline and only use the second-stage weights at inference time.

</details>

## With Transformers

<details>
<summary>Click to learn how to use cde-small-v2 with Transformers</summary>

### Loading the model

Our model can be loaded using `transformers` out-of-the-box with "trust remote code" enabled. We use the default BERT uncased tokenizer:
```python
import transformers

model = transformers.AutoModel.from_pretrained("jxm/cde-small-v2", trust_remote_code=True)
tokenizer = transformers.AutoTokenizer.from_pretrained("answerdotai/ModernBERT-base")
```

#### Note on prefixes

*Nota bene*: Like all state-of-the-art embedding models, our model was trained with task-specific prefixes. To do retrieval, you can prepend the following strings to queries & documents:

```python
query_prefix = "search_query: "
document_prefix = "search_document: "
```

### First stage

```python
minicorpus_size = model.config.transductive_corpus_size
minicorpus_docs = [ ... ] # Put some strings here that are representative of your corpus, for example by calling random.sample(corpus, k=minicorpus_size)
assert len(minicorpus_docs) == minicorpus_size # You must use exactly this many documents in the minicorpus. You can oversample if your corpus is smaller.
minicorpus_docs = tokenizer(
    [document_prefix + doc for doc in minicorpus_docs],
    truncation=True,
    padding=True,
    max_length=512,
    return_tensors="pt"
).to(model.device)
import torch
from tqdm.autonotebook import tqdm

batch_size = 32

dataset_embeddings = []
for i in tqdm(range(0, len(minicorpus_docs["input_ids"]), batch_size)):
    minicorpus_docs_batch = {k: v[i:i+batch_size] for k,v in minicorpus_docs.items()}
    with torch.no_grad():
        dataset_embeddings.append(
            model.first_stage_model(**minicorpus_docs_batch)
        )

dataset_embeddings = torch.cat(dataset_embeddings)
```

### Running the second stage

Now that we have obtained "dataset embeddings" we can embed documents and queries like normal. Remember to use the document prefix for documents:
```python
docs = tokenizer(
    [document_prefix + doc for doc in docs],
    truncation=True,
    padding=True,
    max_length=512,
    return_tensors="pt"
).to(model.device)

with torch.no_grad():
  doc_embeddings = model.second_stage_model(
      input_ids=docs["input_ids"],
      attention_mask=docs["attention_mask"],
      dataset_embeddings=dataset_embeddings,
  )
doc_embeddings /= doc_embeddings.norm(p=2, dim=1, keepdim=True)
```

and the query prefix for queries:
```python
queries = queries.select(range(16))["text"]
queries = tokenizer(
    [query_prefix + query for query in queries],
    truncation=True,
    padding=True,
    max_length=512,
    return_tensors="pt"
).to(model.device)

with torch.no_grad():
  query_embeddings = model.second_stage_model(
      input_ids=queries["input_ids"],
      attention_mask=queries["attention_mask"],
      dataset_embeddings=dataset_embeddings,
  )
query_embeddings /= query_embeddings.norm(p=2, dim=1, keepdim=True)
```

these embeddings can be compared using dot product, since they're normalized.

</details>

### What if I don't know what my corpus will be ahead of time?

If you can't obtain corpus information ahead of time, you still have to pass *something* as the dataset embeddings; our model will work fine in this case, but not quite as well; without corpus information, our model performance drops from 65.0 to 63.8 on MTEB. We provide [some random strings](https://huggingface.co/jxm/cde-small-v2/resolve/main/random_strings.txt) that worked well for us that can be used as a substitute for corpus sampling.


## With Sentence Transformers

<details open="">
<summary>Click to learn how to use cde-small-v2 with Sentence Transformers</summary>

### Loading the model

Our model can be loaded using `sentence-transformers` out-of-the-box with "trust remote code" enabled:
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("jxm/cde-small-v2", trust_remote_code=True)
```

#### Note on prefixes

*Nota bene*: Like all state-of-the-art embedding models, our model was trained with task-specific prefixes. To do retrieval, you can use `prompt_name="query"` and `prompt_name="document"` in the `encode` method of the model when embedding queries and documents, respectively.

### First stage

```python
minicorpus_size = model[0].config.transductive_corpus_size
minicorpus_docs = [ ... ] # Put some strings here that are representative of your corpus, for example by calling random.sample(corpus, k=minicorpus_size)
assert len(minicorpus_docs) == minicorpus_size # You must use exactly this many documents in the minicorpus. You can oversample if your corpus is smaller.

dataset_embeddings = model.encode(
    minicorpus_docs,
    prompt_name="document",
    convert_to_tensor=True
)
```

### Running the second stage

Now that we have obtained "dataset embeddings" we can embed documents and queries like normal. Remember to use the document prompt for documents:

```python
docs = [...]
queries = [...]

doc_embeddings = model.encode(
    docs,
    prompt_name="document",
    dataset_embeddings=dataset_embeddings,
    convert_to_tensor=True,
)
query_embeddings = model.encode(
    queries,
    prompt_name="query",
    dataset_embeddings=dataset_embeddings,
    convert_to_tensor=True,
) 
```

these embeddings can be compared using cosine similarity via `model.similarity`:
```python
similarities = model.similarity(query_embeddings, doc_embeddings)
topk_values, topk_indices = similarities.topk(5)
```

<details>
<summary>Click here for a full copy-paste ready example</summary>

```python
from sentence_transformers import SentenceTransformer
from datasets import load_dataset

# 1. Load the Sentence Transformer model
model = SentenceTransformer("jxm/cde-small-v2", trust_remote_code=True)
context_docs_size = model[0].config.transductive_corpus_size  # 512

# 2. Load the dataset: context dataset, docs, and queries
dataset = load_dataset("sentence-transformers/natural-questions", split="train")
dataset.shuffle(seed=42)
# 10 queries, 512 context docs, 500 docs
queries = dataset["query"][:10]
docs = dataset["answer"][:2000]
context_docs = dataset["answer"][-context_docs_size:] # Last 512 docs

# 3. First stage: embed the context docs
dataset_embeddings = model.encode(
    context_docs,
    prompt_name="document",
    convert_to_tensor=True,
)

# 4. Second stage: embed the docs and queries
doc_embeddings = model.encode(
    docs,
    prompt_name="document",
    dataset_embeddings=dataset_embeddings,
    convert_to_tensor=True,
)
query_embeddings = model.encode(
    queries,
    prompt_name="query",
    dataset_embeddings=dataset_embeddings,
    convert_to_tensor=True,
)

# 5. Compute the similarity between the queries and docs
similarities = model.similarity(query_embeddings, doc_embeddings)
topk_values, topk_indices = similarities.topk(5)
print(topk_values)
print(topk_indices)

"""
tensor([[0.5495, 0.5426, 0.5423, 0.5292, 0.5286],
        [0.6357, 0.6334, 0.6177, 0.5862, 0.5794],
        [0.7648, 0.5452, 0.5000, 0.4959, 0.4881],
        [0.6802, 0.5225, 0.5178, 0.5160, 0.5075],
        [0.6947, 0.5843, 0.5619, 0.5344, 0.5298],
        [0.7742, 0.7742, 0.7742, 0.7231, 0.6224],
        [0.8853, 0.6667, 0.5829, 0.5795, 0.5769],
        [0.6911, 0.6127, 0.6003, 0.5986, 0.5936],
        [0.6796, 0.6053, 0.6000, 0.5911, 0.5884],
        [0.7624, 0.5589, 0.5428, 0.5278, 0.5275]], device='cuda:0')
tensor([[   0,  296,  234, 1651, 1184],
        [1542,  466,  438, 1207, 1911],
        [   2, 1562,  632, 1852,  382],
        [   3,  694,  932, 1765,  662],
        [   4,   35,  747,   26,  432],
        [ 534,  175,    5, 1495,  575],
        [   6, 1802, 1875,  747,   21],
        [   7, 1913, 1936,  640,    6],
        [   8,  747,  167, 1318, 1743],
        [   9, 1583, 1145,  219,  357]], device='cuda:0')
"""
# As you can see, almost every query_i has document_i as the most similar document.

# 6. Print the top-k results
for query_idx, top_doc_idx in enumerate(topk_indices[:, 0]):
    print(f"Query {query_idx}: {queries[query_idx]}")
    print(f"Top Document: {docs[top_doc_idx]}")
    print()
"""
Query 0: when did richmond last play in a preliminary final
Top Document: Richmond Football Club Richmond began 2017 with 5 straight wins, a feat it had not achieved since 1995. A series of close losses hampered the Tigers throughout the middle of the season, including a 5-point loss to the Western Bulldogs, 2-point loss to Fremantle, and a 3-point loss to the Giants. Richmond ended the season strongly with convincing victories over Fremantle and St Kilda in the final two rounds, elevating the club to 3rd on the ladder. Richmond's first final of the season against the Cats at the MCG attracted a record qualifying final crowd of 95,028; the Tigers won by 51 points. Having advanced to the first preliminary finals for the first time since 2001, Richmond defeated Greater Western Sydney by 36 points in front of a crowd of 94,258 to progress to the Grand Final against Adelaide, their first Grand Final appearance since 1982. The attendance was 100,021, the largest crowd to a grand final since 1986. The Crows led at quarter time and led by as many as 13, but the Tigers took over the game as it progressed and scored seven straight goals at one point. They eventually would win by 48 points – 16.12 (108) to Adelaide's 8.12 (60) – to end their 37-year flag drought.[22] Dustin Martin also became the first player to win a Premiership medal, the Brownlow Medal and the Norm Smith Medal in the same season, while Damien Hardwick was named AFL Coaches Association Coach of the Year. Richmond's jump from 13th to premiers also marked the biggest jump from one AFL season to the next.

Query 1: who sang what in the world's come over you
Top Document: Life's What You Make It (Talk Talk song) "Life's What You Make It" is a song by the English band Talk Talk. It was released as a single in 1986, the first from the band's album The Colour of Spring. The single was a hit in the UK, peaking at No. 16, and charted in numerous other countries, often reaching the Top 20.

Query 2: who produces the most wool in the world
Top Document: Wool Global wool production is about 2 million tonnes per year, of which 60% goes into apparel. Wool comprises ca 3% of the global textile market, but its value is higher owing to dying and other modifications of the material.[1] Australia is a leading producer of wool which is mostly from Merino sheep but has been eclipsed by China in terms of total weight.[30] New Zealand (2016) is the third-largest producer of wool, and the largest producer of crossbred wool. Breeds such as Lincoln, Romney, Drysdale, and Elliotdale produce coarser fibers, and wool from these sheep is usually used for making carpets.

Query 3: where does alaska the last frontier take place
Top Document: Alaska: The Last Frontier Alaska: The Last Frontier is an American reality cable television series on the Discovery Channel, currently in its 7th season of broadcast. The show documents the extended Kilcher family, descendants of Swiss immigrants and Alaskan pioneers, Yule and Ruth Kilcher, at their homestead 11 miles outside of Homer.[1] By living without plumbing or modern heating, the clan chooses to subsist by farming, hunting and preparing for the long winters.[2] The Kilcher family are relatives of the singer Jewel,[1][3] who has appeared on the show.[4]

Query 4: a day to remember all i want cameos
Top Document: All I Want (A Day to Remember song) The music video for the song, which was filmed in October 2010,[4] was released on January 6, 2011.[5] It features cameos of numerous popular bands and musicians. The cameos are: Tom Denney (A Day to Remember's former guitarist), Pete Wentz, Winston McCall of Parkway Drive, The Devil Wears Prada, Bring Me the Horizon, Sam Carter of Architects, Tim Lambesis of As I Lay Dying, Silverstein, Andrew WK, August Burns Red, Seventh Star, Matt Heafy of Trivium, Vic Fuentes of Pierce the Veil, Mike Herrera of MxPx, and Set Your Goals.[5] Rock Sound called the video "quite excellent".[5]

Query 5: what does the red stripes mean on the american flag
Top Document: Flag of the United States The flag of the United States of America, often referred to as the American flag, is the national flag of the United States. It consists of thirteen equal horizontal stripes of red (top and bottom) alternating with white, with a blue rectangle in the canton (referred to specifically as the "union") bearing fifty small, white, five-pointed stars arranged in nine offset horizontal rows, where rows of six stars (top and bottom) alternate with rows of five stars. The 50 stars on the flag represent the 50 states of the United States of America, and the 13 stripes represent the thirteen British colonies that declared independence from the Kingdom of Great Britain, and became the first states in the U.S.[1] Nicknames for the flag include The Stars and Stripes,[2] Old Glory,[3] and The Star-Spangled Banner.

Query 6: where did they film diary of a wimpy kid
Top Document: Diary of a Wimpy Kid (film) Filming of Diary of a Wimpy Kid was in Vancouver and wrapped up on October 16, 2009.

Query 7: where was beasts of the southern wild filmed
Top Document: Beasts of the Southern Wild The film's fictional setting, "Isle de Charles Doucet", known to its residents as the Bathtub, was inspired by several isolated and independent fishing communities threatened by erosion, hurricanes and rising sea levels in Louisiana's Terrebonne Parish, most notably the rapidly eroding Isle de Jean Charles. It was filmed in Terrebonne Parish town Montegut.[5]

Query 8: what part of the country are you likely to find the majority of the mollisols
Top Document: Mollisol Mollisols occur in savannahs and mountain valleys (such as Central Asia, or the North American Great Plains). These environments have historically been strongly influenced by fire and abundant pedoturbation from organisms such as ants and earthworms. It was estimated that in 2003, only 14 to 26 percent of grassland ecosystems still remained in a relatively natural state (that is, they were not used for agriculture due to the fertility of the A horizon). Globally, they represent ~7% of ice-free land area. As the world's most agriculturally productive soil order, the Mollisols represent one of the more economically important soil orders.

Query 9: when did fosters home for imaginary friends start
Top Document: Foster's Home for Imaginary Friends McCracken conceived the series after adopting two dogs from an animal shelter and applying the concept to imaginary friends. The show first premiered on Cartoon Network on August 13, 2004, as a 90-minute television film. On August 20, it began its normal run of twenty-to-thirty-minute episodes on Fridays, at 7 pm. The series finished its run on May 3, 2009, with a total of six seasons and seventy-nine episodes. McCracken left Cartoon Network shortly after the series ended. Reruns have aired on Boomerang from August 11, 2012 to November 3, 2013 and again from June 1, 2014 to April 3, 2017.
"""
```

</details>

### Colab demo

We've set up a short demo in a Colab notebook showing how you might use our model:
[Try our model in Colab:](https://colab.research.google.com/drive/1ddWeNj9nztHrwtoSEtaArfs7_NZhZA6k?usp=sharing)

### Training details

All non-mentioned other hyperparameters (learning, etc.) are either in the config or CDE paper. If not, please raise an issue here: https://github.com/jxmorris12/cde


#### Model details

cde-small-v2 includes a number of modeling changes from cde-small-v1:
- used the recently-released [ModernBERT](https://huggingface.co/blog/modernbert)
- added a residual connection between the model stages, which helps conditioning and gradient flow
- disabled pooling over instruction tokens
- disable position-embedding nullification over contextual tokens
- disable weight decay (not sure if this one helped or not)

#### Unsupervised training

Trained for six epochs on the nomic-unsupervised dataset with cluster size of 512 and batch size of 512, using GTR clusters and GTE-large filtering. (Probably would have performed better with GTE clustering too, but that's an expensive operation that we didn't rerun.)

#### Supervised training

Trained for four epochs on the BGE dataset with GTE clusters and GTE hard-negative filtering.

### Cite us

Used our model, method, or architecture? Want to cite us? Here's the ArXiv citation information:
```
@misc{morris2024contextualdocumentembeddings,
      title={Contextual Document Embeddings}, 
      author={John X. Morris and Alexander M. Rush},
      year={2024},
      eprint={2410.02525},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.02525}, 
}
```