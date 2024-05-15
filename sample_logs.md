## Sample logs 

```shell
(.venv) dhruvparthasarathy@Dhruvs-MacBook-Air cell-count-analysis % docker compose up        
WARN[0000] Found orphan containers ([cell-count-analysis-analysis-1]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 2/0
 ⠿ Container cell-count-analysis-task-2-1  Created                                                                                   0.0s
 ⠿ Container cell-count-analysis-task-1-1  Created                                                                                   0.0s
Attaching to cell-count-analysis-task-1-1, cell-count-analysis-task-2-1
cell-count-analysis-task-1-1  | ===============Succesfully loaded data:===============
cell-count-analysis-task-1-1  |   project subject condition  age  ... cd8_t_cell cd4_t_cell nk_cell monocyte
cell-count-analysis-task-1-1  | 0    prj1    sbj1  melanoma   70  ...      24000      42000    6000    12000
cell-count-analysis-task-1-1  | 1    prj1    sbj1  melanoma   70  ...      22000      40000    2000     6000
cell-count-analysis-task-1-1  | 2    prj1    sbj1  melanoma   70  ...      26250      37500   10000    16250
cell-count-analysis-task-1-1  | 3    prj1    sbj2   healthy   65  ...      17100      18000    4500    22500
cell-count-analysis-task-1-1  | 4    prj1    sbj3  melanoma   75  ...      30000      37500    4500    18000
cell-count-analysis-task-1-1  | 
cell-count-analysis-task-1-1  | [5 rows x 15 columns]
cell-count-analysis-task-1-1  | Total  number of samples: 17
cell-count-analysis-task-1-1  | ===============Succesfully uploaded data to data/updated-cell-count.csv:===============
cell-count-analysis-task-1-1  |   sample  total_count population  count  percentage
cell-count-analysis-task-1-1  | 0     s1       120000     b_cell  36000        30.0
cell-count-analysis-task-1-1  | 1     s2       100000     b_cell  30000        30.0
cell-count-analysis-task-1-1  | 2     s3       125000     b_cell  35000        28.0
cell-count-analysis-task-1-1  | 3     s4        90000     b_cell  27900        31.0
cell-count-analysis-task-1-1  | 4     s5       150000     b_cell  60000        40.0
cell-count-analysis-task-1-1 exited with code 0
cell-count-analysis-task-2-1  | Succesfully loaded data:
cell-count-analysis-task-2-1  |   project subject condition  age  ... cd8_t_cell cd4_t_cell nk_cell monocyte
cell-count-analysis-task-2-1  | 0    prj1    sbj1  melanoma   70  ...      24000      42000    6000    12000
cell-count-analysis-task-2-1  | 1    prj1    sbj1  melanoma   70  ...      22000      40000    2000     6000
cell-count-analysis-task-2-1  | 2    prj1    sbj1  melanoma   70  ...      26250      37500   10000    16250
cell-count-analysis-task-2-1  | 3    prj1    sbj2   healthy   65  ...      17100      18000    4500    22500
cell-count-analysis-task-2-1  | 4    prj1    sbj3  melanoma   75  ...      30000      37500    4500    18000
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | [5 rows x 15 columns]
cell-count-analysis-task-2-1  | Total  number of samples: 17
cell-count-analysis-task-2-1  |   sample  total_count population  count  percentage
cell-count-analysis-task-2-1  | 0     s1       120000     b_cell  36000        30.0
cell-count-analysis-task-2-1  | 1     s2       100000     b_cell  30000        30.0
cell-count-analysis-task-2-1  | 2     s3       125000     b_cell  35000        28.0
cell-count-analysis-task-2-1  | 3     s4        90000     b_cell  27900        31.0
cell-count-analysis-task-2-1  | 4     s5       150000     b_cell  60000        40.0
cell-count-analysis-task-2-1  | project                          prj1
cell-count-analysis-task-2-1  | subject                          sbj1
cell-count-analysis-task-2-1  | condition                    melanoma
cell-count-analysis-task-2-1  | age                                70
cell-count-analysis-task-2-1  | sex                                 F
cell-count-analysis-task-2-1  | treatment                         tr1
cell-count-analysis-task-2-1  | response                            y
cell-count-analysis-task-2-1  | sample                             s2
cell-count-analysis-task-2-1  | sample_type                      PBMC
cell-count-analysis-task-2-1  | time_from_treatment_start         7.0
cell-count-analysis-task-2-1  | b_cell                          30000
cell-count-analysis-task-2-1  | cd8_t_cell                      22000
cell-count-analysis-task-2-1  | cd4_t_cell                      40000
cell-count-analysis-task-2-1  | nk_cell                          2000
cell-count-analysis-task-2-1  | monocyte                         6000
cell-count-analysis-task-2-1  | total_count                    100000
cell-count-analysis-task-2-1  | b_cell_percent                   30.0
cell-count-analysis-task-2-1  | cd8_t_cell_percent               22.0
cell-count-analysis-task-2-1  | cd4_t_cell_percent               40.0
cell-count-analysis-task-2-1  | nk_cell_percent                   2.0
cell-count-analysis-task-2-1  | monocyte_percent                  6.0
cell-count-analysis-task-2-1  | Name: 1, dtype: object
cell-count-analysis-task-2-1  | B_cell - Responders: Statistics=0.886, p-value=0.299
cell-count-analysis-task-2-1  | B_cell - Non-Responders: Statistics=0.958, p-value=0.795
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | Cd8_t_cell - Responders: Statistics=0.960, p-value=0.820
cell-count-analysis-task-2-1  | Cd8_t_cell - Non-Responders: Statistics=0.828, p-value=0.135
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | Cd4_t_cell - Responders: Statistics=0.954, p-value=0.771
cell-count-analysis-task-2-1  | Cd4_t_cell - Non-Responders: Statistics=0.813, p-value=0.103
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | Nk_cell - Responders: Statistics=0.952, p-value=0.757
cell-count-analysis-task-2-1  | Nk_cell - Non-Responders: Statistics=0.881, p-value=0.314
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | Monocyte - Responders: Statistics=0.918, p-value=0.489
cell-count-analysis-task-2-1  | Monocyte - Non-Responders: Statistics=0.846, p-value=0.181
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | B_cell - Statistics=-0.008, p-value=0.994
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | Cd8_t_cell - Statistics=0.463, p-value=0.654
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | Cd4_t_cell - Statistics=4.941, p-value=0.001
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | Nk_cell - Statistics=1.848, p-value=0.098
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1  | Monocyte - Statistics=-2.904, p-value=0.017
cell-count-analysis-task-2-1  | 
cell-count-analysis-task-2-1 exited with code 0
```
