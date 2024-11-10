# Training and testing models for biases
## Dataset Adult


### 1. Assessing fairness for Logistic Regression


Group: **Female**

- TPR: 0.0863

- FPR: 0.0111

- FN_FP_ratio: 7.5206


Group: **Male**

- TPR: 0.1262

- FPR: 0.0248

- FN_FP_ratio: 9.2278


#### Statistical Test Results:

- TPR:

	- Test: t-test

	- Statistic: -4.8139

	- p-value: 0.0000

- FPR:

	- Test: t-test

	- Statistic: -11.0649

	- p-value: 0.0000

- FN_FP_ratio:

	- Test: t-test

	- Statistic: -2.0613

	- p-value: 0.0462


**Overall average accuracy**: 0.842


### 2. Assessing fairness for Random Forest


Group: **Female**

- TPR: 0.2556

- FPR: 0.0335

- FN_FP_ratio: 1.7676


Group: **Male**

- TPR: 0.2892

- FPR: 0.0596

- FN_FP_ratio: 3.0884


#### Statistical Test Results:

- TPR:

	- Test: t-test

	- Statistic: -2.3445

	- p-value: 0.0244

- FPR:

	- Test: t-test

	- Statistic: -15.3159

	- p-value: 0.0000

- FN_FP_ratio:

	- Test: t-test

	- Statistic: -12.4910

	- p-value: 0.0000


**Overall average accuracy**: 0.843


### 3. Assessing fairness for Support Vector Machine


Group: **Female**

- TPR: 0.1843

- FPR: 0.0092

- FN_FP_ratio: 9.2422


Group: **Male**

- TPR: 0.1793

- FPR: 0.0244

- FN_FP_ratio: 8.8223


#### Statistical Test Results:

- TPR:

	- Test: t-test

	- Statistic: 0.3714

	- p-value: 0.7124

- FPR:

	- Test: t-test

	- Statistic: -11.9265

	- p-value: 0.0000

- FN_FP_ratio:

	- Test: t-test

	- Statistic: 0.2874

	- p-value: 0.7754


**Overall average accuracy**: 0.853


### 4. Assessing fairness for K-Nearest Neighbors


Group: **Female**

- TPR: 0.3198

- FPR: 0.0723

- FN_FP_ratio: 0.7517


Group: **Male**

- TPR: 0.3661

- FPR: 0.1090

- FN_FP_ratio: 1.5051


#### Statistical Test Results:

- TPR:

	- Test: t-test

	- Statistic: -3.9426

	- p-value: 0.0003

- FPR:

	- Test: t-test

	- Statistic: -11.8540

	- p-value: 0.0000

- FN_FP_ratio:

	- Test: t-test

	- Statistic: -14.1194

	- p-value: 0.0000


**Overall average accuracy**: 0.817
## Dataset Credit


### 1. Assessing fairness for Logistic Regression


Group: **1**

- TPR: 0.2411

- FPR: 0.0327

- FN_FP_ratio: 8.1295


Group: **2**

- TPR: 0.2309

- FPR: 0.0228

- FN_FP_ratio: 9.8724


#### Statistical Test Results:

- TPR:

	- Test: t-test

	- Statistic: 1.0203

	- p-value: 0.3141

- FPR:

	- Test: t-test

	- Statistic: 3.8938

	- p-value: 0.0004

- FN_FP_ratio:

	- Test: t-test

	- Statistic: -1.6678

	- p-value: 0.1036


**Overall average accuracy**: 0.810


### 2. Assessing fairness for Random Forest


Group: **1**

- TPR: 0.3770

- FPR: 0.0675

- FN_FP_ratio: 3.0086


Group: **2**

- TPR: 0.3673

- FPR: 0.0532

- FN_FP_ratio: 3.1822


#### Statistical Test Results:

- TPR:

	- Test: t-test

	- Statistic: 0.8113

	- p-value: 0.4223

- FPR:

	- Test: t-test

	- Statistic: 4.7039

	- p-value: 0.0000

- FN_FP_ratio:

	- Test: t-test

	- Statistic: -1.0256

	- p-value: 0.3116


