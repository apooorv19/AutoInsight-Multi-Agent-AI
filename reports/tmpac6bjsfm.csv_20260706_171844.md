# AutoInsight AI Report
## Dataset Overview
- Dataset: tmpac6bjsfm.csv
- Dimensions: 526 rows x 25 columns
- Duplicate rows: 0
- Numerical columns: rownames, wage, educ, exper, tenure, numdep, smsa, northcen, south, west, construc, ndurman, trcommpu, trade, services, profserv, profocc, clerocc, servocc, lwage, expersq, tenursq
- Categorical columns: nonwhite, female, married
- Datetime columns: None
## Summary Statistics
### Summary Statistics

```text
          count     mean      std    min      25%      50%      75%       max
rownames  526.0  263.500  151.987  1.000  132.250  263.500  394.750   526.000
wage      526.0    5.896    3.693  0.530    3.330    4.650    6.880    24.980
educ      526.0   12.563    2.769  0.000   12.000   12.000   14.000    18.000
exper     526.0   17.017   13.572  1.000    5.000   13.500   26.000    51.000
tenure    526.0    5.105    7.224  0.000    0.000    2.000    7.000    44.000
numdep    526.0    1.044    1.262  0.000    0.000    1.000    2.000     6.000
smsa      526.0    0.722    0.448  0.000    0.000    1.000    1.000     1.000
northcen  526.0    0.251    0.434  0.000    0.000    0.000    0.750     1.000
south     526.0    0.356    0.479  0.000    0.000    0.000    1.000     1.000
west      526.0    0.169    0.375  0.000    0.000    0.000    0.000     1.000
construc  526.0    0.046    0.209  0.000    0.000    0.000    0.000     1.000
ndurman   526.0    0.114    0.318  0.000    0.000    0.000    0.000     1.000
trcommpu  526.0    0.044    0.205  0.000    0.000    0.000    0.000     1.000
trade     526.0    0.287    0.453  0.000    0.000    0.000    1.000     1.000
services  526.0    0.101    0.301  0.000    0.000    0.000    0.000     1.000
profserv  526.0    0.259    0.438  0.000    0.000    0.000    1.000     1.000
profocc   526.0    0.367    0.482  0.000    0.000    0.000    1.000     1.000
clerocc   526.0    0.167    0.374  0.000    0.000    0.000    0.000     1.000
servocc   526.0    0.141    0.348  0.000    0.000    0.000    0.000     1.000
lwage     526.0    1.623    0.532 -0.635    1.203    1.537    1.929     3.218
expersq   526.0  473.435  616.045  1.000   25.000  182.500  676.000  2601.000
tenursq   526.0   78.150  199.435  0.000    0.000    4.000   49.000  1936.000
```
### Mean

```text
                0
rownames  263.500
wage        5.896
educ       12.563
exper      17.017
tenure      5.105
numdep      1.044
smsa        0.722
northcen    0.251
south       0.356
west        0.169
construc    0.046
ndurman     0.114
trcommpu    0.044
trade       0.287
services    0.101
profserv    0.259
profocc     0.367
clerocc     0.167
servocc     0.141
lwage       1.623
expersq   473.435
tenursq    78.150
```
### Median

```text
                0
rownames  263.500
wage        4.650
educ       12.000
exper      13.500
tenure      2.000
numdep      1.000
smsa        1.000
northcen    0.000
south       0.000
west        0.000
construc    0.000
ndurman     0.000
trcommpu    0.000
trade       0.000
services    0.000
profserv    0.000
profocc     0.000
clerocc     0.000
servocc     0.000
lwage       1.537
expersq   182.500
tenursq     4.000
```
### Standard Deviation

```text
                0
rownames  151.987
wage        3.693
educ        2.769
exper      13.572
tenure      7.224
numdep      1.262
smsa        0.448
northcen    0.434
south       0.479
west        0.375
construc    0.209
ndurman     0.318
trcommpu    0.205
trade       0.453
services    0.301
profserv    0.438
profocc     0.482
clerocc     0.374
servocc     0.348
lwage       0.532
expersq   616.045
tenursq   199.435
```
### Skewness

```text
              0
rownames  0.000
wage      2.013
educ     -0.621
exper     0.709
tenure    2.116
numdep    1.168
smsa     -0.996
northcen  1.152
south     0.605
west      1.770
construc  4.367
ndurman   2.435
trcommpu  4.475
trade     0.944
services  2.660
profserv  1.106
profocc   0.554
clerocc   1.788
servocc   2.073
lwage     0.392
expersq   1.497
tenursq   4.385
```
### Correlation

