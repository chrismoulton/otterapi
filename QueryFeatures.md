Otter provides **features** for a query when the search.json method is called with query\_features=1 and window=dynamic.  These features describe second-order statistics about the level of supply of the query in Topsy's corpus.  The features can be used to train robust classifiers for fresh & trending queries.

The features are described below, using the following example:

```
$ curl -i http://otter.topsy.com/search.json?window=dynamic&q=iphone&query_features=1&rankcount_maxdays=14

      "query_features" : {
         "topsy_momentum_d1" : 77630,
         "topsy_count_d14" : 3069383,
         "topsy_window_picked" : 1,
         "topsy_peak_height_stddevs_d14" : 3.0209111645379,
         "topsy_normalized_sum_d14" : 1641.55063526661,
         "topsy_count_d1" : 143766,
         "topsy_stddev_d14" : 83.2568605857359,
         "topsy_window_picked_method" : 1,
         "topsy_top_link_in_cnt_influential" : 309,
         "topsy_peak_position_d14" : 7,
         "topsy_top_link_qius" : 1.78786e-07,
         "topsy_velocity_d1" : 54,
         "topsy_top_link_score" : 14.3181,
         "topsy_total_count" : 26908148,
         "topsy_top_link_in_cnt" : 2538,
         "topsy_window_count" : 3127
      },

```

## Picked window values ##

These features relate to the window that was picked. The search results provided are from this picked window, as are quality scores and other features that relate to the search results themselves.&nbsp; &nbsp;

| **Feature** | **Example value** | **Description** |
|:------------|:------------------|:----------------|
| topsy\_window\_count | 2248              | count in picked window |
| topsy\_window\_picked | 1                 | window picked, in hours: 1 = past hour, 24 = past day etc |
| topsy\_window\_picked\_method | 1                 | method used to pick window (hour or day doesn't matter, applies to final window picked); 0 is "peak height"; 1 is "count priority"; 2 is "slope priority". see description of window picking methods below for more details. |

## Day histogram analysis values ##

These features relate to the analysis of the histogram of values for day results, i.e. the result counts for each day from the past day to the oldest day considered. The rankcount\_maxdays parameter determines the number of days considered, and this value is included in the names of the variables returned. Assuming rankcount\_maxdays=14, the variables in this section will end with a _d14 suffix._

| **Feature** | **Example value** | **Description** |
|:------------|:------------------|:----------------|
| topsy\_count\_d14 | 3148426           | sum of actual result count for each day in the period (rankcount\_maxdays days) |
| topsy\_normalized\_sum\_d14 | 1581.48684314174  | sum of normalized count for each day. normalized count is actual count divided by the baseline (e.g. twitter traffic) |
| topsy\_stddev\_d14 | 63.3996824089592  | standard deviation of normalized counts |
| topsy\_peak\_height\_stddevs\_d14 | 2.51324146711823  | height of selected peak measured in stddevs above valley marking beginning of peak - previously this value was "window\_score" |
| topsy\_peak\_position\_d14| 11                | position of start of peak in days. if topsy\_window\_picked\_method = 0, topsy\_window\_picked will be the same as this number times 24 (as topsy\_window\_picked is in hours). Note that d11 here is the start of the peak; so the valley is in d12; the actual height of the peak maybe in a more recent day, e.g. if it was a 3-day peak going from d9-d11 with the highest point in d10, the peak height refers to the height of d10 over d12 |

In the example, the above d14 variables mean: there were actually 3148426 results over 14 days. Normalized by the background baseline, the total was 1581 with stddev of 63; the peak started at d11 out of d14, with height of 2.5 stddevs above the the valley. The position highest point of the peak is not included here.

## Trend for query over last 1 day ##

| **Feature** | **Example value** | **Description** |
|:------------|:------------------|:----------------|
| topsy\_count\_d1 | 100042            | count of results in past day |
| topsy\_momentum\_d1 | 50067             | weighted sum of counts for each hour for d1. formula is: sum for i in 1..24&nbsp; (count\[i\] **i/24) where 24 is the past hour. \\**|
| topsy\_velocity\_d1 | 51                | 100 **momentum / count - count is like "mass" in this formula**|

## Result Quality Features ##

These are features for the top result in the picked window.  The parameters provide a proxy for the quality and support for all results in the window.

| **Feature** | **Example value** | **Description** |
|:------------|:------------------|:----------------|
| topsy\_top\_link\_in\_cnt\_influential | 10                | number of influential citations for top result in picked window |
| topsy\_top\_link\_qius | 2.46363e-08       | query independent url score for the top result in picked window |
| topsy\_top\_link\_score | 14.747            | result score of the top result in the picked window |
| topsy\_top\_link\_in\_cnt | 239               | number of citations for top result in picked window |

## Global Features ##

| **Feature** | **Example value** | **Description** |
|:------------|:------------------|:----------------|
| topsy\_total\_count | 27490926          | all time total count |