**Overall average accuracy**: 0.815


### 3. Assessing fairness for Support Vector Machine


Group: **1**

- TPR: 0.3490

- FPR: 0.0502

- FN_FP_ratio: 4.3095


Group: **2**

- TPR: 0.3334

- FPR: 0.0405

- FN_FP_ratio: 4.5481


#### Statistical Test Results:

- TPR:

	- Test: t-test

	- Statistic: 1.3244

	- p-value: 0.1933

- FPR:

	- Test: t-test

	- Statistic: 3.1773

	- p-value: 0.0030

- FN_FP_ratio:

	- Test: t-test

	- Statistic: -0.7151

	- p-value: 0.4789


**Overall average accuracy**: 0.820


### 4. Assessing fairness for K-Nearest Neighbors


Group: **1**

- TPR: 0.3644

- FPR: 0.0939

- FN_FP_ratio: 2.2357


Group: **2**

- TPR: 0.3586

- FPR: 0.0772

- FN_FP_ratio: 2.2158


#### Statistical Test Results:

- TPR:

	- Test: t-test

	- Statistic: 0.4569

	- p-value: 0.6504

- FPR:

	- Test: t-test

	- Statistic: 4.1443

	- p-value: 0.0002

- FN_FP_ratio:

	- Test: t-test

	- Statistic: 0.1321

	- p-value: 0.8956


**Overall average accuracy**: 0.794
## Dataset Bank


### 1. Assessing fairness for Logistic Regression


Group: **divorced**

- TPR: 0.0055

- FPR: 0.0011

- FN_FP_ratio: 7.3500


Group: **married**

- TPR: 0.0018

- FPR: 0.0009

- FN_FP_ratio: 64.1250


Group: **single**

- TPR: 0.0015

- FPR: 0.0011

- FN_FP_ratio: 48.3250


#### Statistical Test Results:

- TPR:

	- Test: ANOVA

	- Statistic: 1.3902

	- p-value: 0.2573

- FPR:

	- Test: ANOVA

	- Statistic: 0.1435

	- p-value: 0.8666

- FN_FP_ratio:

	- Test: ANOVA

	- Statistic: 8.9794

	- p-value: 0.0004

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)    -56.775     0.000   -90.054   -23.496
 (0 - 2)    -40.975     0.012   -74.254    -7.696
 (1 - 0)     56.775     0.000    23.496    90.054
 (1 - 2)     15.800     0.492   -17.479    49.079
 (2 - 0)     40.975     0.012     7.696    74.254
 (2 - 1)    -15.800     0.492   -49.079    17.479


```


**Overall average accuracy**: 0.882


### 2. Assessing fairness for Random Forest


Group: **divorced**

- TPR: 0.1273

- FPR: 0.0394

- FN_FP_ratio: 3.2912


Group: **married**

- TPR: 0.1617

- FPR: 0.0476

- FN_FP_ratio: 2.0068


Group: **single**

- TPR: 0.1681

- FPR: 0.0653

- FN_FP_ratio: 2.3311


#### Statistical Test Results:

- TPR:

	- Test: ANOVA

	- Statistic: 6.2536

	- p-value: 0.0035

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)     -0.034     0.020    -0.064    -0.005
 (0 - 2)     -0.041     0.005    -0.071    -0.011
 (1 - 0)      0.034     0.020     0.005     0.064
 (1 - 2)     -0.006     0.864    -0.036     0.023
 (2 - 0)      0.041     0.005     0.011     0.071
 (2 - 1)      0.006     0.864    -0.023     0.036


```

- FPR:

	- Test: ANOVA

	- Statistic: 38.1462

	- p-value: 0.0000

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)     -0.008     0.025    -0.015    -0.001
 (0 - 2)     -0.026     0.000    -0.033    -0.019
 (1 - 0)      0.008     0.025     0.001     0.015
 (1 - 2)     -0.018     0.000    -0.025    -0.010
 (2 - 0)      0.026     0.000     0.019     0.033
 (2 - 1)      0.018     0.000     0.010     0.025


