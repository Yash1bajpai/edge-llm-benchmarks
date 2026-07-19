| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| qwen2 3B Q4_K - Medium         |   1.79 GiB |     3.09 B | CPU        |       6 |           pp128 |         41.45 ± 0.00 |
| qwen2 3B Q4_K - Medium         |   1.79 GiB |     3.09 B | CPU        |       6 |           tg128 |          8.16 ± 0.00 |
| qwen2 3B Q8_0                  |   3.05 GiB |     3.09 B | CPU        |       6 |           pp128 |         24.79 ± 0.00 |
| qwen2 3B Q8_0                  |   3.05 GiB |     3.09 B | CPU        |       6 |           tg128 |          5.37 ± 0.00 |
| phi3 3B Q4_K - Medium          |   2.23 GiB |     3.82 B | CPU        |       6 |           pp128 |         21.97 ± 0.00 |
| phi3 3B Q4_K - Medium          |   2.23 GiB |     3.82 B | CPU        |       6 |           tg128 |          7.07 ± 0.00 |
| phi3 3B Q8_0                   |   3.78 GiB |     3.82 B | CPU        |       6 |           pp128 |          7.32 ± 0.00 |
| phi3 3B Q8_0                   |   3.78 GiB |     3.82 B | CPU        |       6 |           tg128 |          0.09 ± 0.00 |

build: 571d0d540 (10068)