```text
          rownames   wage   educ  exper  tenure  numdep   smsa  northcen  south   west  construc  ndurman  trcommpu  trade  services  profserv  profocc  clerocc  servocc  lwage  expersq  tenursq
rownames     1.000 -0.116 -0.083  0.078   0.006   0.048 -0.323     0.090  0.253 -0.101     0.114    0.080     0.045  0.084    -0.004    -0.080   -0.051    0.015   -0.029 -0.104    0.080    0.013
wage        -0.116  1.000  0.406  0.113   0.347  -0.054  0.178    -0.029 -0.103  0.088     0.004    0.074     0.056 -0.190    -0.142     0.085    0.442   -0.141   -0.253  0.937    0.030    0.267
educ        -0.083  0.406  1.000 -0.300  -0.056  -0.215  0.224     0.061 -0.117  0.016    -0.077   -0.012     0.108 -0.059    -0.073     0.214    0.497   -0.008   -0.163  0.431   -0.331   -0.069
exper        0.078  0.113 -0.300  1.000   0.499  -0.056 -0.117     0.011  0.050 -0.017    -0.073    0.101    -0.048 -0.105     0.041    -0.021   -0.006   -0.040   -0.071  0.111    0.961    0.423
tenure       0.006  0.347 -0.056  0.499   1.000  -0.027  0.001     0.014 -0.025 -0.021    -0.026    0.161     0.064 -0.126    -0.063    -0.060    0.091   -0.073   -0.113  0.326    0.459    0.922
numdep       0.048 -0.054 -0.215 -0.056  -0.027   1.000 -0.096    -0.090  0.088  0.008     0.014    0.016    -0.015  0.048    -0.062    -0.072   -0.123    0.029    0.055 -0.095   -0.131   -0.057
smsa        -0.323  0.178  0.224 -0.117   0.001  -0.096  1.000     0.055 -0.231  0.099    -0.007   -0.098     0.008  0.018     0.010     0.046    0.146    0.107   -0.030  0.200   -0.111    0.004
northcen     0.090 -0.029  0.061  0.011   0.014  -0.090  0.055     1.000 -0.430 -0.261    -0.021   -0.001    -0.059  0.020    -0.063     0.069    0.069   -0.024    0.043 -0.016    0.034    0.009
south        0.253 -0.103 -0.117  0.050  -0.025   0.088 -0.231    -0.430  1.000 -0.335     0.028    0.121     0.016  0.029     0.002    -0.085   -0.104    0.029   -0.026 -0.090    0.021   -0.029
west        -0.101  0.088  0.016 -0.017  -0.021   0.008  0.099    -0.261 -0.335  1.000    -0.001   -0.098     0.052 -0.040     0.068    -0.035   -0.007    0.001   -0.022  0.072   -0.023   -0.041
construc     0.114  0.004 -0.077 -0.073  -0.026   0.014 -0.007    -0.021  0.028 -0.001     1.000   -0.078    -0.047 -0.139    -0.073    -0.129   -0.091    0.024   -0.088  0.023   -0.067   -0.029
ndurman      0.080  0.074 -0.012  0.101   0.161   0.016 -0.098    -0.001  0.121 -0.098    -0.078    1.000    -0.077 -0.228    -0.120    -0.212   -0.000   -0.129   -0.111  0.083    0.094    0.126
trcommpu     0.045  0.056  0.108 -0.048   0.064  -0.015  0.008    -0.059  0.016  0.052    -0.047   -0.077     1.000 -0.136    -0.072    -0.126   -0.008    0.079   -0.060  0.077   -0.044    0.052
trade        0.084 -0.190 -0.059 -0.105  -0.126   0.048  0.018     0.020  0.029 -0.040    -0.139   -0.228    -0.136  1.000    -0.212    -0.375    0.058   -0.037    0.033 -0.215   -0.083   -0.092
services    -0.004 -0.142 -0.073  0.041  -0.063  -0.062  0.010    -0.063  0.002  0.068    -0.073   -0.120    -0.072 -0.212     1.000    -0.198   -0.124   -0.032    0.173 -0.187    0.050   -0.026
profserv    -0.080  0.085  0.214 -0.021  -0.060  -0.072  0.046     0.069 -0.085 -0.035    -0.129   -0.212    -0.126 -0.375    -0.198     1.000    0.163    0.189    0.098  0.113   -0.028   -0.082
profocc     -0.051  0.442  0.497 -0.006   0.091  -0.123  0.146     0.069 -0.104 -0.007    -0.091   -0.000    -0.008  0.058    -0.124     0.163    1.000   -0.341   -0.308  0.445   -0.037    0.044
clerocc      0.015 -0.141 -0.008 -0.040  -0.073   0.029  0.107    -0.024  0.029  0.001     0.024   -0.129     0.079 -0.037    -0.032     0.189   -0.341    1.000   -0.181 -0.119   -0.046   -0.048
servocc     -0.029 -0.253 -0.163 -0.071  -0.113   0.055 -0.030     0.043 -0.026 -0.022    -0.088   -0.111    -0.060  0.033     0.173     0.098   -0.308   -0.181    1.000 -0.318   -0.021   -0.076
lwage       -0.104  0.937  0.431  0.111   0.326  -0.095  0.200    -0.016 -0.090  0.072     0.023    0.083     0.077 -0.215    -0.187     0.113    0.445   -0.119   -0.318  1.000    0.023    0.236
expersq      0.080  0.030 -0.331  0.961   0.459  -0.131 -0.111     0.034  0.021 -0.023    -0.067    0.094    -0.044 -0.083     0.050    -0.028   -0.037   -0.046   -0.021  0.023    1.000    0.414
tenursq      0.013  0.267 -0.069  0.423   0.922  -0.057  0.004     0.009 -0.029 -0.041    -0.029    0.126     0.052 -0.092    -0.026    -0.082    0.044   -0.048   -0.076  0.236    0.414    1.000
```
### Categorical Summary

```text
          count  unique      top  freq
nonwhite    526       2    White   472
female      526       2     Male   274
married     526       2  Married   320
```
## Visualizations
- Histogram: rownames: Distribution of rownames.
- Boxplot: rownames: Spread and outliers for rownames.
- Correlation Heatmap: Pairwise correlations across numeric columns.
- Bar Chart: nonwhite: Top categories in nonwhite.
- Scatter Plot: rownames vs wage: Relationship between rownames and wage.
## AI Insights
### Insights

- LLM output was unavailable, so this summary is rule-based.
- Strong correlations detected: lwage vs wage (0.94), exper vs expersq (0.96), tenure vs tenursq (0.92).
- 5 visualization(s) were generated successfully.
- Next step: confirm these patterns against domain knowledge before making decisions.
## Warnings
- Insight generation error: Error code: 413 - {'error': {'message': 'Request too large for model `openai/gpt-oss-120b` in organization `org_01k26hyfqwehqamjtwm2mvm88z` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 8864, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}