```

- FN_FP_ratio:

	- Test: ANOVA

	- Statistic: 10.2948

	- p-value: 0.0002

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)      1.284     0.000     0.576     1.993
 (0 - 2)      0.960     0.005     0.252     1.669
 (1 - 0)     -1.284     0.000    -1.993    -0.576
 (1 - 2)     -0.324     0.517    -1.033     0.384
 (2 - 0)     -0.960     0.005    -1.669    -0.252
 (2 - 1)      0.324     0.517    -0.384     1.033


```


**Overall average accuracy**: 0.856


### 3. Assessing fairness for Support Vector Machine


Group: **divorced**

- TPR: 0.0082

- FPR: 0.0029

- FN_FP_ratio: 8.6083


Group: **married**

- TPR: 0.0154

- FPR: 0.0014

- FN_FP_ratio: 71.0275


Group: **single**

- TPR: 0.0010

- FPR: 0.0003

- FN_FP_ratio: 6.4250


#### Statistical Test Results:

- TPR:

	- Test: ANOVA

	- Statistic: 8.0164

	- p-value: 0.0009

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)     -0.007     0.119    -0.016     0.001
 (0 - 2)      0.007     0.123    -0.001     0.016
 (1 - 0)      0.007     0.119    -0.001     0.016
 (1 - 2)      0.014     0.001     0.006     0.023
 (2 - 0)     -0.007     0.123    -0.016     0.001
 (2 - 1)     -0.014     0.001    -0.023    -0.006


```

- FPR:

	- Test: ANOVA

	- Statistic: 4.9766

	- p-value: 0.0102

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)      0.001     0.199    -0.001     0.003
 (0 - 2)      0.003     0.007     0.001     0.005
 (1 - 0)     -0.001     0.199    -0.003     0.001
 (1 - 2)      0.001     0.343    -0.001     0.003
 (2 - 0)     -0.003     0.007    -0.005    -0.001
 (2 - 1)     -0.001     0.343    -0.003     0.001


```

- FN_FP_ratio:

	- Test: ANOVA

	- Statistic: 20.8280

	- p-value: 0.0000

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)    -62.419     0.000   -89.774   -35.064
 (0 - 2)      2.183     0.980   -25.172    29.539
 (1 - 0)     62.419     0.000    35.064    89.774
 (1 - 2)     64.603     0.000    37.247    91.958
 (2 - 0)     -2.183     0.980   -29.539    25.172
 (2 - 1)    -64.603     0.000   -91.958   -37.247


```


**Overall average accuracy**: 0.883


### 4. Assessing fairness for K-Nearest Neighbors


Group: **divorced**

- TPR: 0.1048

- FPR: 0.0224

- FN_FP_ratio: 6.7439


Group: **married**

- TPR: 0.1294

- FPR: 0.0250

- FN_FP_ratio: 4.1000


Group: **single**

- TPR: 0.1066

- FPR: 0.0335

- FN_FP_ratio: 4.9838


#### Statistical Test Results:

- TPR:

	- Test: ANOVA

	- Statistic: 2.9535

	- p-value: 0.0602

- FPR:

	- Test: ANOVA

	- Statistic: 9.8601

	- p-value: 0.0002

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)     -0.003     0.583    -0.009     0.004
 (0 - 2)     -0.011     0.000    -0.017    -0.005
 (1 - 0)      0.003     0.583    -0.004     0.009
 (1 - 2)     -0.009     0.005    -0.015    -0.002
 (2 - 0)      0.011     0.000     0.005     0.017
 (2 - 1)      0.009     0.005     0.002     0.015


```

- FN_FP_ratio:

	- Test: ANOVA

	- Statistic: 7.3630

	- p-value: 0.0014

	- Post-hoc Tukey HSD Results:

```
Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)      2.644     0.001     0.956     4.332
 (0 - 2)      1.760     0.039     0.072     3.448
 (1 - 0)     -2.644     0.001    -4.332    -0.956
 (1 - 2)     -0.884     0.423    -2.572     0.804
 (2 - 0)     -1.760     0.039    -3.448    -0.072
 (2 - 1)      0.884     0.423    -0.804     2.572


```


**Overall average accuracy**: 0.873
